# 48. Support multiple PCF versions in the API

Date: 2025-03-26

## Context

As we are moving from PACT version 2.x to version 3.0 and beyond, there will be a growing need to support multiple versions simultaneously, at least during the timespan that companies and solution providers upgrade to a newer version of their
software and systems. Starting with PACT API version 3.0, we propose the API to support the exchange of ProductFootprints 
conforming to multiple versions of the ProductFootprint data model, including both version 2.x and version 3.0 and possible
future versions. This enhancement will ensure future backward compatibility while enabling the 
adoption of the latest features and improvements introduced in version 3.0.

Previously, the API was tightly coupled to a single version of the ProductFootprint data model, limiting flexibility and 
requiring users to upgrade their systems whenever a new version of the data model was introduced. By decoupling the API 
from a specific ProductFootprint version, this proposal allows for greater flexibility and smoother transitions between 
versions.

## Status

To be presented in Tech WG 26 Mar 2025.

This proposal is based on: [Multi-Version API Design](https://backlog.carbon-transparency.org).


**Tech Specs**

Final decision will be or is updated in the Technical Specifications v3.0.0.

## Introduction

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

### Identifying PCF schema versions

For a client of the API to identify the schema of the PCF a property `$schema` will be included in each PCF starting version 3.0, pointing to the applicable version of the JSON-schema.

This is not something which can be 

### Syntax of the `Accept` HTTP Header

Following REST API best practices, the HTTP `Accept` header will be used by any client of the API to denote what data model version it 
will accept. 

Because PCFs are backwards compatible *within* a given *major* version, clients only need to specify a *major* version number.

The Accept header conforms to

```http
Accept: application/json; version=X
```
where X can be any major version of the PACT data model; currently 1, 2 or 3.

A client can signal that it accepts multiple version by using

```http
Accept: application/json;version=X, application/json;version=Y
```

### Changes to API actions

#### Action GetFootprint

Include `Accept` HTTP Header in the request. Reply with 406 if the requested version(s) are not supported.

#### Action ListFootprints

Include `Accept` HTTP Header in the request. Reply with 406 if the requested version(s) are not supported.

#### Action Events

- Event `ProductFootprint.Request.Created`. The data recipient (client) POST this event and uses the `Accept` HTTP Header.
- Event `ProductFootprint.Request.Fulfilled` POST a PCF in reply the to the request event. The PCF includes the schema version which MUST correspond to the requested version. 
- Event `ProductFootprint.Request.Rejected`: schema version not relevant, as no PCF data will be send back
- Event `ProductFootprint.Published`: schema version not relevant, as the data recipient only receives a list of ID's. The data recipient needs to specify the `Accept` header in subsequent calls to   **GetFootprint** to actually obtain the PCFs.

### HTTP 406 Error response

If the data-owner receives a request for a PCF schema version which it can not support, it MUST respond with a **406 Not Acceptable** error code. It MUST include a list of supported major versions in the error description:

```http
HTTP/1.1 406 Not Acceptable
Date: Wed, 26 Jun 2025 12:00:00 GMT
Content-Type: application/json

{
  "code": "Unsupported",
  "message": "Supported versions: 2,3",
  "versions": [2,3]
}

```


### Practical Examples

**Requesting ProductFootprints (Version 3.0):**

```http
GET /3/footprints/?geography=DE&companyId=xyz HTTP/1.1
Host: api.example.com
Accept: application/json;version=3
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
GET /3/footprints/{id} HTTP/1.1
Host: api.example.com
Accept: application/json; version=2
```

**Response (Version 2.x):**

```json
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
