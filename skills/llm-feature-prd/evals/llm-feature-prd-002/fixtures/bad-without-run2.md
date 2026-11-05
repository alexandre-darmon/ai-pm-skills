Je n'ai pas pu enregistrer le PRD dans un fichier, car l'outil d'écriture est désactivé dans cette session. Le voici en entier ci-dessous.

# PRD – Agent de remboursement (Service Client)
Statut : brouillon v1, 2026-11-05

## 1. Problème
Environ 40 000 demandes de remboursement par mois sont traitées par 6 personnes, avec un délai de 3 jours. Le temps est perdu surtout en file d'attente et en recherche manuelle de commande, pas en prise de décision.

## 2. Objectifs et métriques

| Métrique | Aujourd'hui | Cible |
|---|---|---|
| Délai de résolution | 3 jours | Même jour (p90 < 24 h, cas automatiques < 15 min) |
| Taux d'erreur de remboursement | À mesurer (sprint 0) | < 1 % des remboursements automatisés |
| Coût par demande | n/a | < 0,10 € (modèle et infrastructure) |
| Taux d'automatisation | 0 % | 60–70 % à terme (hypothèse, à confirmer en shadow) |
| CSAT | À mesurer | Pas de dégradation |

Le seuil de 1 % sert aussi de garde-fou : au-delà sur une semaine glissante, l'automatisation est freinée automatiquement.

## 3. Périmètre
**Inclus (v1) :**
- Lecture de la demande en français, classification de l'intention, extraction de la référence de commande.
- Consultation de la commande dans le back office et vérification de l'éligibilité.
- Remboursement direct, partiel ou total, jusqu'au montant de la commande (moins ce qui est déjà remboursé), sur le moyen de paiement d'origine.
- Réponse au client en français.
- Escalade vers un humain, avec un résumé pré-rempli, quand le cas n'est pas sûr.

**Exclus (v1) :** autres langues (routées vers un humain), remboursement vers un autre moyen de paiement, montants supérieurs à la commande, gestes commerciaux, logistique des retours, litiges transporteur et chargebacks, voix, pièces jointes (routées vers un humain).

## 4. Exigences fonctionnelles
1. **Compréhension** : sortie structurée (intention, référence de commande, motif, montant demandé, confiance).
2. **Vérification** : la commande doit correspondre au demandeur (e-mail ou compte). Sinon, une seule question au client, puis escalade.
3. **Éligibilité déterministe** : la politique de remboursement est du code (statut de livraison, délai, déjà remboursé, catégories exclues). Le modèle propose, le moteur de règles décide.
4. **Exécution** : un seul outil `issue_refund(order_id, amount, reason_code, idempotency_key)`. Les contrôles sont côté serveur, pas dans le prompt : montant ≤ reste remboursable, idempotence, moyen de paiement d'origine, plafonds.
5. **Réponse client** : en français, par gabarits quand c'est possible, sans promesse au-delà de ce que renvoie le back office.
6. **Escalade** si l'un de ces cas se présente :
   - faible confiance ;
   - identité non concordante ;
   - règle échouée ou cas limite ;
   - montant au-dessus du plafond ;
   - client signalé ;
   - ton juridique, fraude ou colère ;
   - erreur d'outil.
