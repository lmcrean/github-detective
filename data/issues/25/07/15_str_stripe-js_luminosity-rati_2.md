issue title: Luminosity ratio of the focus indicator on 'x' button is less than required 3:1 ratio on the 'scan ....' popup.
labels: bug
comment count: 2
hyperlink: https://github.com/stripe/stripe-js/issues/779
status: open
date opened: 2025-07-15
repo 30d_merge_rate: 12

====

description:
### What happened?

**Test Environment:** 
OS: Windows 11 Enterprise Insider Preview Version 24H2(OS Build 26100.4349)
Browser Edge Version: 138.0.3351.77 (Official build) (64-bit)
Tool: Accessibility insights for windows.

**User Impact:**
Low vision users will be impacted if the luminosity ratio of keyboard focus indicator is less than minimum required contrast ratio as users will not be able to identify the keyboard focus on the screen and will not be able to navigate properly.

**Steps to Repro:**

1. Open URL: https://site-f51sq.powerappsportals.com/?stepid=99ae0891-8aaa-4d1d-afcc-75e37ec374da in latest edge browser.
2. Company page will be opened.
3. Press tab key to reach 'Cost edit field' and provide input.
4. Press tab key to reach 'Next button' and activate with enter key.
5. Step-2 page will be opened > press tab key to reach 'card' and use right arrow key to reach 'Cash app pay' and press enter key.
6. Press tab key to reach 'Pay now button' and press enter key.
7. Scan pop will be displayed.> press tab key to reach 'Close' button.
8. Verify whether luminosity ratio of focus indicator on 'X' button is meeting required ratio or not.

**Actual Result:**
Luminosity ratio of the focus indicator on 'x' button is 1.8:1 which is less than required ratio of 3:1 on the 'scan ....' popup.

**Refer Attachment:**
1.Luminosity ratio of the focus indicator on 'x' button is less than required 31 ratio on the 'scan ....' popup.png
2.Luminosity ratio of the focus indicator on 'x' button is less than required 31 ratio on the 'scan ....' popup.mp4

https://github.com/user-attachments/assets/4359af9a-a3f2-45e4-8e8a-20f37a7aaef2
<img width="960" height="594" alt="Image" src="https://github.com/user-attachments/assets/d4c920d2-ac50-4ea7-b5a4-4aa89d1bd762" />

**Expected Result:** 
Luminosity ratio of the focus indicator on 'x' button should be more or equal to 3:1.

### Environment

Edge Version: 138.0.3351.77 (Official build) (64-bit)

### Reproduction

https://site-f51sq.powerappsportals.com/?stepid=99ae0891-8aaa-4d1d-afcc-75e37ec374da

===

comment #1 by github-actions[bot], 2025-08-05, 02:17:19
This issue has been automatically marked as stale because it has not had recent activity. It will be closed if no further activity occurs. Thank you for your contributions.

comment #2 by msftedad, 2025-08-07, 09:49:34
Issue is still repro'ing. Please don't close this issue.
