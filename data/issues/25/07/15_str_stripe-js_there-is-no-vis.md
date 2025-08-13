issue title: There is no visual label for the form elements (like email, country combo box, mobile number, First and last name) under the 'Pay' tab.
labels: bug
comment count: 2
hyperlink: https://github.com/stripe/stripe-js/issues/781
status: open
date opened: 2025-07-15
repo 30d_merge_rate: 12

====

description:
### What happened?

**User Impact:**
Visual users will be impacted if there is no visual label for the control. Person having limited cognitive abilities and dyslexia person cannot easily understand the purpose of the elements if there is no visual label. Placeholder cannot be the sole means of identifying the purpose of the field.

**Steps to Repro:**

1. Open URL: [Home](https://site-f51sq.powerappsportals.com/?stepid=99ae0891-8aaa-4d1d-afcc-75e37ec374da) in latest edge browser.
2. Company page will be opened.
3. Press tab key to reach 'Cost edit field' and provide input.
4. Press tab key to reach 'Next button' and activate with enter key.
5. Step-2 page will be opened > Press tab key to reach 'Card details' session and provide details.
6. Optional details will be added.
7. Verify whether label is defined for the form elements (like email, country combo box, mobile number, First and last name) under the 'Pay' tab or not.

**Actual Result:**
There is no visual label for the form elements (like email, country combo box, mobile number, First and last name) under the 'Pay' tab.

**Refer Attachment:**
1.There is no visual label for the form elements (like email, country combo box, mobile number, First and last name) under the Pay tab.png
2.There is no visual label for the form elements (like email, country combo box, mobile number, First and last name) under the Pay tab.mp4

https://github.com/user-attachments/assets/14a04a7a-3e73-4293-bdf7-84b01e2fc19e
<img width="960" height="570" alt="Image" src="https://github.com/user-attachments/assets/f390ea46-dc05-4325-b7b7-cbd779f9354c" />

**Expected Result:**
Visual label should be defined for the form elements (like email, country combo box, mobile number, First and last name etc..,) under the 'Pay' tab.
EX: Also, Screen reader should announce as "Phone number 081234 56789 edit required suggestions available" when focus lands on 'Phone number' field.

### Environment

Browser Edge Version: 138.0.3351.77 on OS: Windows 11 Enterprise Insider Preview Version 24H2(OS Build 26100.4349) 

### Reproduction

https://site-f51sq.powerappsportals.com/?stepid=99ae0891-8aaa-4d1d-afcc-75e37ec374da

===

comment #1 by github-actions[bot], 2025-08-05, 02:17:16
This issue has been automatically marked as stale because it has not had recent activity. It will be closed if no further activity occurs. Thank you for your contributions.

comment #2 by msftedad, 2025-08-07, 09:50:12
Issue is still repro'ing. Please don't close this issue.
