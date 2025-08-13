issue title: Latency toxic is not bidirectional (and this is undocumented)
labels: none
comment count: 0
hyperlink: https://github.com/shopify/toxiproxy/issues/655
status: open
date opened: 2025-07-20
repo 30d_merge_rate: 7

====

description:
I'm using toxiproxy to test an networked game that uses [Cristian's Algorithm](https://en.wikipedia.org/wiki/Cristian's_algorithm) to synchronize a client clock with a server clock.  On a typical TCP connection, latency will be symmetric after the first few messages are exchanged.

Based on my testing, the `latency` toxic is unidirectional, applying only to host-to-client communications.  This asymmetric delay breaks the assumptions underlying this clock sync method.  When running client and server on the same PC with a toxiproxy between them, a clock sync request dispatched at T=475218ms reaches the server at T=475218ms (ie, immediately) and the reply is received at T=475278ms (with the 60ms latency I configured).

```
TRACE  time sync_receive: Roundtrip 60ms (client real time 180475218~180475278)
        Host's real time: 180475218
```

Furthermore, the unidirectional latency is undocumented:  indeed, the README implies otherwise:

> **latency**
> Add a delay to all data going through the proxy. The delay is equal to `latency` +/- `jitter`.

If latency were indeed applied to all data going through the proxy, I would expect a `latency` toxic valued at 25ms to produce 50ms of roundtrip delay.  But this is not the case (and this project seems much too mature to change the default behavior).

So, I recommend updating the documentation to reflect the "one-way" nature of the latency toxic.

In the future, a bidirectional mode for the latency toxic would be very useful for applications like mine.  Symmetric latency allows for a much better simulation of real-world network conditions than the current toxic.

===
