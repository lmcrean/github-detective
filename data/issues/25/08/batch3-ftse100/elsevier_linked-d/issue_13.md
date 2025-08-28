metadata {
link: https://github.com/elsevierlabs-os/linked-data/issues/13
labels: None
data opened: 2023-08-04T15:19:15Z
author: kvistgaard
hyperlink: https://github.com/elsevierlabs-os/linked-data/issues/13
issue title: Add convert to Mermaid
}

issue description:
It will be great to add the possibility of converting to Mermaid.

Maybe [CRITERIA](https://github.com/chin-rcip/CRITERIA) can be reused.

comments (list all):
- **RinkeHoekstra** (2024-03-29T08:53:17Z):
  That's a brilliant idea!

However, CRITERIA is a Python package, so we'll have to look elsewhere. Open to suggestions!

- **lloyd-jackman-thomsonreuters** (2024-06-04T13:10:36Z):
  +1 for this idea as I am currently having to keep my TTL and mermaid diagrams in synch manually

- **RinkeHoekstra** (2024-07-24T12:24:52Z):
  Any thoughts on which Mermaid visualisation you'd like to see? Class diagrams or ER diagrams?

- **lloyd-jackman-thomsonreuters** (2024-07-24T12:41:32Z):
  Hello Rinke

The Class diagram would make more sense allowing for the creation of schema diagrams for types of nodes, their properties and relations.  Such a view, based on the schema in the TTL, when pushed to mermaid would allow the view to then be pushed to Azure DevOps wiki pages with their native mermaid diagram support.

I can also imagine the utility in the ER diagram, but it would require OWL to be used to properly describe the cardinality of each relationship.

Thank you and best regards


Lloyd Jackman

Product Owner, DaaS Data Pipeline

London Stock Exchange Group



***@***.******@***.***>



lseg.com



[wPvoEp5tmbNFAAAAABJRU5ErkJggg==]



***@***.***?anonymous&ep=signature>             Book time to meet with ***@***.***?anonymous&ep=signature>
________________________________
From: Rinke Hoekstra ***@***.***>
Sent: 24 July 2024 2:25 PM
To: elsevierlabs-os/linked-data ***@***.***>
Cc: Lloyd Jackman ***@***.***>; Comment ***@***.***>
Subject: Re: [elsevierlabs-os/linked-data] Add convert to Mermaid (Issue #13)

*** EXTERNAL EMAIL ***


Any thoughts on which Mermaid visualisation you'd like to see? Class diagrams or ER diagrams?

—
Reply to this email directly, view it on GitHub<https://github.com/elsevierlabs-os/linked-data/issues/13#issuecomment-2247781033>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFUY6E7EQZ7IJZQ22REGSA3ZN6MKVAVCNFSM6AAAAAA3ELJEP6VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDENBXG44DCMBTGM>.
You are receiving this because you commented.Message ID: ***@***.***>
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


- **RinkeHoekstra** (2024-07-29T13:20:14Z):
  The problem with class-diagrams or ER-diagrams is that they are class-based, not instance-based. 

We can do one of the following:

* Only represent RDFS and/or OWL information from the graph as Mermaid diagram (this may be very disappointing for graphs without schema)
* Guess RDFS class information from the graph to create Mermaid diagrams (this may turn ugly when nodes have multiple types).
* Abuse the Mermaid notation for instance information (e.g. every URI Resource is a Mermaid Class)

Don't think there's a solution that's both elegant and satisfying 

- **lloyd-jackman-thomsonreuters** (2024-07-29T15:20:14Z):
  CORPORATE

Hello Rinke

I agree that it is not simple, but I would prioritise the use case for creating a mermaid diagram for the schema of the graph as many graphs are simply too large to effectively see anything but spaghetti.  Mermaid diagrams, in my experience, are used first and foremost in technical documentation and talking to people about the schema is the priority in documenting a graph.  I think that the rationale of class and ER diagrams being class-oriented is relatively well understood.

The second point you make about guessing class information from instances is interesting but isn't simple for the reasons you mentioned.  I had some good discussions with both StarDog and Cambridge Semantics on the subject of graphs without schemas in a previous professional capacity and there is an agreement with both of those vendors that well-structured graphs start with the schema and then have the instances implemented.  It might be well worth a separate request to consider a functionality in Linked Data for creating a schema on the basis of instance data, but in reality, it is unlikely to be able to apply constraints in a very reliable manner.  Perhaps such a feature should only be considered as a "get you going" schema in the same way as you might ask ChatGPT to draft something you for - subject to subsequent human review.

Best regards


Lloyd Jackman

Product Owner, DaaS Data Pipeline

London Stock Exchange Group



***@***.******@***.***>



lseg.com



[wPvoEp5tmbNFAAAAABJRU5ErkJggg==]



***@***.***?anonymous&ep=signature>             Book time to meet with ***@***.***?anonymous&ep=signature>
________________________________
From: Rinke Hoekstra ***@***.***>
Sent: 29 July 2024 3:20 PM
To: elsevierlabs-os/linked-data ***@***.***>
Cc: Lloyd Jackman ***@***.***>; Comment ***@***.***>
Subject: Re: [elsevierlabs-os/linked-data] Add convert to Mermaid (Issue #13)

*** EXTERNAL EMAIL ***


The problem with class-diagrams or ER-diagrams is that they are class-based, not instance-based.

We can do one of the following:

  *   Only represent RDFS and/or OWL information from the graph as Mermaid diagram (this may be very disappointing for graphs without schema)
  *   Guess RDFS class information from the graph to create Mermaid diagrams (this may turn ugly when nodes have multiple types).
  *   Abuse the Mermaid notation for instance information (e.g. every URI Resource is a Mermaid Class)

Don't think there's a solution that's both elegant and satisfying

—
Reply to this email directly, view it on GitHub<https://github.com/elsevierlabs-os/linked-data/issues/13#issuecomment-2255928539>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AFUY6E6FAJWFYPLBRD5TLK3ZOY6SJAVCNFSM6AAAAAA3ELJEP6VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDENJVHEZDQNJTHE>.
You are receiving this because you commented.Message ID: ***@***.***>
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



