metadata {
link: https://github.com/Sage/carbon/issues/7310
labels: Enhancement, On Backlog
data opened: 2025-04-22T10:57:01Z
author: StephenArthur
hyperlink: https://github.com/Sage/carbon/issues/7310
issue title: Add customisable styling to SettingsRow title
}

issue description:
### Description

Currently, when using the SettingsRow component, the title can only be customised via the headingType prop. This is very limiting currently when trying to implement UX designs as it causes accessibility issues.


### Suggested solution

Currently the Typography component allows for text to be formatted in alternate styles, for example an h2 heading in the style of an h5 heading:
` h2TypographyProps={ { variant: 'h5', fontWeight: 'var(--fontWeights500)', as: 'h2' } }` 

If SettingsRow could receive a prop that could achieve the same effect - e.g. headingProps - this would be ideal.

### Demo URL

https://stackblitz.com/edit/parsium-carbon-starter-ae2hbv6q?file=src%2Fmain.tsx,src%2FApp.tsx

### Alternatives

I understand that Carbon already support custom titles in Accordion so that functionality could also be reflected in SettingsRow.

### Additional context

_No response_

### Confidentiality

- [x] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **damienrobson-sage** (2025-04-22T13:07:25Z):
  FE-7216


