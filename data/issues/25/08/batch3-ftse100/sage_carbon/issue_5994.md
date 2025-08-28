metadata {
link: https://github.com/Sage/carbon/issues/5994
labels: Enhancement, On Backlog, flat-table
data opened: 2023-04-26T09:57:58Z
author: PaulSumner-Sage
hyperlink: https://github.com/Sage/carbon/issues/5994
issue title: FlatTable to have additional "FlatTableFooter" component
}

issue description:
### Desired behaviour

We have FLatTableHeader but no FlatTableFooter. Can this be added?

### Current behaviour

No ability to use Carbon components to add footer to a FlatTable.

### Suggested Solution

new component: FlatTableFooter which will wrap around FlatTableRow in a similar way to native <tfoot> usage

### CodeSandbox or Storybook URL

_No response_

### Anything else we should know?

### Confidentiality

- [X] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **Parsium** (2023-05-02T15:32:05Z):
  For future triage, currently we support a `footer` prop for `FlatTable`, which renders any passed node within a `<div>` inside the table. This allows us to render text or other components such as `Pager` just fine, but causes a visual bug when other `FlatTable` subcomponents like `FlatTableCell` or `FlatTableHeader` are passed. Support for these subcomponents would be useful to allow for patterns such as summary rows.

Creating a dedicated `FlatTableFooter` would be better for consistency with the other `FlatTable` subcomponents, but we need to clarify if Design System would want to restrict the content placed in the table footer.

- **clairedenning** (2023-06-06T09:59:37Z):
  @Parsium Would you be able to render a FlatTableFooter AND the Pager at the same time? It looks like that could be a requirement.


- **Parsium** (2023-06-06T12:57:15Z):
  Hi @clairedenning 👋🏼 I suppose you mean something like in the following image, where we could have pagination and custom content in the table footer?

![Screenshot 2023-06-06 at 13 50 52](https://github.com/Sage/carbon/assets/18368713/7b740487-c993-44d4-aca8-8d308d580d76)

We would be able to render anything in the footer, but we need to decide what kind of content to allow for - if we want to limit it to just summary rows and pagination, or if there is other content we would like to support.

- **clairedenning** (2023-06-06T16:49:27Z):
  I think for now, we're proposing just a summary row, and pagination. But that's not to say that in the future there might be a need for customised content.


- **clairedenning** (2023-06-07T15:01:12Z):
  Lisa Ying has added a grey "table footer row" to the table in Figma. The table can also have Pagination at the bottom.
https://www.figma.com/file/Tau6qv5iyr8wthWNqYktej/DS-Official-Components?type=design&node-id=31496%3A156711&t=HEEr4vsJdZKHoAlS-1 
![image](https://github.com/Sage/carbon/assets/49988488/53a75121-dff4-41a8-9e3b-f0dfea7fbe5f)


- **Parsium** (2023-06-08T08:52:19Z):
  Thanks for this @designerlisa @clairedenning! I'll go ahead and create a ticket for us then to implement this into Carbon 👍🏼 

- **Parsium** (2023-06-08T10:12:39Z):
  ~FE-6005~ FE-6186


