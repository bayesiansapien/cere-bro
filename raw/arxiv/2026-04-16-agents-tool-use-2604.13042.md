---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13042
category: cs.AI
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13042
published: 2026-04-16
authors: Erik Johan Nystad, Francisco Mart\'in-Recuerda
---

# A Pythonic Functional Approach for Semantic Data Harmonisation in the ILIAD Project

**arXiv:** https://arxiv.org/abs/2604.13042
**Authors:** Erik Johan Nystad, Francisco Mart\'in-Recuerda

## Abstract

arXiv:2604.13042v1 Announce Type: cross  Abstract: Semantic data harmonisation is a central requirement in the ILIAD project, where heterogeneous environmental data must be harmonised according to the Ocean Information Model (OIM), a modular family of ontologies for enabling the implementation of interoperable Digital Twins of the Ocean. Existing approaches to Semantic Data Harmonisation, such as RML and OTTR, offer valuable abstractions but require extensive knowledge of the technical intricacies of the OIM and the Semantic Web standards, including namespaces, IRIs, OWL constructors, and ontology design patterns. Furthermore, RML and OTTR oblige practitioners to learn specialised syntaxes and dedicated tooling. Data scientists in ILIAD have found these approaches overly cumbersome and have therefore expressed the need for a solution that abstracts away these technical details while remaining seamlessly integrated into their Python-based environments. To address these requirements, we have developed a Pythonic functional approach to semantic data harmonisation that enables users to produce correct RDF through simple function calls. The functions, structured as Python libraries, encode the design patterns of the OIM and are organised across multiple levels of abstraction. Low-level functions directly expose OWL and RDF syntax, mid-level functions encapsulate ontology design patterns, and high-level domain-specific functions orchestrate data harmonisation tasks by invoking mid-level functions. According to feedback from ILIAD data scientists, this approach satisfies their requirements and substantially enhances their ability to participate in harmonisation activities. In this paper, we present the details of our Pythonic functional approach to semantic data harmonisation and demonstrate its applicability within the ILIAD Aquaculture pilot.
