issue title: Not respecting `ignore` list on checks
labels: Bug, area:theme-check
comment count: 1
hyperlink: https://github.com/shopify/theme-tools/issues/1012
status: open
date opened: 2025-07-09
repo 30d_merge_rate: 11

====

description:
This is my `.theme-check.yml` fil in the repo.

```yml
root: src

RemoteAsset:
  enabled: true
  ignore:
    - snippets/head-assets.liquid
    - snippets/video.liquid
    - snippets/image.liquid
```

But still getting these warnings when running the workflow
<img width="746" height="366" alt="Image" src="https://github.com/user-attachments/assets/27e7d51a-6cdf-4c4c-be80-5f59e64675cb" />

This is the config for the workflow
```yml
- name: Theme Check
        uses: shopify/theme-check-action@v2
        with:
          theme_root: './src'
          flags: '--fail-level warning'
          token: ${{ github.token }}
          base: main
```

===

comment #1 by karreiro, 2025-07-21, 09:55:58
This issue seems to be related to https://github.com/Shopify/theme-tools/issues/1006
