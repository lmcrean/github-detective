issue title: Does not show store credit payment option
labels: Bug
comment count: 12
hyperlink: https://github.com/shopify/checkout-sheet-kit-swift/issues/302
status: open
date opened: 2025-06-05
repo 30d_merge_rate: 44

====

description:
### What area is the issue related to?

Checkout Sheet Kit

### What version of Checkout Sheet Kit are you using?

3.1.2

### Reproducible sample code

_No response_

### Steps to Reproduce

Enable Store credit for Shopify store. Login a customer using Customer Account API OAuth flow. Add store credit to customer account in Shopify Admin. Create customer cart with buyerIdentity set and add products to cart. Open cart checkoutUrl using checkout sheet kit.

### Expected Behavior

Store credit payment option should be shown the same as checkout in the web.

### Actual Behavior

Store credit payment option is not shown though customer is logged in checkout page. Store credit is shown when checkout is opened through the online store

### Screenshots/Videos/Log output

![Image](https://github.com/user-attachments/assets/e54fa0d0-f296-46b0-aadc-a97aac340650)

### Storefront domain

showpo-aunz-prod.myshopify.com

===

comment #1 by kiftio, 2025-06-06, 08:08:43
Hi @rcbello we're working on an update to the authentication mechanism to address this. We'll let you know when there's an update

comment #2 by rcbello, 2025-06-07, 10:08:37
Thanks, @kiftio . That's great to hear. Looking forward to the update.

comment #3 by github-actions[bot], 2025-07-08, 03:51:51
This issue has been automatically marked as stale because it has not had recent activity. It will be closed if no further activity occurs in 30 days. Thank you for your contributions.

comment #4 by joshgare, 2025-07-20, 12:40:50
We are also seeing clients with this issue @kiftio - do you have an update on this?

comment #5 by kiftio, 2025-07-21, 08:22:05
Hi @joshgare, a colleague has now opened a PR which resolves this, I think it'll most likely be merged/deployed this week. 

I'll add an update here when it's available

comment #6 by joshgare, 2025-07-25, 16:53:50
@kiftio any news? We've got some large Shopify Plus clients who aren't too happy at the moment

comment #7 by kiftio, 2025-07-28, 16:09:46
@joshgare apologies that it's taken a little longer than I first mentioned

I checked-in, and it's waiting on one more review, so hopefully not too far off

comment #8 by joshgare, 2025-07-28, 17:08:07
Thanks for the update @kiftio - I'll feedback that this is progressing to our clients!

comment #9 by staggy-stag, 2025-08-05, 08:42:12
@kiftio - is there an update on this? [We are the client mentioned previously]

comment #10 by joshgare, 2025-08-11, 12:27:27
@kiftio have you been able to get this merged in?

comment #11 by kiftio, 2025-08-11, 12:29:54
Hi, sorry, I was away last week.

It looks like it's now merged, but behind a feature flag. I'm checking if we're able to roll out the flag to additional stores or we're waiting on some additional testing.

comment #12 by kiftio, 2025-08-12, 15:28:45
The team is working through an issue, before rolling the change out
