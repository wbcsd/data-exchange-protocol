# 49. Hotfix to include in 3.0 for future support for multiple versions

Date: 2025-05-20

## Context

The PACT Technical Specifications currently define both the API exchange methods *and* the data model of the PCFs being exchanged. These are tightly coupled, which means any backwards incompatible change to either requires a new major version release. In addition, the exchange API is expected to change much less and much less frequent going forward than the data model.

ADR 0048 proposes a comprehensive solution for supporting multiple versions of the Product Carbon Footprint (PCF) data model over the same API. This would allow data owners to publish PCFs using different data model versions, and data recipients to specify which version they can consume. However, implementing this full solution requires more testing, feedback, and real-world use cases from solution providers.

To introduce a future implementation of multi-version support without breaking compatibility with existing 3.0 implementation, and forcing a major version upgrade to version 4.0, we propose to introduce a small modification to the 3.0 API that will lay the groundwork for this capability.

## Status

Proposed

## Proposal

Add a mandatory version parameter to all API endpoints in version 3.0 of the PACT Technical Specifications. For the 3.0 release, this parameter will be fixed to `version=3`.

Specifically:

1. For synchronous endpoints:
   - Add a required query parameter `version` to the `ListFootprints` endpoint.
   - The only acceptable value in 3.0 will be `version=3`. 
   - Any other value will result in a 400 Bad Request error

2. For asynchronous event-based communication:
   - Add a required propery `version` to the CloudEvents data payload for the `Request Created Event`, requesting a PCF from the the data owner. 
   - The only acceptable value in 3.0 will be `version=3`. This must be checked immediately upon receiving the request event and will result in an immediate 400 Bad Request error if not found.

This change will allow us to:
1. Establish the version parameter pattern in the API
2. Ensure all implementations of 3.0 check for and validate this parameter
3. Enable a future minor release (e.g., 3.1) to support multiple data model versions by allowing other values for `version`


## Considerations

### Benefits

1. **Future compatibility**: This change establishes a foundation for implementing multi-version support in a future minor release without breaking backward compatibility.

2. **Minimal impact**: Since the parameter is fixed to `version=3` initially, there is minimal complexity added to current implementation efforts.

3. **Known patterns**: Several mature APIs include version parameters separate from the API version to allow for more flexible evolution. Examples include:

   - **Stripe API**: Stripe uses a date-based versioning system where the API version is specified in request headers (`Stripe-Version`), while maintaining the same endpoints. This allows them to evolve their data models independently from the API structure.
   
   - **Salesforce API**: Salesforce uses URL path versioning (e.g., `/v53.0/`) but maintains backwards compatibility for older versions of resource representations, effectively separating the API contract from resource schemas.
   
   - **Azure API Management**: Microsoft's Azure allows APIs to maintain multiple versions with different underlying schemas while preserving the same API surface through version parameters.
   
   This approach of separating the API contract version from the data model version provides greater flexibility for evolution while maintaining backward compatibility.

### Risks and Mitigations

1. **Increased complexity**: This adds a parameter that currently has only one valid value, which might seem unnecessary. However, the documentation will explain the purpose is to enable future capabilities.

2. **Potential confusion**: Implementers might confuse the API version ("/3/") with the `version` parameter. Clear documentation will distinguish between the API contract version and the data model specification version.

3. **Implementation overhead**: Solution providers will need to implement parameter validation logic for a parameter with only one valid value initially. This is a minor overhead but necessary for future compatibility.

### Alternative Approaches

1. **Wait for v4.0**: We could wait until v4.0 to implement multi-version support. Benefits are that we would have This would delay the benefits of supporting multiple data model versions.

2. **Implement full multi-version support now**: We could implement the full solution proposed in ADR 0048 immediately, but this would introduce significant complexity without the benefit of feedback from real-world implementations.

3. **Rely on current approach**: Currently software solutions can support multiple versions by implementing multiple versions of both data model *and* API, where the endpoint determines the version:

   - pcf.exchange.com/pact/2/...
   - pcf.exchange.com/pact/3/...

Compared to one single API supporting multiple versions of the dara model, this approach incurs the extra overhead of implementing each version of the API as well. Note however, that for a typical software solution, the complexity of the API is much lower compared to the PCF data model and its corresponding logic and user-interface.

4. **Use content negotiation**: We could use HTTP content negotiation mechanisms instead of query parameters. This was rejected as it would require more significant changes to client implementations.

### Backward Compatibility

This change maintains backward compatibility with any draft implementations of 3.0, as it only adds a required parameter with a fixed value. Future minor releases that extend the allowed values of ` `version` will remain backward compatible with 3.0 implementations.

