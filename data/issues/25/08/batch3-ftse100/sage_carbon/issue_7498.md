metadata {
link: https://github.com/Sage/carbon/issues/7498
labels: Enhancement, triage
data opened: 2025-08-20T16:50:08Z
author: PaulSumner-Sage
hyperlink: https://github.com/Sage/carbon/issues/7498
issue title: [Profile] Make email prop possible to not be a mailTo link
}

issue description:
### Description

There are times we want to use the [Profile] component to show the current user their own information. There's little value in a mailTo link of their own email address: can we have a prop/option added to show the email in plain text instead of a link?

### Suggested solution

prop or other option to toggle email being a link

### Demo URL

https://carbon.sage.com/?path=/docs/profile--docs

### Alternatives

_No response_

### Additional context

_No response_

### Confidentiality

- [x] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **edleeks87** (2025-08-26T10:42:40Z):
  @ljemmo @harpalsingh can I just check we're happy to action this feature request?

- **ljemmo** (2025-08-26T12:24:45Z):
  @edleeks87 it looks like the profile component inside the Beta DS supports the ability to switch off and on the link text and/or passing on plain text. We also support the ability to pass in custom child content.

<img width="353" height="155" alt="Image" src="https://github.com/user-attachments/assets/ecc6b179-d74d-4cdc-b079-be7f8267562a" />
<img width="236" height="181" alt="Image" src="https://github.com/user-attachments/assets/243816fc-57aa-4d26-8c40-93c67ccfe159" />

I'd suggest we add a profile / portrait ticket to the audit backlog that covers all this. 




