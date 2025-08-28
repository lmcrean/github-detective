metadata {
link: https://github.com/Sage/carbon/issues/6192
labels: Bug, On Backlog, stale
data opened: 2023-07-12T14:13:27Z
author: amieedwards-sage
hyperlink: https://github.com/Sage/carbon/issues/6192
issue title: Dialog can't be accessed correctly by a screen reader
}

issue description:
### Current behaviour

Focus isn't being pulled to the `Dialog` properly, so the modal can't be accessed correctly by a screen reader.

### Martin Underhill’s findings in the Accessibility Audit:

There is a `tabindex="0"` on the dialog in, which I’m guessing is to set the focus on that element. This attribute is then removed dynamically when the user’s focus is shifted from the dialog element. 
This is nearly the right behaviour, however by doing this it creates a container that has to be ‘drilled’ down into with `VO + shift + down` when using VoiceOver.

The correct behaviour should be a simple `VO + right` to move into the dialog content.

This can be achieved by using `tabindex="-1"`, which doesn’t create a container that has to be drilled down into, and there’s no need to remove this attribute as it can’t be tabbed to by the user – it’s only for setting focus programmatically.

### Expected behaviour

When opening the Dialog component focus should be pulled and then using VoiceOver the user should be able to use the keyboard command `VO + →` to cycle through the elements within the modal.


### CodeSandbox or Storybook URL

https://cwf65m.csb.app

### JIRA Ticket (Sage Only)

SBS-47556

### Suggested Solution

### Chris Merrington Comments 12/07/23:

- Focus should be pulled to the dialog and contents can be reached via `VO + →`  without the need to use `VO + shift + down` (Looks like the preferred method for Martin)

or

- pull focus to an element inside the dialog (similar to the W3C example)

### Carbon Version

119.4.0

### Design Tokens Version

4.19.0

### What browsers are you seeing the problem on?

Safari

### What Operating System are you seeing the problem on?

MacOS

### Anything else we should know?

_No response_

### Confidentiality

- [X] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **tomdavies73** (2023-07-25T13:13:14Z):
  FE-6069

- **stale[bot]** (2025-04-26T14:40:20Z):
  This issue has been automatically marked as stale because it has not had recent activity. If you believe this issue is still valid and required please comment below. It will be reviewed by the core Carbon team and may be closed if no further activity occurs. Thank you for your contributions.


- **chriswaymansage** (2025-07-14T14:53:10Z):
  Can this be revisited please
It is needed for SBS-47556


