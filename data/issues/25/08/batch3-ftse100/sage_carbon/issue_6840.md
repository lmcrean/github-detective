metadata {
link: https://github.com/Sage/carbon/issues/6840
labels: Bug, On Backlog, select
data opened: 2024-07-18T10:04:23Z
author: Harveyhoward
hyperlink: https://github.com/Sage/carbon/issues/6840
issue title: Multi-select remove option once selected 
}

issue description:
### Description

The multi select component when interacted with drops down all potential options. Once an option is selected from the drop down it is added to the "please select field" but remains an unusable option in the dropdown list.
I would expect that once an options is selected it is removed from the options list.
Why? If a user has a number of options with similar names it can become confusing to know which had been added, shortening the options list dynamically resolves this.

### Reproduction

https://carbon.sage.com/?path=/docs/select-multiselect--docs

### Steps to reproduce

_No response_

### JIRA ticket numbers (Sage only)

_No response_

### Suggested solution

_No response_

### Carbon version

125.1.1

### Design tokens version

_No response_

### Relevant browsers

Chrome, Safari

### Relevant OSs

MacOS

### Additional context

_No response_

### Confidentiality

- [X] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **edleeks87** (2024-07-18T10:27:11Z):
  @harpalsingh @ljemmo we discussed this on slack with @Harveyhoward and @tempertemper (I'll send the thread to you on there). Is this something DS/product want to add? We'd need to do I a fairly comprehensive rewrite as the current iteration relies heavily on the selected options being in the list to generate the Pill values so if it's a yes it might be more manageable to include this feature in the future rewrite we do for our Select components but in the interim we wondered if adding some form of option highlighting might be a good addition for now (see below for examples in other libs)?

https://mui.com/material-ui/react-select/#multiple-select
https://ant.design/~demos/select-demo-automatic-tokenization

- **ljemmo** (2024-07-19T14:15:49Z):
  @edleeks87 on my end i'll create a ticket for us to review the entire component and get back to you with a review. @ingridzillinger  FYI.


open issue for you guys here: number 74 on DS board



- **edleeks87** (2024-07-23T13:15:00Z):
  No problem we're happy to wait for the outcome of the above to be decided

- **nicktitchmarsh** (2024-09-03T15:13:06Z):
  FE-6311


