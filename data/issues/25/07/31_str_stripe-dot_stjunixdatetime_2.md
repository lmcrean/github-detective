issue title: STJUnixDateTimeConverter does not handle nullable DateTime properties correctly
labels: bug
comment count: 5
hyperlink: https://github.com/stripe/stripe-dotnet/issues/3157
status: open
date opened: 2025-07-31
repo 30d_merge_rate: 8

====

description:
### Describe the bug

When deserializing a `Stripe.Event` payload using `System.Text.Json`, `DateTime?` properties will throw an exception when the value is `null`.

Here's a sample of the JSON payload used. Here it's a `customer.subscription.created` event, but I managed to reproduce this issue with almost any Stripe event received by webhook. [event.json](https://github.com/user-attachments/files/21535936/event.json)

Stack:

```
System.Text.Json.JsonException : Unexpected token parsing date. Expected Integer or String, got Null.
   at Stripe.Infrastructure.STJUnixDateTimeConverter.Read(Utf8JsonReader& reader, Type typeToConvert, JsonSerializerOptions options) in /_/src/Stripe.net/Infrastructure/JsonConverters/STJUnixDateTimeConverter.cs:line 43
```

### To Reproduce

Run this code:

```
var payload = "{\n  \"id\": \"evt_1Rr1JvFtG20dLAMsr7rHdgc2\",\n  \"object\": \"event\",\n  \"account\": \"acct_1RmfQsFtG20dLAMs\",\n  \"api_version\": \"2025-07-30.basil\",\n  \"context\": \"acct_1RmfQsFtG20dLAMs\",\n  \"created\": 1753986915,\n  \"data\": {\n    \"object\": {\n      \"id\": \"sub_1Rr1JuFtG20dLAMseqyV6s6G\",\n      \"object\": \"subscription\",\n      \"application\": \"ca_SmZ5iAGaRQDDNPqhbcsigRQREqD0dLt1\",\n      \"application_fee_percent\": null,\n      \"automatic_tax\": {\n        \"disabled_reason\": null,\n        \"enabled\": false,\n        \"liability\": null\n      },\n      \"billing_cycle_anchor\": 1753986914,\n      \"billing_cycle_anchor_config\": null,\n      \"billing_mode\": {\n        \"type\": \"classic\",\n        \"updated_at\": 0\n      },\n      \"billing_thresholds\": null,\n      \"cancel_at\": null,\n      \"cancel_at_period_end\": false,\n      \"canceled_at\": null,\n      \"cancellation_details\": {\n        \"comment\": null,\n        \"feedback\": null,\n        \"reason\": null\n      },\n      \"collection_method\": \"charge_automatically\",\n      \"created\": 1753986914,\n      \"currency\": \"usd\",\n      \"customer\": \"cus_SmZKVtb338KqvK\",\n      \"days_until_due\": null,\n      \"default_payment_method\": \"pm_1Rr0QcFtG20dLAMsU9KmfBDC\",\n      \"default_source\": null,\n      \"default_tax_rates\": [],\n      \"description\": null,\n      \"discounts\": [],\n      \"ended_at\": null,\n      \"invoice_settings\": {\n        \"account_tax_ids\": null,\n        \"issuer\": {\n          \"account\": null,\n          \"type\": \"self\"\n        }\n      },\n      \"items\": {\n        \"object\": \"list\",\n        \"data\": [\n          {\n            \"id\": \"si_SmaUvBvBsIYUlI\",\n            \"object\": \"subscription_item\",\n            \"billing_thresholds\": null,\n            \"created\": 1753986915,\n            \"current_period_end\": 1756665314,\n            \"current_period_start\": 1753986914,\n            \"discounts\": [],\n            \"metadata\": {},\n            \"plan\": {\n              \"id\": \"price_1Rr0BmFtG20dLAMsgqSmxAvZ\",\n              \"object\": \"plan\",\n              \"active\": true,\n              \"amount\": 1167,\n              \"amount_decimal\": 1167,\n              \"billing_scheme\": \"per_unit\",\n              \"created\": 1753982566,\n              \"currency\": \"usd\",\n              \"interval\": \"month\",\n              \"interval_count\": 1,\n              \"livemode\": false,\n              \"metadata\": {\n                \"3c_round_up\": \"0\",\n                \"3c_zone_id\": \"1\",\n                \"3c_agreement_id\": \"5\"\n              },\n              \"meter\": null,\n              \"nickname\": \"Zone 1\",\n              \"product\": \"3c_agreement_5\",\n              \"tiers\": null,\n              \"tiers_mode\": null,\n              \"transform_usage\": null,\n              \"trial_period_days\": null,\n              \"usage_type\": \"licensed\"\n            },\n            \"price\": {\n              \"id\": \"price_1Rr0BmFtG20dLAMsgqSmxAvZ\",\n              \"object\": \"price\",\n              \"active\": true,\n              \"billing_scheme\": \"per_unit\",\n              \"created\": 1753982566,\n              \"currency\": \"usd\",\n              \"currency_options\": null,\n              \"custom_unit_amount\": null,\n              \"livemode\": false,\n              \"lookup_key\": null,\n              \"metadata\": {\n                \"3c_round_up\": \"0\",\n                \"3c_zone_id\": \"1\",\n                \"3c_agreement_id\": \"5\"\n              },\n              \"nickname\": \"Zone 1\",\n              \"product\": \"3c_agreement_5\",\n              \"recurring\": {\n                \"interval\": \"month\",\n                \"interval_count\": 1,\n                \"meter\": null,\n                \"trial_period_days\": null,\n                \"usage_type\": \"licensed\"\n              },\n              \"tax_behavior\": \"unspecified\",\n              \"tiers\": null,\n              \"tiers_mode\": null,\n              \"transform_quantity\": null,\n              \"type\": \"recurring\",\n              \"unit_amount\": 1167,\n              \"unit_amount_decimal\": 1167\n            },\n            \"quantity\": 1,\n            \"subscription\": \"sub_1Rr1JuFtG20dLAMseqyV6s6G\",\n            \"tax_rates\": []\n          }\n        ],\n        \"has_more\": false,\n        \"url\": \"/v1/subscription_items?subscription=sub_1Rr1JuFtG20dLAMseqyV6s6G\"\n      },\n      \"latest_invoice\": \"in_1Rr1JvFtG20dLAMsdm4DSlKg\",\n      \"livemode\": false,\n      \"metadata\": {},\n      \"next_pending_invoice_item_invoice\": null,\n      \"on_behalf_of\": null,\n      \"pause_collection\": null,\n      \"payment_settings\": {\n        \"payment_method_options\": null,\n        \"payment_method_types\": null,\n        \"save_default_payment_method\": null\n      },\n      \"pending_invoice_item_interval\": null,\n      \"pending_setup_intent\": null,\n      \"pending_update\": null,\n      \"schedule\": \"sub_sched_1Rr1JuFtG20dLAMsgegakr2q\",\n      \"start_date\": 1753986914,\n      \"status\": \"active\",\n      \"test_clock\": null,\n      \"transfer_data\": null,\n      \"trial_end\": null,\n      \"trial_settings\": {\n        \"end_behavior\": {\n          \"missing_payment_method\": \"create_invoice\"\n        }\n      },\n      \"trial_start\": null\n    },\n    \"previous_attributes\": null\n  },\n  \"livemode\": false,\n  \"pending_webhooks\": 4,\n  \"request\": {\n    \"id\": \"req_MKH4UX85vdDnq3\",\n    \"idempotency_key\": \"caaec5d2-bf4d-4009-ab91-316a2e5394c4:283c3507-60c3-51e5-3df5-8b6f15f37ff6\"\n  },\n  \"type\": \"customer.subscription.created\"\n}";

// Works
JsonConvert.DeserializeObject<Stripe.Event>(payload);

// Fails
JsonSerializer.Deserialize<Stripe.Event>(payload);
```

### Expected behavior

Properly deserialize the property into a null DateTime.

### Code snippets

```csharp

```

### OS

Windows 11

### .NET version

.NET 8

### Library version

Stripe.net 48.4.0

### API version

2025-07-30.basil

### Additional context

_No response_

===

comment #1 by sebastiencrevier, 2025-07-31, 18:59:15
I've managed to nail down the issue is coming from [STJUnixDateTimeConverter.Read](https://github.com/stripe/stripe-dotnet/blob/ca7fcdad65da585313980b3fa042b3358af5b628/src/Stripe.net/Infrastructure/JsonConverters/STJUnixDateTimeConverter.cs#L27)
`nullable` is completely discarded, when it should be used to determine if the type is nullable and return `null` in this case.

See the Newtonsoft version [UnixDateTimeConverter](https://github.com/stripe/stripe-dotnet/blob/ca7fcdad65da585313980b3fa042b3358af5b628/src/Stripe.net/Infrastructure/JsonConverters/UnixDateTimeConverter.cs#L55) does this properly.

comment #2 by sebastiencrevier, 2025-07-31, 19:00:49
Same issue was closed here: https://github.com/stripe/stripe-dotnet/issues/3108

comment #3 by prathmesh-stripe, 2025-08-04, 21:15:26
Thanks for reporting this and providing detailed examples. I'm looking into reproducing and fixing this. 

comment #4 by prathmesh-stripe, 2025-08-07, 00:11:02
We currently do not support using STJ for deserializing json payloads, only for serializing (to e.g. return Stripe objects from ASP.NET handlers or other similar use cases). For event parsing, you can use [EventUtility::ConstructEvent()](https://github.com/stripe/stripe-dotnet/blob/master/src/Stripe.net/Services/Events/EventUtility.cs#L109) to parse the event payload with nullable DateTime. Stripe Docs has an [example](https://docs.stripe.com/webhooks?lang=dotnet#example-endpoint) for creating a webhook handler in .NET.

Can you share a bit about how you were running into this issue, and if ConstructEvent will work for your use case? 

comment #5 by jsgoupil, 2025-08-09, 17:27:35
@prathmesh-stripe I understand, however, your repo does have code for serializing and deserializing. So it's not obvious that your library does not support this. Especially that it fails at runtime with obscure problems rather than just saying `NotImplementedException`

When we receive your event, we store it in a ServiceBus queue on Azure. We moved away all serialization from Newtonsoft to STJ (as the new standard and speed improvement).
