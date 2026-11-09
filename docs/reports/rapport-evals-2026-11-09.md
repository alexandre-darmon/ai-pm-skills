# Rapport d'évaluation des skills — 9 novembre 2026

## Résumé

- **22 skills sur 27 passent les règles du repo.** Pour les 10 skills revérifiés, c'est le verdict sur 3 passes qui compte ; pour les 17 autres, c'est le verdict sur une passe.
- **Les skills améliorent nettement les réponses de Sonnet 5.5** : 0,93 de score moyen avec le skill contre 0,59 sans, soit **+34 points**. Le minimum demandé par le repo est de 10 points.
- **Les skills se déclenchent bien.** Sur les cas où le skill doit être appelé, il l'a été dans 86 cas sur 87 au run à une passe. Sur les cas où il doit rester silencieux, il n'a jamais été appelé : 27 sur 27 à une passe, 30 sur 30 à trois passes.
- **Les 6 skills déjà validés retrouvent les scores de leurs baselines figées.** Seul `conversation-analysis` montre une fragilité : la règle « masquer les données personnelles avant tout appel au modèle » a été oubliée 2 fois sur 7 passes au total.
- **Deux graders donnaient de faux résultats.** Ils ont été corrigés et protégés par des fixtures, ce qui a fait passer deux skills de plus.
- **Le juge Haiku confirme le sens du gain, mais il le voit 5 fois plus petit** (+6 points). Il n'est pas calibré : ses notes sont une indication, pas une mesure.
- **Le run local Qwen + Gemma est en pause** à 34 réponses sur 228. Les fichiers sont gardés pour plus tard.

## 1. Ce qui a été lancé

| Run | Modèle qui répond | Juge | Cas | Passes | Réponses | Durée | Coût (équivalent API) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Claude, 1 passe | Sonnet 5.5, dans Claude Code | Haiku 5.5 | 114 (27 skills) | 1 | 228 | 11 min + 5 min de jugement | 13,04 $ |
| Claude, 3 passes | Sonnet 5.5, dans Claude Code | Haiku 5.5 | 41 (10 skills en échec) | 3 | 246 | 8 min + 10 min de jugement | 14,15 $ |
| Local (en pause) | Qwen 3.8 27B, via Ollama | Gemma 4 31B | 114 | 1 | 34 sur 228 | ~85 à 190 s par réponse | 0 $ |

- Les deux runs Claude ont tourné sur l'abonnement, sans clé API. Les coûts en dollars sont ceux que l'outil d'évaluation calcule en équivalent API. Le coût du jugement Haiku n'a pas été mesuré.
- Chaque cas est joué **avec** le skill et **sans** lui, par le même agent et avec les mêmes outils. Seul change le fait que le skill soit disponible ou non.
- Les réponses sont notées par les graders du repo : des regex, un contrôle « le skill s'est déclenché », et les lignes rouges (une seule faute fait échouer le cas). Les règles de réussite sont celles de `run_evals.py` : score ≥ seuil, aucune ligne rouge manquée sur aucune passe, gain moyen ≥ 10 points, skill silencieux sur le cas négatif.
- Le juge aveugle reprend la grille de `judge_answers.py`. Il ne sait pas quelle réponse a eu le skill, et les mentions du skill sont retirées. Il note de 1 à 5 cinq critères génériques (justesse, actionnable, honnête sur les inconnues, attentif aux risques, spécifique au cas), plus un critère « atteint l'objectif du cas » rapporté à part. Chaque réponse est jugée deux fois, pour mesurer la variabilité du juge. Il n'est jamais appliqué aux skills juridiques (étape `govern`), comme le demande AGENTS.md.

## 2. Résultats du run à une passe (27 skills)

Les chiffres tiennent compte des deux graders corrigés (section 5).

