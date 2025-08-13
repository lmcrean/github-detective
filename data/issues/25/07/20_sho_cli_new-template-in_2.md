issue title: New template install issues shopify issues
labels: none
comment count: 7
hyperlink: https://github.com/shopify/cli/issues/6162
status: open
date opened: 2025-07-20
repo 30d_merge_rate: 77

====

description:
Hi, today I followed the doc instructions to set up the template I have never used JS before outside of some jquery in .net. SI I downloaded node following their instructions on their site.  When I run ``shopify app dev``` or any shopify cmd for that matter running into errors 

Here are some cmds I ran and their outputs 


NPM Version 
```ps
PS C:\Users\ahugh\source\repos\KaininLTDWebApp> node -v
v20.15.0
```

NPM Shopify Add
```ps
PS C:\Users\ahugh\source\repos\KaininLTDWebApp> npm add @shopify/shopify-api
npm warn deprecated @shopify/network@3.3.0: Package no longer supported. Contact Support at https://www.npmjs.com/support for more info.

added 29 packages in 15s

3 packages are looking for funding
  run `npm fund` for details
```

Shopify Version 
```ps
PS C:\Users\ahugh\source\repos\KaininLTDWebApp> shopify -v
C:\Program Files (x86)\Nodist\bin\node_modules\@shopify\cli\bin\run.js:5
import runCLI from '../dist/index.js'
       ^^^^^^

SyntaxError: Unexpected identifier
    at Module._compile (internal/modules/cjs/loader.js:749:23)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:816:10)
    at Module.load (internal/modules/cjs/loader.js:672:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:612:12)
    at Function.Module._load (internal/modules/cjs/loader.js:604:3)
    at Function.Module.runMain (internal/modules/cjs/loader.js:868:12)
    at internal/main/run_main_module.js:21:11
```



===

comment #1 by lizkenyon, 2025-07-22, 13:27:32
Hi there 👋 

Sorry that you have run into this. 

Could you share what instructions you followed to get started?

comment #2 by Neh333, 2025-07-22, 16:02:33
Hi,

First I installed node JS using NPM and after that I ran
```ps 
npm init @shopify/app@latest -- --template=node 
```
Then followed the prompts I used an existing shopify app as I tried to use shpopifysharp for C# and .net but I came to the conclusion I'd be better off learning JS and node (I was wondering if this could be an issue and was going to try making a new app in shopify but am unsure) 

comment #3 by Neh333, 2025-07-22, 21:31:13
Hi so I Deleted my old app, created a shopify dev store then did the following to see if I could find a fix

```ps
PS C:\Users\ahugh> cd source/repos
PS C:\Users\ahugh\source\repos> npm init @shopify/app@latest -- --template=node

> npx
> create-app --template=node

?  We recommend installing Shopify CLI globally in your system. Would you like to install it now?
√  Yes

?  Create this project as a new app on Shopify?
√  Yes, create it as a new app

?  App name:
√  Kainin-LTD

Running npm install -g @shopify/cli@latest...
npm warn deprecated boolean@3.2.0: Package no longer supported. Contact Support at https://www.npmjs.com/support for more info.

changed 26 packages in 4s

8 packages are looking for funding
  run `npm fund` for details
╭─ info ───────────────────────────────────────────────────────────────────────╮
│                                                                              │
│  Initializing project with `npm`                                             │
│  Use the `--package-manager` flag to select a different package manager.     │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯


╭─ success ────────────────────────────────────────────────────────────────────╮
│                                                                              │
│  kainin-ltd is ready for you to build!                                       │
│                                                                              │
│  Next steps                                                                  │
│    • Run `cd kainin-ltd`                                                     │
│    • For extensions, run `shopify app generate extension`                    │
│    • To see your app, run `shopify app dev`                                  │
│                                                                              │
│  Reference                                                                   │
│    • Shopify docs [1]                                                        │
│    • For an overview of commands, run `shopify app --help`                   │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯
[1] https://shopify.dev

PS C:\Users\ahugh\source\repos> cd kainin-ltd
PS C:\Users\ahugh\source\repos\kainin-ltd> shopify app dev
C:\Program Files (x86)\Nodist\bin\node_modules\@shopify\cli\bin\run.js:5
import runCLI from '../dist/index.js'
       ^^^^^^

