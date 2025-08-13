issue title: When I format Liquid code with Shopify Liquid then it is replaced with empty code
labels: none
comment count: 1
hyperlink: https://github.com/shopify/theme-tools/issues/1004
status: open
date opened: 2025-07-16
repo 30d_merge_rate: 11

====

description:
**Describe the bug**

<!-- A clear and concise description of what the bug is. -->
When I format Liquid code using the Shopify Liquid formatter, the code is replaced with an empty block. This happens consistently and removes all the Liquid content. Please check the attached video for a demonstration of the issue.

**Source**

<!-- Please paste the source code that causes your problem -->
{% if product.available %}
  <p>{{ product.title }} is available.</p>
{% endif %}


**Expected behaviour**

<!-- Describe what you expect should happen -->
The Liquid code should be formatted cleanly and preserved—without removing or emptying it. I expect indentation or spacing fixes, but not code deletion.

**Actual behaviour**

<!-- Describe what actually happens -->
When I run the formatter (e.g., via VS Code or CLI), it removes all the code, leaving the file or snippet completely empty.

**Debugging information**

OS: Mac

OS Version: macOS 10.15.7

Theme Check Version: 1.15.0

Shopify Liquid Formatter: Shopify.theme-check-vscode



**Additional context**
When I format Liquid code with Shopify Liquid then it is replaced with empty code


https://github.com/user-attachments/assets/13f37172-dce6-406d-bebc-508c31d1c4f6


===

comment #1 by graygilmore, 2025-07-24, 16:15:39
@mdarifulislamroni521 would you mind trying this on the Dawn or Horizon themes and letting us know if you get the same behavior? Trying to determine if this is a broad issue or something related to your specific theme. Thanks!