7. **Traçabilité** : chaque décision est journalisée (entrée, champs extraits, règles évaluées, appels d'outils, version du modèle, coût).

## 5. Contraintes non fonctionnelles
- **Hébergement UE** : inférence, logs, stockage et sous-traitants. Un DPA et l'absence d'entraînement sur nos données sont à confirmer en sprint 0. C'est bloquant.
- **Français uniquement**, en entrée et en sortie.
- **Coût** : moins de 0,10 € par demande, soit moins de 4 000 €/mois. Un petit modèle rapide (classe Haiku) pour l'extraction et la réponse, du code pour le reste, et un plafond de tokens par requête. Je n'ai pas vérifié les tarifs actuels en région UE : à valider avec des volumes de tokens réels au sprint 1.
- **Latence** : p95 < 60 s pour les cas automatiques.
- **Repli** : si l'agent ou le modèle tombe, les tickets retournent dans la file humaine sans perte.
- **RGPD** : minimisation des données envoyées au modèle, DPIA avant la mise en production, droit de demander un humain (art. 22).

## 6. Contrôles de risque (l'agent déplace de l'argent)
1. **Injection de prompt et ingénierie sociale** : le texte client est une donnée non fiable. Les plafonds et paramètres sont imposés par la couche outil, quoi que dise le modèle.
2. **Plafonds** : par remboursement (départ bas, par exemple 50 €, à fixer avec la Finance), par client et par jour, et global par jour. « Jusqu'au montant de la commande » est le plafond final, atteint par paliers.
3. **Signaux de fraude** : fréquence anormale, compte récent, identité non concordante, alors un humain traite le cas.
4. **Kill switch** : un interrupteur qui repasse immédiatement en mode suggestion seule.
5. **Freinage automatique** si l'erreur dépasse 1 % ou si la dépense est anormale.
6. **Réversibilité** : chaque remboursement porte un tag « agent » et une clé d'idempotence, pour le retrouver et l'annuler en masse.

## 7. Définition d'une « erreur de remboursement »
Est une erreur, à l'audit :
- un remboursement émis alors que la politique l'interdit ;
- un mauvais montant ;
- une mauvaise commande ou un mauvais client ;
- un doublon ;
- une réponse client erronée sur l'issue.

Les remboursements éligibles manqués sont suivis à part, car ils coûtent du CSAT et non de l'argent.

L'audit se fait sur un échantillon hebdomadaire aléatoire d'au moins 400 remboursements automatisés, plus 100 % des remboursements annulés ou contestés. À 1 % sur environ 25 000 remboursements automatisés par mois, cela représente jusqu'à 250 erreurs par mois. La cible est un plafond, et on vise nettement en dessous.

## 8. Plan de livraison en 2 sprints

**Sprint 0 (environ 1 semaine, prérequis) :**
- Politique de remboursement écrite et transformée en règles (Support et Finance).
- Accès API au back office (lecture de commande, remboursement) et un environnement sandbox.
- Hébergement UE, DPA et début de DPIA.
- État de référence : taux d'erreur actuel, volumes par motif, panier moyen, et 500 tickets historiques étiquetés avec la bonne issue (jeu d'évaluation).

**Sprint 1 : construction et mode shadow**
- Compréhension, recherche de commande, moteur de règles, brouillons de réponse, escalade, journal d'audit.
- Banc d'évaluation avec au moins 98 % d'accord avec la décision humaine sur les cas que l'agent choisit d'automatiser.
- Mode shadow sur le trafic réel : l'agent décide et rédige, les humains émettent encore les remboursements.
- Mesure du coût réel par demande.

**Sprint 2 : mise en production contrôlée**
- `issue_refund` activé sur le segment le plus sûr (par exemple livré, dans le délai, ≤ 50 €, sans signal), à 10 % du trafic, puis 25 %, 50 % et 100 % du segment. Chaque palier exige une erreur < 1 % et aucun incident majeur.
- Tableau de bord : volume, automatisation, délai, erreur, dépense, motifs d'escalade.
- Runbook, kill switch testé, équipe formée à la file d'escalade.

**Point d'attention :** « live en deux sprints » veut dire en production sur un segment plafonné, avec la montée en charge engagée. La couverture complète jusqu'au montant total de la commande, pour tous les types de commande, sera pilotée par les données d'audit, pas par le calendrier.

## 9. Équipe
Les 6 conseillers ne sont pas remplacés par ce PRD. Leur temps passe aux escalades, aux audits et aux cas limites. Toute décision d'effectifs est hors périmètre et à prendre après 2–3 mois de données.

## 10. Risques et questions ouvertes

| Point | Impact / action |
|---|---|
| Pas d'API ou de sandbox propre dans le back office | Bloque le sprint 1. À confirmer en sprint 0, repli en mode suggestion seule. |
| Politique de remboursement en partie implicite | Atelier de règles avec les conseillers, les cas ambigus sont escaladés. |
| Pas de taux d'erreur de référence | Auditer un échantillon des remboursements humains du mois dernier. |
| Disponibilité du modèle en région UE | À vérifier en sprint 0. |
| RGPD, décision automatisée | Revue par le DPO. |
| Canaux d'entrée et outil de ticketing | Le Product doit confirmer (e-mail, formulaire, chat). |
| Panier moyen et perte maximale acceptable par jour | La Finance fixe les plafonds. |

## 11. Critères go / no-go pour chaque palier
- En shadow : au moins 98 % d'accord sur les cas automatisés, aucun remboursement contraire à la politique.
- Coût réel < 0,10 € par demande.
- Kill switch et freinage automatique testés.
- DPIA et DPA validés.
- Plafonds approuvés par la Finance.

Les chiffres entre parenthèses (plafond de 50 €, 60–70 % d'automatisation, 98 % d'accord) sont des hypothèses de départ de ma part. Ils doivent être confirmés par vos données.

Trois points décideront du délai de deux sprints : l'existence d'une API back office exploitable, une politique de remboursement écrite, et l'accord du DPO sur l'hébergement UE. Je peux aussi détailler le jeu d'évaluation ou le schéma d'architecture si vous voulez.