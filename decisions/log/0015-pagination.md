# 15. Pagination (Pull) for handling high Data Volume

Date: 2022-11-08

## Status

Accepted

## Context

### Business Context
The `ListFootprints` Action may return a lot of results. In order to be able to limit the output, the end point shall support pagination in a backwards-compatible way.

## Decision

0. Pagination is done server-side.
1. Pagination support is *optional* for backwards-compatibility reasons.
2. Pagination is enabled by setting the *optional* query parameter `limit` for the `ListFootprints` action. It defines the maximum number of product footprints returned in the response body
3. Host systems not supporting pagination respond in the way currently specified
4. Host systems supporting pagination return a HTTP `Link` Header for pagination (see below for details)

## Detailed Technical Proposal

### Overview and Reasoning

Pagination is handled server-side / through the host system by supplying an opaque pagination link to the data recipient[^1] via the HTTP `Link` header (see [REST API Changes](#rest-api-changes)). The header is present in case there are additional ProductFootprints retrievable by the data recipient and the host system supports pagination. 

Pagination is implemented server-side such that host systems remain in full control over the pagination process at any time; such that
- they can invalidate opaque pagination links if needed and at their discretion
- pagination cannot be parallelized by data recipients, giving them more control over accepted and anticipatable load by data recipients
- host systems are free to choose and implement pagination strategies that fit their underlying components and services best

### "Contract" between Host system and data recipient

In case a host system supports pagination and returns a pagination link
1. a data recipient CAN call the pagination link more than once
2. upon each call, the host system MUST return the same set of Product footprints
4. If a response contains a second pagination link and the data recipient upon calling the second pagination link, the previous pagination link MAY no longer work
   - i.e. clients MUST NOT assume that previous pagination links continue to return results after advancing in the pagination process
5. a pagination link MUST be valid for 180 seconds after creation 
6. a data recipient SHOULD retry calling the pagination link after the server returned an error
   1. and SHOULD use a randomized exponential back-off strategy when retrying

### REST API Changes 

The Action `ListFootprints` is extended by the *optional* request parameter `limit`, such that
   1. The value of `limit` is the *maximum* number of ProductFootprints returned in the response body
  
In case a host system supports pagination and the `limit` query parameter is set, 

1. The host system MAY return less ProductFootprints than requested via `limit` (but must respond with 1 or more ProductFootprints in case there are any, of course)
2. The host system MUST return a `Link` header if there are additional ProductFootprints ready to be retrieved, such that
   1. The `Link` header conforms to [RFC8288](https://www.rfc-editor.org/rfc/rfc8288)
   2. The value of the `rel` parameter is equal to `next`
   3. the target IRI (RFC8288, section 3.1) of the `Link` header is absolute
   4. The value of `host` of the target IRI is equal to the value of the `host` request header from the original `ListFootprints` HTTP request 

In case a host system supports pagination and a data recipient queries the system using a target IRI of a `Link` header
1. the host system MUST return further ProductFootprints upon successful authentication (Bearer Token as for the usual request authentication). The number of ProductFootprints returned MUST NOT exceed the original value of `limit`, and a host system MAY return less than `limit` ProductFootprints. 
2. the host system must return a `Link` header conforming with previous description in case there are additional ProductFootprints available

In case a host system does *not* support pagination, the host system responds the request in the way as currently specified (full listing of product footprints, no `Link` response header).


### Example

Example Request:

```http
GET /0/footprints?limit=20 HTTP/2
host: api.example.com
authorization: Bearer [BearerToken]
```

Example Response:

```http
HTTP/1.1 200 OK
date: Mon, 23 May 2022 19:33:16 GMT
content-type: application/json
content-length: [...]
link: <https://api.example.com/0/footprints?[...]>; rel="next"

{
	"data": [
    ...
  ]
}
```

Example of an *non-conforming* response:

```http
HTTP/1.1 200 OK
date: Mon, 23 May 2022 19:33:16 GMT
content-type: application/json
content-length: [...]
link: <https://api.other-corp.com/0/footprints?[...]>; rel="next"

{
	"data": [
    ...
  ]
}
```

**(The response is non-conforming as the link target IRI is pointing to a different `host`)**


## Consequences

1. Technical Specification must be updated accordingly
2. Solutions must be updated if they want to support pagination (applies to data receivers and data owners)
3. Pagination is directed and sequential / non-concurrent: a data recipient enumerates the ProductFootprints from request to request, as a previous request is necessary to access the next `Link` target IRI for the subsequent data fetch.


[^1]: This is terminology used in the Use Case 001 Tech Specs. A `data recipient` is a client making HTTP requests against a Use Case 001 HTTP REST API.