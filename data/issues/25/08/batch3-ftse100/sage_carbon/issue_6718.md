metadata {
link: https://github.com/Sage/carbon/issues/6718
labels: Bug, On Backlog, Best Practices - Accessibility, stale, Squad Vortex, select
data opened: 2024-05-06T08:42:10Z
author: justin-rankin
hyperlink: https://github.com/Sage/carbon/issues/6718
issue title: Select + Grouped Options - Critical AXE issue: ARIA roles contain invalid children
}

issue description:
### Description

For Carbon [**Select dropdown menu with grouped Options**](https://carbon.sage.com/?path=/docs/select--docs#option-groups):
**AXE DevTools** _correctly_ displays what is flagged as a **_critical_** accessibility issue:

**_"Certain ARIA roles must contain particular children"_**


![h4-CRITICAL-AXE](https://github.com/Sage/carbon/assets/79138818/a6d7f8a1-fdbd-49b9-b9ec-ee7f6c05caaa)

---

This critical issue is being caused by Carbon's rendering of the **`<h4>`** tag in the DOM, as a sibling to of the list of (correct) **`<li>`**  node, that are the only valid children of the parent **`<ul>`** tag...

```html
<ul>
  <h4>Group - A</h4> <!--- 👈🏼 invalid child DOM node --> 
  <li>Option A1</li>
  <li>Option A2</li>
  <li>Option A3</li>
  <h4>Group - B</h4> <!--- 👈🏼 invalid child DOM node --> 
  <li>Option B1</li>
  <li>Option B2</li>
  <li>Option b3</li>
</ul>
```

![h4-in-DOM](https://github.com/Sage/carbon/assets/79138818/d5663173-73c6-47cb-a8a0-8864e5cb6705)


---

Even if **`<h4>`** is wrapped inside of a **`<li>`** tag, **AXE** still gives an accessibility warning about semantical order of the heading **`<h1...h5 />`** tags, though the warning level which is no longer **critical**.

---



### Reproduction

https://carbon.sage.com/?path=/docs/select--docs#option-groups

### Steps to reproduce

This is produced simply by using the documented **`<OptionGroupHeader />`** component among the array of **`<Option />`** components, when implementing the **`<Select />`**, which purpose is to visually and group options via a bold non-option, non-clickable heading..

### JIRA ticket numbers (Sage only)

SBS-92771

### Suggested solution

In order to avoid this AXE warning, perhaps the **`<OptionGroupHeader />`** component could:

- wrap the heading in a **`<li>`** tag, to ensure all _direct_ children of **`<ui>`** are correctly **`<li>`**
- for the heading text, using a strong, heavier weight without actually using **`<h4>`** to avoid the semantic ordering issue (check accessibility guidelines for this)

### Carbon version

v134.0.0 (latest, and older versions)

### Design tokens version

_No response_

### Relevant browsers

Firefox, Chrome, Safari, Microsoft Edge

### Relevant OSs

MacOS, Windows, Linux

### Additional context

_No response_

### Confidentiality

- [X] I confirm there is no confidential or commercially sensitive information included.

comments (list all):
- **nineteen88** (2024-05-07T13:45:37Z):
  FE-6571

- **DipperTheDan** (2024-05-08T09:55:50Z):
  I'll be addressing this as part of the work in ticket FE-6285.

- **stale[bot]** (2025-07-19T05:06:50Z):
  This issue has been automatically marked as stale because it has not had recent activity. If you believe this issue is still valid and required please comment below. It will be reviewed by the core Carbon team and may be closed if no further activity occurs. Thank you for your contributions.



