metadata {
link: https://github.com/Sage/carbon/issues/7497
labels: Bug, On Backlog
data opened: 2025-08-20T15:04:10Z
author: gusch
hyperlink: https://github.com/Sage/carbon/issues/7497
issue title: MenuItem: styles are not consistently computed so order they are applied can vary
}

issue description:
### Description

With Carbon v155.9.1, our menu is correctly displayed

<img width="524" height="62" alt="Image" src="https://github.com/user-attachments/assets/3b7d1303-8d77-492f-abe2-71d8f5610a26" />

With Carbon v155.10.0, it is misaligned

<img width="553" height="93" alt="Image" src="https://github.com/user-attachments/assets/ea255c69-f4e0-4b8c-92a7-c80fe376e70c" />

I can't reproduce in stackblitz.
Only thing i see is that the css rules are not in the same order.
On 155.9.1, padding: 11px 16px 10px is overriden by a padding: 0
In 155.10.0, it is the other way.

<img width="594" height="255" alt="Image" src="https://github.com/user-attachments/assets/c1f05f65-97da-4638-b723-6994482fe202" />


### Reproduction

https://stackblitz.com/edit/parsium-carbon-starter-3yjsyt5n?file=src%2Fmain.tsx,src%2FApp.tsx,package.json

### Steps to reproduce

_No response_

### JIRA ticket numbers (Sage only)

_No response_

### Suggested solution

_No response_

### Carbon version

155.10.0

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
- **edleeks87** (2025-08-26T10:49:38Z):
  FE-7456


