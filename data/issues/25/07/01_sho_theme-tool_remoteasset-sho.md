issue title: RemoteAsset shouldn't throw for video_source.url
labels: Bug
comment count: 0
hyperlink: https://github.com/shopify/theme-tools/issues/995
status: open
date opened: 2025-07-01
repo 30d_merge_rate: 11

====

description:
**Describe the bug**
source.url in the following code throw error: `Use one of the asset_url filters to serve assets for better performance. theme-check[RemoteAsset](https://shopify.dev/docs/storefronts/themes/tools/theme-check/checks/remote-asset)`

**Source**
<!-- Please paste the source code that causes your problem -->
```liquid
{% for source in video.sources %}
  <source src='{{ source.url }}' type='{{ source.mime_type }}'>
{% endfor %}
```

**Expected behaviour**
As the [video_source](https://shopify.dev/docs/api/liquid/objects/video_source#video_source).url property returns a CDN url, it doesn't return the right URL when the ` | asset_url` filter is added.

**Actual behaviour**
N/A

**Debugging information**
 - MacOS 15.4.1
 - @shopify/theme-check-common 3.19.0
 - shopify.theme-check-vscode 3.9.7


**Additional context**
I know I can use the `| video_tag` filter and it doesn't throw but I actually need to manually create the tag here for specific business reasons.


===
