# 48. Support for Multi-Version ProductFootprint Exchange in the API

Date: 2025-03-26

## Context

Starting with API version 3.0, the API now supports the exchange of ProductFootprints conforming to multiple versions of the ProductFootprint data model, including both version 2.x and version 3.0. This enhancement ensures backward compatibility with existing implementations while enabling the adoption of the latest features and improvements introduced in version 3.0.

Previously, the API was tightly coupled to a single version of the ProductFootprint data model, limiting flexibility and requiring users to upgrade their systems whenever a new version of the data model was introduced. By decoupling the API from a specific ProductFootprint version, this proposal allows for greater flexibility and smoother transitions between versions.

## Status

To be presented in Tech WG 02 Apr 2025.

This proposal is based on: [Multi-Version API Design](https://www.notion.so/Multi-Version-API-Design-1234567890abcdef1234567890abcdef?pvs=21).

**Methodology**

The final decision will be updated in the PACT Framework v3.0.0.

**Tech Specs**

Final decision will be (or is) updated in the Technical Specifications v3.0.0.

## Context

The PACT API prior to version 3.0 was limited to exchanging ProductFootprints conforming to a single version of the data model. This limitation created challenges for organizations needing to maintain compatibility with older systems while adopting newer data model versions.

The introduction of multi-version support addresses these challenges by enabling the API to handle requests and responses for both version 2.x and version 3.0 ProductFootprints. This approach ensures backward compatibility while allowing users to benefit from the latest features of the ProductFootprint data model.

The proposal specifically addresses the following key aspects:

- **Backward Compatibility**: Ensures that systems relying on version 2.x ProductFootprints can continue to function without modification.
- **Version Negotiation**: Introduces mechanisms for clients to specify the desired ProductFootprint version in API requests.
- **Future-Proofing**: Lays the groundwork for supporting additional ProductFootprint versions in future API updates.

## Proposal

### Multi-Version Support Mechanism

The following table outlines the key changes to the API to enable multi-version support:

| Feature | Description |
| --- | --- |
| **Version Negotiation** | Clients specify the desired ProductFootprint version using the `Accept` HTTP header. The server responds with the requested version, if available. |
| **Default Behavior** | If no version is specified, the server defaults to the latest supported version (currently 3.0). |
| **Error Handling** | If the requested version is not supported, the server responds with HTTP 406 (Not Acceptable) and includes a list of supported versions in the `Accept-Version` header. |
| **Response Metadata** | The server includes the version of the returned ProductFootprint in the `Content-Type` response header. |

### Practical Examples

**Requesting ProductFootprints (Version 3.0):**

```http
GET /footprints/?geography=DE&companyId=xyz HTTP/1.1
Host: api.example.com
Accept: application/json; version=3
```

```http
HTTP/1.1 200 OK
Content-Type: application/json

[{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "$schema": "https://specs.carbon-transparency.org/pact/3.0.0-datamodel.yaml"
  "specVersion": "3.0.0",
  "status": "Active",
  "created": "2025-03-01T00:00:00Z",
  "productDescription": "Example Product",
  ...
},
...
]
```

**Requesting a ProductFootprint (Version 2.x):**
```http
GET /footprints/{id} HTTP/1.1
Host: api.example.com
Accept: application/json; version=2

**Response (Version 2.x):**

{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "specVersion": "2.3.0",
  "status": "Active",
  "created": "2025-03-01T00:00:00Z",
  "productDescription": "Sample",
  ...
}
```


## Considerations

**Backward Compatibility**: The API must ensure that existing clients using version 2.x ProductFootprints can continue to function without requiring changes.

**Future Expansion**: The design should accommodate additional ProductFootprint versions in the future without requiring significant changes to the API.

**Split documentation**: This will require a split between specifications of the Exchange API and the specifications of the different versions of the data model.