| Skill | Étape | Statut | Avec | Sans | Gain | Déclenché | Négatif silencieux | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agent-design-and-tooling | build | draft | 0,90 | 0,53 | +0,37 | 3/3 | 1/1 | passe |
| agent-knowledge-base | data | draft | 0,93 | 0,66 | +0,27 | 2/3 | 1/1 | passe |
| ai-act-classification | govern | tested | 1,00 | 0,72 | +0,28 | 3/3 | 1/1 | passe |
| ai-adoption-plan | transform | draft | 0,93 | 0,72 | +0,20 | 3/3 | 1/1 | échec |
| ai-brand-positioning | strategy | draft | 0,81 | 0,58 | +0,22 | 3/3 | 1/1 | échec |
| ai-data-requirements | specify | draft | 0,97 | 0,66 | +0,31 | 3/3 | 1/1 | passe |
| ai-incident-playbook | govern | draft | 1,00 | 0,51 | +0,49 | 4/4 | 1/1 | passe |
| ai-initiative-pitch | strategy | draft | 0,77 | 0,46 | +0,31 | 3/3 | 1/1 | échec |
| ai-interaction-patterns | specify | draft | 0,90 | 0,80 | +0,10 | 3/3 | 1/1 | échec |
| ai-literacy-program | transform | draft | 0,94 | 0,76 | +0,18 | 3/3 | 1/1 | passe |
| ai-moat-7-powers | strategy | draft | 0,93 | 0,53 | +0,40 | 3/3 | 1/1 | passe |
| ai-opportunity-assessment | strategy | draft | 1,00 | 0,60 | +0,40 | 3/3 | 1/1 | passe |
| ai-roi-quantification | measure | draft | 0,93 | 0,67 | +0,26 | 3/3 | 1/1 | passe |
| assistant-kpis-cost-per-outcome | measure | tested | 1,00 | 0,29 | +0,71 | 3/3 | 1/1 | passe |
| build-evals | measure | tested | 0,98 | 0,35 | +0,63 | 4/4 | 1/1 | passe |
| chat-with-your-data-scoping | specify | draft | 0,82 | 0,65 | +0,17 | 3/3 | 1/1 | échec |
| conversation-analysis | measure | tested | 0,87 | 0,26 | +0,61 | 4/4 | 1/1 | échec |
| cse-consultation | govern | tested | 1,00 | 0,58 | +0,42 | 4/4 | 1/1 | passe |
| dpia-prescreen | govern | draft | 1,00 | 0,79 | +0,21 | 4/4 | 1/1 | passe |
| llm-feature-prd | specify | tested | 0,96 | 0,33 | +0,62 | 3/3 | 1/1 | passe |
| model-card-ai-registry | govern | draft | 0,81 | 0,57 | +0,24 | 3/3 | 1/1 | échec |
| model-selection | measure | draft | 1,00 | 0,74 | +0,26 | 3/3 | 1/1 | passe |
| prd-to-claude-code | build | draft | 1,00 | 0,68 | +0,32 | 3/3 | 1/1 | passe |
| process-ai-redesign | transform | draft | 0,83 | 0,48 | +0,36 | 3/3 | 1/1 | échec |
| release-to-production | measure | draft | 1,00 | 0,62 | +0,38 | 3/3 | 1/1 | passe |
| semantic-layer-design | data | draft | 0,95 | 0,60 | +0,34 | 4/4 | 1/1 | passe |
| system-prompt-and-guardrails | build | draft | 0,76 | 0,66 | +0,10 | 3/3 | 1/1 | échec |

**Moyenne :** 0,93 avec le skill, 0,59 sans, soit +0,34. 18 skills sur 27 passent.

### Les 6 skills validés comparés à leurs baselines figées

Les baselines datent du 6 novembre 2026, avec 3 passes par cas.

| Skill | Avec (ce run) | Sans (ce run) | Avec (baseline) | Sans (baseline) |
| --- | --- | --- | --- | --- |
| ai-act-classification | 1,00 | 0,72 | 1,00 | 0,68 |
| assistant-kpis-cost-per-outcome | 1,00 | 0,29 | 0,99 | 0,27 |
| build-evals | 0,98 | 0,35 | 1,00 | 0,51 |
| conversation-analysis | 0,87 | 0,26 | 0,96 | 0,21 |
| cse-consultation | 1,00 | 0,58 | 0,99 | 0,65 |
| llm-feature-prd | 0,96 | 0,33 | 1,00 | 0,29 |

Les résultats sont reproductibles. Seul `conversation-analysis` recule avec le skill, à cause d'une ligne rouge manquée (voir la section 4).

## 3. Confirmation sur 3 passes (les 10 skills en échec)

