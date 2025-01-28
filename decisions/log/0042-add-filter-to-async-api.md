Date: 2024-11-11

 ## Status

 Proposed

Work in progress. Feedback gathered during v2.2 and v2.3 specification process. Now being presented to the Tech Working group for inclusion in version PACT Tech Specs 3.0


 ## Context

Being able to select Footprints based on a filter is a must-have for all real-life scenario’s.
This is true for both the synchronous as well as the asynchronous way of getting footprints. 

Currently this is functionality is implied in the API specifciation in two ways:
 
  - First, as a `$filter` OData query-parameter for the sync API (`/2/footprints`) which has been OPTIONAL. 
  - Second, in the async API (/2/event footprint-request.created) takes a `FootprintFragment` as a crude input filter.

### Observations

- Filtering in the async API is optional in v2.
- Using a ProductFootprintFragment offers a crude way to search and not precisely specified.

  For example, given a fragment:

    { 
        "productIds": ["x","y"]
        "standardsUsed: ["z"]
    }

It is unclear if this means looking for any PCF with both productId="x" *and* productId="y" *and* standardsUsed="z" or 
other logic, like productId="x" *or* productId="y"?

An initial proposal was presented in December 2024 to make the OData $filter implementation **MANDATORY** for both synchronous and asynchronous API’s. 

However this was met with pushback from the Tech WG on 18/12/24, because implementing the OData filter:
  - Requires substantial development effort for a perceived overkill of search capabilties.
  - Brings with it unneccesary complications like searching on non-indexed fields being able to construct wildly expensive queries.
  - Does not map well on the async use-case. In case a recipient requests the creation of a PCF, a full OData query can not easily be used to infer what conditions the newly created PCF should match.

As a consequence, after consulting with the Tech WG on 15/1/2025 a limited list of crucial search criteria has been assembled and a new proposal is made to filter on these, using only simple OR + AND operators.


## Proposal 

1) Add the following limited list of criteria to the `List-Footprints` and `Event-FootprintRequest-Created` methods:
    
    * PfId
    * ProductId
    * CompanyId
    * Classification
    * Geography
    * ValidOn
    * ValidBefore
    * ValidAfter
    * Status

2) It must be possible to match: 
    
    * multiple values for the same criterium: e.g. *ProductID* 1 **OR** 2
  
    * on multiple criteria: e.g. (*ProductID* 1 **OR** 2) **AND** (*Region* DE)

3) No other logical operations other than these limited AND/OR combinations will be supported

4) The OData `$filter` parameter for `ListFootprints`  stays **OPTIONAL**. For any implementation already supporting OData, this proposal will be trivial to implement. 


### Criteria

* `productId` (string) can be 1 or more product ID's. Will return all footprints which have a corresponding ID in their `productIds` attribute. Note that a footprint itself can also have multiple product IDs.
* `companyId` (string) can be 1 or more company ID's. Will return all footprints with corresponding id's in the `companyIds` attribute. Note that a footprint itself can also have multiple company IDs.
* `geography` (string) can be 1 or more geographic specifiers. Values specified can denote `geographicRegion` or `geographyCountry` or `geographyCountrySubdivision`. Will return all footprints within the specified geography.
* `classification` (string) can be 1 or more product classifications. Will return all footprints with corresponding values in the `productClassifications` attribute. Note that a footprint itself can have multiple classifications.
* `validOn` (date-string) will match all PCF's which where valid on the date specified: footprint.validityPeriodBegin <= validOn AND validFrom <= footprint.validityPeriodEnd
* `validAfter` (date-string) will match PCF's whith validAfter < footprint.validityPeriodBegin
* `validBefore` (date-string) will match PCF's whith validBefore > footprint.validityPeriodEnd


### Synchronous API:

Implementors MUST accept the criteria mentioned above for the `ListFootprints` method as regular querystring parameters.

    example.org/pact/3/footprint?productId=1234&productId=5678&validFrom=2020-01-20&validOn=2025-12-31

### Asynchronous API:

Include a `filter` object in the `FootprintRequest.Created` event. This object can contain the fixed set of criteria.  

    {
        "type": "org.wbcsd.pathfinder.ProductFootprintRequest.Created.v1",
        "specversion": "1.0",
        "id": "EventId",
        "source": "//EventHostname/EventSubpath",
        "time": "2022-05-31T17:31:00Z",
        "data": {
        --> "filter": {
              "productId": ["1234","5678"],
              "geography": ["DE"],
              "validFrom": "2024-12-30T00:00:00"
            }
            "comment": PFRequestComment
        }
    }

This will enable data recipients to select product footprints with sufficient flexibility for real-world scenario's.

## Extensions

Implementors MAY offer additional criteria to filter on. In doing so, both the sync (ListFootprints) AND async (Events/ProductFootprintRequest.Created) methods MUST implement these criteria.

Additional critera MUST be named x-<implementor>-<criterium>. For example, adding functionality to search for product footprints based on an invoice-id, an software provider could choose to use: 

  `x-atq-invoice-id`

This will enable queries like `.../footprint/?x-atq-invoice-id=12345&geography=FR`


## Consequences

Implementing filtering will be MANDATORY from 3.0 on both ListFootprints and Events methods. 

As any v2 ProductFootprintFragment can easily be expressd as a query, using the ProductFootprintFragment will become OBSOLETE in a later version.

Depending on usage and number of implementations, the 2.x optional OData $filter might become OBSOLETE in a later version as well.

