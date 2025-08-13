issue title: Add `shopify-app-next` package
labels: none
comment count: 1
hyperlink: https://github.com/shopify/shopify-app-js/issues/2681
status: open
date opened: 2025-07-14
repo 30d_merge_rate: 10

====

description:
## Overview

Currently, `shopify-app-js` provides `shopify-app-remix` and `shopify-app-express` packages to streamline the integration between `shopify-api` and `shopify-app-session-storage-*` packages. However, there's no equivalent for nextjs.

Given next's popularity, a dedicated `shopify-app-next` package would greatly benefit developers by automating the connection between `shopify-api` and session storage, similar to the existing Remix and Express implementations. This would reduce boilerplate and improve the developer experience for Shopify app development with Next.js.


===

comment #1 by s-harshdeep, 2025-08-07, 14:52:59
Thank you for taking the time to share this feedback! I've passed your suggestion to the team.

Remix/React Router is our recommended framework for building Shopify apps, and our framework packages are designed to support our official templates. While we don't currently have plans to create an official Next.js package, I understand the value this would bring to developers using Next.js.

The good news is that the Shopify developer community has already created some great solutions for Next.js integration that you might want to explore. These community packages can help streamline the connection between `shopify-api` and session storage in Next.js applications
