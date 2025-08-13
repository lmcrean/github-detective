issue title: RemoteAsset shouldn't throw for hash URLs
labels: none
comment count: 0
hyperlink: https://github.com/shopify/theme-tools/issues/982
status: open
date opened: 2025-06-13
repo 30d_merge_rate: 11

====

description:
**Describe the bug**

That's a perfectly valid URL. 

![Image](https://github.com/user-attachments/assets/dc7a1ce2-a892-4718-8a63-358e374dc0de)

**Source**
<!-- Please paste the source code that causes your problem -->
```liquid
    <link
      rel="expect"
      href="#MainContent"
      blocking="render"
      id="view-transition-render-blocker"
    >
```

**Expected behaviour**
No error. URLs that start with `#` are links to anchors on the page. This is not a remote URL as it is a link to the same page. 

**Actual behaviour**
Error

===
