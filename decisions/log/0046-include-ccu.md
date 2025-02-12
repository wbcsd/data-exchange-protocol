# 46. Include Carbon Capture and Usage (CCU) attributes

Date: 2025-02-07

## Context

In order to report on Carbon Capture and Utilization (**CCU**) in declaring a PCF, a number of attributes need to be added to the PACT data model.
Note: this proposal ONLY deals with CCU, NOT with Carbon Capture and Storage (**CCS**)

After reaching consensus on the Methodology WG and sub-working groups, this proposal describes the changes to be implemented in version 3.0 of the PACT data model. 

## Status

To be presented in Tech WG 12 Feb 2024

This proposal is based on: [Including CCU and CCS methodology](https://www.notion.so/Including-CCU-and-CCS-methodology-41228936da0d405d9814e4ae17f7c25f?pvs=21)

**Methodology**

The final decision will be updated in the PACT Framework v3

**Tech Specs**

Final decision will be (or is) updated in the Technical Specifications v. 3.0.0.

## Context

The PACT Methodology v2 does not  include methodologies to calculate CCU and CCUS/CCS.

Some initiatives already providing guidance on how to calculate CCU and CCUS and it would be beneficial to have a consistent methodology for accounting and reporting of Carbon Capture Utilization and Storage (CCU and CCS) technologies. 

The current data model lacks specific attributes for representing key aspects of CCU and CCS processes, leading to insufficient transparency and hindering accurate emissions accounting.

For simplicity, this proposal will focus on CCU attributes and  leverages feedback from various initiatives, including TfS, Catena-X, and Green x Digital. The goal is to align with existing and emerging standards such as ISO 14067 and the GHG Protocol, while ensuring clarity, flexibility, and user-friendliness.

The proposal specifically addresses the following key aspects:

- **Calculation Approach**: Enables reporting of both the "Cut-off" and "Credit" approaches for CCU, as outlined in the proposal.
- **Proof of Certification**: include information (via URL) to certification document
- **Carbon Content**: For simplicity, include both biogenic and non-biogenic (fossil) content. ~~Differentiates between biogenic and non-biogenic carbon content for enhanced accuracy and clarity.~~
- ~~**Emissions from Capture and Processing**: Includes emissions associated with the capture and processing of CO2.~~
- ~~**Traceability**: Requires information on the origin and pathway of the captured CO2, facilitating supply chain transparency.~~


## Proposal
## Proposal

### New and Modified Attributes for CCU Accounting

The following table outlines the proposed new and modified attributes to be incorporated into the data model. For each attribute, a detailed description, mandatory or optional status, and unit of measurement are provided.

| Attribute | Description | Unit of Measurement |
| --- | --- | --- |
| `ccuCarbonContent` | The amount of captured carbon (both biogenic and fossil) in the product. | kg C |
| `ccuOrigin` | Information about the origin (fossil or biogenic) and path of the captured CO2 used in CCU, including the name and location of the capture facility. This information enhances transparency and traceability, enabling tracking of CO2 across the value chain. | N/A |
| `ccuCalculationApproach` | The calculation approach for CCU: "Cut-off" or "Credit." This aligns with the two accounting methods presented in the proposal. | N/A |
| `ccuCreditCertification` | (Only for Credit Approach) a URL to documentation verifying the certification from an external bookkeeping scheme. This attribute ensures the reliability and avoids double counting of credits within the crediting system. | N/A |

### Considerations

- **Alignment with GHGP Land Sector and Removals Guidance**: As the proposal recommends, the data model expansion should align with the Greenhouse Gas Protocol (GHGP) Land Sector and Removals Guidance. This alignment will ensure consistency in accounting and reporting removals achieved through CCS and facilitate data comparability across different standards.
- **Flexibility for Future Expansion**: The design of the data model should be adaptable to accommodate future data attributes and evolving reporting requirements for CCU and CCS technologies. As these technologies advance and new methodologies emerge, the data model should facilitate seamless integration of new data elements.
- **Data Availability and Quality**: Access to reliable and high-quality data for all attributes is crucial for accurate accounting and reporting. The framework should provide guidance on data collection methods, data quality assessment, and the use of secondary data sources when primary data is unavailable. Additionally, addressing potential data gaps and uncertainties associated with CCU and CCS processes is essential.
- **User-Friendliness and Practical Implementation**: The expanded data model should be user-friendly and cater to various levels of user expertise. This includes clear guidance on data input, calculations, and reporting requirements. Additionally, the implementation process should consider the resources and capabilities of different companies, particularly smaller enterprises, to ensure smooth adoption of the expanded data model.

### Pros

- **Enhanced Transparency and Traceability**: The expanded data model enables a granular and detailed understanding of CCU and CCS processes. By capturing information on carbon origin, calculation approaches, emissions from capture and processing, and CCS-specific details, the proposed attributes significantly enhance the transparency and traceability of emissions accounting.
- **Improved Data Quality and Comparability**: The standardized data attributes and reporting requirements promote consistency and accuracy in reported data. This improved data quality facilitates meaningful comparisons between different CCU and CCS projects and allows for benchmarking and informed decision-making.
- **Support for Emerging Markets and Technologies**: The inclusion of both cut-off and credit approaches for CCU provides flexibility to accommodate different industry practices and business models. This adaptability is crucial for supporting the growth and adoption of CCU and CCS in various sectors.

### Cons

- **Increased Complexity**: Adding multiple attributes to the data model can introduce complexity, particularly for users less familiar with CCU and CCS accounting. The framework should provide comprehensive guidance and resources to mitigate this complexity and ensure the correct application of the expanded data model.
- **Potential Implementation Challenges**: Integrating the new data attributes into existing reporting systems and processes may require adjustments and investments from companies. Addressing potential challenges related to data collection, validation, and management will be crucial for successful implementation.
- **Continuous Updates and Maintenance**: The rapidly evolving nature of CCU and CCS technologies necessitates ongoing updates and revisions to the data model. Ensuring that the framework remains up-to-date and aligned with the latest scientific understanding and industry practices will be an ongoing effort.

### Consequences

- **Backwards Compatibility**: As this would break backwards compatibility with version 2.x these changes should - if accepted - be included from version 3 upwards.

## Status

