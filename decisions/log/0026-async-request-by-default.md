# 26. Switch to async request/response as mandatory (default) behaviour.

Date: 2023-11-07

## Status

Proposed

## Context

Current version of the specification[^1] favors synchronous communication over asynchronous communication. As, especially in the early stages of the network, most requests will target not yet existing PF values, the existing approach using synchronous `ListFootprints` calls will not work. In addition, requests cannot be prioritized by most relevant products, as calls are either based on PF ids (`GetFootprint` ) and not on the ids of the related products or even all PFs are requested in a whole (`ListFootprints`).

The specification[^1] already adresses this by supporting `PF Request Events and Responses`. But this feature is optional at the moment whereas synchronous communication mechanisms (as `ListFootprints`) is defined as mandatory. This complicates or even block integration of existing PCF exchange apps as those apps usually work in an asynchrounous way  and productId focused.

## Decision

The following changes to the tech spec Bikeshed file[^1] shall be made:

1. Change content of `Host System Minimum Requirements` section:
   * Change `Action ListFootprints` from _mandatory_ to _optional_, i.e. move it from _MUST_ to _SHOULD_ paragraph. 
   * Change `Action Events` from _optional_ to _mandatory_, i.e. move it from _SHOULD__ to _MUST_ paragraph. 

2. Add an example of a `ProductFootprintFragment` querying a PF via productId to section `PF Request Event syntax`:
  ```json

     { 
      "productIds": [
        "urn:gtin:4712345060507"
      ]
     }

  ```
3. Add an example of an asynchrounous PF request / repsonse flow to the `Examples` section:
   
   Example PF Request Event

   HTTP request
   ```
      POST Subpath/2/events HTTP/1.1
      host: Hostname
      authorization: Bearer BearerToken
      content-type: application/cloudevents+json; charset=UTF-8
      {
        "type": "org.wbcsd.pathfinder.ProductFootprintRequest.Created.v1",
        "specversion": "1.0",
        "id": "848dcf00-2c18-400d-bcb8-11e45bbf7ebd",
        "source": "//RequesterEventHostname/EventSubpath",
        "time": "2023-11-06T16:23:00Z",
        "data": {
           "pf": { 
               "productIds": ["urn:gtin:4712345060507"]
           },
           "comment": "Please provide current PCF value."
        }
      }
   ```
   HTTP response
   ```
      HTTP/1.1 200 OK
      content-length: 0
   ```

   Example PF Response Event
   HTTP request
   ```
      POST Subpath/2/events HTTP/1.1
      host: Hostname
      authorization: Bearer BearerToken
      content-type: application/cloudevents+json; charset=UTF-8
      {
        "type": "org.wbcsd.pathfinder.ProductFootprintRequest.Fulfilled.v1",
        "specversion": "1.0",
        "id": "5afe8fbf-0ea9-477c-a1df-2d3c95f7eec0",
        "source": "//ProviderEventHostname/EventSubpath",
        "time": "2023-11-08T13:26:00Z",
        "data": {
           "requestEventId": "848dcf00-2c18-400d-bcb8-11e45bbf7ebd"
           "pfs": [
                    {
                    "id": "d9be4477-e351-45b3-acd9-e1da05e6f633",
                    "specVersion": "2.0.1-20230314",
                    "version": 1,
                    "created": "2022-05-22T21:47:32Z",
                    "status": "Active",
                    "companyName": "My Corp",
                    "companyIds": [
                        "urn:uuid:51131FB5-42A2-4267-A402-0ECFEFAD1619",
                        "urn:epc:id:sgln:4063973.00000.8"
                    ],
                    "productDescription": "Cote'd Or Ethanol",
                    "productIds": [
                        "urn:gtin:4712345060507"
                    ],
                    "productCategoryCpc": "3342",
                    "productNameCompany": "Green Ethanol",
                    "comment": "",
                    "pcf": {
                        "declaredUnit": "liter",
                        "unitaryProductAmount": "12.0",
                        "pCfExcludingBiogenic": "0.0",
                        "fossilGhgEmissions": "0.123",
                        "fossilCarbonContent": "0.0",
                        "biogenicCarbonContent": "0.0",
                        "landManagementGhgEmissions": "0.01",
                        "characterizationFactors": "AR5",
                        "crossSectoralStandardsUsed": [
                        "GHG Protocol Product standard"
                        ],
                        "productOrSectorSpecificRules": [
                        {
                            "operator": "EPD International",
                            "ruleNames": [
                            "ABC 2021"
                            ]
                        }
                        ],
                        "boundaryProcessesDescription": "End-of-life included",
                        "referencePeriodStart": "2021-01-01T00:00:00Z",
                        "referencePeriodEnd": "2022-01-01T00:00:00Z",
                        "geographyCountry": "FR",
                        "secondaryEmissionFactorSources": [
                        {
                            "name": "Ecoinvent",
                            "version": "1.2.3"
                        }
                        ],
                        "exemptedEmissionsPercent": 3.1,
                        "exemptedEmissionsDescription": "",
                        "packagingEmissionsIncluded": false,
                        "primaryDataShare": 56.12,
                        "assurance": {
                        "coverage": "product line",
                        "level": "reasonable",
                        "boundary": "Cradle-to-Gate",
                        "providerName": "My Auditor",
                        "completedAt": "2022-12-08T14:47:32Z",
                        "standardName": "ISO ...",
                        "comments": "This is a comment"
                        }
                    },
                    "extensions": [
                        {
                        "specVersion": "2.0.0",
                        "dataSchema": "https://catalog.carbon-transparency.com/shipment/1.0.0/data-model.json",
                        "data": {
                            "shipmentId": "S1234567890",
                            "consignmentId": "Cabc.def-ghi",
                            "shipmentType": "PICKUP",
                            "weight": 10,
                            "transportChainElementId": "ABCDEFGHI"
                        }
                        }
                    ]
                }
            ]
        }
      }
   ```
   HTTP response
   ```
      HTTP/1.1 200 OK
      content-length: 0
   ```

## Consequences

Although synchronous requests are still supported, asynchronous communication will be promoted to be the favored way of PCF exchange. This enables app provider to get the data needed to calculate non existing PFs and provide those as soon as they are available. On the oother hand pf consumers do not have to ask for a not yet existing PF over and over again, but can be sure to get this PF delivered as soon as it is available.

Implementors will have to provide `Action Events` by default, whereas `ListFootprints` become optional. As the first change can be seen as compatible from a consumers view (breaking from an PF providers view), the second one is a breaking change for an API consumer.

[^1]: [spec/v2/index.bs](../../spec/v2/index.bs)
