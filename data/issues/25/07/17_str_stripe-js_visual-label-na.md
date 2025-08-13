issue title: Visual label names are not descriptive for Expiration combo box in windows.
labels: bug
comment count: 2
hyperlink: https://github.com/stripe/stripe-js/issues/786
status: open
date opened: 2025-07-17
repo 30d_merge_rate: 12

====

description:
### What happened?

**Test Environment:**
OS: Windows 11 24H2 (OS Build 26100.4652)
Application Name: Microsoft Build Registration 2025
Browser: Edge Chromium Version 138.0.3351.83 (Official build) (64-bit)
URL: https://codepen.io/serena206/pen/azzNGZW

**User Impact:**
Cognitive users will be impacted by the lack of descriptive labels for Expiration combo boxes, as it can cause confusion and difficulty in accurately selecting the correct expiration date.

**Repro Steps:**

1. Open the URL: https://codepen.io/serena206/pen/azzNGZW in edge chromium browser.
2. 'Credit Card Details' page will open. Press tab key to navigate to the 'Expiration Date' combo box.
3. Verify whether Visual label names are descriptive for Expiration combo box or not.

**Actual Result:**
Label names are not descriptive for Expiration combo boxes. Date, Month and Year labels are not provided for those combo boxes.

**Refer Attachment:**
1. Visual label names are not descriptive for Expiration combo box in windows.png
2. Visual label names are not descriptive for Expiration combo box in windows.mp4

https://github.com/user-attachments/assets/10cd1e29-d030-4285-9809-5bdee97750c4
<img width="969" height="520" alt="Image" src="https://github.com/user-attachments/assets/9b3dc9bf-7c71-4fcd-a967-f463f9e30a4d" />

**Expected Result:**
Date, Month and Year label names should be provided for those combo boxes under Expiration section.

### Environment

Edge Chromium Version 138.0.3351.83 on Windows 11 24H2 (OS Build 26100.4652)

### Reproduction

https://codepen.io/serena206/pen/azzNGZW

===

comment #1 by github-actions[bot], 2025-08-07, 02:17:05
This issue has been automatically marked as stale because it has not had recent activity. It will be closed if no further activity occurs. Thank you for your contributions.

comment #2 by msftedad, 2025-08-07, 09:35:02
Issue is still repro'ing. Please don't close this issue.
