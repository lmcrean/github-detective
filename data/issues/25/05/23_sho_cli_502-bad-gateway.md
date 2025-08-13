issue title: 502 Bad Gateway Error When Using HTTP Proxy with `shopify theme dev`
labels: Type: Bug, Area: @shopify/cli, Area: @shopify/cli-kit
comment count: 10
hyperlink: https://github.com/shopify/cli/issues/5890
status: open
date opened: 2025-05-23
repo 30d_merge_rate: 77

====

description:
### Please confirm that you have:

- [x] Searched [existing issues](.) to see if your issue is a duplicate. (If you’ve found a duplicate issue, feel free to add additional information in a comment on it.)
- [x] Reproduced the issue in [the latest CLI version](https://www.npmjs.com/package/@shopify/cli).

### In which of these areas are you experiencing a problem?

Theme

### Expected behavior

The CLI should successfully render the storefront through the configured HTTP proxy.



### Actual behavior

The CLI fails to render the storefront with a 502 Bad Gateway error, despite proper proxy configuration.

### Verbose output

<details>
  <summary>Verbose output</summary>

  ```
Failed to render storefront with status 502 (Bad Gateway).
URL: [REDACTED]

TypeError: fetch failed
    at node:internal/deps/undici/undici:13510:13
    at process.processTicksAndRejections (node:internal/process/task_queues:105:5)
    at async render2 [...]
    at async Object.handler [...]
    at async Server.<anonymous> [...]
  ```

</details>

### Reproduction steps

1.Set HTTP proxy environment variables:
```powershell
$env:SHOPIFY_HTTP_PROXY = "http://127.0.0.1:PORT"
$env:SHOPIFY_HTTPS_PROXY = "http://127.0.0.1:PORT"
2.Run shopify theme dev -e development
3.CLI starts successfully and provides preview URLs
4.Immediately encounters 502 Bad Gateway error

### Operating System

Windows 11

### Shopify CLI version (`shopify --version`)

@shopify/cli/0.0.0-snapshot-20250313171017

### Shell

powershell

### Node version (run `node -v` if you're not sure)

v22.15.1

### What language and version are you using in your application?

_No response_

===

comment #1 by jpallard6120, 2025-05-26, 15:24:48
I have the exact same error here. Log output identical to @reeswell.  

- WSL 2 on Windows 10
- @shopify/cli/3.80.7 wsl-x64 node-v24.1.0

comment #2 by jpallard6120, 2025-05-26, 15:31:48
> I have the exact same error here. Log output identical to [@reeswell](https://github.com/reeswell).
> 
> * WSL 2 on Windows 10
> * @shopify/cli/3.80.7 wsl-x64 node-v24.1.0


Removing a plugin through `shopify plugin reset` solved the issue for me. 

comment #3 by reeswell, 2025-05-27, 05:37:06
> > I have the exact same error here. Log output identical to [@reeswell](https://github.com/reeswell).
> > 
> > * WSL 2 on Windows 10
> > * @shopify/cli/3.80.7 wsl-x64 node-v24.1.0
> 
> Removing a plugin through `shopify plugin reset` solved the issue for me.

Thank you for your response. However, when I tried `shopify plugins reset`, it shows "Found 0 plugin" and the issue still persists.

Here's what I've tried:
1. Ran `shopify plugins reset` -> Result: "Found 0 plugin"
2. Completely uninstalled and reinstalled Shopify CLI
3. Cleared npm cache and configurations

My environment:
- WSL 2 on Windows 11
- @shopify/cli/3.53.0
- Node.js v22.15.1
- - Theme: Liquid theme 

comment #4 by charlespwd, 2025-06-12, 16:25:35
Do you have docs for the SHOPIFY_HTTP_PROXY? Couldn't find anything. 

comment #5 by charlespwd, 2025-06-12, 16:28:42
Looks l like a CLI core/kit issue

comment #6 by reeswell, 2025-06-19, 09:58:56
> Do you have docs for the SHOPIFY_HTTP_PROXY? Couldn't find anything.

#5520 

comment #7 by fredmanxu, 2025-07-05, 11:04:16
Same error, How did you finally solve it?

comment #8 by HowardTangOvO, 2025-07-07, 04:40:50
Same error, Is there any solution for this?


comment #9 by cmoaciopm, 2025-08-03, 01:40:26
Same error. Any update for this issue?

comment #10 by wmlutz, 2025-08-08, 21:09:50
I am also having this problem. I'm commenting so I get notifications if an answer pops up.
