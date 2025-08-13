issue title: ERROR  Warning: TypeError: Cannot read property 'bubblingEventTypes' of null
labels: bug
comment count: 0
hyperlink: https://github.com/shopify/flash-list/issues/1668
status: open
date opened: 2025-05-20
repo 30d_merge_rate: 7

====

description:
<!-- Thanks for taking the time to fill out this bug report!

If this is not a bug report, please use other relevant channels:
- [Create a feature proposal on Discussions](https://github.com/Shopify/flash-list/discussions/new)
- [Chat with others in the #flash-list channel on Shopify React Native Open Source Discord](https://discord.com/channels/928252803867107358/986654488326701116)

Before you proceed:

- Make sure you are on latest versions of the FlashList package.
- If you are having an issue with your machine or build tools, the issue belongs on another repository as that is outside of the scope of FlashList. -->

## Current behavior

<!-- What code are you running and what is happening? Include a screenshot or video if it's a UI related issue. -->
Simply rendering the FlashList (even right after splash screen) causes the error immediately.

```javascript
        <FlashList
          data={[
            {
              title: "First Item",
            },
            {
              title: "Second Item",
            },
          ]}
          renderItem={({ item }) => <Text>{item.title}</Text>}
          estimatedItemSize={200}
        />
```

## Expected behavior

<!-- What do you expect to happen instead? -->
FllashList renders with no errors

## To Reproduce

<!-- Please provide a way to reproduce the problem if it's possible. Use the fixture app to create an example that reproduces the bug and provide a link to a GitHub repository under your username. -->

- create a new project with react native
- install FlashList and run `pod install`
- import and create list with FlashList
- run the project, will get the error

## Platform:

- [x] iOS
- [ ] Android

## Environment

<!-- What is the exact version of @shopify/flash-list that you are using? -->

`package.json`
```
{
  "name": "my-app",
  "version": "0.0.1",
  "private": true,
  "resolutions": {
    "react-native/react-devtools-core": "4.27.2",
    "instabug-reactnative": "11.0.0",
    "react-native-gesture-handler": "^2.13.4"
  },
  "dependencies": {
    "@design-system": "1.1.0-rc-98",
    "@shopify/flash-list": "^1.8.0",
    "react": "18.2.0",
    "react-native": "^0.75.5",
  },
  "devDependencies": {
    "@babel/core": "^7.20.0",
    "@types/react": "^19.0.10",
    "@types/react-native": "^0.67.1",
    "typescript": "^4.8.4"
  },
  "engines": {
    "node": ">=16"
  }
}
```

`Podfile`

```
ENV['RCT_NEW_ARCH_ENABLED'] = '0'
source 'https://cdn.cocoapods.org/'

platform :ios, '16.0'

require Pod::Executable.execute_command('node', ['-p',
  'require.resolve(
    "react-native/scripts/react_native_pods.rb",
    {paths: [process.argv[1]]},
  )', __dir__]).strip

install! 'cocoapods', :deterministic_uuids => false
prepare_react_native_project!

use_frameworks!

target 'MyApp' do
  config = use_native_modules!
  use_react_native!(
      :path => config[:reactNativePath],
      :hermes_enabled => flags[:hermes_enabled],
      :fabric_enabled => flags[:fabric_enabled],
      :app_path => "#{Pod::Config.instance.installation_root}/.."
    )

  target 'MyAppTests' do
    inherit! :complete
    # Pods for testing
  end

  post_install do |installer|
    installer.pods_project.targets.each do |target|
      target.build_configurations.each do |config|
        config.build_settings['ENABLE_BITCODE'] = 'NO'
        config.build_settings['BITCODE_GENERATION_MODE'] = 'none'
      end
    end

    react_native_post_install(
              installer,
              config[:reactNativePath],
              :mac_catalyst_enabled => false
            )
```

Similar issue: https://github.com/Shopify/flash-list/issues/1352

===
