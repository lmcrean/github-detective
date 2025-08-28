metadata {
link: https://github.com/Sage/carbon/issues/6101
labels: Bug, On Backlog, draggable, popover-container
data opened: 2023-06-07T16:11:42Z
author: sage-syfre
hyperlink: https://github.com/Sage/carbon/issues/6101
issue title: Drag and drop broken when a popover is on the page
}

issue description:
### Current behaviour

Since version 107.1.0
When a popover is on a page, useDrag() of react-dnd is not working anymore
It's OK with version 107.0.0
It's OK with version 107.1.0 if I remove all the popovers from the page.
I suspect that the ClickAwayWrapper introduced in release 107.1.0 and used in the popover component prevents the drag operation to begin
 

### Expected behaviour

Working drag operation

### CodeSandbox or Storybook URL

https://carbon.sage.com/?path=/docs/popover-container--default

### JIRA Ticket (Sage Only)

_No response_

### Suggested Solution

In popover-container.component.tsx

line 215 :
  //const handleClick = useClickAwayListener(handleClickAway, "mousedown");
  const handleClick = useClickAwayListener(handleClickAway, isOpen?"mousedown":"");

### Carbon Version

118.5.2

### Design Tokens Version

_No response_

### What browsers are you seeing the problem on?

Firefox, Chrome

### What Operating System are you seeing the problem on?

Windows

### Anything else we should know?

I don't reproduce with your DraggableContainer in your storybook

Probably related to this one :
https://github.com/Sage/carbon/issues/6066

### Confidentiality

- [X] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **DipperTheDan** (2023-06-13T13:25:05Z):
  FE-6010

- **nicktitchmarsh** (2023-06-14T10:33:46Z):
  @sage-syfre, are you implementing your own drag behaviour with react-dnd? We can investigate but we need a reproducible example in codesandbox ideally. Please also bare in mind that drag-and-drop isn't considered accessible on its own and isn't a recommended pattern. 

- **nicktitchmarsh** (2025-01-20T15:45:21Z):
  FE-6907 is removing our dependency on react-dnd. This should address this error


