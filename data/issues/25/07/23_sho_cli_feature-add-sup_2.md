issue title: [Feature]: Add support for "Automatic Workspace Folders"
labels: Type: Enhancement, Area: @shopify/theme
comment count: 0
hyperlink: https://github.com/shopify/cli/issues/6151
status: open
date opened: 2025-07-23
repo 30d_merge_rate: 77

====

description:
### What area(s) will this request affect?

Running your code locally, Theme

### What type of change do you want to see?

New feature

### Overview

Google Chrome added support for [Automatic Workspace Folders][AWF] on the latest release, it would be amazing to support that feature.

The implementation should be quite simple, as the only requirement is to serve a file on a very specific request with a simple JSON file.

The expected usage would be:

I've start the `theme serve` command and open the development server on my browser, it makes a request to: `localhost:9292/.well-known/appspecific/com.chrome.devtools.json`, the server returns a JSON with the following content:

~~~ json
{
  "workspace": {
    "root": "{{ current path }}/assets",
    "uuid": "{{ random UUID }}"
  }
}
~~~

Then modifying asset code on the browser would change the actual assets on the theme, making developers happy.

[AWF]: http://goo.gle/devtools-automatic-workspace-folders

### Motivation

Currently, when working on different themes, this need to be manually setup for each one.

===