SyntaxError: Unexpected identifier
    at Module._compile (internal/modules/cjs/loader.js:749:23)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:816:10)
    at Module.load (internal/modules/cjs/loader.js:672:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:612:12)
    at Function.Module._load (internal/modules/cjs/loader.js:604:3)
    at Function.Module.runMain (internal/modules/cjs/loader.js:868:12)
    at internal/main/run_main_module.js:21:11
PS C:\Users\ahugh\source\repos\kainin-ltd>
```

comment #4 by Neh333, 2025-07-23, 14:32:10
DId this, same issue still 
```PS`

C:\Windows\system32> # Docker has specific installation instructions for each operating system.
>> # Please refer to the official documentation at https://docker.com/get-started/
>>
>> # Pull the Node.js Docker image:
>> docker pull node:22-alpine
>>
>> # Create a Node.js container and start a Shell session:
>> docker run -it --rm --entrypoint sh node:22-alpine
>>
>> # Verify the Node.js version:
>> node -v # Should print "v22.17.1".
>>
>> # Verify npm version:
>> npm -v # Should print "10.9.2".
>>
22-alpine: Pulling from library/node
79a0252b29f6: Download complete
4f24e34311a0: Download complete
ccf5d6e6ff24: Download complete
Digest: sha256:5539840ce9d013fa13e3b9814c9353024be7ac75aca5db6d039504a56c04ea59
Status: Downloaded newer image for node:22-alpine
docker.io/library/node:22-alpine
```

even ran VSC as an admin and ran ```shopify app dev``` and ```npm run dev```

comment #5 by Neh333, 2025-07-25, 04:35:09
Even tried using WSL (ubuntu distro) but that would not even clone the template or even make a directory after running ```npm init @shopify/app@latest -- --template=node```

comment #6 by Neh333, 2025-07-25, 04:54:37
Sorry not trying to spam genuinely confused and hopefully I can give best context possible to be guided. Ran through all of these but yet still no luck. I have all the shoplifty CLI requirements  

```ps

PS C:\Windows\system32> shopify version
C:\Program Files (x86)\Nodist\bin\node_modules\@shopify\cli\bin\run.js:5
import runCLI from '../dist/index.js'
       ^^^^^^

SyntaxError: Unexpected identifier
    at Module._compile (internal/modules/cjs/loader.js:749:23)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:816:10)
    at Module.load (internal/modules/cjs/loader.js:672:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:612:12)
    at Function.Module._load (internal/modules/cjs/loader.js:604:3)
    at Function.Module.runMain (internal/modules/cjs/loader.js:868:12)
    at internal/main/run_main_module.js:21:11
PS C:\Windows\system32>         npm uninstall -g @shopify/cli @latest

removed 26 packages in 334ms
PS C:\Windows\system32>         npm cache clean --force
npm warn using --force Recommended protections disabled.
PS C:\Windows\system32>         npm install -g @shopify/cli@latest
npm warn deprecated boolean@3.2.0: Package no longer supported. Contact Support at https://www.npmjs.com/support for more info.

added 26 packages in 7s

8 packages are looking for funding
  run `npm fund` for details
PS C:\Windows\system32> shopify version
C:\Program Files (x86)\Nodist\bin\node_modules\@shopify\cli\bin\run.js:5
import runCLI from '../dist/index.js'
       ^^^^^^

SyntaxError: Unexpected identifier
    at Module._compile (internal/modules/cjs/loader.js:749:23)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:816:10)
    at Module.load (internal/modules/cjs/loader.js:672:32)
    at tryModuleLoad (internal/modules/cjs/loader.js:612:12)
    at Function.Module._load (internal/modules/cjs/loader.js:604:3)
    at Function.Module.runMain (internal/modules/cjs/loader.js:868:12)
    at internal/main/run_main_module.js:21:11
PS C:\Windows\system32> node -v
v20.15.0
PS C:\Windows\system32> git -v
git version 2.43.0.windows.1
PS C:\Windows\system32>

```

comment #7 by lizkenyon, 2025-07-25, 13:57:10
Hi there 👋 

> C:\Program Files (x86)\Nodist\bin\node_modules\@shopify\cli\bin\run.js:5
import runCLI from '../dist/index.js'
       ^^^^^^

This looks like an issue in the CLI. I will transfer the issue over to that team!
