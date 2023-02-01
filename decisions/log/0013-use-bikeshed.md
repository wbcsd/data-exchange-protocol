# 13. Use Bikeshed as language and tooling for technical specification documents

Date: 2022-10-19

## Status

Accepted

## Context

Google Docs was used for writing the "Use Case 001" technical specification[^1]. This has several shortcomings, starting from

1. we cannot link ADRs with changes to the specification. 
2. verification on the changes made to the specification from version to version, is increasingly hard
3. writing specifications that are free of certain classes of syntactical errors, is not really feasible with Google Docs. 
    - as an example: it is not possible to check references against property ids, etc. 
4. increases transparency, and hopefully thereby inducing trust as well, into the processes around writing technical specifications

We propose the use of Bikeshed for writing technical documentation. It is used by other organizatios as well, such as W3C. 

As a language, Bikeshed generally improves the documentation process:

1. Data structures can be tagged as such in the prosa parts
2. A specification is just a plain text file which can then also be versioned as such
3. It is possible to reference terms, term definitions, chapters, data structures, and properties of data structures natively within the text
4. These links are checked. Reference to a non-existing item (chapter, data structure, etc.) causes a build to fail
   1. i.e. this allows for a CI-like experience when writing and publishing technical specifications
5. The output of Bikeshed is HTML which can then be used for "official" websites listing the agreed upon technical specifications


## Decision

1. Migrating away from Google Docs, we will start using Bikeshed exclusively for technical specification documents from now on


## Consequences

Authors willing to contribute must learn the Bikeshed syntax. The syntax follows Markdown with additions. Documentation can be accessed here[^2]. 


[^1]: https://www.carbon-transparency.com/media/1qcdbdyn/pathfinder-network_technical-specifications-for-use-case-001.pdf
[^2]: https://tabatkins.github.io/bikeshed/
