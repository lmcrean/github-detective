issue title: Screen reader is not announcing accessible name for 'Country' combo box available on pay tab.
labels: bug
comment count: 2
hyperlink: https://github.com/stripe/stripe-js/issues/780
status: open
date opened: 2025-07-15
repo 30d_merge_rate: 12

====

description:
### What happened?

**Observation:**
This issue is observed with all three screen readers.

**User Impact:**
Screen reader users will be impacted as they cannot understand the purpose of the combo box is there is no accessible name. Screen reader users get confused to understand the purpose of it and hence may not access it effectively.

**Steps to Repro:**

1. Open URL: https://site-f51sq.powerappsportals.com/?stepid=99ae0891-8aaa-4d1d-afcc-75e37ec374da in latest edge browser.
2. Company page will be opened.
3. Press tab key to reach 'Cost edit field' and provide input.
4. Press tab key to reach 'Next button' and activate with enter key.
5. Step-2 page will be opened > Press tab key to reach 'Card details' session and provide details.
6. Optional details will be added > press tab key to reach 'Country combo box'.
7. Verify whether screen reader is announcing accessible for 'Country combo box' or not.

**Actual Result:**
Screen reader is not announcing accessible name for 'Country' combo box available on pay tab.

**Refer Attachment:**
1.Screen reader is not announcing accessible name for 'Country' combo box available on pay tab.png
2.Screen reader is not announcing accessible name for 'Country' combo box available on pay tab.mp4

<img width="960" height="573" alt="Image" src="https://github.com/user-attachments/assets/458e4328-42f8-4023-965f-6f645410eb63" />
https://github.com/user-attachments/assets/c25b90b5-ffb9-49ec-90cb-7063ca0ccaa6

**Expected Result:**
Screen reader should announce accessible name for 'Country' combo box available on pay tab.
it should announce as "Country/ pin code India+91 combo box collapsed required has popup".

### Environment

OS: Windows 11 Enterprise Insider Preview Version 24H2(OS Build 26100.4349) Browser Edge Version: 138.0.3351.77 (Official build) (64-bit) Screen reader: NVDA Version: 2025.1.2 (2025.1.2.36913)

### Reproduction

https://site-f51sq.powerappsportals.com/?stepid=99ae0891-8aaa-4d1d-afcc-75e37ec374da

===

comment #1 by github-actions[bot], 2025-08-05, 02:17:17
This issue has been automatically marked as stale because it has not had recent activity. It will be closed if no further activity occurs. Thank you for your contributions.

comment #2 by msftedad, 2025-08-07, 09:50:49
Issue is still repro'ing. Please don't close this issue.
