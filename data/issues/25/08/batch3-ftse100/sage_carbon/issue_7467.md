metadata {
link: https://github.com/Sage/carbon/issues/7467
labels: Enhancement, On Backlog
data opened: 2025-07-30T10:56:03Z
author: karol-miernik-sage
hyperlink: https://github.com/Sage/carbon/issues/7467
issue title: Enable prop to disable focus on FlatTable
}

issue description:
### Description

To meet accessibility point raised by the Sage Design team together with Sage Accessibility team, we would like to have an option to disable focus on FlatTable. This is needed as when non interactive elements are in FlatTable, we don't want focus to be enable on whole FlatTable.  

### Suggested solution

Add prop that can control FlatTable focus (enabled by default, disabled as on option).

### Demo URL

_No response_

### Alternatives

_No response_

### Additional context

_No response_

### Confidentiality

- [x] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **nineteen88** (2025-08-06T09:04:25Z):
  Hi @karol-miernik-sage - can I just get some clarity on exactly what it is you are wanting/needing here? You need a way to disable focus entirely on Flat Table so you can bypass for it a certain reason? Feel free to message me on Slack to provide your use case so we can make sure this is something we want to support. Thank you!

- **karol-miernik-sage** (2025-08-12T13:18:09Z):
  @nineteen88 
Hi,
On the product that we are building, there is a requirement to disable flat-table from being focusable as it is not interactive (there is no action/button on it just contain some data)

 What we want to achieve to disable that element from being focused via keyboard navigation.

- **tomdavies73** (2025-08-19T13:49:21Z):
  FE-7454


