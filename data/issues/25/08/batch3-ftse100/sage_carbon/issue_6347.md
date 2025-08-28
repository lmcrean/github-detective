metadata {
link: https://github.com/Sage/carbon/issues/6347
labels: Bug, On Backlog, stale
data opened: 2023-10-04T12:49:29Z
author: kohli-pratik-sage
hyperlink: https://github.com/Sage/carbon/issues/6347
issue title: Select options cannot be wrapped in a custom component
}

issue description:
### Current behaviour

When `<Option />` is wrapped within a custom wrapper component and used in `<Select />`, a TypeScript error is seen and if wrapped in a fragment, transform styles are not applied resulting in all options to sit on top of each other.

TS error:
```
'<wrapping-component>' cannot be used as a JSX component.
  Its return type 'Element | Element[] | null' is not a valid JSX element.
    Type 'Element[]' is missing the following properties from type 'ReactElement<any, any>': type, props, keyts(2786)
```

This is not the case if a function is used to return the `<Option />` JSX and is called within the `<Select />`.

Use-case:
For situations where the content within the `<Select />` is api dependant, either Options or a api error message will be shown. In this situation and where the logic to render the appropriate element(s) could be complex/include multiple conditions, it would good to have the ability to separate the logic from the Select and into a wrapping component, in case it helps with readability.

### Expected behaviour

The wrapping component is rendered as expected within the `<Select />`.

### CodeSandbox or Storybook URL

https://codesandbox.io/s/jovial-waterfall-shkx3v?file=/src/App.tsx

### JIRA Ticket (Sage Only)

_No response_

### Suggested Solution

_No response_

### Carbon Version

120.5.0

### Design Tokens Version

4.25.0

### What browsers are you seeing the problem on?

Microsoft Edge

### What Operating System are you seeing the problem on?

MacOS

### Anything else we should know?

_No response_

### Confidentiality

- [X] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **nineteen88** (2023-10-10T13:25:11Z):
  FE-6239

- **stale[bot]** (2025-04-26T14:40:18Z):
  This issue has been automatically marked as stale because it has not had recent activity. If you believe this issue is still valid and required please comment below. It will be reviewed by the core Carbon team and may be closed if no further activity occurs. Thank you for your contributions.



