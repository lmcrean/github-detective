issue title: Stripe SDK confirmPayment must not be null
labels: none
comment count: 4
hyperlink: https://github.com/stripe/stripe-react-native/issues/2048
status: open
date opened: 2025-08-08
repo 30d_merge_rate: 34

====

description:
Argument 1 (NSDictionary) of StripeSdk.confirmPayment must not be null
RCTLogArgumentError(RCTModuleMethod*, unsigned long, objc_object*, char const*)
    RCTModuleMethod.mm:67
__41-[RCTModuleMethod processMethodSignature]_block_invoke.96
-[RCTModuleMethod invokeWithBridge:module:arguments:]
facebook::react::invokeInner(RCTBridge*, RCTModuleData*, unsigned int, folly::dynamic const&, int, (anonymous namespace)::SchedulingContext)
facebook::react::RCTNativeModule::invoke(unsigned int, folly::dynamic&&, int)::$_0::operator()() const
invocation function for block in facebook::react::RCTNativeModule::invoke(unsigned int, folly::dynamic&&, int)
B51E7CDB-ABC9-35AF-B8BB-2DCE23BC4D6E
B51E7CDB-ABC9-35AF-B8BB-2DCE23BC4D6E
B51E7CDB-ABC9-35AF-B8BB-2DCE23BC4D6E
B51E7CDB-ABC9-35AF-B8BB-2DCE23BC4D6E
B51E7CDB-ABC9-35AF-B8BB-2DCE23BC4D6E
_pthread_wqthread
start_wqthread

===

comment #1 by porter-stripe, 2025-08-08, 15:05:01
@andhac can you please share some code to repro the issue?

comment #2 by andhac, 2025-08-08, 15:49:13
 try{
   if (!paymentResponse.data.client_secret) {
     console.error('Client secret is missing in payment response');
     throw new Error('Invalid payment response: client_secret is missing');
   }

    const {error} = await confirmPayment(paymentResponse.data.client_secret);
 
  if (error) {
     console.log('Payment error:', error);
     throw new Error(error.message);
   }
 }catch(error){
   console.log('Error confirming payment:', error);
 }

comment #3 by porter-stripe, 2025-08-11, 17:21:43
@andhac we have made a fix for this, it will be included in the next release.

comment #4 by andhac, 2025-08-11, 18:15:42
@porter-stripe what was the issue could you please share?
