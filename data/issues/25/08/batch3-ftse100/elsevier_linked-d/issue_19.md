metadata {
link: https://github.com/elsevierlabs-os/linked-data/issues/19
labels: None
data opened: 2024-07-23T14:27:44Z
author: lloyd-jackman-thomsonreuters
hyperlink: https://github.com/elsevierlabs-os/linked-data/issues/19
issue title: Visualisation not displaying Labels
}

issue description:
Using the Linked Data: Visualize function on RDF in a TTL file, labels of nodes are not shown without hovering over them.

![image](https://github.com/user-attachments/assets/70f4111d-c864-4305-8bd5-cabe0aa82a9a)

![image](https://github.com/user-attachments/assets/71aba35d-cc23-453f-86f0-e5975fe53105)

This seems to be different from the screenshots shown on https://marketplace.visualstudio.com/items?itemName=Elsevier.linked-data

![image](https://github.com/user-attachments/assets/6970640a-7fac-43be-b2b8-03228997dd98)

Labels for nodes have been formed in the RDF TTL using standard notation (example below):

`
PREFIX  ex:     <http://www.example.com/>
PREFIX  rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX  rdfs:   <http://www.w3.org/2000/01/rdf-schema#>

ex:Lloyd rdfs:label "Lloyd".
`
In this case , I would expect a single node with the label "Lloyd" next to it, but I do not see this.

![image](https://github.com/user-attachments/assets/f40bac99-ec58-4f6c-83ba-82acca1393b9)


comments (list all):
- **lloyd-jackman-thomsonreuters** (2024-07-23T14:34:39Z):
  I then changed my VS Code theme in case it was written in black and is simply not visible (worth checking), but this didn't solve the issue.

I then noticed something interesting with my one node graph. I get the one node and can hover to get the details.

![image](https://github.com/user-attachments/assets/cd404983-a22a-4aab-9044-2ecff68120a0)

If I then click it, it breaks out the node with the literal forming its own node and rdfs:label forming a relation.

![image](https://github.com/user-attachments/assets/69c9ca68-d1e9-476f-9001-c7bf56a3c319)

I am not sure if this is expected behaviour or if there is a use case for this.


- **RinkeHoekstra** (2024-07-24T12:22:12Z):
  You are absolutely right, the screenshots are outdated and what you're seeing is the expected behavior.

The reasons for the change in the visualisation are that 1) the code was migrated to the latest version of D3js (the older version was really quite ancient), 2) showing the IRIs as labels becomes a huge mess when dealing with large graphs and/or absolute IRIs and 3) the computations needed to prevent the labels from overlapping is prohibitively expensive. 

The last reason is also why the visualisation now has straight edges instead of arcs, `rdf:type` edges are hidden by default, and triples with literal objects are collapsed into the node. I could try and make this optional. We're working in the background to optimise the inspector a bit more, and one of the features is to have some configuration toggles on the visualisation itself (e.g. show/hide `rdf:type` edges). 

In the meantime I will use your issue to at least update the README.



- **lloyd-jackman-thomsonreuters** (2024-07-24T12:29:49Z):
  CORPORATE

Hello Rinke

Thank you for your reply, and I completely understand the performance considerations and potential mess.  Making it optional, or only available up to a configurable number of nodes, would be of significant benefit when using viewing the results of a CONSTRUCT SPARQL query, rather than viewing the whole.  As regards the length of IRIs, using the prefixes would definitely improve this, perhaps with a legend overlay box providing the prefix mapping like in the start of the TTL file.

Many thanks for your feedback and great work


Lloyd Jackman

Product Owner, DaaS Data Pipeline

London Stock Exchange Group



***@***.******@***.***>



lseg.com



[wPvoEp5tmbNFAAAAABJRU5ErkJggg==]



***@***.***?anonymous&ep=signature>             Book time to meet with ***@***.***?anonymous&ep=signature>
________________________________
From: Rinke Hoekstra ***@***.***>
Sent: 24 July 2024 2:22 PM
To: elsevierlabs-os/linked-data ***@***.***>
Cc: Lloyd Jackman ***@***.***>; Author ***@***.***>
Subject: Re: [elsevierlabs-os/linked-data] Visualisation not displaying Labels (Issue #19)

*** EXTERNAL EMAIL ***


You are absolutely right, the screenshots are outdated and what you're seeing is the expected behavior.

The reasons for the change in the visualisation are that 1) the code was migrated to the latest version of D3js (the older version was really quite ancient), 2) showing the IRIs as labels becomes a huge mess when dealing with large graphs and/or absolute IRIs and 3) the computations needed to prevent the labels from overlapping is prohibitively expensive.

The last reason is also why the visualisation now has straight edges instead of arcs, rdf:type edges are hidden by default, and triples with literal objects are collapsed into the node. I could try and make this optional. We're working in the background to optimise the inspector a bit more, and one of the features is to have some configuration toggles on the visualisation itself (e.g. show/hide rdf:type edges).

In the meantime I will use your issue to at least update the README.

—
Reply to this email directly, view it on GitHub<https://github.com/elsevierlabs-os/linked-data/issues/19#issuecomment-2247775909>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFUY6EZ5KXJ3KCCXMTRDFL3ZN6MAXAVCNFSM6AAAAABLKR5G7WVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDENBXG43TKOJQHE>.
You are receiving this because you authored the thread.Message ID: ***@***.***>
------------------------------------------------------------------------------------------------------------
 
Please read these warnings and restrictions:
This e-mail transmission is strictly confidential and intended solely for the ordinary user of the e-mail address to which it was addressed. It may contain legally privileged and/or CONFIDENTIAL information.
The unauthorised use, disclosure, distribution and/or copying of this e-mail or any information it contains is prohibited and could, in certain circumstances, constitute a criminal offence.
If you have received this e-mail in error or are not an intended recipient please inform London Stock Exchange Group (“LSEG”) immediately by return e-mail or telephone 020 7797 1000.
LSEG may collect, process and retain your personal information for its business purposes. For more information please see our Privacy Policy.
We advise that in keeping with good computing practice the recipient of this e-mail should ensure that it is virus free. We do not accept responsibility for any virus that may be transferred by way of this e-mail.
E-mail may be susceptible to data corruption, interception and unauthorised amendment, and we do not accept liability for any such corruption, interception or amendment or any consequences thereof. 
Calls to London Stock Exchange Group may be recorded to enable LSEG to carry out its regulatory responsibilities.
For more details on the LSEG group of companies click here 
London Stock Exchange Group plc
10 Paternoster Square
London 
EC4M 7LS
Registered in England and Wales No 05369106
 
------------------------------------------------------------------------------------------------------------



