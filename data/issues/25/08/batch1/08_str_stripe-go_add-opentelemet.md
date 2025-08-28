issue title: Add Opentelemetry support
labels: future, feature-request
comment count: 6
hyperlink: https://github.com/stripe/stripe-go/issues/2104
status: open
date opened: 2025-08-08
repo 30d_merge_rate: 7

====

description:
### Is your feature request related to a problem? Please describe.

We are trying to figure out what is the most optimal way to add OTEL to the Stripe API calls.

### Describe the solution you'd like

Ideally, the library already comes with OTEL integration.

~~Or maybe we suppose to build a custom backend for it?! Unsure~~

It seems that the backend call takes the replaced URL, ideally we should be able to pass
https://opentelemetry.io/docs/specs/semconv/registry/attributes/url/#url-template

In this case, `/v1/charges/{id}`

```go
func (c Client) Get(id string, params *stripe.ChargeParams) (*stripe.Charge, error) {
	path := stripe.FormatURLPath("/v1/charges/%s", id)
	charge := &stripe.Charge{}
	err := c.B.Call(http.MethodGet, path, c.Key, params, charge)
	return charge, err
}
```

### Describe alternatives you've considered

Wraps manually every API call

### Additional context



===

comment #1 by mbroshi-stripe, 2025-08-12, 14:10:39
Thanks for bringing this to our attention! We have not considered this use case before, and you are right that we pass the formatted `path` with ID(s) to `Call`. I am not familiar with `url.template`: Can you tell me how you might instead expect to receive the `path` parameter to take advantage of it?

comment #2 by yordis, 2025-08-12, 14:33:07
@mbroshi-stripe it depends of your specification you are following, but, it is safe to assume OpenAPI.

In this particular case, it would be `/v1/charges/{charge}` or whatever it is in your OpenAPI spec


```yaml
'/v1/charges/{charge}':
    get:
      description: >-
        <p>Retrieves the details of a charge that has previously been created.
        Supply the unique charge ID that was returned from your previous
        request, and Stripe will return the corresponding charge information.
        The same information is returned when creating or refunding the
        charge.</p>
      operationId: GetChargesCharge
```

Ideally, you already integrate with OTEL directly btw, I feel that it is such critical component by now, or, you allow me to inject the http client, and provide me enough data, worth reading https://opentelemetry.io/docs/specs/semconv/http/http-spans/ to see what to expect

comment #3 by mbroshi-stripe, 2025-08-12, 17:29:16
Thanks for the additional information! We will consider for future work to better integrate with OTEL. In the meantime, there is an example in our [README](https://github.com/stripe/stripe-go?tab=readme-ov-file#google-appengine) for injecting your own HTTP client into the Stripe client:
```go
httpClient := ...
backends := stripe.NewBackends(httpClient)
sc := stripe.NewClient("sk_test_123", stripe.WithBackends(backends))
// or sc := client.New("sk_test_123", backends) if you are using `client.API`
```
In theory, it should receive enough information in the `http.Request` that is passed in when you make an API call.

comment #4 by yordis, 2025-08-12, 18:08:18
> In theory, it should receive enough information in the http.Request that is passed in when you make an API call.

Right right, I am gonna move in that direction, hopefully get all the metadata required or direct-integration with OTEL at some point.

> We will consider for future work to better integrate with OTEL.

Thus far, would that be direct integration or opening the API to allow a better integration with it?

comment #5 by mbroshi-stripe, 2025-08-12, 19:00:23
> Thus far, would that be direct integration or opening the API to allow a better integration with it?

I would love to get your feedback on this question! I was imagining opening the API to allow for better integration, but we haven't fleshed out what the integration will look like yet. Another area that was brought up in a [previous issue](https://github.com/stripe/stripe-go/issues/1281) was better logging support. If you had examples of another SDK that has particularly good integration with OTEL, or if you had any other thoughts to share, I'd love to get your feedback.

comment #6 by yordis, 2025-08-12, 20:41:33
It is tricky,

I feel that direct support for OTEL is a expected situation by now, most likely a very safe bet to have direct support (Google Go SDKs come with that built-in, as an example, at least critical stuff like Spanner client), it all depends if you want to cover the 80/20 rule for now.

If you want the ultimate software architecture design that will allow everyone to be happy, you will need a combination of swapping the HTTP client + Middleware pipeline. Which will allow you to control the OTEL using a middleware, and the logging as well.
Since Go has the `contex.Context` as first parameter, you let the users to take advantage of that to pass whatever unstructured data they want for their own sake.

Being said, I am bias towards simplicity, the cost of OTEL is quite low and you will cover most the industry
