issue title: Luminosity ratio of the focus indicator on 'country' is less than required ratio of 3:1.
labels: bug
comment count: 2
hyperlink: https://github.com/stripe/stripe-js/issues/782
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
Low vision users will be impacted if the luminosity ratio of keyboard focus indicator is less than minimum required contrast ratio as users will not be able to identify the keyboard focus on the screen and will not be able to navigate properly.

**Steps to Repro:**

1. Open URL: https://site-f51sq.powerappsportals.com/?stepid=99ae0891-8aaa-4d1d-afcc-75e37ec374da in latest edge browser.
2. Company page will be opened.
3. Press tab key to reach 'Cost edit field' and provide input.
4. Press tab key to reach 'Next button' and activate with enter key.
5. Step-2 page will be opened > Press tab key to reach 'Card details' session and provide details.
6. Optional details will be added > press tab key to reach 'Country combo box'.
7. Verify whether luminosity ratio of the focus indicator on 'country' is meeting required ratio or not.

**Actual Result:**
Luminosity ratio of the focus indicator on 'country' is less than required ratio of 3:1.

**Refer Attachment:**
1.Luminosity ratio of the focus indicator on 'country' is less than required ratio of 31.png
2.Luminosity ratio of the focus indicator on 'country' is less than required ratio of 31.mp4

<img width="960" height="580" alt="Image" src="https://github.com/user-attachments/assets/911fac11-742e-463f-95d6-60859ae4b996" />
https://github.com/user-attachments/assets/5528b028-067f-4b13-a0d7-51a48e5f4445

**Expected Result:**
Luminosity ratio of the focus indicator on 'country' should be more or equal to 3:1.

**Note:**
Same issue is being observed on 'Link', 'Terms', 'Privacy policy', 'Learn more' controls.

### Environment

Browser Edge Version: 138.0.3351.77 on OS: Windows 11 Enterprise Insider Preview Version 24H2(OS Build 26100.4349)

### Reproduction

https://site-f51sq.powerappsportals.com/?stepid=99ae0891-8aaa-4d1d-afcc-75e37ec374da

===

comment #1 by github-actions[bot], 2025-08-05, 02:17:14
This issue has been automatically marked as stale because it has not had recent activity. It will be closed if no further activity occurs. Thank you for your contributions.

comment #2 by msftedad, 2025-08-07, 09:51:21
Issue is still repro'ing. Please don't close this issue.