La doc du repo est claire : une seule passe donne une indication, il en faut 3 pour confirmer. Ce run a joué 3 fois chaque cas des 10 skills en échec, avec les mêmes graders et dans un dossier séparé.

| Skill | Avec | Sans | Gain | Déclenché | Négatif silencieux | 1 passe | 3 passes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| agent-knowledge-base | 0,91 | 0,68 | +0,23 | 6/9 | 3/3 | échec | **passe** (après correction du grader) |
| ai-adoption-plan | 0,96 | 0,70 | +0,26 | 9/9 | 3/3 | échec | **passe** |
| ai-brand-positioning | 0,83 | 0,61 | +0,21 | 9/9 | 3/3 | échec | échec |
| ai-initiative-pitch | 0,93 | 0,47 | +0,45 | 9/9 | 3/3 | échec | échec |
| ai-interaction-patterns | 0,93 | 0,80 | +0,13 | 7/9 | 3/3 | échec | **passe** (après correction du grader) |
| chat-with-your-data-scoping | 0,95 | 0,60 | +0,35 | 9/9 | 3/3 | échec | échec |
| conversation-analysis | 0,91 | 0,23 | +0,68 | 12/12 | 3/3 | échec | échec |
| model-card-ai-registry | 1,00 | 0,64 | +0,36 | 9/9 | 3/3 | échec | **passe** |
| process-ai-redesign | 0,94 | 0,50 | +0,44 | 9/9 | 3/3 | échec | échec |
| system-prompt-and-guardrails | 0,96 | 0,77 | +0,18 | 9/9 | 3/3 | échec | **passe** |

Bilan : 3 échecs étaient de la variation aléatoire, 2 venaient de graders faux, et 5 sont confirmés.

## 4. Les 5 échecs confirmés, et leur cause

Pour chaque passe en échec, j'ai vérifié que le skill s'était bien déclenché. Dans les 5 cas ci-dessous, il l'était : l'échec porte donc bien sur le contenu de la réponse avec le skill.

| Skill | Ce qui manque | Fréquence | Lecture |
| --- | --- | --- | --- |
| ai-brand-positioning | `failure-behaviour` : dire ce que fait l'IA quand elle n'est pas sûre (signaler, passer la main à un humain) | 7 passes sur 9 | Systématique. Soit le skill ne pousse pas assez ce point, soit le regex exige une formulation trop précise. Il faut relire 2 ou 3 réponses pour trancher. Le cas 002 manque aussi `gain-inputs` (3 fois sur 3). |
| process-ai-redesign | `fallback-hours` (cas 001) : solution de repli en dehors des heures ouvrées | 3 fois sur 3 | Systématique. Probablement un point que le skill ne couvre pas. `approach-per-step` manque aussi 2 fois sur 3. Le seuil est de 0,90 et le cas 001 est à 0,83. |
| ai-initiative-pitch | ligne rouge `redline-no-rollout-ask` (cas 001) : ne pas demander un déploiement complet d'emblée | 1 fois sur 3 | Oubli ponctuel, mais la règle du repo est stricte : une ligne rouge manquée une fois fait échouer le cas. |
| chat-with-your-data-scoping | ligne rouge `redline-no-spot-check` (cas 003) | 1 fois sur 3 | Oubli ponctuel. |
| conversation-analysis | lignes rouges `redline-route-by-confidence` (cas 002) et `redline-mask-first` (cas 003) | 1 fois sur 3 chacune | **À surveiller, c'est un skill validé.** Sa baseline réussissait ces deux lignes rouges 3 fois sur 3. `redline-mask-first` est aussi manquée au run à une passe, soit 2 oublis sur 7 passes en tout : une vraie fragilité. |

**Problème de déclenchement (à part).** Deux skills ne se déclenchent pas toujours :
- `agent-knowledge-base` ne se déclenche jamais sur son cas 003 (0 fois sur 3) ;
- `ai-interaction-patterns` ne se déclenche que sur 1 passe sur 3 de son cas 003.

Ce critère ne compte pas dans le score, mais ça veut dire que leur description ne couvre pas ce type de demande.

## 5. Les graders corrigés

Les deux lignes rouges suivantes se déclenchaient sur des réponses correctes.

