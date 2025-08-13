issue title: Screen reader does not announce the name for info (i) button in windows.
labels: bug
comment count: 2
hyperlink: https://github.com/stripe/stripe-js/issues/785
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
Screen Reader: NVDA (2025.1.2), JAWS, Narrator
URL: https://codepen.io/serena206/pen/Byaeyyb?editors=1001

**User Impact:**
Screen reader users will be impacted as won't get the purpose of the control if Screen reader does not announce the name for info (i) button in windows.

**Pre-Requisite:**

1. Turn on Screen Readers:
     NVDA: Ctrl + Alt + N
     JAWS: Ctrl + Alt + J
     Narrator: Ctrl + win + Enter
2. Verbosity:
     NVDA: Default
     JAWS: Beginner, Highest
     Narrator: Default

**Repro Steps:**

1. Open the URL: https://codepen.io/serena206/pen/Byaeyyb?editors=1001 in edge chromium browser.
2. Payment page will open. Press tab key to navigate to the 'Info (i)' button. 
3. Verify whether screen reader is announcing the name for info (i) button in windows or not.

**Actual Result:**
Screen reader does not announce the name for info (i) button in windows.
Screen reader announces as 'Button'

**Refer Attachment:**
1.Screen reader does not announce the name for info (i) button in windows.png
2.Screen reader does not announce the name for info (i) button in windows.mp4

https://github.com/user-attachments/assets/e922cf2f-3373-4a12-be79-c5ddcf6ccd07
<img width="969" height="539" alt="Image" src="https://github.com/user-attachments/assets/88e2bc7e-a7e6-4646-8a28-b5a210caf7c7" />

**Expected Result:**
Screen reader should announce the name as 'Info' for info (i) button in windows.

### Environment

Edge Chromium Version 138.0.3351.83 on Windows 11 24H2 (OS Build 26100.4652)

### Reproduction

https://codepen.io/serena206/pen/Byaeyyb?editors=1001

===

comment #1 by github-actions[bot], 2025-08-07, 02:17:06
This issue has been automatically marked as stale because it has not had recent activity. It will be closed if no further activity occurs. Thank you for your contributions.

comment #2 by msftedad, 2025-08-07, 09:34:21
Issue is still repro'ing. Please dont close this issue.
