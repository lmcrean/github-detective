issue title: Error identification message is not provided at "Credit card number", CVC/CVN" and "Expiration date" form fields.
labels: bug
comment count: 2
hyperlink: https://github.com/stripe/stripe-js/issues/784
status: open
date opened: 2025-07-15
repo 30d_merge_rate: 12

====

description:
### What happened?

**User Impact:** 
Keyboard/Screen reader users are impacted as error identification message not appearing users may struggle to complete transactions due to unclear errors, leading to frustration and drop-offs.

**Steps to Repro:**

1. Open URL: https://codepen.io/serena206/pen/Byaeyyb in latest edge browser.
2. Code pen will be displayed on screen.
3. Tab to "Submit" button without filling the form fields and press enter key.
4. Verify whether on activating submit button error identification message is appearing for "Credit card number", CVC/CVN" and "Expiration date" form fields or not.

**Actual Result:** 
Error identification message is not provided at "Credit card number", CVC/CVN" and "Expiration date" form fields.

**Refer Attachment:**
1.Error identification message is not provided at Credit card number, CVCCVN and Expiration date form fields.png
2.Error identification message is not provided at Credit card number, CVCCVN and Expiration date form fields.mp4

https://github.com/user-attachments/assets/bdfa2eb5-c30b-4364-a456-225f0dcfc41c
<img width="960" height="590" alt="Image" src="https://github.com/user-attachments/assets/ef6f188e-54ae-4286-883d-dd066d87ea43" />

**Expected Result:** 
Error identification message should be provided at "Credit card number", CVC/CVN" and "Expiration date" form fields.


### Environment

Browser Edge Version: 136.0.3240.50 (Official build) (64-bit) on OS: Windows 11 Enterprise Insider Preview Version 24H2(OS Build 26100.3775)

### Reproduction

https://codepen.io/serena206/pen/Byaeyyb

===

comment #1 by github-actions[bot], 2025-08-05, 02:17:11
This issue has been automatically marked as stale because it has not had recent activity. It will be closed if no further activity occurs. Thank you for your contributions.

comment #2 by msftedad, 2025-08-05, 09:11:38
Issue is still repro'ing. Please dont close this issue.