| Grader | Faux positif | Correction |
| --- | --- | --- |
| `agent-knowledge-base-001/redline-not-everything` | « I wouldn't index all 40 » et « I would not index all… » étaient comptés comme « tout indexer », tout comme le titre « Decision on "index everything" » | Le regex reconnaît maintenant les autres formes de refus (wouldn't, would not, won't, against, rather than…). Il ignore aussi la demande du sponsor quand elle est citée entre guillemets ou rapportée (« wants », « proposing »…). |
| `ai-interaction-patterns-003/redline-no-uncalibrated` | « If it calibrates: show the score », « keep the score hidden » et « If it's well calibrated…, show a flag » étaient comptés comme « afficher un score non calibré » | « if / once / when / after… calibrated » placé avant, ainsi que « hidden » ou « off » placé après, ne comptent plus. |

- **Vérification.** J'ai testé chaque nouveau regex sur toutes les réponses sauvegardées (Claude à une et trois passes, Qwen) avant de modifier les fichiers. Les réponses qui cèdent vraiment au sponsor (« I can index all 40 but tag the 12 ») et les fixtures `bad.md` sont toujours détectées.
- **Protection.** Les 3 vraies réponses signalées à tort sont ajoutées comme fixtures `good-run*.md`. Le validateur échouera si ce faux positif revient. `validate_skills.py` donne 0 problème.
- **Re-notation sans coût.** Les deux runs ont été recalculés à partir des réponses sauvegardées, sans aucun nouvel appel au modèle.

## 6. Le juge aveugle (Haiku 5.5)

| Mesure | Run à une passe (22 skills jugés) | Run à trois passes (9 skills jugés) |
| --- | --- | --- |
| Note générique avec skill | 0,78 | 0,77 |
| Note générique sans skill | 0,71 | 0,72 |
| Écart | **+0,06** | **+0,04** |
| « Atteint l'objectif » avec / sans | 0,76 / 0,50 | 0,72 / 0,52 |
| Longueur avec / sans skill (mots) | 954 / 619 | 1 016 / 613 |
| Écart moyen entre les deux passes du juge | 0,05 | 0,05 |
| Corrélation juge / regex, par réponse | 0,38 | 0,27 |
| Corrélation juge / longueur, par réponse | 0,34 | 0,43 |
| Corrélation du gain juge / gain regex, par skill | 0,49 | 0,35 |

Notes moyennes sur 5, run à une passe :

| Critère | Avec | Sans |
| --- | --- | --- |
| Justesse du raisonnement | 4,00 | 3,91 |
| Actionnable | 4,22 | 4,05 |
| Honnête sur les inconnues | 4,23 | 3,88 |
| Attentif aux risques | 4,04 | 3,73 |
| Spécifique au cas | 4,04 | 3,69 |
| Atteint l'objectif du cas | 4,05 | 2,99 |

