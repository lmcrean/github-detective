pull all the open issues from these 4 repos

Sage,carbon,https://github.com/Sage/carbon,2025-08-28,0,292,TypeScript,77,28,52.5
rropen,terraform-provider-cscdm,https://github.com/rropen/terraform-provider-cscdm,2025-08-15,13,0,Go,10,2,6.0
GSK-Biostatistics,docorator,https://github.com/GSK-Biostatistics/docorator,2025-08-28,0,0,R,10,1,5.5
elsevierlabs-os,linked-data,https://github.com/elsevierlabs-os/linked-data,2025-08-14,14,34,TypeScript,9,1,5.0


and output in this dir.

use subdirs e.g. 

sage_carbon/
rropen_terraf/
GSK-Bio_docorat/
elsevier_linked-d/

in each subdir show 1 file per issue

must be an OPEN issue

in each issue .md file show

metadata {
link
labels
data opened
author
hyperlink
issue title
}
issue description

comments (list all)


use .env in the root to increase github api rate limits

check scripts/* for useful existing python code that might help