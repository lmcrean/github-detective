metadata {
link: https://github.com/Sage/carbon/issues/6263
labels: Bug, On Backlog, stale
data opened: 2023-08-17T13:37:05Z
author: edleeks87
hyperlink: https://github.com/Sage/carbon/issues/6263
issue title: Issues with scrollbar layout when FlatTable has sticky header
}

issue description:
### Current behaviour

The scrollbar stretches the length of the table wrapper when the table is scrollable, this is because the overflow is on the wrapper container

### Expected behaviour

Scrollbar should be on the body when there is a sticky header but on the wrapper when there isn't but the table is scrollable 

### CodeSandbox or Storybook URL

https://carbon.sage.com/?path=/docs/flat-table--with-sticky-head

### JIRA Ticket (Sage Only)

_No response_

### Suggested Solution

We can likely remove some of the complexity on the sticky header functionality as if it is outside the scrollable container it will be sticky and multiple rows will stack by default

### Carbon Version

latest

### Design Tokens Version

latest

### What browsers are you seeing the problem on?

Firefox, Chrome, Safari, Microsoft Edge

### What Operating System are you seeing the problem on?

MacOS

### Anything else we should know?

_No response_

### Confidentiality

- [X] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **edleeks87** (2023-08-22T13:07:44Z):
  FE-6186

- **camilledegomme** (2023-09-20T15:09:02Z):
  @edleeks87 just curious, is there any ETA on this request?


- **edleeks87** (2023-10-17T08:44:44Z):
  @camilledegomme sorry I missed this. I'll bump the priority on it so it'll be picked up in the next sprint hopefully. I needed to discuss with DS as it requires some redesign around how some of the sticky headers/footers etc work so we needed to to agree on that first.

- **camilledegomme** (2023-11-15T14:47:30Z):
  @edleeks87 just curious, do you have any update?

- **camilledegomme** (2024-01-11T10:22:57Z):
  @edleeks87 , do you have an update?


- **edleeks87** (2024-03-27T11:56:45Z):
  Hi @camilledegomme sorry I missed that you'd tagged me. I've sent a POC to UX for what this change would look like as adding this in would mean we'd need to remove some features we currently support, such as supporting having the header and footer independently sticky. I'll chase this up with them, we've refined the ticket so once they okay it we can pull it into sprint

- **stale[bot]** (2025-04-26T14:40:13Z):
  This issue has been automatically marked as stale because it has not had recent activity. If you believe this issue is still valid and required please comment below. It will be reviewed by the core Carbon team and may be closed if no further activity occurs. Thank you for your contributions.



