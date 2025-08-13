issue title: Shopify Session Storage For Mongo - Intermittent Errors
labels: none
comment count: 1
hyperlink: https://github.com/shopify/shopify-app-js/issues/2680
status: open
date opened: 2025-07-14
repo 30d_merge_rate: 10

====

description:
When using the Shopify Session Storage for Mongo adapter, I am seeing weird intermittent Mongo timeouts. The error looks like so : 

```
Unhandled Rejection: MongoServerSelectionError: Server selection timed out after 30000 ms
    at Topology.selectServer (/var/task/node_modules/mongodb/lib/sdam/topology.js:321:38)
    at runNextTicks (node:internal/process/task_queues:65:5)
    at listOnTimeout (node:internal/timers:549:9)
    at process.processTimers (node:internal/timers:523:7)
    at async Topology._connect (/var/task/node_modules/mongodb/lib/sdam/topology.js:200:28)
    at async Topology.connect (/var/task/node_modules/mongodb/lib/sdam/topology.js:152:13)
    at async topologyConnect (/var/task/node_modules/mongodb/lib/mongo_client.js:233:17)
    at async MongoClient._connect (/var/task/node_modules/mongodb/lib/mongo_client.js:246:13)
    at async MongoClient.connect (/var/task/node_modules/mongodb/lib/mongo_client.js:171:13)
    at async MongoDBSessionStorage.init (/var/task/node_modules/@shopify/shopify-app-session-storage-mongodb/dist/cjs/mongodb.js:86:9) 
```

I typically see this when hosted remotely (Vercel), but *sometimes* I can get it when developing an app locally. If I get it locally, restarting the app resolves it. 

There doesn't seem to be a huge rhyme or reason about when this happens. Because I can sometimes get it purely on startup, or other times after a while. What I actually presume is it's mostly a startup issue and since my app is low traffic, Vercel causes a cold start after a while which triggers it all. 

I note that there is this issue here on the Vercel repo with several other users reporting the issue : https://github.com/vercel/vercel/discussions/11178. It looks like it could be specific to AWS Lambdas and how the connections are pooled. 

Notably, some users said they solved the issue by wrapping the connect method in a promise : https://github.com/vercel/vercel/discussions/11178#discussioncomment-9581058

I'm not entirely sure on the implications of this. On one hand, the code at first look would cause you to "reconnect" each time you make a call, even within the same request. But then again, I think that the MongoClient itself is caching everything, and the Connect call is mostly dressing (You don't actually need to call connect at all, the first query will connect itself). 

I am testing the following code : 

I added a private variable on the MongoDBSessionStorageclass : 

```
  private collectionCheck : boolean = false;
```

I changed the ready promise to this : 

```
this.ready = new Promise(resolve => { resolve(this.init()) } );
```

And then I changed the init function to this : 

```
  private async init() {
    this.client = new (mongodb as any).MongoClient(this.dbUrl.toString());
    await this.client.connect();
    if(!this.collectionCheck) {
      await this.client.db().command({ping: 1});
      await this.createCollection();
      this.collectionCheck = true;
    }
  }

```

Happy to be the test bunny for this but clearly something is up. 

I would note, this isn't my forte. I sure as heck would not be using Remix if it was up to me, but the boilerplate from Spotify kinda demands it so any help is much appreciated. 


===

comment #1 by mindingdata, 2025-07-14, 06:01:07
So far, in my early tests, this "solves" the problem in a round about way (With a couple more changes). Here's why. 

There is definitely something about the network connectivity when Vercel (And by extension AWS Lambda) starts up. I'm not sure if it's specific to Vercel, AWS Lambda, Remix/SSR frameworks, or Shopify code itself. Because I can sometimes replicate it locally, that tends to point more towards the latter. 

However, what I can see is that I added a "Warmup" script to my app. As soon as I deploy to Vercel, I immediately start hitting endpoints that would call MongoDB. This is often the best way to replicate this issue. 

What I noticed before however was that the error never went away. Now, it seems like it might fail on the first request, then it goes away. So why? 

I believe the issue is with caching the promise. 

The original code has : 

```
this.ready = this.init();
```

And subsequent code like to load a session would call 

```
await this.ready;
```

This works because if the promise is already resolved (e.g. On the first call), then it will never be resolved again. But... What if it isn't resolved? What if the very first call to connect to mongo fails and the promise is failed/rejected? Well... Then it's forever failed/rejected. 

I'm slowly making other changes, but so far, this seems somewhat promising. 


