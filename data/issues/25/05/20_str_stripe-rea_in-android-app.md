issue title: In Android app crash in release mode
labels: none
comment count: 11
hyperlink: https://github.com/stripe/stripe-react-native/issues/1938
status: open
date opened: 2025-05-20
repo 30d_merge_rate: 34

====

description:
**Describe the bug**

Android app is crash while initialising stripe

**To Reproduce**
  useEffect(() => {
        initializeStripe()
    }, [])

export const initializeStripe = async () => {
    const publishableKey = "km2Vp...."
    if (!publishableKey) {
        console.warn('Stripe key is missing!');
        return;
    }
    try {
        const resStripeInit = await initStripe({
            publishableKey,
            merchantIdentifier: 'merchant.identifier',
        });
        console.log('resStripeInit resStripeInit:-- ', resStripeInit);
    } catch (error) {
        console.log('error initializeStripe raised', error);
    }
}
**Expected behavior**


**Smartphone (please complete the following information):**
 - Device: Android 11

**Additional context**
 "react-native": "0.78.1",
  "@stripe/stripe-react-native": "^0.45.0", also on  "^0.46.0"

===

comment #1 by porter-stripe, 2025-05-20, 20:26:33
@akshSekhon can you provide the full stack track and the compose version you are using?

comment #2 by joacub, 2025-05-22, 20:01:34
> [@akshSekhon](https://github.com/akshSekhon) can you provide the full stack track and the compose version you are using?

This issue occurs due to a JSON parsing error combined with the new Android task manager behavior on many devices. Additionally, handleNextAction is being called with 3 arguments, but it expects 4

comment #3 by tjclawson-stripe, 2025-05-23, 00:11:29
Hey @akshSekhon can you provide your kotlin version as well?

comment #4 by sfriedman-stripe, 2025-05-30, 16:21:33
Hi @akshSekhon, just following up again here. Could you please share the full stack trace, Compose version, and Kotlin version?

comment #5 by akshSekhon, 2025-06-05, 10:44:14
@sfriedman-stripe @tjclawson-stripe  @porter-stripe  Sorry for late response please check below information

**Android Configrations**

 ext {
       buildToolsVersion = "35.0.0"
       minSdkVersion = 24
       compileSdkVersion = 34
       targetSdkVersion = 34
       ndkVersion = "27.1.12297006"
       kotlinVersion = "2.0.21"
    }

  "react-native": "0.78.1",
  "@stripe/stripe-react-native": "^0.47.1",


**System Config**

System:
  OS: macOS 15.3.1
  CPU: (6) x64 Intel(R) Core(TM) i5-8500B CPU @ 3.00GHz
  Memory: 62.96 MB / 8.00 GB
  Shell:
    version: "5.9"
    path: /bin/zsh
Binaries:
  Node:
    version: 23.10.0
    path: /usr/local/bin/node
  Yarn:
    version: 4.8.1
    path: /usr/local/bin/yarn
  npm:
    version: 10.9.2
    path: /usr/local/bin/npm
  Watchman:
    version: 2025.03.10.00
    path: /usr/local/bin/watchman
Managers:
  CocoaPods:
    version: 1.16.2
    path: /usr/local/bin/pod
SDKs:
  iOS SDK:
    Platforms:
      - DriverKit 24.5
      - iOS 18.5
      - macOS 15.5
      - tvOS 18.5
      - visionOS 2.5
      - watchOS 11.5
  Android SDK: Not Found
IDEs:
  Android Studio: 2024.2 AI-242.23726.103.2422.13103373
  Xcode:
    version: 16.4/16F6
    path: /usr/bin/xcodebuild
Languages:
  Java:
    version: 17.0.14
    path: /usr/bin/javac
  Ruby:
    version: 2.6.10
    path: /usr/bin/ruby
npmPackages:
  "@react-native-community/cli":
    installed: 15.0.1
    wanted: 15.0.1
  react:
    installed: 19.0.0
    wanted: 19.0.0
  react-native:
    installed: 0.78.1
    wanted: 0.78.1
  react-native-macos: Not Found
npmGlobalPackages:
  "*react-native*": Not Found
Android:
  hermesEnabled: true
  newArchEnabled: true
iOS:
  hermesEnabled: true
  newArchEnabled: true



***Crash Logs***

obtaining output fd from tombstoned, type: kDebuggerdTombstone
2025-06-05 16:05:49.192   831-831   /system/bin/tombstoned  tombstoned                           I  received crash request for pid 26850
2025-06-05 16:05:49.193 26862-26862 crash_dump32            crash_dump32                         I  performing dump of process 26756 (target tid = 26850)
2025-06-05 16:05:49.218 26862-26862 DEBUG                   crash_dump32                         A  *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
2025-06-05 16:05:49.218 26862-26862 DEBUG                   crash_dump32                         A  Build fingerprint: 'Redmi/olivewood/olivewood:10/QKQ1.191014.001/V12.5.6.0.QCQINXM:user/release-keys'
2025-06-05 16:05:49.219 26862-26862 DEBUG                   crash_dump32                         A  Revision: '0'
2025-06-05 16:05:49.219 26862-26862 DEBUG                   crash_dump32                         A  ABI: 'arm'
2025-06-05 16:05:49.220 26862-26862 DEBUG                   crash_dump32                         A  Timestamp: 2025-06-05 16:05:49+0530
2025-06-05 16:05:49.220 26862-26862 DEBUG                   crash_dump32                         A  pid: 26756, tid: 26850, name: mqt_v_js  >>> com.jeangilles <<<
2025-06-05 16:05:49.220 26862-26862 DEBUG                   crash_dump32                         A  uid: 10550
2025-06-05 16:05:49.220 26862-26862 DEBUG                   crash_dump32                         A  signal 6 (SIGABRT), code -1 (SI_QUEUE), fault addr --------
2025-06-05 16:05:49.220 26862-26862 DEBUG                   crash_dump32                         A  Abort message: 'JNI ERROR (app bug): attempt to use stale Local 0x1 (should be 0x5)'
2025-06-05 16:05:49.220 26862-26862 DEBUG                   crash_dump32                         A      r0  00000000  r1  000068e2  r2  00000006  r3  701fa2f8
2025-06-05 16:05:49.220 26862-26862 DEBUG                   crash_dump32                         A      r4  701fa30c  r5  701fa2f0  r6  00006884  r7  0000016b
2025-06-05 16:05:49.221 26862-26862 DEBUG                   crash_dump32                         A      r8  701fa308  r9  701fa2f8  r10 701fa328  r11 701fa318
2025-06-05 16:05:49.221 26862-26862 DEBUG                   crash_dump32                         A      ip  000068e2  sp  701fa2c8  lr  a7dd5d07  pc  a7dd5d1a
2025-06-05 16:05:50.155 26862-26862 DEBUG                   crash_dump32                         A  
                                                                                                    backtrace:
2025-06-05 16:05:50.155 26862-26862 DEBUG                   crash_dump32                         A        #00 pc 0005ed1a  /apex/com.android.runtime/lib/bionic/libc.so (abort+166) (BuildId: 940109a4b687bf19a1c73c8c92365f8c)
2025-06-05 16:05:50.155 26862-26862 DEBUG                   crash_dump32                         A        #01 pc 0037e221  /apex/com.android.runtime/lib/libart.so (art::Runtime::Abort(char const*)+1684) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.155 26862-26862 DEBUG                   crash_dump32                         A        #02 pc 000084dd  /system/lib/libbase.so (android::base::LogMessage::~LogMessage()+392) (BuildId: 7d8757d0af891f885311e79971c7fb33)
2025-06-05 16:05:50.156 26862-26862 DEBUG                   crash_dump32                         A        #03 pc 001e0cf9  /apex/com.android.runtime/lib/libart.so (art::IndirectReferenceTable::AbortIfNoCheckJNI(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> const&)+168) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.156 26862-26862 DEBUG                   crash_dump32                         A        #04 pc 00291367  /apex/com.android.runtime/lib/libart.so (art::IndirectReferenceTable::GetChecked(void*) const+278) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.156 26862-26862 DEBUG                   crash_dump32                         A        #05 pc 003b351f  /apex/com.android.runtime/lib/libart.so (art::Thread::DecodeJObject(_jobject*) const+54) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.156 26862-26862 DEBUG                   crash_dump32                         A        #06 pc 00377a67  /apex/com.android.runtime/lib/libart.so (art::(anonymous namespace)::ArgArray::BuildArgArrayFromVarArgs(art::ScopedObjectAccessAlreadyRunnable const&, art::ObjPtr<art::mirror::Object>, std::__va_list)+82) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.156 26862-26862 DEBUG                   crash_dump32                         A        #07 pc 00378b13  /apex/com.android.runtime/lib/libart.so (art::InvokeVirtualOrInterfaceWithVarArgs(art::ScopedObjectAccessAlreadyRunnable const&, _jobject*, _jmethodID*, std::__va_list)+290) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.156 26862-26862 DEBUG                   crash_dump32                         A        #08 pc 002a503d  /apex/com.android.runtime/lib/libart.so (art::JNI::CallVoidMethodV(_JNIEnv*, _jobject*, _jmethodID*, std::__va_list)+480) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.156 26862-26862 DEBUG                   crash_dump32                         A        #09 pc 0024bfe9  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libreactnative.so (offset 0x29b4000) (BuildId: ed48fa53d517301d)
2025-06-05 16:05:50.156 26862-26862 DEBUG                   crash_dump32                         A        #10 pc 00319853  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libreactnative.so (offset 0x29b4000) (facebook::react::JavaTurboModule::setEventEmitterCallback(facebook::jni::alias_ref<_jobject*>)+338) (BuildId: ed48fa53d517301d)
2025-06-05 16:05:50.156 26862-26862 DEBUG                   crash_dump32                         A        #11 pc 00146981  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libappmodules.so (offset 0x23b8000) (facebook::react::NativeStripeSdkModuleSpecJSI::NativeStripeSdkModuleSpecJSI(facebook::react::JavaTurboModule::InitParams const&)+7808) (BuildId: 73f1a7c3f9efd5bfb8b7829f93a6036eff430571)
2025-06-05 16:05:50.157 26862-26862 DEBUG                   crash_dump32                         A        #12 pc 001496b5  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libappmodules.so (offset 0x23b8000) (facebook::react::rnstripe_ModuleProvider(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>> const&, facebook::react::JavaTurboModule::InitParams const&)+84) (BuildId: 73f1a7c3f9efd5bfb8b7829f93a6036eff430571)
2025-06-05 16:05:50.157 26862-26862 DEBUG                   crash_dump32                         A        #13 pc 0016f695  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libappmodules.so (offset 0x23b8000) (facebook::react::autolinking_ModuleProvider(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>>, facebook::react::JavaTurboModule::InitParams const&)+216) (BuildId: 73f1a7c3f9efd5bfb8b7829f93a6036eff430571)
2025-06-05 16:05:50.157 26862-26862 DEBUG                   crash_dump32                         A        #14 pc 001aaf71  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libappmodules.so (offset 0x23b8000) (facebook::react::javaModuleProvider(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>> const&, facebook::react::JavaTurboModule::InitParams const&)+128) (BuildId: 73f1a7c3f9efd5bfb8b7829f93a6036eff430571)
2025-06-05 16:05:50.157 26862-26862 DEBUG                   crash_dump32                         A        #15 pc 001ab33f  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libappmodules.so (offset 0x23b8000) (BuildId: 73f1a7c3f9efd5bfb8b7829f93a6036eff430571)
2025-06-05 16:05:50.157 26862-26862 DEBUG                   crash_dump32                         A        #16 pc 003270e7  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libreactnative.so (offset 0x29b4000) (facebook::react::DefaultTurboModuleManagerDelegate::getTurboModule(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>> const&, facebook::react::JavaTurboModule::InitParams const&)+94) (BuildId: ed48fa53d517301d)
2025-06-05 16:05:50.157 26862-26862 DEBUG                   crash_dump32                         A        #17 pc 00400abd  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libreactnative.so (offset 0x29b4000) (facebook::react::TurboModuleManager::getTurboModule(facebook::jni::alias_ref<facebook::jni::detail::JTypeFor<facebook::jni::HybridClass<facebook::react::TurboModuleManager, facebook::jni::detail::BaseHybridClass>::JavaPart, facebook::jni::JObject, void>::_javaobject*>, std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>> const&, facebook::jsi::Runtime&)+1120) (BuildId: ed48fa53d517301d)
2025-06-05 16:05:50.157 26862-26862 DEBUG                   crash_dump32                         A        #18 pc 00402f01  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libreactnative.so (offset 0x29b4000) (BuildId: ed48fa53d517301d)
2025-06-05 16:05:50.158 26862-26862 DEBUG                   crash_dump32                         A        #19 pc 00313bc3  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libreactnative.so (offset 0x29b4000) (facebook::react::TurboModuleBinding::getModule(facebook::jsi::Runtime&, std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>> const&) const+46) (BuildId: ed48fa53d517301d)
2025-06-05 16:05:50.158 26862-26862 DEBUG                   crash_dump32                         A        #20 pc 0031434d  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libreactnative.so (offset 0x29b4000) (facebook::react::BridgelessNativeModuleProxy::get(facebook::jsi::Runtime&, facebook::jsi::PropNameID const&)+88) (BuildId: ed48fa53d517301d)
2025-06-05 16:05:50.158 26862-26862 DEBUG                   crash_dump32                         A        #21 pc 0005e7a1  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libhermes.so (offset 0x26a0000) (BuildId: a1f6b59614b4e74ec931eff689b22b2de1ced92b)
2025-06-05 16:05:50.158 26862-26862 DEBUG                   crash_dump32                         A        #22 pc 0007e7e3  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libhermes.so (offset 0x26a0000) (BuildId: a1f6b59614b4e74ec931eff689b22b2de1ced92b)
2025-06-05 16:05:50.158 26862-26862 DEBUG                   crash_dump32                         A        #23 pc 000725ad  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libhermes.so (offset 0x26a0000) (BuildId: a1f6b59614b4e74ec931eff689b22b2de1ced92b)
2025-06-05 16:05:50.158 26862-26862 DEBUG                   crash_dump32                         A        #24 pc 00070857  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libhermes.so (offset 0x26a0000) (BuildId: a1f6b59614b4e74ec931eff689b22b2de1ced92b)
2025-06-05 16:05:50.158 26862-26862 DEBUG                   crash_dump32                         A        #25 pc 00075dc9  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libhermes.so (offset 0x26a0000) (BuildId: a1f6b59614b4e74ec931eff689b22b2de1ced92b)
2025-06-05 16:05:50.158 26862-26862 DEBUG                   crash_dump32                         A        #26 pc 000640c5  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libhermes.so (offset 0x26a0000) (BuildId: a1f6b59614b4e74ec931eff689b22b2de1ced92b)
2025-06-05 16:05:50.158 26862-26862 DEBUG                   crash_dump32                         A        #27 pc 00063cef  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libhermes.so (offset 0x26a0000) (BuildId: a1f6b59614b4e74ec931eff689b22b2de1ced92b)
2025-06-05 16:05:50.158 26862-26862 DEBUG                   crash_dump32                         A        #28 pc 000638e3  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libhermes.so (offset 0x26a0000) (BuildId: a1f6b59614b4e74ec931eff689b22b2de1ced92b)
2025-06-05 16:05:50.158 26862-26862 DEBUG                   crash_dump32                         A        #29 pc 0005a3d9  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libhermes.so (offset 0x26a0000) (BuildId: a1f6b59614b4e74ec931eff689b22b2de1ced92b)
2025-06-05 16:05:50.158 26862-26862 DEBUG                   crash_dump32                         A        #30 pc 0036dfcd  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libreactnative.so (offset 0x29b4000) (facebook::react::Task::execute(facebook::jsi::Runtime&, bool)+188) (BuildId: ed48fa53d517301d)
2025-06-05 16:05:50.158 26862-26862 DEBUG                   crash_dump32                         A        #31 pc 0036c6e1  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libreactnative.so (offset 0x29b4000) (facebook::react::RuntimeScheduler_Modern::executeTask(facebook::jsi::Runtime&, facebook::react::Task&, bool) const+32) (BuildId: ed48fa53d517301d)
2025-06-05 16:05:50.158 26862-26862 DEBUG                   crash_dump32                         A        #32 pc 0036cd91  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libreactnative.so (offset 0x29b4000) (_ZN8facebook5react23RuntimeScheduler_Modern16runEventLoopTickERNS_3jsi7RuntimeERNS0_4TaskENSt6__ndk16chrono10time_pointINS8_12steady_clockENS8_8durationIxNS7_5ratioILx1ELx1000000000EEEEEEE+104) (BuildId: ed48fa53d517301d)
2025-06-05 16:05:50.159 26862-26862 DEBUG                   crash_dump32                         A        #33 pc 0036cae3  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libreactnative.so (offset 0x29b4000) (facebook::react::RuntimeScheduler_Modern::runEventLoop(facebook::jsi::Runtime&, bool)+106) (BuildId: ed48fa53d517301d)
2025-06-05 16:05:50.159 26862-26862 DEBUG                   crash_dump32                         A        #34 pc 0024223f  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libreactnative.so (offset 0x29b4000) (BuildId: ed48fa53d517301d)
2025-06-05 16:05:50.159 26862-26862 DEBUG                   crash_dump32                         A        #35 pc 00397f45  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libreactnative.so (offset 0x29b4000) (BuildId: ed48fa53d517301d)
2025-06-05 16:05:50.159 26862-26862 DEBUG                   crash_dump32                         A        #36 pc 000106a3  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libfbjni.so (offset 0x264c000) (_ZN8facebook3jni6detail13MethodWrapperIMNS0_15JNativeRunnableEFvvEXadL_ZNS3_3runEvEES3_vJEE8dispatchENS0_9alias_refIPNS1_8JTypeForINS0_11HybridClassIS3_NS0_9JRunnableEE8JavaPartESA_vE11_javaobjectEEE+54) (BuildId: bc1f23c0c45e1c7ad496193c948e61d7f39b15e9)
2025-06-05 16:05:50.159 26862-26862 DEBUG                   crash_dump32                         A        #37 pc 0001061d  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/base.apk!libfbjni.so (offset 0x264c000) (_ZN8facebook3jni6detail15FunctionWrapperIPFvNS0_9alias_refIPNS1_8JTypeForINS0_11HybridClassINS0_15JNativeRunnableENS0_9JRunnableEE8JavaPartES7_vE11_javaobjectEEEESC_vJEE4callEP7_JNIEnvP8_jobjectSF_+32) (BuildId: bc1f23c0c45e1c7ad496193c948e61d7f39b15e9)
2025-06-05 16:05:50.159 26862-26862 DEBUG                   crash_dump32                         A        #38 pc 000ff3a3  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/oat/arm/base.odex (art_jni_trampoline+74)
2025-06-05 16:05:50.159 26862-26862 DEBUG                   crash_dump32                         A        #39 pc 01379359  /system/framework/arm/boot-framework.oat (android.os.Handler.dispatchMessage+64) (BuildId: 81b8f6764550f41e19bea13c496b0efb5b4e3c05)
2025-06-05 16:05:50.159 26862-26862 DEBUG                   crash_dump32                         A        #40 pc 000d7bc5  /apex/com.android.runtime/lib/libart.so (art_quick_invoke_stub_internal+68) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.159 26862-26862 DEBUG                   crash_dump32                         A        #41 pc 004369b5  /apex/com.android.runtime/lib/libart.so (art_quick_invoke_stub+252) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.159 26862-26862 DEBUG                   crash_dump32                         A        #42 pc 000dffeb  /apex/com.android.runtime/lib/libart.so (art::ArtMethod::Invoke(art::Thread*, unsigned int*, unsigned int, art::JValue*, char const*)+178) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.159 26862-26862 DEBUG                   crash_dump32                         A        #43 pc 002136fd  /apex/com.android.runtime/lib/libart.so (art::interpreter::ArtInterpreterToCompiledCodeBridge(art::Thread*, art::ArtMethod*, art::ShadowFrame*, unsigned short, art::JValue*)+280) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.160 26862-26862 DEBUG                   crash_dump32                         A        #44 pc 0020f015  /apex/com.android.runtime/lib/libart.so (bool art::interpreter::DoCall<false, false>(art::ArtMethod*, art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)+716) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.160 26862-26862 DEBUG                   crash_dump32                         A        #45 pc 0042c6eb  /apex/com.android.runtime/lib/libart.so (MterpInvokeSuper+1278) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.160 26862-26862 DEBUG                   crash_dump32                         A        #46 pc 000d2894  /apex/com.android.runtime/lib/libart.so (mterp_op_invoke_super+20) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.160 26862-26862 DEBUG                   crash_dump32                         A        #47 pc 01811394  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/oat/arm/base.vdex (com.facebook.react.bridge.queue.MessageQueueThreadHandler.dispatchMessage)
2025-06-05 16:05:50.160 26862-26862 DEBUG                   crash_dump32                         A        #48 pc 001eea01  /apex/com.android.runtime/lib/libart.so (_ZN3art11interpreterL7ExecuteEPNS_6ThreadERKNS_20CodeItemDataAccessorERNS_11ShadowFrameENS_6JValueEbb.llvm.13441198129006899262+192) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.160 26862-26862 DEBUG                   crash_dump32                         A        #49 pc 001f31f3  /apex/com.android.runtime/lib/libart.so (art::interpreter::EnterInterpreterFromEntryPoint(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame*)+126) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.160 26862-26862 DEBUG                   crash_dump32                         A        #50 pc 0042049d  /apex/com.android.runtime/lib/libart.so (artQuickToInterpreterBridge+852) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.160 26862-26862 DEBUG                   crash_dump32                         A        #51 pc 000dc5a1  /apex/com.android.runtime/lib/libart.so (art_quick_to_interpreter_bridge+32) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.160 26862-26862 DEBUG                   crash_dump32                         A        #52 pc 01380237  /system/framework/arm/boot-framework.oat (android.os.Looper.loop+1302) (BuildId: 81b8f6764550f41e19bea13c496b0efb5b4e3c05)
2025-06-05 16:05:50.160 26862-26862 DEBUG                   crash_dump32                         A        #53 pc 000d7bc5  /apex/com.android.runtime/lib/libart.so (art_quick_invoke_stub_internal+68) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.161 26862-26862 DEBUG                   crash_dump32                         A        #54 pc 00436ac9  /apex/com.android.runtime/lib/libart.so (art_quick_invoke_static_stub+248) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.161 26862-26862 DEBUG                   crash_dump32                         A        #55 pc 000dffff  /apex/com.android.runtime/lib/libart.so (art::ArtMethod::Invoke(art::Thread*, unsigned int*, unsigned int, art::JValue*, char const*)+198) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.161 26862-26862 DEBUG                   crash_dump32                         A        #56 pc 002136fd  /apex/com.android.runtime/lib/libart.so (art::interpreter::ArtInterpreterToCompiledCodeBridge(art::Thread*, art::ArtMethod*, art::ShadowFrame*, unsigned short, art::JValue*)+280) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.161 26862-26862 DEBUG                   crash_dump32                         A        #57 pc 0020f015  /apex/com.android.runtime/lib/libart.so (bool art::interpreter::DoCall<false, false>(art::ArtMethod*, art::Thread*, art::ShadowFrame&, art::Instruction const*, unsigned short, art::JValue*)+716) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.161 26862-26862 DEBUG                   crash_dump32                         A        #58 pc 0042e18d  /apex/com.android.runtime/lib/libart.so (MterpInvokeStatic+348) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.161 26862-26862 DEBUG                   crash_dump32                         A        #59 pc 000d2994  /apex/com.android.runtime/lib/libart.so (mterp_op_invoke_static+20) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.161 26862-26862 DEBUG                   crash_dump32                         A        #60 pc 0181193a  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/oat/arm/base.vdex (com.facebook.react.bridge.queue.MessageQueueThreadImpl.lambda$startNewBackgroundThread$2+70)
2025-06-05 16:05:50.161 26862-26862 DEBUG                   crash_dump32                         A        #61 pc 0042e3d5  /apex/com.android.runtime/lib/libart.so (MterpInvokeStatic+932) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.161 26862-26862 DEBUG                   crash_dump32                         A        #62 pc 000d2994  /apex/com.android.runtime/lib/libart.so (mterp_op_invoke_static+20) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.161 26862-26862 DEBUG                   crash_dump32                         A        #63 pc 0181142c  /data/app/com.jeangilles-R56Km6yIWG_xY9rF3DKmBQ==/oat/arm/base.vdex (com.facebook.react.bridge.queue.MessageQueueThreadImpl$$ExternalSyntheticLambda1.run+4)
2025-06-05 16:05:50.161 26862-26862 DEBUG                   crash_dump32                         A        #64 pc 001eea01  /apex/com.android.runtime/lib/libart.so (_ZN3art11interpreterL7ExecuteEPNS_6ThreadERKNS_20CodeItemDataAccessorERNS_11ShadowFrameENS_6JValueEbb.llvm.13441198129006899262+192) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.161 26862-26862 DEBUG                   crash_dump32                         A        #65 pc 001f31f3  /apex/com.android.runtime/lib/libart.so (art::interpreter::EnterInterpreterFromEntryPoint(art::Thread*, art::CodeItemDataAccessor const&, art::ShadowFrame*)+126) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.161 26862-26862 DEBUG                   crash_dump32                         A        #66 pc 0042049d  /apex/com.android.runtime/lib/libart.so (artQuickToInterpreterBridge+852) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.161 26862-26862 DEBUG                   crash_dump32                         A        #67 pc 000dc5a1  /apex/com.android.runtime/lib/libart.so (art_quick_to_interpreter_bridge+32) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.162 26862-26862 DEBUG                   crash_dump32                         A        #68 pc 00433469  /system/framework/arm/boot.oat (java.lang.Thread.run+64) (BuildId: 244eb7f65b0596b53f1700d26db9c376b050fa2a)
2025-06-05 16:05:50.162 26862-26862 DEBUG                   crash_dump32                         A        #69 pc 000d7bc5  /apex/com.android.runtime/lib/libart.so (art_quick_invoke_stub_internal+68) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.162 26862-26862 DEBUG                   crash_dump32                         A        #70 pc 004369b5  /apex/com.android.runtime/lib/libart.so (art_quick_invoke_stub+252) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.162 26862-26862 DEBUG                   crash_dump32                         A        #71 pc 000dffeb  /apex/com.android.runtime/lib/libart.so (art::ArtMethod::Invoke(art::Thread*, unsigned int*, unsigned int, art::JValue*, char const*)+178) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.162 26862-26862 DEBUG                   crash_dump32                         A        #72 pc 00377b0b  /apex/com.android.runtime/lib/libart.so (art::(anonymous namespace)::InvokeWithArgArray(art::ScopedObjectAccessAlreadyRunnable const&, art::ArtMethod*, art::(anonymous namespace)::ArgArray*, art::JValue*, char const*)+54) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.162 26862-26862 DEBUG                   crash_dump32                         A        #73 pc 00378893  /apex/com.android.runtime/lib/libart.so (art::InvokeVirtualOrInterfaceWithJValues(art::ScopedObjectAccessAlreadyRunnable const&, _jobject*, _jmethodID*, jvalue const*)+306) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.162 26862-26862 DEBUG                   crash_dump32                         A        #74 pc 003a99cf  /apex/com.android.runtime/lib/libart.so (art::Thread::CreateCallback(void*)+986) (BuildId: 0d4c57d41c0fba3c5d2a46b44f645f43)
2025-06-05 16:05:50.162 26862-26862 DEBUG                   crash_dump32                         A        #75 pc 000a69b7  /apex/com.android.runtime/lib/bionic/libc.so (__pthread_start(void*)+20) (BuildId: 940109a4b687bf19a1c73c8c92365f8c)
2025-06-05 16:05:50.162 26862-26862 DEBUG                   crash_dump32                         A        #76 pc 000601af  /apex/com.android.runtime/lib/bionic/libc.so (__start_thread+30) (BuildId: 940109a4b687bf19a1c73c8c92365f8c)
2025-06-05 16:05:50.802 26862-26862 crash_dump32            crash_dump32                         E  cannot open libmiuindbg.so: No such file or directory

comment #6 by MadeinFrance, 2025-06-08, 08:04:37
Same issue on `@stripe/stripe-react-native@0.47.1` and `react-native@0.79.3`

<img width="1028" alt="Image" src="https://github.com/user-attachments/assets/52d78c58-cc84-43b3-a5f6-1eb28d4ad7d3" />

Android:

```
buildToolsVersion = "35.0.0"
minSdkVersion = 24
compileSdkVersion = 35
targetSdkVersion = 35
ndkVersion = "27.1.12297006"
kotlinVersion = "2.0.21"


supportLibVersion = "28.0.0"
androidXAnnotation = "1.1.0"
androidXBrowser = "1.0.0"
```

Proguard:
```
-dontwarn com.stripe.**

-keep class com.google.crypto.** { *; }
-keep class com.stripe.** { *; }
```

Stacktrace:
```
*** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
pid: 0, tid: 28797 >>> com.myApp <<<

backtrace:
  #00  pc 0x00000000004dead0  /apex/com.android.art/lib/libart.so (art::(anonymous namespace)::ArgArray::BuildArgArrayFromVarArgs(art::ScopedObjectAccessAlreadyRunnable const&, art::ObjPtr<art::mirror::Object>, std::__va_list) (.__uniq.245181933781456475607640333933569312899)+164)
  #01  pc 0x00000000004df553  /apex/com.android.art/lib/libart.so (art::JValue art::InvokeVirtualOrInterfaceWithVarArgs<_jmethodID*>(art::ScopedObjectAccessAlreadyRunnable const&, _jobject*, _jmethodID*, std::__va_list)+386)
  #02  pc 0x000000000038e1f1  /apex/com.android.art/lib/libart.so (art::JNI<false>::CallVoidMethodV(_JNIEnv*, _jobject*, _jmethodID*, std::__va_list)+452)
  #03  pc 0x00000000002610c9  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libreactnative.so (_JNIEnv::CallVoidMethod(_jobject*, _jmethodID*, ...)+7766016) (BuildId: 270b54780d6cbe9c)
  #04  pc 0x00000000003338c3  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libreactnative.so (facebook::react::JavaTurboModule::setEventEmitterCallback(facebook::jni::alias_ref<_jobject*>)+338) (BuildId: 270b54780d6cbe9c)
  #05  pc 0x00000000001ea4c9  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libappmodules.so (facebook::react::NativeStripeSdkModuleSpecJSI::NativeStripeSdkModuleSpecJSI(facebook::react::JavaTurboModule::InitParams const&)+7808) (BuildId: 76c4f4a529d719f12e79a701f17ab6816b650492)
  #06  pc 0x00000000001ed1fd  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libappmodules.so (facebook::react::rnstripe_ModuleProvider(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>> const&, facebook::react::JavaTurboModule::InitParams const&)+84) (BuildId: 76c4f4a529d719f12e79a701f17ab6816b650492)
  #07  pc 0x0000000000238765  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libappmodules.so (facebook::react::autolinking_ModuleProvider(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>>, facebook::react::JavaTurboModule::InitParams const&)+428) (BuildId: 76c4f4a529d719f12e79a701f17ab6816b650492)
  #08  pc 0x000000000027c1e9  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libappmodules.so (facebook::react::javaModuleProvider(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>> const&, facebook::react::JavaTurboModule::InitParams const&)+128) (BuildId: 76c4f4a529d719f12e79a701f17ab6816b650492)
  #09  pc 0x000000000027c5b7  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libappmodules.so (std::__ndk1::__function::__func<std::__ndk1::shared_ptr<facebook::react::TurboModule> (*)(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>> const&, facebook::react::JavaTurboModule::InitParams const&), std::__ndk1::allocator<std::__ndk1::shared_ptr<facebook::react::TurboModule> (*)(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>> const&, facebook::react::JavaTurboModule::InitParams const&)>, std::__ndk1::shared_ptr<facebook::react::TurboModule> (std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>> const&, facebook::react::JavaTurboModule::InitParams const&)>::operator()(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>> const&, facebook::react::JavaTurboModule::InitParams const&)+344064) (BuildId: 76c4f4a529d719f12e79a701f17ab6816b650492)
  #10  pc 0x0000000000341c17  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libreactnative.so (facebook::react::DefaultTurboModuleManagerDelegate::getTurboModule(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>> const&, facebook::react::JavaTurboModule::InitParams const&)+94) (BuildId: 270b54780d6cbe9c)
  #11  pc 0x000000000042da31  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libreactnative.so (facebook::react::TurboModuleManager::getTurboModule(facebook::jni::alias_ref<facebook::jni::detail::JTypeFor<facebook::jni::HybridClass<facebook::react::TurboModuleManager, facebook::jni::detail::BaseHybridClass>::JavaPart, facebook::jni::JObject, void>::_javaobject*>, std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>> const&, facebook::jsi::Runtime&)+1120) (BuildId: 270b54780d6cbe9c)
  #12  pc 0x000000000042fe75  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libreactnative.so (std::__ndk1::__function::__func<facebook::react::TurboModuleManager::createTurboModuleProvider(facebook::jni::alias_ref<facebook::jni::detail::JTypeFor<facebook::jni::HybridClass<facebook::react::TurboModuleManager, facebook::jni::detail::BaseHybridClass>::JavaPart, facebook::jni::JObject, void>::_javaobject*>, facebook::jsi::Runtime*)::$_0, std::__ndk1::allocator<facebook::react::TurboModuleManager::createTurboModuleProvider(facebook::jni::alias_ref<facebook::jni::detail::JTypeFor<facebook::jni::HybridClass<facebook::react::TurboModuleManager, facebook::jni::detail::BaseHybridClass>::JavaPart, facebook::jni::JObject, void>::_javaobject*>, facebook::jsi::Runtime*)::$_0>, std::__ndk1::shared_ptr<facebook::react::TurboModule> (std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>> const&)>::operator()(std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>> const&)+7766016) (BuildId: 270b54780d6cbe9c)
  #13  pc 0x000000000032dc33  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libreactnative.so (facebook::react::TurboModuleBinding::getModule(facebook::jsi::Runtime&, std::__ndk1::basic_string<char, std::__ndk1::char_traits<char>, std::__ndk1::allocator<char>> const&) const+46) (BuildId: 270b54780d6cbe9c)
  #14  pc 0x000000000032e3bd  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libreactnative.so (facebook::react::BridgelessNativeModuleProxy::get(facebook::jsi::Runtime&, facebook::jsi::PropNameID const&)+88) (BuildId: 270b54780d6cbe9c)
  #15  pc 0x000000000005e6a1  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libhermes.so (BuildId: c55e5ab177441b3912b03cc3fdbc46a7fa1d8288)
  #16  pc 0x000000000007e6d3  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libhermes.so (BuildId: c55e5ab177441b3912b03cc3fdbc46a7fa1d8288)
  #17  pc 0x00000000000724bd  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libhermes.so (BuildId: c55e5ab177441b3912b03cc3fdbc46a7fa1d8288)
  #18  pc 0x0000000000070767  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libhermes.so (BuildId: c55e5ab177441b3912b03cc3fdbc46a7fa1d8288)
  #19  pc 0x0000000000075cd9  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libhermes.so (BuildId: c55e5ab177441b3912b03cc3fdbc46a7fa1d8288)
  #20  pc 0x0000000000063fd5  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libhermes.so (BuildId: c55e5ab177441b3912b03cc3fdbc46a7fa1d8288)
  #21  pc 0x0000000000063bff  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libhermes.so (BuildId: c55e5ab177441b3912b03cc3fdbc46a7fa1d8288)
  #22  pc 0x00000000000635d3  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libhermes.so (BuildId: c55e5ab177441b3912b03cc3fdbc46a7fa1d8288)
  #23  pc 0x000000000005a2e9  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libhermes.so (BuildId: c55e5ab177441b3912b03cc3fdbc46a7fa1d8288)
  #24  pc 0x000000000038aebd  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libreactnative.so (facebook::react::Task::execute(facebook::jsi::Runtime&, bool)+188) (BuildId: 270b54780d6cbe9c)
  #25  pc 0x00000000003895bd  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libreactnative.so (facebook::react::RuntimeScheduler_Modern::executeTask(facebook::jsi::Runtime&, facebook::react::Task&, bool) const+32) (BuildId: 270b54780d6cbe9c)
  #26  pc 0x0000000000389c71  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libreactnative.so (facebook::react::RuntimeScheduler_Modern::runEventLoopTick(facebook::jsi::Runtime&, facebook::react::Task&, std::__ndk1::chrono::time_point<std::__ndk1::chrono::steady_clock, std::__ndk1::chrono::duration<long long, std::__ndk1::ratio<1ll, 1000000000ll>>>)+112) (BuildId: 270b54780d6cbe9c)
  #27  pc 0x00000000003899bf  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libreactnative.so (facebook::react::RuntimeScheduler_Modern::runEventLoop(facebook::jsi::Runtime&, bool)+106) (BuildId: 270b54780d6cbe9c)
  #28  pc 0x000000000025780b  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libreactnative.so (_ZNSt6__ndk110__function6__funcIZZN8facebook5react13ReactInstanceC1ENS_10unique_ptrINS3_9JSRuntimeENS_14default_deleteIS6_EEEENS_10shared_ptrINS3_18MessageQueueThreadEEENSA_INS3_12TimerManagerEEENS_8functionIFvRNS2_3jsi7RuntimeERKNS3_14JsErrorHandler14ProcessedErrorEEEEPNS3_18jsinspector_modern10HostTargetEENK3$_0clINSF_IFvSI_EEEEEDaT_EUlvE_NS_9allocatorISX_EEFvvEEclEv+7766016) (BuildId: 270b54780d6cbe9c)
  #29  pc 0x00000000003b4d99  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libreactnative.so (std::__ndk1::__function::__func<facebook::react::(anonymous namespace)::wrapRunnable(std::__ndk1::function<void ()>&&)::$_0, std::__ndk1::allocator<facebook::react::(anonymous namespace)::wrapRunnable(std::__ndk1::function<void ()>&&)::$_0>, void ()>::operator()()+7766016) (BuildId: 270b54780d6cbe9c)
  #30  pc 0x00000000000106a3  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libfbjni.so (facebook::jni::detail::MethodWrapper<void (facebook::jni::JNativeRunnable::*)(), &facebook::jni::JNativeRunnable::run(), facebook::jni::JNativeRunnable, void>::dispatch(facebook::jni::alias_ref<facebook::jni::detail::JTypeFor<facebook::jni::HybridClass<facebook::jni::JNativeRunnable, facebook::jni::JRunnable>::JavaPart, facebook::jni::JRunnable, void>::_javaobject*>)+54) (BuildId: bc1f23c0c45e1c7ad496193c948e61d7f39b15e9)
  #31  pc 0x000000000001061d  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/split_config.armeabi_v7a.apk!libfbjni.so (facebook::jni::detail::FunctionWrapper<void (*)(facebook::jni::alias_ref<facebook::jni::detail::JTypeFor<facebook::jni::HybridClass<facebook::jni::JNativeRunnable, facebook::jni::JRunnable>::JavaPart, facebook::jni::JRunnable, void>::_javaobject*>), facebook::jni::detail::JTypeFor<facebook::jni::HybridClass<facebook::jni::JNativeRunnable, facebook::jni::JRunnable>::JavaPart, facebook::jni::JRunnable, void>::_javaobject*, void>::call(_JNIEnv*, _jobject*, void (*)(facebook::jni::alias_ref<facebook::jni::detail::JTypeFor<facebook::jni::HybridClass<facebook::jni::JNativeRunnable, facebook::jni::JRunnable>::JavaPart, facebook::jni::JRunnable, void>::_javaobject*>))+32) (BuildId: bc1f23c0c45e1c7ad496193c948e61d7f39b15e9)
  #32  pc 0x000000000036c295  /data/misc/apexdata/com.android.art/dalvik-cache/arm/boot.oat (art_jni_trampoline+68)
  #33  pc 0x00000000009a2b5f  /data/misc/apexdata/com.android.art/dalvik-cache/arm/boot.oat (android.os.Handler.dispatchMessage+70)
  #34  pc 0x00000000000a046c  /apex/com.android.art/lib/libart.so (nterp_helper+2908)
  #35  pc 0x00000000004423fa  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/base.apk (com.facebook.react.bridge.queue.MessageQueueThreadHandler.dispatchMessage+10)
  #36  pc 0x00000000009a627f  /data/misc/apexdata/com.android.art/dalvik-cache/arm/boot.oat (android.os.Looper.loopOnce+854)
  #37  pc 0x00000000009a5ea1  /data/misc/apexdata/com.android.art/dalvik-cache/arm/boot.oat (android.os.Looper.loop+1024)
  #38  pc 0x000000000009f9bc  /apex/com.android.art/lib/libart.so (nterp_helper+172)
  #39  pc 0x0000000000442774  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/base.apk (com.facebook.react.bridge.queue.MessageQueueThreadImpl$Companion.startNewBackgroundThread$lambda$1+76)
  #40  pc 0x000000000009f9bc  /apex/com.android.art/lib/libart.so (nterp_helper+172)
  #41  pc 0x00000000004426a8  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/base.apk (com.facebook.react.bridge.queue.MessageQueueThreadImpl$Companion.a)
  #42  pc 0x000000000009f9bc  /apex/com.android.art/lib/libart.so (nterp_helper+172)
  #43  pc 0x00000000004424c8  /data/app/~~Kw9mY4lSoExVPsgqmFzBsw==/com.myApp-4rcGfJFi-brCdoHF8tshCg==/base.apk (com.facebook.react.bridge.queue.c.run+4)
  #44  pc 0x00000000004a02bf  /data/misc/apexdata/com.android.art/dalvik-cache/arm/boot.oat (java.lang.Thread.run+70)
  #45  pc 0x00000000000a4775  /apex/com.android.art/lib/libart.so (art_quick_invoke_stub_internal+68)
  #46  pc 0x00000000005acb0d  /apex/com.android.art/lib/libart.so (art_quick_invoke_stub+248)
  #47  pc 0x0000000000208dd5  /apex/com.android.art/lib/libart.so (art::ArtMethod::Invoke(art::Thread*, unsigned int*, unsigned int, art::JValue*, char const*)+120)
  #48  pc 0x0000000000517c2b  /apex/com.android.art/lib/libart.so (art::Thread::CreateCallback(void*)+1106)
  #49  pc 0x00000000000ad29f  /apex/com.android.runtime/lib/bionic/libc.so (__pthread_start(void*)+40)
  #50  pc 0x0000000000063d1b  /apex/com.android.runtime/lib/bionic/libc.so (__start_thread+30)
```

comment #7 by MadeinFrance, 2025-06-10, 20:16:08
> Hey [@akshSekhon](https://github.com/akshSekhon) can you provide your kotlin version as well?

2.0.21 see my details above.

comment #8 by akshSekhon, 2025-06-13, 11:51:55
@MadeinFrance have you found any solution?

comment #9 by lerkstaffie, 2025-06-27, 08:04:48
@akshSekhon I've also observed this issue in production for users with Samsung Galaxy A13 devices. It seems like a react-native bug.

Linked the issue here:
https://github.com/facebook/react-native/issues/49510

comment #10 by damianoserpetta, 2025-07-09, 09:59:55
Facing the same issue with Samsung Galaxy A13 (SM-A137F/DSN).

**Context**:
_RN_
"@stripe/stripe-react-native": "0.48.0",
"expo": "^53.0.11",
"react-native": "0.79.3",
"react": "19.0.0",

_Android_
minSdkVersion=30
compileSdkVersion=35
targetSdkVersion=35
ndkVersion=27.1.12297006
kotlinVersion=2.0.21

_Stacktrace_
```
verification.cc:114] GC tried to mark invalid reference 0xecb30d38
verification.cc:114] ref=0xecb30d38 <invalid address>
libc  A  Fatal signal 6 (SIGABRT), code -1 (SI_QUEUE) in tid 4083 (HeapTaskDaemon), pid 4073
```


comment #11 by Smiter15, 2025-07-09, 13:09:20
I’m also seeing this crash in our Expo/React Native app when using stripe-react-native 0.45.0 or 0.46.0 in a production (Hermes+TurboModules) build.
Downgrading to 0.43.0 immediately fixes it.

Environment:
stripe-react-native: 0.45.0 → 0.46.0 (crashes), 0.43.0 (works)

Expo SDK: 53.0.17
React Native: 0.79.5
Android OS: 11 (Moto E20, arm)
Hermes engine: enabled
New Architecture (TurboModules/JSI): enabled

Reproduction steps
Build a release APK with `npx expo prebuild && ./gradlew assembleRelease`
Install on device via `adb install -r app-release.apk`
Observe immediate SIGABRT in the mqt_v_js thread

```
F libc    : Fatal signal 6 (SIGABRT) …  
Abort message: 'JNI ERROR (app bug): attempt to use stale Local 0x1 (should be 0x5)'  
…  
#12  libreactnative.so  facebook::react::NativeStripeSdkModuleSpecJSI::NativeStripeSdkModuleSpecJSI(...)  
```
