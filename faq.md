# FAQ

## Introduction

- **What are the PACT Technical Specifications V3?**
    
    The PACT Technical Specifications V3 are an HTTP REST API specification for the secure exchange of Product Carbon Footprint (PCF) data across interoperable software solutions. The specification includes a data model for PCF data and an API for data exchange. Any solution which implements the specification is able to exchange PCF data in an interoperable way with each other. 
    
    For more details, visit [Technical Specifications v3](https://docs.carbon-transparency.org/tr/data-exchange-protocol/latest).
    
- **Why did PACT release a new version of the Technical Specifications?**
    
    PACT Technical Specifications V1 were released in June 2022, followed by V2 released February 2023.  PACT released the PACT Technical Specifications V3 in April 2025 with an updated data model and protocol for exchanging product-level greenhouse gas (GHG) emission data based on the PACT Methodology V3 (previously Pathfinder Framework) . 
    
    This new version reflects feedback from a consensus-based decision-making process within PACT's Technology Working Group, where stakeholders actively address challenges related to Scope 3 and primary data sharing. The specifications have evolved through two years of collaboration with the WBCSD community, technology partners, and key initiatives.
    For more details, see the [Release Plan](RELEASE-PLAN.md). 
    
- **How were PACT Technical Specifications V3 developed?**
    
    Following the V2 release, feedback was collected from global adopters of the technical specification. In parallel feedback was also raised regarding the PACT Methodology (previously Pathfinder Framework). All feedback received is documented here [here](https://backlog.carbon-transparency.org/). PACT convened two working groups since August 2023 to address the feedback and reach consensus regarding revisions (PACT Methodology Working Group and PACT Technology Working Group). The PACT Technology Working Group meets every 2-3 weeks at alternating times to support global participation. The PACT Technical Specification V3 was the outcome of consensus-based decision making process within the PACT Technology Working Group.
    
    Please see our [decision making criteria](https://wbcsd.sharepoint.com/sites/ClimateEnergy/Documents%20partages/Forms/AllItems.aspx?id=%2Fsites%2FClimateEnergy%2FDocuments%20partages%2FClimate%20Imperative%2F04%20Workstreams%2F05%20PACT%2F03%20Workstreams%2F99%20Overarching%2F06%20Standard%20Evolution%20Process%2FPACT%20Decision%20Making%20Policy%2Epdf&parent=%2Fsites%2FClimateEnergy%2FDocuments%20partages%2FClimate%20Imperative%2F04%20Workstreams%2F05%20PACT%2F03%20Workstreams%2F99%20Overarching%2F06%20Standard%20Evolution%20Process&p=true&ga=1) and the [Network contribution policy](https://wbcsd.sharepoint.com/sites/ClimateEnergy/Documents%20partages/Forms/AllItems.aspx?id=%2Fsites%2FClimateEnergy%2FDocuments%20partages%2FClimate%20Imperative%2F04%20Workstreams%2F05%20PACT%2F03%20Workstreams%2F04%20Technology%2F02%20Tech%20Working%20Group%2FPACT%20Network%20Contribution%20Policy%2Epdf&parent=%2Fsites%2FClimateEnergy%2FDocuments%20partages%2FClimate%20Imperative%2F04%20Workstreams%2F05%20PACT%2F03%20Workstreams%2F04%20Technology%2F02%20Tech%20Working%20Group&p=true&ga=1) for further information. Get in touch with PACT if you are interested in joining the working groups.
    
- **Who are the PACT Technical Specifications V3 designed for?**
    - The PACT Technical Specifications V3 are intended for:
        - **Software Developers** building tools for exchanging product carbon footprints using the PACT Methodology.
        - **Product Managers and Sustainability Experts** seeking to understand product footprint data semantics and exchange processes.
        - **Anyone** interested in the technological foundations of the PACT Network.
- **How does the release of V3 align with PACT's overall goals and strategy?**
    - PACT seeks to turn the Scope 3 emissions challenge into an opportunity for companies and organizations by enabling consistent calculation and exchange of primary data of product cradle-to-gate emissions across value chain partners.
    
    Specifically, PACT:
    
    1. Creates convergence and **harmonization on upstream Scope 3 emissions transparency** to ensure an integrated and aligned global ecosystem with close collaboration between all stakeholders
    2. **Establishes the PACT Methodology (methodological guideline)** by building on the GHG Protocol and other existing standards to enable consistent product-level emissions calculation and primary data exchange
    3. Defines the **PACT Network** and **PACT Technical Specifications** for the secure exchange of Product Carbon Footprint data across technology solutions, linking global value chains and industries.
    
    The **PACT Technical Specifications V3** ensures the practical implementation of a standardized approach for digital data exchange, ensuring interoperability and data consistency.
    

## Release Timeline and Feedback Process

- **When was V3 officially released?**
    
    V3 was released April 30, 2025, see the [release plan](RELEASE-PLAN.md).
    
    [Register for the launch events in June 2025 to learn more](https://wbcsd.my.salesforce-sites.com/GuestEventPageV2?aId=a5sVj0000004pFF) 
    
- **Was there a public review period for V3?**
    
    Yes, the public consultation phase began February 18, 2025 and ended March 28, 2025.
    
- **How can the community provide feedback on V3?**
    
    If you have a GitHub account, please log onto the platform and raise an issue directly on [GitHub](https://github.com/wbcsd/data-exchange-protocol/issues). Alternatively, please share your feedback via email to: [pact@wbcsd.org](mailto:pact@wbcsd.org) and [schuurmans@wbcsd.org](mailto:schuurmans@wbcsd.org).
    
    For in-depth information on rationale behind changes, please visit the [PACT Backlog](https://backlog.carbon-transparency.org) and [PACT on GitHub](https://github.com/wbcsd/data-exchange-protocol).
    
- **Will there be future releases beyond V3?**
    
    V3 will be a long-term release. You can expect some patch releases for the upcoming year. The tech community will gather insights during the adoption and usage of V3, and based on that decide on future minor releases (backwards compatible).
    
- **How does the release of PACT Technical Specification V3 align with the release of PACT Methodology V3?**
    
    While the PACT Methodology V3 prescribes the way to calculate product carbon footprints (PCFs), the PACT Technical Specification specifies both the data model and the way to exchange these PCFs. The updated data model for V3 is a reflection of the V3 Methodology. 
    
    It is important however to note that the V3 data model can accommodate PCFs calculated according to Methodology V2 AND V3.
    
- **How can V3 be used?**
    
    PACT encourages the adoption of the PACT Technical Specifications to create digital solutions supporting value chain transparency and decarbonization. PACT supports companies to create so-called "PACT Conformant Solutions", i.e. software which implements the Technical Specifications, and promotes conformant solutions via the PACT website and other marketing channels. The Technical Specifications include a license which explicitly allows for the creation of commercial derivatives, [see here](LICENSE.md). Derivative works (software, derived specifications, etc.) must cite WBCSD PACT.
    

## Key Changes and Impact on V2 Users

- **What are the major differences between V2 and V3?**
    
    Changes to the V3 data model:
    
    - new properties to accommodate for V3 of the PACT Methodology. E.g. on biogenic GHG emissions and removals.
    - improved clarity on properties for specifying the amount per declared unit.
    - addition of new units of measurement for service-related PCFs
    - uniform naming schema for product-, company- and classification-identifiers.
    - simplified versioning of PCFs by removing the distinction between minor and major PCF versions.
    - Consistent in usage of decimal numbers for any non-integer values.
    
    Changes to the V3 API:
    
    - Simplified filtering on a specific set of criteria to enable a data recipient to request relevant PCFs to the data owner.
    - Re-use of these criteria for requesting the creation of new PCFs  through the asynchronous Event API.
    - Deprecation of the previous optional OData V4 $filter.
- **Is V3 backwards compatible with V2?**
    
    No. V3.0 is a **major** version following V2.3, and it will not be backwards compatible. 
    
    V3 includes changes to the data model that are not backwards compatible with V2.x. This means solutions conforming to V2 cannot exchange data with V3.
    
    PACT uses [Semantic Versioning](https://semver.org/) to maintain versions of the Technical Specifications. In summary, this implies: 
    
    - **MINOR changes** (e.g., V2.3.x to V2.2.x) are backwards compatible.
    - **MAJOR changes** (e.g., V3.x.x to V2.x.x) are not backwards compatible.
    
    It will, however, be possible to transform V2.x PCFs to V3 PCFs and exchange these over the V3 API. This will give software solutions the opportunity to use older, already calculated, PCFs and exchange these together with new PCFs. 
    
- **What is the deprecation timeline for V2?**
    
    See [Release Plan](RELEASE-PLAN.md) for deprecation timelines.
    
- **Will PACT continue to maintain V2 and support solutions using V2 after V3 is released?**
    
    Yes, PACT will continue to maintain all three stable minor versions of V2 (V2.1.0, V2.2.0, and V2.3.0) even after the release of V3. To encourage adoption of later versions of the standard, PACT will deprecate V2 in April 2026, after which PACT will no longer support nor promote solutions using V2.
    
    Access all the previous stable versions [here](https://docs.carbon-transparency.org/) 
    
    Also, find the [Release Plan](RELEASE-PLAN.md) 
    
- **Does the release of V3 mean that a solution targeting V3 has to go through Conformance Testing again, even if it was tested for V2?**
    
    Yes, Conformance Testing status is tied to a given version; to become Conformant to V3, solutions must complete the Conformance Testing process. This said, solutions will always retain conformance status to a given version. [Start the process here](https://www.carbon-transparency.org/guides/guide-join-pact-network).
    
    If you are already listed as a PACT Conformant solution for V2, you of course retain this status. To be listed as V3 conformant on the [PACT Website](https://www.carbon-transparency.org/network), you will need to complete the testing process for V3.
    
- **Is there any timeline that is requiring V2 PACT Conformant Solutions to become conformant to V3 by?**
    
    No, there is no fixed timeline for V2 PACT Conformant Solutions to become conformant to V3. PACT recommends solutions plan to become conformant within 6 months of the release of V3. However, solutions not conformant to V3 by the V2 deprecation timeline (April 2026) will no longer be promoted by PACT and removed from the PACT website.
    

## Support and Resources

- **What resources are available to help adopt V3? Where can I find these resources?**
    
    You can find all technical documentation related to V3 [here](https://docs.carbon-transparency.org)
    
    All additional documentation can be found [here](https://www.carbon-transparency.org/pact-technology) under the ‘Getting Started’ and ‘Developer Resources’ section. 
    
- **Are there tools available to validate conformance with V3?**
    
    Yes, PACT offers a Conformance Tool which any company may use on-demand to automatically validate the conformance of their solution to any version of the PACT Technical Specifications (V2 or later). The tool will be launched in June 2025. Use of the tool will be mandatory to achieve conformance status. [Learn more](https://www.carbon-transparency.org/pact-network-services)
    
- **What should I do if I have questions while implementing a V3 solution?**
    
    If you should encounter any issues please get in touch with Arunav Chakravarty, [chakravarty@wbcsd.org](mailto:chakravarty@wbcsd.org)
