issue title: Luminosity ratio of the text is less than required 4.5:1 under the scan 'cash app pay' popup.
labels: bug
comment count: 2
hyperlink: https://github.com/stripe/stripe-js/issues/783
status: open
date opened: 2025-07-15
repo 30d_merge_rate: 12

====

description:
### What happened?

**Test Environment:** 
OS: Windows 11 Enterprise Insider Preview Version 24H2(OS Build 26100.4349) 
Browser Edge Version: 138.0.3351.77 (Official build) (64-bit)
Tool: Accessibility insights for windows

**User Impact:**
If the color contrast ratio of text is less than the minimum required ratio of 4.5:1, then users with low vision will find it difficult to read the text properly and not able to understand the information which that text conveys and get disoriented.

**Steps to Repro:**

1. Open URL: https://site-f51sq.powerappsportals.com/?stepid=99ae0891-8aaa-4d1d-afcc-75e37ec374dain latest edge browser.
2. Company page will be opened.
3. Press tab key to reach 'Cost edit field' and provide input.
4. Press tab key to reach 'Next button' and activate with enter key.
5. Step-2 page will be opened > Press tab key to reach 'Card' and use right arrow key to reach 'Cash app pay' and activate with enter key.
6. Press tab key to reach 'Pay now button' and activate with enter key.
7. Scan pop up will be displayed.
8. Verify luminosity ratio of text is meeting required ratio or not.

**Actual Result:**
Luminosity ratio of the text is 3.3:1 which is less than required ratio of 4.5:1 in windows.

**Refer Attachment:**
1.The luminosity ratio of the text is 3.31 which is less than required ratio of 4.51 in windows.png
2.The luminosity ratio of the text is 3.31 which is less than required ratio of 4.51 in windows.mp4

<img width="960" height="579" alt="Image" src="https://github.com/user-attachments/assets/16e640ad-fd18-4675-b93e-6037425ff6d0" />
https://github.com/user-attachments/assets/84c3b4e9-0023-484e-a744-932fb5f7a897


**Expected Result:**
Luminosity ratio of the text should be more or equal to 4.5:1 in windows.

### Environment

Browser Edge Version: 138.0.3351.77 on Windows 11 Enterprise Insider Preview Version 24H2(OS Build 26100.4349) 

### Reproduction

https://site-f51sq.powerappsportals.com/?stepid=99ae0891-8aaa-4d1d-afcc-75e37ec374da

===

comment #1 by github-actions[bot], 2025-08-05, 02:17:13
This issue has been automatically marked as stale because it has not had recent activity. It will be closed if no further activity occurs. Thank you for your contributions.

comment #2 by msftedad, 2025-08-05, 09:11:19
Issue is still repro'ing. Please dont close this issue.
