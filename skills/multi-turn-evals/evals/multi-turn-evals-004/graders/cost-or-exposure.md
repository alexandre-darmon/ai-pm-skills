---
type: regex  # prices the run in calls, or the exposure at 25,000 conversations a month
pattern: '\b\d{1,3}([ ,.]\d{3})+ (model |LLM |API |assistant )?calls|(scenarios?|conversations?)[^\n]{0,30}(×|x|\*)[^\n]{0,30}(×|x|\*)[^\n]{0,30}(turns?|messages?|calls)|25[ ,.]?000[^\n]{0,40}(×|x|\*)|(×|x|\*)[^\n]{0,20}25[ ,.]?000'
flags: i
---
