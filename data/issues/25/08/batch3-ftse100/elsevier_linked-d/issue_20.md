metadata {
link: https://github.com/elsevierlabs-os/linked-data/issues/20
labels: None
data opened: 2024-07-24T12:31:08Z
author: RinkeHoekstra
hyperlink: https://github.com/elsevierlabs-os/linked-data/issues/20
issue title: Adopt RDF/JS library (pending ES module support in VSCode)
}

issue description:
Adopting the RDF/JS libraries has benefits over using Oxigraph and rdflib.js. 

* It allows for more finegrained control of rendering, and supports the preservation of namespace prefixes when converting from one format to another. 
* It supports TriG

Current blocker is the lack of support for ES modules in Electron, and consequently VSCode. This means that we cannot import any of the RDF/JS libraries natively as this requires an unsupported dynamic import.

Until [VSCode](https://github.com/microsoft/vscode-loader/issues/36) and [Electron](https://github.com/electron/electron/issues/21457) support this.

comments (list all):
No comments found.
