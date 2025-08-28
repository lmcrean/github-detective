metadata {
link: https://github.com/Sage/carbon/issues/6890
labels: Bug, On Backlog, Squad Nebula
data opened: 2024-08-08T14:39:15Z
author: johnb-sage
hyperlink: https://github.com/Sage/carbon/issues/6890
issue title: Link wrapping an image does not get focus styling on GlobalHeader
}

issue description:
### Description

An image wrapped in Link (e.g. a logo) is not styled when focused on GlobalHeader.

### Reproduction

https://stackblitz.com/edit/parsium-carbon-starter-hfnajo?file=src%2FApp.tsx

### Steps to reproduce

Tab to the Logo, no focus styling is applied.

Also note the focus styling on the text link, seems that box shadow is being incorrectly applied.

### JIRA ticket numbers (Sage only)

_No response_

### Suggested solution

_No response_

### Carbon version

141.4.4

### Design tokens version

_No response_

### Relevant browsers

Chrome

### Relevant OSs

MacOS

### Additional context

_No response_

### Confidentiality

- [X] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **Parsium** (2024-08-13T14:11:15Z):
  Thanks for raising this @johnb-sage 👍🏼 

May I check what styling you expect to see when the logo in the demo is focused? Have you received any specific designs for this? We assume the logo would require the standard gold focus ring, similar to this example:

<img width="214" alt="Screenshot 2024-08-13 at 15 08 26" src="https://github.com/user-attachments/assets/051d7488-4fed-47b6-8d06-a70ff09414d3">


- **johnb-sage** (2024-08-13T15:07:32Z):
  @Parsium I feel GlobalHeader wouldn't comfortably support the double focus ring. Since space is tight in this case a much thinner focus style might be more appropriate?

- **nineteen88** (2024-08-20T13:08:02Z):
  @harpalsingh Hey, would you be able to take a look at this and advise on what the focus border should look like. Thanks!

- **harpalsingh** (2024-09-04T10:25:04Z):
  @nineteen88 yep so this is the expectation of the focus on a logo visula, so its an internal version of the double border:

![Screenshot 2024-09-04 at 11 24 13](https://github.com/user-attachments/assets/2af9d2d6-04e4-4bb3-bec1-153e64885ffa)


- **nineteen88** (2024-09-10T13:30:36Z):
  FE-6802