**Lecture**
- Le juge voit un gain dans le même sens que les regex, mais bien plus petit. Ce gain vient surtout de trois critères : être spécifique au cas, nommer les risques, et être honnête sur ce qu'on ne sait pas. Sur la justesse du raisonnement, la différence est faible.
- « Atteint l'objectif » montre un gain beaucoup plus fort (+26 points). Mais les objectifs ont été écrits par l'auteur des skills, donc ce critère est rapporté à part.
- Les réponses avec skill sont 1,5 à 1,7 fois plus longues, et la note du juge augmente avec la longueur. Une partie de son gain peut donc venir de la longueur.
- Le juge est stable (0,05 d'écart entre ses deux passes), mais **il n'est pas calibré**. La règle du repo demande au moins 80 % d'accord avec 20 réponses notées à la main avant de l'utiliser comme mesure.
- Sur 3 skills, le juge ne voit aucun gain, ou un gain négatif : `ai-literacy-program` (−0,02), `system-prompt-and-guardrails` (−0,01) et `agent-knowledge-base` (−0,01 sur 3 passes). Ce sont de bons candidats pour une relecture à la main.

## 7. Le run local (Qwen 3.8 27B, jugé par Gemma 4 31B)

- **Statut :** en pause, avec 34 réponses valides sur 228. Les 194 autres seront refaites à la reprise. Le jugement par Gemma n'a pas encore tourné.
- **Montage :** une petite boucle d'agent qui imite `claude plugin eval`. Le modèle a un outil Skill (qui liste le skill seulement quand il est disponible) et un outil Read limité au dossier du skill. Les dossiers `evals/` ne sont pas lisibles, car ils contiennent des réponses modèles.
- **Incidents et corrections :**
  1. *Un biais en faveur des skills.* Au début, le côté sans skill n'avait aucun outil, alors que le prompt système mentionnait un outil Skill. Qwen s'arrêtait alors sur « je vais chercher un skill… » (8 à 53 mots). C'est corrigé : les deux côtés ont maintenant les mêmes outils, et la liste des skills est simplement vide sans le skill. Les 12 réponses biaisées ont été supprimées.
  2. *Un redémarrage d'Ollama* (changement du contexte à 16k) a fait échouer 194 réponses d'un coup. Désormais, le script attend jusqu'à 10 minutes si Ollama ne répond plus, puis s'arrête proprement. Les réponses en échec sont refaites à la reprise, et le jugement ne démarre que si toute la génération a réussi.
- **Mémoire :** Qwen occupe environ 27 Go sur 32 avec un contexte de 32k tokens, ce qui provoquait du swap. Le contexte est maintenant de 16k, ce qui suffit : le plus gros cas fait environ 13 000 tokens.
- **Premier signal** (`agent-design-and-tooling`, avant la correction du biais, donc à prendre avec précaution) : Qwen a déclenché le skill sur le cas négatif. C'est à vérifier quand le run sera repris.

## 8. Limites

- **Une seule passe par cas pour les 17 skills qui ont passé.** Leur verdict n'est pas confirmé sur 3 passes.
- **Les regex vérifient des mots, pas la qualité du conseil.** Le juge nuance le gain, mais il n'est pas calibré.
- **Environ 3 % des réponses avec skill** (7 sur 237) disent n'avoir pas pu lire un fichier du skill (« access denied ») dans l'environnement de test. C'est trop rare pour expliquer les échecs, mais ça retire parfois un template au modèle.
- **Le coût du juge Haiku n'a pas été mesuré.**

## 9. Prochaines étapes proposées

1. **`conversation-analysis`** (skill validé) : renforcer dans le skill la règle « masquer les données personnelles avant tout appel au modèle », puis relancer 3 passes.
2. **`ai-brand-positioning`** et **`process-ai-redesign`** : relire 2 ou 3 réponses pour savoir si c'est le skill ou le grader qui pèche sur `failure-behaviour` et `fallback-hours`.
3. **`agent-knowledge-base`** et **`ai-interaction-patterns`** : revoir leur description, pour qu'ils se déclenchent sur leur cas 003.
4. **Calibrer le juge** : noter 20 réponses à la main, à l'aveugle, puis comparer Haiku, Sonnet et Gemma sur les mêmes réponses.
5. **Reprendre le run Qwen** quand le Mac est libre, puis le juger avec Gemma.

## 10. Fichiers et commandes

| Dossier | Contenu |
| --- | --- |
| `eval-out/claude/` | Run à une passe : `answers/` (les 228 réponses, plus `runs.json`), `grades/`, `judge/` (scores et `cache.jsonl` des réponses brutes du juge), `report.md`, `run.sh` |
| `eval-out/claude-3runs/` | Run à trois passes, même structure |
| `eval-out/local/` | Run Qwen en pause |

Le dossier `eval-out/` n'est pas suivi par git.

Re-noter les réponses Claude avec un autre juge (pour la calibration), sur exactement les mêmes réponses :

```bash
.venv/bin/python scripts/local_evals.py grade --out eval-out/claude --judge gemma4:31b-mlx
```

Re-noter après une modification des graders (gratuit) :

```bash
.venv/bin/python scripts/local_evals.py grade --out eval-out/claude --no-judge && .venv/bin/python scripts/local_evals.py report --out eval-out/claude
```

Reprendre le run Qwen :

```bash
.venv/bin/python scripts/local_evals.py generate
```

**Changements dans le repo, commités avec ce rapport :**
- `scripts/local_evals.py` (nouveau) ;
- les options `-j` et `--max-cost` dans `scripts/run_evals.py` ;
- les 2 graders corrigés et les 3 nouvelles fixtures.
