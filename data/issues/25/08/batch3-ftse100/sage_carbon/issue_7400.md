metadata {
link: https://github.com/Sage/carbon/issues/7400
labels: Bug, On Backlog
data opened: 2025-06-25T16:21:55Z
author: Chris3y
hyperlink: https://github.com/Sage/carbon/issues/7400
issue title: DialogFullscreen: Field warnings have insufficient colour contrast with grey background
}

issue description:
### Description

Warning messages on form inputs (when in a dialog) have insufficient contrast against their background, when in a dialog (which is usually a bit more grey than white in Sage Theme).

Important note: Axe tool is very inconsistent here and often misses this problem. You can still verify the contrast is insufficient, using browser dev tools and/or manually checking the contrast against standards (WCAG 2.1AA).

I've provided a sandbox where the problem can be verified but using Chrome or Firefox dev tools and/or [webaim-contrast-checker](https://webaim.org/resources/contrastchecker/?fcolor=BF5200FF&bcolor=F2F5F6).

### Reproduction

https://stackblitz.com/edit/parsium-carbon-starter-ebujaks2?file=src%2FApp.tsx

### Steps to reproduce

In most other areas there is a default background colour of #f8f9f9, which is a lighter grey with no contrast issues, so I’d suggest using that.

The full screen dialog background colour is set to #f2f5f6 (#f2f5f6ff / --colorsUtilityMajor025).

https://carbon.sage.com/?path=/docs/dialog-full-screen--default 

The hint text caution uses #bf5200  (#bf5200ff / --colorsSemanticCaution600), and this is a fail on the #f2f5f6 background: https://webaim.org/resources/contrastchecker/?fcolor=BF5200FF&bcolor=F2F5F6

But it will pass if used on a #f8f9f9 background.

### JIRA ticket numbers (Sage only)

_No response_

### Suggested solution

_No response_

### Carbon version

153.0.0

### React version

v18

### Design tokens version

_No response_

### Relevant browsers

Chrome

### Relevant OSs

Windows

### Additional context

_No response_

### Confidentiality

- [x] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **Parsium** (2025-07-01T13:35:41Z):
  Hi @Chris3y,

We previously discussed this with the Design System team, as many contrast issues were raised about the default grey background of `Dialog`. They revised the design to use a white background, which we adopted as the default colour. However, this does not seem to be the case for `DialogFullscreen`, so we will need to update it to align with the Frozen DS spec.

@harpalsingh are you happy with us making the default background colour of `DialogFullscreen` white?

- **harpalsingh** (2025-07-29T09:27:55Z):
  @Parsium we can't do that because there is a use case of both backgrounds still, so we need to look at the issue here on why the content on the dialog isnt in a tile, and we should ensure the color passes on the light grey as well as that use case can happen in the app on the light grey too.

- **harpalsingh** (2025-07-29T09:31:30Z):
  @Parsium @Chris3y will work with @ljemmo and we will bump the warning text token color slight, its .2 off, which visually wont even be noticeable but mathematically fix the contrast checker.

- **ljemmo** (2025-07-29T10:46:26Z):
  @harpalsingh FYI i brought the topic of the gray content area for dialogs and sidebar to the ECT as i know you were wanting to support light gray for notifications. The consensus at the time was to only support white bgs going forward as the BU reps felt that we could simplify to one color.

If you strongly disagree, i'd suggest raising it on the next ECT meeting next thursday or in the ECT slack channel. We recently added 'don't's to represent that decision on our DS docs

- **ljemmo** (2025-07-29T10:50:51Z):
  Additionallly, the new DS offers a warning text hex code that passes on grays, so once that new token is implemented, the contrast ratios will then pass on light grays as well as white. I suggest we close this issue to avoid duplicate fix tickets.

- **harpalsingh** (2025-08-11T13:46:47Z):
  @ljemmo Yes I can bring this up in the next ECT as I was not involved in the previous decisions.

- **ljemmo** (2025-08-11T14:28:18Z):
  @harpalsingh and @Chris3y - the hex code for warning text was #C93E08

- **harpalsingh** (2025-08-11T15:08:12Z):
  For reference this will be the updated visual to compare to current version.

<img width="740" height="335" alt="Image" src="https://github.com/user-attachments/assets/def0bc43-ec65-46f2-9073-cb5bc4997928" />

- **Parsium** (2025-08-11T15:34:24Z):
  FE-7444 - to update colour of warning text as per designs


