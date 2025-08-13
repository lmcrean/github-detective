issue title: Add ability to simulate terminal error codes
labels: feature-request
comment count: 3
hyperlink: https://github.com/stripe/stripe-terminal-react-native/issues/1007
status: open
date opened: 2025-08-01
repo 30d_merge_rate: 19

====

description:
**Is your feature request related to a problem? Please describe.**
The problem is able to proactively code against terminal error codes that may happen in production environment with real hardware. Some of them are straight forward and happen quite often in development that I can handle. Errors like `USER_ERROR.CANCELED` when cancelling a pending discovery or `BLUETOOTH_SCAN_TIMED_OUT` when using the timeout property when discovering readers. Other ones like `READER_SOFTWARE_UPDATE_FAILED_INTERRUPTED` or even `GENERIC_READER_ERROR` which with empty codes will actually throw `UNEXPECTED_SDK_ERROR`. Since different callbacks are called under different situations with these error codes, it seems nearly impossible to proactively defend against these errors in a way that allows us to get app back into a good spot without restarting the app completely and most of the time disconnecting and reconnecting the reader.

**Describe the solution you'd like**
It would be amazing to have a way to simulate the SDK to throw some of these errors when using `simulated: true` like we have the ability to call `simulateReaderUpdate('random')` and have the correct callbacks fire as if it were happening in production.

**Describe alternatives you've considered**
My current workflow is wait for one of these errors to be thrown in production, check the logs and see when and what callback was fired when it produced the error and go update it after it's already happened, which doesn't feel like a good strategy to dealing with errors.


===

comment #1 by tlin-c-stripe, 2025-08-04, 04:44:41
It probably not easy to have a single API to simulate error as different API might have different error/flow, what we usually do is to provide a more specific simulation like `simulateReaderUpdate` which will make the intention much clear to know what it relate to. So if you can share some specific flow/simulation is not enough from your point that would be helpful.

> it seems nearly impossible to proactively defend against these errors in a way that allows us to get app back into a good spot without restarting the app completely

I'm also quite curious about what error do you get when you have to restart the app? 


comment #2 by imjakechapman, 2025-08-04, 17:24:10
They ones we see most often are `USER_ERROR.READER_SOFTWARE_UPDATE_FAILED_BATTERY_LOW`, `INTEGRATION_ERROR.ALREADY_CONNECTED_TO_READER`, `READER_ERROR.READER_COMMUNICATION_ERROR` (this ones for S700), `NETWORK_ERROR.STRIPE_API_CONNECTION_ERROR` and `READER_SOFTWARE_UPDATE_FAILED_INTERRUPTED`

Having some utility methods we could use when reader is simulated would be fantastic.  Maybe some thing that can broken out by error type:

`simulateUserError('READER_SOFTWARE_UPDATE_FAILED_BATTERY_LOW')`
`simulateReaderError('READER_COMMUNICATION_ERROR')`
`simulateNetworkError('STRIPE_API_CONNECTION_ERROR')`

comment #3 by tlin-c-stripe, 2025-08-12, 03:16:38
Thanks for your update, the feature request part had been brought to the team. Will update if we have new progress.


And it a bit not clear which error(s) you encounter will need the app to restart. Could you elaborate more. Thanks!
