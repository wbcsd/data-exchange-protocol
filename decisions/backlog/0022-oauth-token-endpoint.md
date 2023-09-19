# 22. Oauth2.0 Token endpoint url (Proposal #1)

Date: 2023-09-19

## Status

In Progress

## Context

The Tech. Specs. (both V1 and V2) specify the path/endpoint for the Action `Authenticate` to conform to the following structure: `AuthSubPath/auth/token`. This specification goes beyond what is suggested in the referenced standard 'The OAuth 2.0 Authorization Framework' (https://www.rfc-editor.org/rfc/rfc6749), which specifies the structure as: `AuthSubPath/token`. The more strict specification of the path creates conformance challenges for host systems that:
    
* reuse an exsting service that is implemented based on the standard (rfc-6749), but does not offer the capability to control the authentication path / token endpoint in full.
    
For example, the following path `https://some-domain.com/oauth/token` adheres to the standard (rfc-6749) but is not conforming to the current Tech. Specs. (see 6.5.1). The same would apply to the path `https://some-domain.com/token`. 

Any change to the specifications of the path/endpoint for the Action `Authenticate` could potentially impact or break backwards-compatibility.

## Summary

We propose to alter the specified structure of the authentication path / token endpoint for the Action `Authenticate` in the Tech. Specs. The current structure:

* POST `AuthSubPath/auth/token`

The proposed structure:

* POST `AuthSubPath/token` / `AuthSubPath`

This change aligns the Tech. Specs. to the referenced standard (rfc-6749) and does not impact the authentication flow beyond the path / endpoint. 

* backwards 

If successful, a data recipient authenticates through this endpoint instead of the “regular”`Authenticate` endpoint and its static path / URL.

Otherwise, the authentication flow remains the same and a data recipent attempts to retrieve its token through the regular `Authenticate` Action.

This way, a backwards-compatible authentication flow is established. 

By relying on `OpenId Connect` to discover this endpoint, all parties (Host system implementers, solutions providers, etc.) gain more flexibility in how to operate and to maintain their systems.

## Example 1:

A Host system has the following set up:

1. The so-called `OpenID Connect Issuer`; i.e. URL used to construct the path to the OpenId Provider Configuration Document is set to`https://server.example.com/subpath`
2. The token endpoint is available under `[https://idp.example.com/another-subpath/token`(i.e.](https://idp.example.com/another-subpath/token(i.e.) this path does ***not*** conform to Tech Specs V2)

A Data recipient will then perform the following HTTP calls during the Authentication flow:

1. it will retrieve an OpenId Configuration document from the issuer from the following URL:  `[https://server.example.com/subpath/.well-knonw/openid-configuration](https://server.example.com/subpath)` 
2. it then validates the document and looks up the `token_endpoint` URL entry (an example `openid-configuration` Document is given below
3. it then requests an access token 
4. and then uses this token to proceed and to calls to the other HTTP Actions (e.g. `ListFootprints`, `Events`, etc.)

### `openid-configuration` example request and response

```javascript
GET /subpath/.well-known/openid-configuration
Content-Type: application/json

{
   "issuer":
     "https://server.example.com/subpath",
   "token_endpoint":
     "https://idp.example.com/another-subpath/token",
   [...]
}
```

## Decision

### Technical Specification

1. With Version 2.1, a Host System SHOULD implement an `OpenId Connected-based Authentication Mechanism`
2. This mechanism is based upon an `OpenId Provider Configuration Document` . A Host System SHOULD make the  `OpenId Provider Configuration Document` available conforming with **[OpenID Connect Discovery 1.0 incorporating errata set 1](https://openid.net/specs/openid-connect-discovery-1_0.html) Section 4** with `token_endpoint` defined
3. The Authentication flow is updated as follows:
    1. A Data recipient before Authenticating, MUST request the `OpenId Provider Configuration Document` from a Host System before making calls to the `Authenticate` action
    2. If a conforming document is found, the Data Recipient SHOULD attempt to retrieve a Bearer token from the endpoint defined in the `token_endpoint` property of the `OpenId Provider Configuration Document` retrieved (the HTTP request by a Data Recipient is **equivalent** to the v2.0 Tech specs Authenticate action *except that URI CAN be different)*
    3. If such a document is not found, the Data Recipient SHOULD fall back to  authentication flow of Tech Specs Version 2.0 (i.e.  the `AuthSubPath/auth/token`syntax)
4. A Host System MAY return an appropriate error response to Data Recipients if they no longer support calls to 2.0-series `Action Authenticate` under the `/auth/token` syntax. In this case, they MUST support the `OpenId Connected-based Authentication Mechanism`

## Consequences

1. As this ADR changes the overall functionality in a critical aspect (authentication flow),  the Tech Specs Version number must be updated from 2.0.x to 2.1.y.
2. The OpenId Connect Discovery mechanism is tied to a domain name where the `.well-known/openid-configuration` file is hosted (the `OpenId Connect Issuer`)
    1. For data security and data consistency reasons, any change to the domain name needs to be communicated and synchronized with data recipients in an appropriate fashion
    2. Data owners need to understand that the URL used to construct the full URL to the `.well-known/openid-configuration` cannot be changed easily later on, and that they consider e.g. the usage of their own domain name or other strategies to maintain sovereignty over this aspect
3. Solution Providers need to operate an OpenId Connect-conforming authentication implementation if they plan on supporting the `OpenId Connected-based Authentication Mechanism`
    1. OpenId Connect goes beyond the mandatory technical requirements of the V1 an V2.0.x tech specs. 
4. Data Recipients are strongly encouraged to update their implementation soon to support this ADR’s Authentication approach if they want to be fully interoperable with 2.1 series Host Systems.
