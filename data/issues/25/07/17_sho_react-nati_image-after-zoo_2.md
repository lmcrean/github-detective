issue title: Image after zoom is pixelated on Android Emulator
labels: none
comment count: 0
hyperlink: https://github.com/shopify/react-native-skia/issues/3240
status: open
date opened: 2025-07-17
repo 30d_merge_rate: 22

====

description:
Using react-native-skia version 1.9.0.
React native version: 0.76.9
React-native-zoomable-view version: 2.3.1

I'm using the Image component to fit into small rectangles.
When it is zoomed in 4x on android emulator, the image looks pixelated, especially the text.
I have tried using CubicSampling for the image property, as well as other sampling options, but the result is still the same.
How can the image be sharper when zoomed in?

I am using this generic image for now:
https://picsum.photos/id/528/500

This is the image zoomed in:
<img width="484" height="323" alt="Image" src="https://github.com/user-attachments/assets/e4b0db44-3925-474a-80e5-95b02c6a1181" />

===
