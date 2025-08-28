issue title: Add additional headers on request
labels: feature-request
comment count: 0
hyperlink: https://github.com/stripe/stripe-ruby/issues/1634
status: open
date opened: 2025-08-13
repo 30d_merge_rate: 6

====

description:
### Is your feature request related to a problem? Please describe.

Problem being solved: for an internal compliance requirement, I am required to provide a custom hmac header to outbound requests including ones handled by the Stripe gem.


### Describe the solution you'd like

A hook we can integrate with during initialization of Stripe that allows our system to alter the request directly. In this case, add additional headers after inspecting the body content and URI. 

### Describe alternatives you've considered

If a hook for adding headers to the request is unavailable, simply moving the request building to its own method would enable a more narrow monkey patch and this part of the logic is far less likely to see changes in future updates thus providing some extra stability. 


Currently we are looking to monkey patch `Stripe::ConnectionManager#execute_request`. In particular, right before `Net::HTTPGenericRequest.new` is executed, we add our own header content.

### Additional context

If there exists a solution to this problem already, I would also greatly appreciate being pointed to it. 

===
