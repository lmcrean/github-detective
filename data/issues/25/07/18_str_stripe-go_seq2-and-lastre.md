issue title: Seq2 and LastResponse
labels: bug
comment count: 6
hyperlink: https://github.com/stripe/stripe-go/issues/2087
status: open
date opened: 2025-07-18
repo 30d_merge_rate: 7

====

description:
### Describe the bug

Hi there, I've noticed what I believe to be an oversight in the new Stripe Client that's referenced [here](https://github.com/stripe/stripe-go/wiki/Migration-guide-for-Stripe-Client#list-methods).

This problem applies to all List methods but I'll be referencing the List for Disputes going forward. 

Prior to the above change, the List methods would return an `Iter` which the `${Resource}List` types would implement i.e. `stripe.DisputeList{}` and the List method would be used like

```go
p := &stripe.DisputeListParams{
    PaymentIntent: stripe.String(params.PaymentIntentID),
}
p.Context = ctx

iter := c.disputeClient.List(p)

disputeList, ok := iter.List().(*stripe.DisputeList)
if !ok {
    return nil, errFailedToCastToDisputeList
}

disputeListLastResponse, err := getDisputeListLastResponse(disputeList.LastResponse)
if err != nil {
    return nil, err
}
for iter.Next() {
  // Logic associated with a Dispute    
}
```

With the change above, the advice is that we should now have code that looks like the following given that List returns an Seq2 iterator

```go
p := &stripe.DisputeListParams{
    PaymentIntent: stripe.String(params.PaymentIntentID),
}

for dispute, err := range c.disputeClient.List(ctx, p) {
    if err != nil {
        return nil, err
    }
        
    // This is nil
    lastResponse := dispute.LastResponse

    // Logic associated with a Dispute
}
```

The oversight is that if we're using a `preview feature` on the resource (`Dispute`) and we try to follow the advice [here](https://github.com/stripe/stripe-go?tab=readme-ov-file#properties), the LastResponse on each of the returned resources is `nil` and given that the new iterator does not return a DisputeList anymore, we can't access the LastResponse.   



### To Reproduce

1. Make use of a List function with the Client that was introduced in v82.1
2. Try to access LastResponse on the returned resources

### Expected behavior

Either 
1. have the iterator hydrate each resource's `LastResponse`
2. have the iterator return a type which allows for accessing `LastResponse`

### Code snippets

```Go

```

### OS

macOS

### Go version

Go 1.24.4

### stripe-go version

v82.1

### API version

2025-06-30.basil

### Additional context

I had raised [this in your Discord](https://discord.com/channels/841573134531821608/841573134531821616/1395715371528355900) and was asked to create an issue. 

===

comment #1 by helenye-stripe, 2025-07-18, 14:07:25
Hi! Thanks for catching this! We'll look into the issue.

comment #2 by mbroshi-stripe, 2025-07-18, 18:22:00
@jamieaitken This is a great catch, and something we overlooked in the new `stripe.Client` `List` implementation. Restating your suggestions, and to avoid a breaking change, we can either:
1. Have the iterator hydrate each resource's `LastResponse` (which would be the `LastResponse` for that entire page), or
2. Add a new `ListWithPages` (or similar name) that returns an object that has `LastResponse` re-set each time it paginates, in essence acting like the previous `List` implementation.

Can you tell us a little more about your use case for `LastResponse` to help us judge which would be a better approach?



comment #3 by jamieaitken, 2025-07-18, 19:25:12
Hey @mbroshi-stripe 👋  

Sure thing, we make use of a `preview feature` which enables a property on the Dispute object to state whether it was the result of Visa's Rapid Dispute Resolution. With this property being in preview, it's not represented in any of the SDKs but it's still available in the `RawJSON` within `LastResponse`. So, we follow the advice [here](https://github.com/stripe/stripe-go?tab=readme-ov-file#properties) in order to get access to that property.

I personally prefer option 1, as it keeps the interface for each resource simple. 

Would it be possible to have the JSON associated with just that resource be the value of the resource's `LastResponse.RawJSON` rather than be the entire collection though? (I'm aware this is verging on a feature-request territory here)

comment #4 by mbroshi-stripe, 2025-07-18, 21:28:41
Thanks for the added context! Both options definitely have tradeoffs, but I agree that Option 1 is a simpler approach. However, one of its downsides is exactly what you point out:

> Would it be possible to have the JSON associated with just that resource be the value of the resource's LastResponse.RawJSON rather than be the entire collection though? (I'm aware this is verging on a feature-request territory here)

I can see how that might seem more ergonomic, but would definitely be a more involved change on our end, and might have unforeseen edge cases and performance impacts I would need to think through and test (right now we are just dumping the `RawJSON` bytes into `LastResponse` without parsing). I'm also a little concerned with changing the `RawJSON` to look different than the response you would see in your Stripe Dashboard corresponding to that `RequestID` (which would be the entire page's JSON).

In the meantime, I think the workaround for your use case is to use the old `client.API` (even though it's marked as deprecated, it's still supported). Even there, though, you need to be careful since each time the `dispute.Iter` paginates, it will re-set the `LastResponse` with the entire page's JSON.

Since it's not blocking, I don't want to rush out a fix just yet, although I'm currently leaning towards Option 1 without the additional `RawJSON` change.

comment #5 by jamieaitken, 2025-07-23, 16:28:01
@mbroshi-stripe That makes sense. We're still using the deprecated client for resources where access to LastResponse for a List is required.

comment #6 by mbroshi-stripe, 2025-07-29, 12:32:21
Thanks for letting me know. We'll respond on this Issue once we have a fix out.
