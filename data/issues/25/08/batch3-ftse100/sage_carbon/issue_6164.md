metadata {
link: https://github.com/Sage/carbon/issues/6164
labels: Bug, On Backlog, stale
data opened: 2023-06-29T12:12:39Z
author: hagad
hyperlink: https://github.com/Sage/carbon/issues/6164
issue title: Axe Issue with Dialog component having a scrollbar
}

issue description:
### Current behaviour

There is an Axe issue on the Dialog component with a scrollbar (need resize it)

### Expected behaviour

We should not have an axe issue. 

### CodeSandbox or Storybook URL

https://codesandbox.io/s/hopeful-kalam-tgzvs3?file=/src/App.js&resolutionWidth=1024&resolutionHeight=765 https://tgzvs3.csb.app/

### JIRA Ticket (Sage Only)

_No response_

### Suggested Solution

_No response_

### Carbon Version

119.3.3

### Design Tokens Version

_No response_

### What browsers are you seeing the problem on?

Chrome

### What Operating System are you seeing the problem on?

MacOS

### Anything else we should know?

<img width="1308" alt="Capture d’écran 2023-06-29 à 14 13 11" src="https://github.com/Sage/carbon/assets/17086956/3c8bf7b4-b48d-4e39-90db-2a27c8519c81">



### Confidentiality

- [X] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **robinzigmond** (2023-06-29T12:37:44Z):
  Note that the above issue about an iframe is I think a CodeSandbox artifact, which I cannot reproduce. The actual issue which I can reproduce, and which made me ask this to be raised as a Github issue, is the one below, which occurs whenever dialog requires scrollbars and has no focusable content: 
![image](https://github.com/Sage/carbon/assets/25186376/bf135c13-aff6-440e-b0e1-604aa23f95ca)


- **edleeks87** (2023-07-04T13:13:31Z):
  FE-6043

- **stale[bot]** (2025-04-26T14:40:23Z):
  This issue has been automatically marked as stale because it has not had recent activity. If you believe this issue is still valid and required please comment below. It will be reviewed by the core Carbon team and may be closed if no further activity occurs. Thank you for your contributions.



