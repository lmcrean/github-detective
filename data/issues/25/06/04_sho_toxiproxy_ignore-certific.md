issue title: Ignore certificate errors when creating proxy over a https url
labels: none
comment count: 0
hyperlink: https://github.com/shopify/toxiproxy/issues/646
status: open
date opened: 2025-06-04
repo 30d_merge_rate: 7

====

description:
I want to simulate a latency scenario where a https url is called from our java service within kubernetes cluster. toxiproxy is deployed in a separate service and pod within the same cluster.

After creating proxy and updating the url in our service with the new proxied url, we get the below errors within toxiproxy:

from postman we are able to suppress errors with -k, without -k flag or when the calls goes from java service using RestTemplate we get error "error":"writeto tcp x.x.x.x:443->x.x.x.x:64473: read tcp x.x.x.x:443->x.x.x.x:64473: use of closed network connection","caller":"link.go:127","time":"2025-06-04T18:03:56Z","message":"Source terminated"}

I am not sure how to bypass these certificate errors without any code changes.
Is there any setting within toxiproxy for ssl configuration? Or suggested changes within kubernetes to bypass/validate certificates for proxied url.



===
