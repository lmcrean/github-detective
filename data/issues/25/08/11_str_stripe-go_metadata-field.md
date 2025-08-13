issue title: .Metadata field for InvoiceVoidInvoiceParams and SubscriptionCancelParams
labels: bug
comment count: 2
hyperlink: https://github.com/stripe/stripe-go/issues/2105
status: closed
date opened: 2025-08-11
repo 30d_merge_rate: 7

====

description:
### Describe the bug

Error on create InvoiceVoidInvoiceParams or SubscriptionCancelParams with specified Metadata: You cannot specify both the (deprecated) .Params.Metadata and .Metadata in InvoiceVoidInvoiceParams (or SubscriptionCancelParams)

InvoiceVoidInvoiceParams and SubscriptionCancelParams do not expose a .Metadata field. However, you can set metadata via the deprecated .Params.Metadata field, which results in the error mentioned above.

### To Reproduce

1. Set Metadata in InvoiceVoidInvoiceParams
2. Call client.VoidInvoice(id, params) and observe the metadata conflict error.

Same thing with SubscriptionCancelParams but call client.Cancel(id, params) instead.


### Expected behavior

- InvoiceVoidInvoiceParams and SubscriptionCancelParams should expose a top‑level Metadata field
- Accept Params.Metadata without error when .Metadata isn’t defined.

### Code snippets

```Go
params := &stripe.InvoiceVoidInvoiceParams {
  Params:  stripe.Params{Metadata: map[string]string{"foo": "bar"}},
}

params := &stripe.SubscriptionCancelParams {
  Params:  stripe.Params{Metadata: map[string]string{"foo": "bar"}},
}
```

### OS

linux

### Go version

1.22

### stripe-go version

v80

### API version

 2024-09-30

### Additional context

_No response_

===

comment #1 by mbroshi-stripe, 2025-08-12, 15:01:19
Hi @laurent-treeapp! Thanks for reporting this issue! The error you are receiving is certainly confusing because you are not setting `Metadata` on `InvoiceVoidInvoiceParams`--it doesn't exist! 

The `Params.Metadata` field is deprecated and will likely be removed in the future. It should never be necessary to use it. In this case, neither [void invoice](https://docs.stripe.com/api/invoices/void) nor [cancel subscription](https://docs.stripe.com/api/subscriptions/cancel) takes a metadata parameter, and they are correctly left out of the corresponding `Params` structs. You can only attach `Metadata` when you `Create` or `Update` an invoice or subscription. So, while the error you're receiving is confusing, in this case you are correctly receiving an error since the Stripe API would give a validation error on the unexpected `metadata` field.

comment #2 by laurent-treeapp, 2025-08-12, 17:57:19
Oh, got it. Sorry about the confusion.
