# 35. Unambiguous created & updated attribute description

Date: Aug 6, 2024

Author: Beth Hadley

## Status

Proposed
- Discussed with initiatives (TfS, CX) and internally
- To be presented to Tech Working Group August 7, 2024

## Context

### Business Context
The attributes `created` and `updated` in the PACT Tech Specs are defined in an ambiguous way. The current description simply defines "created" as "the timestamp of the creation of the ProductFootprint" which could be interpreted a number of ways functionally:
- When the PCF calculation began
- When the PCF calculate ended
- When the PCF calculation was entered into the software
- When the PCF was made available
- When the PCF was issued (i.e. declared, independent of when or if it has been shared)

Or, alternatively, the meaning could be purely technical without any functional interpretation regarding the PCF itself:
- When the data record was written into the system (i.e. a record created in a database, etc.)

This ambiguity has resulted in confusion and misaligned interpretation of this field. TfS for example has interpreted `created` as the "Date of Issue", whereas (some) solution providers have interpreted `created` as the time stamp of The PCF record being created in their system (without functional meaning necessarily).

When SAP first raised this question to PACT (October 2023) we learned from the early editors of the PACT Tech Specs that the original intention of the attribute was to leave the interpretation ambiguous. We then validated with the Tech Working Group the need to define the attribute unambiguously, and the community agreed with resounding consensus. We decided to pause however on reaching consensus on the definition until we could address all 6 datetime attributes holistically, to ensure the definition agreed does not overlap with the other datetime attributes.
<img width="737" alt="Screenshot 2024-08-06 at 11 59 56" src="https://github.com/user-attachments/assets/54112eb4-0eee-4d57-bb23-c7ada7d53373">

<img width="1016" alt="Screenshot 2024-08-06 at 12 17 08" src="https://github.com/user-attachments/assets/5d99865b-c290-4b98-8ed4-60dc81997285">

## Proposal

Given the above context, we have now clarified that the intention of the `created`  and `updated` attributes are strictly technical; to enable systems to maintain records internally, and to give indication to receiving systems regarding the data records. The attributes are not intended to have any functional interpretation, and further are standard attributes in any data model for data exchange. With this context, we are now able to provide unambiguous definitions of the attributes.

Therefore, we propose to clarify the ambiguity by updating the attribute descriptions accordingly:

```
<tr>
  <td><dfn>created</dfn> : [=DateTime=]
  <td>String
  <td>M
  <td>A ProductFootprint MUST include the property created with value the timestamp of the creation of the ProductFootprint record in the system. No corresponding functional meaning is necessarily attributed to the record creation in the system. The timestamp MUST be in UTC.

<tr>
  <td><dfn>updated</dfn> : [=DateTime=]
  <td>String
  <td>O
  <td>A ProductFootprint SHOULD include the property updated with value the timestamp of the update of the ProductFootprint record in the system. A ProductFootprint MUST NOT include this property if an update of the record has never been performed. No corresponding functional meaning is necessarily attributed to the record update in the system. The timestamp MUST be in UTC.
<tr>
```

## Consequences

1. The above update is a semantic clarification and does not cause a backwards breaking change, therefore the update can be made in Technical Specification V2.3
2. Solution Providers who may have interpreted the attributes differently should take note of this update and update their implementations accordingly.
3. Initiatives (TfS, CX) have been part of this discussion and decision and will likewise take this update into consideration as we continue to work towards harmonization.
