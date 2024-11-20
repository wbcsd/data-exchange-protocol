Date: 2024-11-11

 ## Status

 Proposed

Work in progress. Feedback gathered during v2.2 and v2.3 specification process. Now being presented to the Tech Working group for inclusion in version PACT Tech Specs 3.0


 ## Context

Being able to select Footprints based on a filter is a must-have for all real-life scenario’s.
This is true for both the synchronous as well as the asynchronous way of getting footprints. 

Currently this is functionality is implied in the API specifciation in two ways:
 
  - First, as a `filter` query-parameter fo the sync API (`/2/footprints`) which is OPTIONAL. 
  - Second, in the async API (/2/event footprint-request.created) takes a `FootprintFragment` as a crude input filter.

### Observations

- Filtering in the async API is optional in v2.
- Using a ProductFootprintFragment offers a very crude way to search and not precisely specified.

  For example, given a fragment:

    { 
        "productIds": ["x","y"]
        "standardsUsed: ["z"]
    }

It is unclear if this means looking for any PCF with both productId="x" *and* productId="y" *and* standardsUsed="z" or 
other logic, like productId="x" *or* productId="y"?


## Proposal 

Streamline the sync + async API by 
  1) **Requiring** the `filter` parameter and implementation for Action list-footprints. 
  2) **Adding** the `filter` parameter to the /event/footprint.request.created


### Synchronous API:

Make the exisiting specified filter parameter MANDATORY.

example

    /footprint?query=((x in productids) and|or (pcf.region=’de’ pcf.region=’de-ba’))

As specified in 2.x the filter should be implemented according to the OData query standard: https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html

### Asynchronous API:

Include a `filter` property in the `FootprintRequest.Created` event:

    {
        "type": "org.wbcsd.pathfinder.ProductFootprintRequest.Created.v1",
        "specversion": "1.0",
        "id": "EventId",
        "source": "//EventHostname/EventSubpath",
        "time": "2022-05-31T17:31:00Z",
        "data": {
        --> "filter": "OData Query"
            "comment": PFRequestComment
        }
    }

This will enable data recipients to select product footprints with sufficient flexibility for real-world scenario's.


## Consequences

Any implementation which has not yet implemented filtering for /2/footprints will need to implement this for version 3. 
The event API will have a new filter parameter, offering the exact same way of filtering via the synchronous ListFootprint  action. In version 2 

As any ProductFootprintFragment can easily be expressd as a query, using the ProductFootprintFragment will become OBSOLETE in a later version.

