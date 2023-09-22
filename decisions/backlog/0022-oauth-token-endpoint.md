# 22. Oauth2.0 Token endpoint url (Proposal #1)

Date: 2023-09-19

## Status

In Progress

## Context

The Tech. Specs. (both V1 and V2) specify that the token endpoint for the Action `Authenticate` must conform to the following structure: `AuthSubPath/auth/token`. This specification goes beyond what is suggested in the referenced standard 'The OAuth 2.0 Authorization Framework' (https://www.rfc-editor.org/rfc/rfc6749), which specifies the path to have the structure as: `AuthSubPath/token`. This more strict specification of the path creates conformance challenges for host systems that:
    
* reuse an exsting service that is implemented based on the standard (rfc-6749), but does not offer the capability to control the structure of the token endpoint in full.
    
For example, the following path `https://some-domain.com/oauth/token` adheres to the standard (rfc-6749) but is not conforming to the current Tech. Specs. (see 6.5.1). The same would apply to the path `https://some-domain.com/token`.

## Summary

We propose to change the specified structure of the token endpoint for the Action `Authenticate` in the Tech. Specs. The current structure:

* POST `AuthSubPath/auth/token`

The proposed structure:

* POST `AuthSubPath/token`

This change aligns the Tech. Specs. to the standard (rfc-6749) and grants host systems more flexibility for implementing their token endpoint. The proposed change does not impact the authentication flow beyond the path. 

As the proposed change 'loosens' the current specification, backwards-compatibility is ensured. Any host system that is considered to have a conformant implementation of the Action `Authenticate` under the current Tech. Specs. will also be conformant with the proposed change. Logically, any path that adheres to the currently specified structure `AuthSubPath/auth/token` will also adhere to the proposed structure `AuthSubPath/token`.

However, it needs to be considered that data recipients might need to implement minor adjustments to support the proposed structure. Depending on the implementation, the structure that they append the `AuthSubPath` to needs to be changed from `/auth/token` to `/token`.


## Example:

A Host system has the following set up:

1. The Action `Authenticate` is available under `AuthSubPath/token`. For example, `https://some-domain.com/something/token` (this path does ***not*** conform to current Tech. Specs.).

A Data recipient will then:

1. Call the Action `Authenticate` hosted under `AuthSubPath/token` to requests an access token.
2. and then uses this token to proceed and to calls to the other HTTP Actions (e.g. `ListFootprints`, `Events`, etc.)

## Decision

### Technical Specification

The ADR results a minor change to the Technical Specifications. That is:

#### 6.5.1. Request Syntax (HTTP/1.1)

```javascript
POST AuthSubpath/token HTTP/1.1
host: AuthHostname
accept: application/json
content-type: application/x-www-form-urlencoded
authorization: Basic BasicAuth
content-length: ContentLength

AuthBody

```

## Consequences

1. As this ADR does not change the overall functionality of the authentication flow,  the Tech Specs Version number can be updated from 2.0.x to 2.0.x+1.
2. Host Systems do not need to make any updates to their (conformant) implementations.
3. Data Recipients are strongly encouraged to - if needed - update their implementation and support this ADR’s Authentication approach to ensure full interoperability with Host Systems.
4. Like before, the Action Authenticate is hosted under a dedicated path. To ensure that data recipients are able to authenticate and retrieve a token, any change to the path needs to be communicated and synchronized with data recipients in an appropriate fashion.

