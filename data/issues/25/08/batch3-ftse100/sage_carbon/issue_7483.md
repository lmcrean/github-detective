metadata {
link: https://github.com/Sage/carbon/issues/7483
labels: Bug, On Backlog
data opened: 2025-08-13T14:42:55Z
author: darceykelly
hyperlink: https://github.com/Sage/carbon/issues/7483
issue title: Background is enabled when Responsive Vertical Menu is open
}

issue description:
### Description

When the Responsive Vertical Menu is open, the background is still enabled, has a hover state and buttons/links can be activated. This happens for the 700px breakpoint and above. 

Additionally, for under the 700px breakpoint, when the Responsive Vertical Menu is open, focus is not pulled to the menu and instead will go to the elements behind first then onto the menu. 

### Reproduction

https://stackblitz.com/edit/parsium-carbon-starter-jchqovxf?file=src%2FApp.tsx

### Steps to reproduce

Open Responsive Vertical Menu on a screen over 700px and click the button. 
Open Responsive Vertical Menu on a screen under 700px and tab through. 

### JIRA ticket numbers (Sage only)

SBS-142269
SBS-142208

### Suggested solution

_No response_

### Carbon version

155.5.1

### React version

v17

### Design tokens version

_No response_

### Relevant browsers

Chrome

### Relevant OSs

MacOS

### Additional context

_No response_

### Confidentiality

- [x] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **edleeks87** (2025-08-14T09:35:47Z):
  @tempertemper @harpalsingh can I clarify if trapping focus and disabling the background is the right approach for all states of the menu when it's open (ie at small and large viewports)

- **harpalsingh** (2025-08-14T09:50:32Z):
  I would only expect the focus trap to be valid when the modal view is shown, the fact you can interact with the button above 700px is by design, as it should just close the open menu.

- **harpalsingh** (2025-08-14T09:55:54Z):
  As noted though we need to fix the focus and keyboard trap, but on that need to check if that works as expected in our app? as I would expect the user can navigate the browser still, so is this just an issue in the demo? so might be just focus needs to be applied correctly and the focus order is working fine?

- **tomdavies73** (2025-08-19T13:34:44Z):
  Hi @harpalsingh, what do you recommend are our actions going forward here?

- **harpalsingh** (2025-08-21T07:39:46Z):
  @tomdavies73 I would say we need to investigate how we ensure how when a user clicks outside the open nav it closes and doesnt trigger the action on whatever component, it might mean we need an invisible modal thats clicked?

As for the version just ensure when keyboard activated the first focus is the first item in the menu?

- **amieedwards-sage** (2025-08-27T14:38:31Z):
  @harpalsingh @tomdavies73 Are there any updates on the right solution here?

- **edleeks87** (2025-08-27T15:26:46Z):
  @amieedwards-sage I've chatted to @harpalsingh, we're going to add a focus trap when the sidebar adapts at low resolutions to a modal. When that happens if focus isn't currently in the sidebar we'll move it to the wrapper (default behaviour for focus traps)

- **edleeks87** (2025-08-27T15:30:15Z):
  FE-7458


