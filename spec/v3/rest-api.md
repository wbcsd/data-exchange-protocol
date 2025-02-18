## Introduction ## {#api-intro}

<div class=note>Non-normative</div>

This section defines an [[!rfc9112|HTTP]]-based API for the [=interoperable=] exchange of [[#productfootprint|Product Footprint]] data between [=host systems=].

The scope of the HTTP API is minimal by design. Additional features will be added in future versions of this specification.



## <dfn>Host System</dfn> ## {#api-host-system}

A host system serves the needs of a single or multiple [=data owners=]. Additionally, a host system can also serve the needs of [=data recipients=] if it retrieves data from host systems by calling the HTTP REST API ([[#api]]).

Interoperable data exchange between a data owner and a data recipient can be achieved by

1. the data owner offering <{ProductFootprint}> data through a host system that implements the [[#api|HTTP REST API]], and
2. the data recipient making [[#api-auth|authenticated calls]] to retrieve ProductFootprint data; e.g. by calling the [=Action ListFootprints=].


### Out of scope ### {#api-host-system-out-of-scope}

<div class=note>Non-normative</div>

This standard focuses on the necessary definitions to enable interoperable data exchange between data owners and data recipients. This is mediated through a host system which implements the HTTP REST API defined in this document.

Within the [=PACT=] Project, conforming host systems are called solutions.

Solutions add further functionality on top of this standard in order to enable meaningful and interoperable data exchanges.

The following section briefly describes some of the additional functionality which is beyond the scope of this document:

<ol type="a">
  <li>Footprint calculation according to the PACT Methodology</li>
  <li>Authentication and access management: the act of deciding and setting which product footprint may be accessed by each data recipient</li>
  <li>Credentials management: the overall functionality to generate access credentials for data recipients, to exchange these credentials with data recipients, to rotate or revoke such credentials, etc.</li>
  <li>Logging: creation and storage of access logs and audit trails related to data exchange, authentication processes, etc.</li>
</ol>


## Authentication Flow ## {#api-auth}

A [=host system=] requires a [=data recipient=] to first authenticate before successfully calling an Action (such as [=Action ListFootprints=] or [=Action Events=]). The [=data recipient=] MUST perform the <dfn>authentication flow</dfn>:

1. data recipient attempting to perform the OpenId Connect-based flow, by
    1. retrieving and validating the [=OpenId Provider Configuration Document=] of the host system (see [[!OPENID-CONNECT]]), and then
    2. using as [=AuthEndpoint=] the value of the `token_endpoint` property of the [=OpenId Provider Configuration Document=]
2. otherwise, data recipient using [=AuthHostname=]`/`[=AuthSubpath=]`/auth/token` as the [=AuthEndpoint=] in the next step.
3. data recipient retrieving the [=access token=] from [=AuthEndpoint=] (see [[#api-action-auth-request]]).

Note: The [=authentication flow=] is defined such that a Version [VERSION] data recipient can authenticate against host versions irrespective of their support for OpenID-Connect.

<figure>
  <img src="diagrams/authentication-flow.svg" height="100%" width="100%" >
  <figcaption>Authentication flow.</figcaption>
</figure>


Once the [=authentication flow=] is complete, the [=data recipient=] can call the other actions of the [=host system=]
  - using the value of `access_token` of the response of the [=Action Authenticate=] call as the
    value for a [[!rfc6750]] <dfn>Bearer token</dfn>
  - presenting the Bearer token for subsequent call(s) to the host system in accordance with
    [[!rfc6750]] Section 2.1

[=Access tokens=] SHOULD expire. In this case, data recipients MUST retrieve a new [=access token=]
as described in this section.

## Host system minimum requirements ## {#api-requirements}

A [=host system=] MUST implement actions [=Action Authenticate=], [=Action ListFootprints=], [=Action GetFootprint=], and [=Action Events=].

A [=host system=] MUST offer its actions under https method only.

A [=host system=] SHOULD offer an [=OpenId Provider Configuration Document=] as specified in [[!OPENID-CONNECT]].

A [=host system=] MUST offer all actions under the same [=Hostname=] and [=Subpath=] except for the token endpoint ([=Action Authenticate=] and the endpoint returned from the [=OpenId Provider Configuration Document=]).

A [=host system=] CAN offer the [=OpenId Provider Configuration Document=] and [=Action Authenticate=] under [=AuthHostname=] and [=AuthSubpath=] which are different from [=Hostname=] and [=Subpath=].

If a host system does not offer an [=OpenId Provider Configuration Document=], [=data recipients=] MUST assume that [=Action Authenticate=] is offered under [=AuthHostname=]`/`[=AuthSubpath=]`/auth/token` (see [[#api-auth]]).

<div class=example>
  The host system's DNS domain name is `example.org` and the subpath is `/wbcsd` whereas the ID management system uses a `id.example.org` domain with an empty subpath. The URIs would then be:

    - for [=OpenId Provider Configuration Document=]: [https://id.example.org/.well-known/openid-configuration](https://example.org/wbcsd/.well-known/openid-configuration)
    - for [=Action Authenticate=]: [https://id.example.org/auth/token](https://id.example.org/auth/token)
    - for [=Action ListFootprints=]: [https://example.org/wbcsd/2/footprints](https://example.org/wbcsd/2/footprints)
    - etc.

</div>


## <dfn>Action Authenticate</dfn> ## {#api-action-auth}

Request an access token using client credentials.

[=Host systems=] MUST implement this action in conformance with [[!rfc6749]] Section 4.4 (OAuth2 Client
Credentials).

[=Host systems=] MAY offer this action under a dedicated [=AuthHostname=] and [=AuthSubpath=].



### Request Syntax (HTTP/1.1) ### {#api-action-auth-request}

For reasons of backwards-compatibility with [=data recipients=] implementing the Version 2.0 authentication flow only,
Host systems MUST offer this action under path [=AuthSubpath=]`/auth/token` and hostname [=AuthHostname=].

<pre highlight=http>
POST <l>[=AuthSubpath=]</l>/auth/token HTTP/1.1
host: <l>[=AuthHostname=]</l>
accept: application/json
content-type: application/x-www-form-urlencoded
authorization: Basic <l>[=BasicAuth=]</l>
content-length: <l>[=ContentLength=]</l>

<l>[=AuthBody=]</l>
</pre>

In addition, if a host system supports OpenId Connect, the host system CAN offer and implement this Action under a second URL, and set this URL as the value of `token_endpoint` of the [=OpenId Provider Configuration Document=].

<pre highlight=http>
POST <l>[=AuthEndpoint=]</l> HTTP/1.1
accept: application/json
content-type: application/x-www-form-urlencoded
authorization: Basic <l>[=BasicAuth=]</l>
content-length: <l>[=ContentLength=]</l>

<l>[=AuthBody=]</l>
</pre>

With Request parameters:

: <dfn>AuthEndpoint</dfn>
:: The endpoint to request an [=access token=] after discovering the value by performing the [=authentication flow=].

: <dfn>AuthSubpath</dfn>:
:: If a [=host system=] uses a relative subpath dedicated to serving an [=OpenId Provider Configuration Document=] and creating an [=access token=], then the requesting [=data recipient=] MUST use this subpath.

: <dfn>AuthHostname</dfn>
:: The requesting data recipient MUST use the domain name of the host
    system dedicated to serving an [=OpenId Provider Configuration Document=] and creating an [=access token=].

: <dfn>BasicAuth</dfn>
:: See [[!rfc6749]] Section 4.4.2

: <dfn>AuthBody</dfn>
:: See [[!rfc6749]] Section 4.4

: <dfn>ContentLength</dfn>
:: The length of the Body. See [[!rfc9112]].


### Response Syntax ### {#api-action-auth-response}

<pre highlight=http>
HTTP/1.1 <l>[=AuthStatusCode=]</l> OK
content-type: application/json
content-length: <l>[=ContentLength=]</l>

<l>[=AuthResponseBody=]</l>
</pre>

With action-specific response parameters

: <dfn>AuthStatusCode</dfn>
:: A HTTP response code conforming to [[!rfc6749]] Section 4.4 and Section 5.

: <dfn>AuthResponseBody</dfn>
:: A JSON Object conforming to either RFC 6749 Section 4.4 in case of successful authentication (containing an <dfn>access token</dfn>), or RFC 6749 Section 5.2 otherwise. See [[#api-auth]] for further details


#### Example Successful Response #### {#api-action-auth-response-success}

Example [=AuthResponseBody=] for a successful authenticate call:

<div class=example>
<pre highlight=json>
{
  "access_token": "...",
  "token_type": "bearer"
}
</pre>
</div>


#### Example Error Response #### {#api-action-auth-response-no-success}

Example HTTP call, for instance generated because username or password did not match:

<div class=example>
<pre highlight=http>
HTTP/1.1 400 Bad Request
date: Mon, 23 Oct 2023 19:33:16 GMT
content-type: application/json
</pre>
<pre highlight=json>
{
  "error": "invalid_client",
  "error_description": "Authentication failed"
}
</pre>
</div>

For further details, for instance on the list of specified values of property `error`, consult [[!rfc6749]] Section 5.2.


## <dfn>Action ListFootprints</dfn> ## {#api-action-list}

Lists [[#productfootprint|product footprints]] with [[#api-action-list-pagination|pagination]] and optional [[#api-action-list-filtering|filtering]].

[=Host systems=] SHOULD implement an access management system and only return the [[#productfootprint|product footprints]] for which the [=data owner=] granted access to the requesting [=data recipient=].

### Filtering ### {#api-action-list-filtering}

Filtering on minimal set of criteria MUST be supported by [=Host systems=].

Note: This MUST be the same set of criteria that can be used with [=PF Request Event=]

Note: Optional filtering specified in version 2.2+ (based on OData4) is NOW DEPRECATED. 


: `productId` array(string) 
:: If present, MUST be 1 or more product ID's. Will return all footprints which have a corresponding ID in their `productIds` attribute. Note that a footprint itself can also have multiple product IDs.
: `companyId` array(string) 
:: If present, MUST be 1 or more company ID's. Will return all footprints with corresponding id's in the `companyIds` attribute.
: `geography` array(string) 
:: if present, MUST be 1 or more geographic specifiers. Values specified can denote `geographicRegion` or `geographyCountry` or `geographyCountrySubdivision`. Will return all footprints within the specified geography(s)
: `classification` array(string) 
:: if present, MUST be 1 or more product classifications. Will return all footprints with corresponding values in the `productClassifications` attribute. Note that a footprint itself can have multiple classifications.
: `validOn` (date-string) 
:: if present, MUST match all PCF's which where valid on the date specified: footprint.validityPeriodBegin <= validOn AND validFrom <= footprint.validityPeriodEnd
: `validAfter` (date-string) 
:: if present, MUST match PCF's whith validAfter < footprint.validityPeriodBegin
: `validBefore` (date-string) 
:: if present, MUST match PCF's whith validBefore > footprint.validityPeriodEnd
: `status` (string) 
:: If Present, MUST be either be "Active" or "Deprecated"

#### Extensions

Implementors MAY offer additional criteria to filter on. In doing so, both the sync (ListFootprints) AND async (Events/ProductFootprintRequest.Created) methods MUST implement these criteria.

Additional critera MUST be named x-<implementor>-<criterium>. For example, adding functionality to search for product footprints based on an invoice-id, an software provider could choose to use: 

  `x-atq-invoice-id`

This will enable queries like `.../footprint/?x-atq-invoice-id=12345&geography=FR`


### Pagination ### {#api-action-list-pagination}

[=Host systems=] MUST implement pagination server-side such that

1. The host system MAY return less ProductFootprints than requested through the [=Limit=] request parameter
2. The host system MUST return a `Link` header if there are additional ProductFootprints ready to be retrieved, such that
   1. The `Link` header conforms to [[!RFC8288]]
   2. The value of the `rel` parameter is equal to `next`
   3. the target IRI (RFC8288, section 3.1) of the `Link` header is absolute
   4. The value of `host` of the target IRI is equal to the value of the `host` request header from the original `ListFootprints` HTTP request

The target IRI from a pagination `link` header is called a <dfn>pagination link</dfn>.

Upon a [=host system=] returning a [=pagination link=]

1. a data recipient CAN call the pagination link more than once
2. upon each call, the host system
    1. MUST return the same set of Product Footprints upon successful authentication (i.e. a Bearer token authentication as defined in [[#api-auth]])
    2. MUST NOT return more product footprints than requested in case [=Limit=] was defined by a [=data recipient=]
    3. MUST return a `Link` header conforming with the previous description in case there are additional ProductFootprints available
3. If a response contains a second pagination link and the data recipient upon calling the second pagination link, the previous pagination link MAY no longer work
    - i.e. data recipients MUST NOT assume that previous pagination links continue to return results after advancing in the pagination process
4. a pagination link MUST be valid for at least 180 seconds after creation
5. a data recipient SHOULD retry calling the pagination link after the server returned an error
   1. and SHOULD use a randomized exponential back-off strategy when retrying


### Request Syntax (HTTP/1.1) ### {#api-action-list-request}

<pre highlight=http>
GET <l>[=Subpath=]</l>/3/footprints?<l>[Criteria]</l><l>[=Limit=]</l> HTTP/1.1
host: <l>[=Hostname=]</l>
authorization: Bearer <l>[=BearerToken=]</l>
</pre>

with request parameters:

: <dfn>Subpath</dfn>
:: If a host system uses a relative subpath, then the requesting data recipient MUST prepend this subpath.

: <dfn>Hostname</dfn>
:: The requesting data recipient MUST use the domain name of the host system.

: <dfn>BearerToken</dfn>
:: see [=Bearer Token=] of section [[#api-auth]]

: <dfn>Criteria</dfn>
:: see [Filtering](#api-action-list-filtering) for the parameters which can be specified.

: <dfn>Limit</dfn>
::
    `Limit` is an OPTIONAL request parameter. If defined,
      1. the name of the HTTP request parameter MUST be `limit`
      2. and the value MUST be a positive integer.


### Response Syntax ### {#api-action-list-response}

<pre highlight=http>
HTTP/1.1 <l>[=ListStatusCode=]</l> <l>[=ListStatusText=]</l>
content-type: application/json
content-length: <l>[=ContentLength=]</l>

<l>[=ListResponseBody=]</l>
</pre>


With response parameters

: <dfn>ListStatusCode</dfn>
::
    If the host system returns a list of product footprints, the `HttpStatusCode` MUST be either 200 or 202:
        - `HttpStatusCode` 200 indicates the returned list is the complete result of the given query.
        - `HttpStatusCode` 202 indicates the returned list is an incomplete result of the given query. The host system MAY return this `HttpStatusCode` if it principally decides that it's able to obtain the remaining data in the future. This `HttpStatusCode` MUST NOT be returned if the request parameter `Filter` is not defined. The [=data recipient=] MAY continue to send the same request with exponential-backoff until it receives the complete result, indicated by `HttpStatusCode` 200.

    If the host system responds with an [=error response=], the `HttpStatusCode` MUST match the HTTP Status Code of the respective [=error response code=].

    If the host system does not return the list of [[#productfootprint|ProductFootprints]], it MUST return an error HTTP Status Code (4xx, 5xx).

: <dfn>ListStatusText</dfn>
::
    The HTTP Status text conforming to the HTTP status code [=ListStatusCode=].

: <dfn>ListResponseBody</dfn>
::
    If the host system accepts the [=access token=], the body MUST be a JSON object with property `data` with value the list of <{ProductFootprint|ProductFootprints}>.
    The list MUST be encoded as a JSON array. If the list is empty, the host system MUST return an empty JSON array.

    The host system MUST return the latest version of each footprint and MAY return previous versions. Among the footprints with identical <{ProductFootprint/id}> values,
    the one with the maximum <{ProductFootprint/version}> value is called the latest version and the rest are called the previous versions.

    If the request parameter `Filter` is defined, the specified expression SHOULD be evaluated for each ProductFootprint in the collection as described in [OData v4 specification](http://docs.oasis-open.org/odata/odata/v4.0/errata03/os/complete/part2-url-conventions/odata-v4.0-errata03-os-part2-url-conventions-complete.html#_Toc453752358), and only <{ProductFootprint|ProductFootprints}> where the expression evaluates to true SHOULD be included in the response. ProductFootprints for which the expression evaluates to false or which are not made available for the [=data recipient=] SHOULD be omitted from the list returned in the response.

    If the access token is valid, but the client does not have the necessary permissions to access the requested <{ProductFootprint|ProductFootprints}>, the host system MUST return an error response with code [=AccessDenied=].

    If the host system does not accept the access token because it expired, the body SHOULD be an error response with code [=TokenExpired=].

    In all other cases, the body SHOULD be an error response with code [=BadRequest=].


## <dfn>Action GetFootprint</dfn> ## {#api-action-get}

Retrieves [[#productfootprint|product footprints]].

[=Host systems=] SHOULD implement an access management system and only return the product footprints for which the [=data owner=] granted access to the requesting [=data recipient=].


### Request Syntax ### {#api-action-get-request}

<pre highlight=http>
GET <l>[=Subpath=]</l>/2/footprints/<l>[=GetPfId=]</l> HTTP/1.1
Host: <l>[=Hostname=]</l>
authorization: Bearer <l>[=BearerToken=]</l>
</pre>

with request-specific parameters:

: <dfn>GetPfId</dfn>
:: The value of property <{ProductFootprint/id}> of a product footprint a [=data recipient=] intends to retrieve.


### Response Syntax ### {#api-action-get-response}

<pre highlight=http>
HTTP/1.1 <l>[=GetStatusCode=]</l> <l>[=GetStatusText=]</l>
content-type: application/json
content-length: <l>[=ContentLength=]</l>

<l>[=GetResponseBody=]</l>
</pre>

With response parameters:

: <dfn>GetStatusCode</dfn>
::
    The HTTP Status Code of the response.

    If the host system accepts the [=access token=], the HTTP Status Code MUST be 200.<br/>
    If the host system responds with an [=error response=], the HTTP status code MUST match the HTTP Status Code of the respective [=error response code=].<br/>
    If the host system does NOT return a product footprint, the host system MUST return an error HTTP Status Code (4xx, 5xx).

: <dfn>GetStatusText</dfn>
::
    The HTTP Status text conforming to the HTTP status code [=GetStatusCode=].

: <dfn>GetResponseBody</dfn>
::
    If the host system accepts the access token and allows the requesting data recipient to access the requested product footprint, the body MUST be a JSON object with property data. The value of property data MUST be the product footprint with footprint identifier [=GetPfId=].

    If there were changes to the requested product footprint with identifier [=GetPfId=], the host system SHOULD return the latest product footprint identified with identifier [=GetPfId=] and the maximum value of property version.

    Note: If a host system implements the life cycle rules, then the “latest” version of the requested product footprint is the one with the maximum value of version with <{ProductFootprint/id}> equal to [=GetPfId=].

    If the access token is valid, but the client does not have the necessary permissions to access the requested <{ProductFootprint}>, the host system MUST return an error response with code [=AccessDenied=].

    If the host system does not accept the access token because it expired, the host system SHOULD return an error response with code [=TokenExpired=].

    The host system MAY return an error response with code [=NoSuchFootprint=].

    In all other cases, the body SHOULD be an error response with code [=BadRequest=].


## Action Events ## {#api-action-events}

The <dfn>Action Events</dfn> enables the exchange of event data between [=data owners=] and [=data recipients=].

The Action Events endpoint is specified for the following use cases:

1. enabling a [=data owner=] to notify a [=data recipient=] on updates to 1 or more [[#productfootprint|Product Footprints]] (see [[#api-action-events-case-1]])
2. enabling a [=data recipient=] to request [[#productfootprint|product footprints]] from a [=data owner=] by sending an event to the [=data owner's=] [=Action Events=] endpoint (see [[#api-action-events-case-2]]).

A [=host system=] SHOULD only accept events after authentication (see [[#api-auth]]).

The Action Events endpoint accepts CloudEvent events (see [[!CE]]) encoded in "Structured Content Mode" (see [[!CE-Structured-Content-Mode]].

Support for Action Events is MANDATORY.

If a [=host system=] does NOT implement the [=Action Events=] endpoint,

1. it SHOULD respond with a conforming [=error response=] and HTTP [=error response code=].
1. it SHOULD respond to authenticated Action Events calls with an [=error response=] with code [=NotImplemented=].
2. it MUST respond with an error HTTP Status Code (4xx, 5xx).


### Request Syntax ### {#api-action-events-request}

The general request syntax is:

<pre highlight=http>
POST <l>[=Subpath=]</l>/2/events HTTP/1.1
host: <l>[=Hostname=]</l>
authorization: Bearer <l>[=BearerToken=]</l>
content-type: application/cloudevents+json; charset=UTF-8

<l>[=EventBody=]</l>
</pre>

With request parameters:

: <dfn>EventBody</dfn>
::
    The [=EventBody=] MUST be
    1. a CloudEvents event (see [[!CE]])
    2. encoded as a JSON object as defined in [[!CE-JSON]]
    3. using "Structured Content Mode" (see [[!CE-Structured-Content-Mode]]).

    Further details on the EventBody syntax and semantics are given in [[#api-action-events-case-1]] and [[#api-action-events-case-2]].


### Response Syntax ### {#api-action-events-response}

The [=host system=] upon accepting the event MUST respond with HTTP Status Code 200 and an empty body:

<pre highlight=http>
HTTP/1.1 200 OK
content-length: 0
</pre>

The host system upon <strong>not</strong> accepting the event SHOULD respond with an [=error response=] (see [[#api-error-responses]]).

### Notification of data recipients on Product Footprint updates ### {#api-action-events-case-1}

A [=data owner=] CAN notify a [=data recipient=] about changes to 1 or more [[#productfootprint|product footprints]] by sending a [=PF Update Event=] to the [=data recipient's=] [=Action Events=] endpoint.

A [=data recipient=] upon receiving such an [=PF Update Event=] CAN retrieve the [[#productfootprint|product footprints]] through the [=Action GetFootprint=].

Accordingly, the [=data owner=] of the [=host system=] sending the event MUST make the referenced Product Footprints available to the [=data recipient=] notified through the PF Update Event.

The <dfn>PF Update Event</dfn> is defined as a JSON-encoded CloudEvent event with the following syntax:

<pre highlight=json>
{
  "type": "org.wbcsd.pathfinder.ProductFootprint.Published.v1",
  "specversion": "1.0",
  "id": "<l>[=EventId=]</l>",
  "source": "//<l>[=EventHostname=]</l>/<l>[=EventSubpath=]</l>",
  "time": "2022-05-31T17:31:00Z",
  "data": {
    "pfIds": <l>[=PfIds=]</l>
  }
}
</pre>

with

: <dfn>EventId</dfn>
::
    A unique identifier for the event set by the [=host system=] sending the event.
    The [=EventId=] MUST be a string (see [[!CE-JSON]]).
: <dfn>PfIds</dfn>
::
    A list of [[#productfootprint|product footprint]] that have been updated.
    The [=PfIds=] MUST be the non-empty list of <{ProductFootprint/id}> values of the updated Product Footprints,
    encoded as a JSON array.
: <dfn>EventHostname</dfn>
:: The [=Hostname=] of the [=host system=] sending the event.
: <dfn>EventSubpath</dfn>
:: The handler of the [=host system=] sending the event.


### Asynchronous request and retrieval of Product Footprints ### {#api-action-events-case-2}

A [=data recipient=] CAN request a [=data owner=] to send a [[#productfootprint|product footprint]] by sending a [=PF Request Event=] to the [=data owner's=] [=Action Events=] endpoint.

A [=data owner=] upon receiving a [=PF Request Event=] can then decide how to process the request
1. by sending a [=PF Response Event=] to the [=data recipient's=] [=Action Events=] endpoint
2. by sending a [=PF Response Error Event=] to the [=data recipient's=] [=Action Events=] endpoint to notify the [=data recipient=] that the request cannot be processed, or
3. by not sending any event to the [=data recipient's=] [=Action Events=] endpoint.

If a [=data owner=] accepted a [=PF Request Event=], the host system MUST send the response back to the [=host system=] referenced in `source` of the [=PF Request Event=].

The host system of the [=data owner=] MUST validate the value of `source` before sending the response.

If the host system of the original requestor (the data recipient) is not available or does not accept the response with a HTTP success code (2xx),
the [=data owner's=] host system SHOULD retry sending the response event using exponential backoff.

A host system SHOULD NOT retry sending a response event for more than 3 days.


#### PF Request Event syntax #### {#api-action-events-case-2-request}

The <dfn>PF Request Event</dfn> MUST be a CloudEvent event sent from a [=data recipient=] to a [=data owner=]
containing a set of criteria that reference the product for wich the PCF is being requested. 

Note: The ProductFootprintFragment in version 2.x is OBSOLETE.

Note: This MUST be the same set of criteria that can be used with [=Action ListFootprints=]


Note: this specification does not yet specify the processing requirements of a host system upon
receiving such an event. This means the host system can e.g. ignore 1 or more properties, it might
not accept specific patterns of requests (for instance it might support querying by reference period
but not by geography), etc.

The [=PF Request Event=] is defined as a JSON-encoded CloudEvent event with the following syntax:

<pre highlight=json>
{
  "type": "org.wbcsd.pathfinder.ProductFootprintRequest.Created.v1",
  "specversion": "1.0",
  "id": "<l>[=EventId=]</l>",
  "source": "//<l>[=EventHostname=]</l>/<l>[=EventSubpath=]</l>",
  "time": "2025-01-31T17:31:00Z",
  "data": {
    "productId": ["urn:pact:product-id:1234"]
    "companyId": ["urn:companyId"]
    "geography": ["DE"]
    "classification": ["urn:cpc:9585"]
    "validOn": "2025-02-01T00:00:00Z",
    "validAfter": "2025-02-01T00:00:00Z",
    "validBefore": "2025-02-01T00:00:00Z",
    "status": "Active",
    "comment": <l>[=PFRequestComment=]</l>
  }
}

</pre>

with
: `productId` array(string) 
:: If present, MUST be 1 or more product ID's. Will return all footprints which have a corresponding ID in their `productIds` attribute. Note that a footprint itself can also have multiple product IDs.
: `companyId` array(string) 
:: If present, MUST be 1 or more company ID's. Will return all footprints with corresponding id's in the `companyIds` attribute.
: `geography` array(string) 
:: if present, MUST be 1 or more geographic specifiers. Values specified can denote `geographicRegion` or `geographyCountry` or `geographyCountrySubdivision`. Will return all footprints within the specified geography(s)
: `classification` array(string) 
:: if present, MUST be 1 or more product classifications. Will return all footprints with corresponding values in the `productClassifications` attribute. Note that a footprint itself can have multiple classifications.
: `validOn` (date-string) 
:: if present, MUST match all PCF's which where valid on the date specified: footprint.validityPeriodBegin <= validOn AND validFrom <= footprint.validityPeriodEnd
: `validAfter` (date-string) 
:: if present, MUST match PCF's whith validAfter < footprint.validityPeriodBegin
: `validBefore` (date-string) 
:: if present, MUST match PCF's whith validBefore > footprint.validityPeriodEnd
: `status` (string) 
:: If Present, MUST be either be "Active" or "Deprecated"
: <dfn>PFRequestComment</dfn>
:: The OPTIONAL comment by the [=data recipient=] to the [=data owner=] about the request.
     If defined, the [=PFRequestComment=] MUST be encoded as a JSON string.

The property `data.comment` of a [=PF Request Event=] is OPTIONAL.

#### PF Response Event syntax #### {#api-action-events-case-2-response}

The <dfn>PF Response Event</dfn> is defined as a CloudEvent event sent from a [=data owner=] to a [=data recipient=] after having received a [=PF Request Event=] from a [=data recipient=] and upon successfully fulfilling the request.

The [=PF Response Event=] is defined as a JSON-encoded CloudEvent event with the following syntax:

<pre highlight=json>
{
  "type": "org.wbcsd.pathfinder.ProductFootprintRequest.Fulfilled.v1",
  "specversion": "1.0",
  "id": "<l>[=EventId=]</l>",
  "source": "//<l>[=EventHostname=]</l>/<l>[=EventSubpath=]</l>",
  "data": {
    "requestEventId": "<l>[=ReqEventId=]</l>",
    "pfs": <l>[=Pfs=]</l>
  }
}

</pre>

with

: <dfn>ReqEventId</dfn>
::
    The [=EventId=] of the [=PF Request Event=] that the [=PF Response Event=] is responding to.
    The [=ReqEventId=] MUST be a string (see [[!CE-JSON]]).
: <dfn>Pfs</dfn>
::
    The list of [[#productfootprint|product footprints]] that have been requested with the [=PF Request Event=] and that are accessible to the [=data recipient=], encoded as an array of <{ProductFootprint}> in JSON.

    Otherwise, the value of [=Pfs=] MUST be the empty JSON array.


#### PF Response Error Event syntax #### {#api-action-events-case-2-response-error}

The <dfn>PF Response Error Event</dfn> is defined as a CloudEvent event sent from a [=data owner=] to a [=data recipient=] after having received a [=PF Request Event=] from a [=data recipient=] and upon NOT successfully fulfilling the request.

The [=PF Response Event=] is defined as a JSON-encoded CloudEvent event with the following syntax:

<pre highlight=json>
{
  "type": "org.wbcsd.pathfinder.ProductFootprintRequest.Rejected.v1",
  "specversion": "1.0",
  "id": "<l>[=EventId=]</l>",
  "source": "...",
  "data": {
    "requestEventId": "<l>[=ReqEventId=]</l>",
    "error": <l>[=ReqErrorResponse=]</l>
  }
}

</pre>

with

: <dfn>ReqErrorResponse</dfn>
::
    The error response that the [=data owner=] is sending to the [=data recipient=] to notify the [=data recipient=] that the request cannot be processed.

    The value of [=ReqErrorResponse=] MUST be an [=error response=] (see [[#api-error-responses]]).

## Error responses ## {#api-error-responses}

The actions [=Action GetFootprint=], [=Action ListFootprints=], and
[=Action Events=] specify general error response handling.

This section specifies the shared HTTP error response handling across these actions.

Error responses are specified in detail such that [=data recipients=] can understand
the cause of the error, and so that potentially [=host systems=] can react on and resolve errors automatically.

Note: [=Action Authenticate=] specifies its own error responses (see [[#api-action-auth-response]]).

Whenever a [=host system=] returns an [=error response=], it MUST send a HTTP response such that
  - the HTTP Status Code equals the `HTTP Status Code` defined for the respective [=error response code=] (see <a href="#api-errors-table">Error Codes Table</a>)
  - with content type set to `application/json`, and
  - with response body the [=error response=]

A <dfn>error response</dfn> is a JSON object with the following properties:
    - `code`: a [=error response code=] encoded as a String
    - `message`: a [=error message=] encoded as a String

A <dfn>error response code</dfn> is a value from column `Error Response Code` from the table below.

A <dfn>error message</dfn> is a human-readable error description. Example values are in column `Example Message` in the table below.

<div class=example>
Example [=AccessDenied=] [=error response=]:

<pre class=include-code>
path: examples/error-response-access-denied.json
highlight: json
</pre>
</div>

A [=host system=] MAY return [=error messages=] different from the table below, for instance localized values depending on a [=data recipient=].


<figure id="api-errors-table">
  <table class="data">
    <thead>
      <tr>
        <th>`Error Response Code`
        <th>`Example Message`
        <th>`HTTP Status Code`
    <tbody>
      <tr>
        <td><dfn>AccessDenied</dfn>
        <td>Access denied
        <td>403
      <tr>
        <td><dfn>BadRequest</dfn>
        <td>Bad Request
        <td>400
      <tr>
        <td><dfn>NoSuchFootprint</dfn>
        <td>The specified footprint does not exist.
        <td>404
      <tr>
        <td><dfn export>NotImplemented</dfn>
        <td>The specified Action or header you provided implies functionality that is not implemented
        <td>400
      <tr>
        <td><dfn>TokenExpired</dfn>
        <td>The specified access token has expired
        <td>401
      <tr>
        <td>InternalError
        <td>An internal or unexpected error has occurred
        <td>500

  </table>
  <figcaption>Listing of error codes and their related error response codes.</figcaption>
</figure>


### Error processing by a data recipient ### {#api-error-responses-processing}

A requesting [=data recipient=] MUST use the code property and potentially also the HTTP Status Code to differentiate between the different errors.



## Examples ## {#api-examples}

<div class=note>Non-normative</div>

### Example Action ListFootprints request and response ### {#api-action-list-example}


<div class="example">

Example request:

<pre highlight=http>
GET /2/footprints?limit=10 HTTP/2
host: api.pathfinder.sine.dev
authorization: Bearer [BearerToken]
</pre>

Example response HTTP headers:
<pre highlight=http>
HTTP/1.1 200 OK
date: Mon, 23 May 2022 19:33:16 GMT
content-type: application/json
content-length: 1831
server: Pathfinder
link: &lt;https://api.pathfinder.sine.dev/2/footprints?limit=10&amp;offset=10&gt;; rel="next"
</pre>

Example response body:
<pre class=include-code>
path: examples/list-footprints-response.json
highlight: json
</pre>

Example response empty body:
<pre highlight=json>
{
  "data": []
}
</pre>

</div>

### Example Error Response ### {#api-error-response-example}

<div class=example>

Example request:

<pre highlight=http>
GET /2/footprints HTTP/2
host: api.pathfinder.sine.dev
</pre>

Example response headers:

```http
HTTP/1.1 403 Forbidden
date: Mon, 23 May 2022 19:33:16 GMT
content-type: application/json
content-length: 44
server: Pathfinder
```
Example response body:
<pre class=include-code>
path: examples/error-response-access-denied.json
highlight: json
</pre>

</div>

### Example PF Request and Response Events  ### {#api-action-events-example}

<strong>Example PF Request Event:</strong>
<div class="example">
<pre highlight=http>
POST Subpath/2/events HTTP/1.1
host: api.pathfinder.sine.dev
authorization: Bearer [BearerToken]
content-type: application/cloudevents+json; charset=UTF-8
</pre>

Example PF Request Event body
```json
  {
    "type": "org.wbcsd.pathfinder.ProductFootprintRequest.Created.v1",
    "specversion": "1.0",
    "id": "848dcf00-2c18-400d-bcb8-11e45bbf7ebd",
    "source": "//RequesterEventHostname/EventSubpath",
    "time": "2023-11-06T16:23:00Z",
    "data": {
        "pf": {
            "productIds": [
                "urn:gtin:4712345060507"
            ]
        },
        "comment": "Please provide current PCF value."
    }
  }
```
Example PF Request Event response headers
  ```http
    HTTP/1.1 200 OK
    content-length: 0
  ```
</div>
<strong>Example PF Response Event:</strong>
<div class="example">
<pre highlight=http>
POST Subpath/2/events HTTP/1.1
host: api.pathfinder.sine.dev
authorization: Bearer [BearerToken]
content-type: application/cloudevents+json; charset=UTF-8
</pre>

Example PF Response Event body
<pre class=include-code>
path: examples/pf-response-event.json
highlight: json
</pre>

Example Response Event response headers
  ```http
    HTTP/1.1 200 OK
    content-length: 0
  ```
</div>


### Example Action GetFootprint request and response ### {#api-action-get-example}

<div class="example">

Example request:

<pre highlight=http>
GET /2/footprint/91715e5e-fd0b-4d1c-8fab-76290c46e6ed HTTP/2
host: api.pathfinder.sine.dev
authorization: Bearer [BearerToken]
</pre>

Example response HTTP headers:
<pre highlight=http>
HTTP/1.1 200 OK
date: Mon, 23 May 2022 19:33:16 GMT
content-type: application/json
content-length: 1831
server: Pathfinder
</pre>

Example response body:
<pre class=include-code>
path: examples/get-footprint-response.json
highlight: json
</pre>

</div>

