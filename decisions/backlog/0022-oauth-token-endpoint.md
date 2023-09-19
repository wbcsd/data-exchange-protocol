# 22. Oauth2.0 Token endpoint url (Proposal #1)

Date: 2023-09-19

## Status

In Progress

## Context

The Tech. Specs. (both V1 and V2) specify the path/endpoint for the Action `Authenticate` to conform to the following structure: `AuthSubPath/auth/token`. This specification goes beyond what is suggested in the referenced standard 'The OAuth 2.0 Authorization Framework' (https://www.rfc-editor.org/rfc/rfc6749), which specifies the structure as: `AuthSubPath/token`. The more strict specification of the path creates conformance challenges for host systems that:
    
* reuse an exsting service that is implemented based on the standard (rfc-6749), but does not offer the capability to control the authentication path / token endpoint in full.
    
For example, the following path `https://some-domain.com/oauth/token` adheres to the standard (rfc-6749) but is not conforming to the current Tech. Specs. (see 6.5.1). The same would apply to the path `https://some-domain.com/token`.

## Summary

We propose to change the specified structure of the authentication path / token endpoint for the Action `Authenticate` in the Tech. Specs. The current structure:

* POST `AuthSubPath/auth/token`

The proposed structure:

* POST `AuthSubPath/token` / `AuthSubPath`

This change aligns the Tech. Specs. to the standard (rfc-6749) and grants host systems more flexibility for implementing their authentication path / token endpoint. The proposed change does not impact the authentication flow beyond the path / endpoint. 

As the proposed change 'loosens' the current specification, backwards-compatibility is ensured. Any host system that is considered conformant under the current Tech. Specs. will also be conformant with the proposed change. Any path that adheres to the currently specified structure `AuthSubPath/auth/token` will logically also adhere to the proposed structure `AuthSubPath/token`.

Nevertheless, it needs to be considered that recipient systems might need implement minor adjustments to support the proposed structure.


## Example:

A Host system has the following set up:

1. The Action `Authenticate` is available under `AuthSubPath/token`. For example, `https://some-domain.com/something/token` (this path does ***not*** conform to current Tech. Specs.)

A Data recipient will then:

1. Call the Action `Authenticate` hosted under `AuthSubPath/token` to requests an access token.
2. and then uses this token to proceed and to calls to the other HTTP Actions (e.g. `ListFootprints`, `Events`, etc.)

## Decision

### Technical Specification

The ADR results in only a minor change to the Technical Specifications. That is:

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

1. As this ADR changes the overall functionality in a critical aspect (authentication flow),  the Tech Specs Version number must be updated from 2.0.x to 2.1.y.
2. The OpenId Connect Discovery mechanism is tied to a domain name where the `.well-known/openid-configuration` file is hosted (the `OpenId Connect Issuer`)
    1. For data security and data consistency reasons, any change to the domain name needs to be communicated and synchronized with data recipients in an appropriate fashion
    2. Data owners need to understand that the URL used to construct the full URL to the `.well-known/openid-configuration` cannot be changed easily later on, and that they consider e.g. the usage of their own domain name or other strategies to maintain sovereignty over this aspect
3. Solution Providers need to operate an OpenId Connect-conforming authentication implementation if they plan on supporting the `OpenId Connected-based Authentication Mechanism`
    1. OpenId Connect goes beyond the mandatory technical requirements of the V1 an V2.0.x tech specs. 
4. Data Recipients are strongly encouraged to update their implementation soon to support this ADR’s Authentication approach if they want to be fully interoperable with 2.1 series Host Systems.
