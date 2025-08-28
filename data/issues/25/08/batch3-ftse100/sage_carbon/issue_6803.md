metadata {
link: https://github.com/Sage/carbon/issues/6803
labels: Enhancement, On Backlog, More Information Required, Squad Nebula, drawer
data opened: 2024-06-28T08:28:42Z
author: elvis-iacobescu-sage
hyperlink: https://github.com/Sage/carbon/issues/6803
issue title: There is no way to add borders to a drawer component
}

issue description:
### Description

I have 2 components Breadcrumbs and a drawer component. The drawer has a 1px border top In the designs. Right now I have to do a workaround to be able to add a top border(`<Hr my={0} >`). We need a way to add borders to the box component or the drawer component designs.

### Suggested solution

Add a border to the box Component or the Drawer component, or create a specific component that would be able to add borders around existing components

### Demo URL

_No response_

### Alternatives

_No response_

### Additional context

_No response_

### Confidentiality

- [X] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **PaulSumner-Sage** (2024-07-01T12:37:41Z):
  I would suggest that the `<Drawer />` component work when not "fullscreen" in an app and has the option to have a top/bottom border when required instead of _another_ component required to make it look correct on a page

- **edleeks87** (2024-07-02T09:04:11Z):
  @ljemmo and @harpalsingh thoughts on updating the designs for Drawer to support the above?

- **ljemmo** (2024-08-06T14:52:18Z):
  @elvis-iacobescu-sage please can you share a design via slack or teams for us to understand what this change would mean visually?

- **nineteen88** (2024-08-20T13:12:36Z):
  @ljemmo @elvis-iacobescu-sage Hey both. Just chasing to see if you got anywhere further with this and if designs had been shared so a decision could be made? Thanks!

- **edleeks87** (2024-09-24T13:13:42Z):
  @ljemmo any updates?

- **nineteen88** (2024-10-08T13:20:43Z):
  @edleeks87 I believe @ljemmo was still waiting for a response from @elvis-iacobescu-sage regarding the designs so that a decision could be made. Elvis, would it be possible to pick this up with Luke when you get a moment? Thank you!

- **spookendiesel** (2024-10-08T13:29:38Z):
  This was the expected design from UX
(Screenshot  1 removed and added to ticket)

And this is how it looks with no top border
(Screenshot 2 removed and added to ticket)


- **ljemmo** (2024-10-09T08:17:57Z):
  ok thanks @spookendiesel - the request seems fair enough. @nineteen88 or @edleeks87  from a DS perspective happy to support this. In the newest DS version we offer standard and subtle border colors so i suggest we offer the same props here. Thoughts appreciated.

- **harpalsingh** (2024-10-09T08:21:38Z):
  @spookendiesel Do you know which designer provided that version of breadcrumbs and/or was this a requirement because the following design of breadcrumbs wasnt possible?

(Screenshot 3 removed and added to ticket)

@ljemmo We might want to consider if this is a border on the top of  the Drawer or its a border at the bottom of a container with the breadcrumbs first.


- **spookendiesel** (2024-10-09T08:50:32Z):
  > @spookendiesel Do you know which designer provided that version of breadcrumbs and/or was this a requirement because the following design of breadcrumbs wasnt possible?
> 
> @ljemmo We might want to consider if this is a border on the top of the Drawer or its a border at the bottom of a container with the breadcrumbs first.

@harpalsingh I think it was Dale Pealing. The original discussion can be found here 

(Link removed and added to ticket)

- **nicktitchmarsh** (2024-10-22T12:15:39Z):
  FE-6872

- **nicktitchmarsh** (2025-02-19T11:20:23Z):
  @ljemmo & @harpalsingh,

Do we need to support only the border variants, i.e. default would be the existing right/left border depending on orientation. Setting subtle will set the colour of the current default border as well as top and bottom? etc.

Or should we offer more granular control in terms of setting top, left, right and bottom borders independently?

- **ljemmo** (2025-02-19T13:11:07Z):
  IMo i can't see a usecase for granular border control. Setting borders based on the orientation makes sense to me.

- **harpalsingh** (2025-06-18T11:54:59Z):
  So "Orientation" isnt really a thing with Drawer, its more about if its against the edge of something. I feel wel should allow turning on borders left/right/top and bottom as needed, because the usage can vary on which edge is against something with a border or component. Allowing that flexibility gives it better usage.


