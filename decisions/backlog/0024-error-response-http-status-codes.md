# 24. Error Responses HTTP status codes (Proposal #1)

Date: 2023-09-21

## Status

In Progress

## Context

The Tech. Specs. (both V1 and V2) builds on existing standards for the (bearer) token usage. In the 'Authentication and Request Flows' (6.3) section, the Tech. Specs. refer to the standard 'The OAuth 2.0 Authorization Framework: Bearer Token Usage' (https://www.rfc-editor.org/rfc/rfc6750). However, the requirements in the Tech. Specs. related to the usage of tokens for the various actions (ListFootprints, GetFootprint, Events) deviate from what is prescribed in the standard around handling errors. As a result, a host system cannot follow the standard and meet Tech. Specs. requirements at the same time. For Example:

#### Action GetFootprint
* **Tech. Specs. (both V1 and V2), Section 6.4.3.2/6.7.2:**
  * *"If the host system does not accept the access token, GetResponseBody MUST be an error response with code AccessDenied."* (403 - Forbidden)
  * *"If the host system does not accept the access token because it expired, GetResponseBody SHOULD be an error response with code TokenExpired."* (401 - Unauthorized)
* **RFC6750 (https://www.rfc-editor.org/rfc/rfc6750) Section 3.1:**
  * *"The access token provided is expired, revoked, malformed, or invalid for other reasons.  The resource SHOULD respond with the HTTP 401 (Unauthorized) status code. The client MAY request a new access token and retry the protected resource request."*

For example, in case of an invalid token, returning a `401 Unauthorized` is considered not conformant to the Tech. Specs. while it does follow the referenced standard. At the same time, returning a `403 Unauthorized` in case of an invalid token does not follow the standard.

## Summary

In general, we propose to stick to standards as much as possible. Hence, we propose to adjust the specifications in such a way that it aligns with the standard. In this case, that means changing the requirement for returning a `403 Forbidden` (AccessDenied) to returning a `401 Unauthorized`. Host systems can then decide if they want to implement a specific response in case of an expired token or not.


## Decision

### Technical Specification (V2)

* **6.6. Action ListFootprints**: *"If the host system does not accept the access token, the body MUST be an error response with code InvalidToken"*
* **6.7. Action GetFootprint**: *"If the host system does not accept the access token, the body MUST be an error response with code InvalidToken"*
* **6.8. Action Event**:
  * *"If the host system does not accept the access token, the body MUST be an error response with code InvalidToken"*
  * *"If the host system does not accept the access token because it expired, GetResponseBody SHOULD be an error response with code TokenExpired."*
  * *"In all other cases, for instance in case of a malformed value of the header authorization, GetResponseBody SHOULD be an error response with code BadRequest."*
* **6.9. Error Responses**: 401 - Unauthorized | InvalidToken | Invalid Token


## Consequences

1. As this ADR creates a breaking change, the Tech Specs Version number must be updated from 2.0.x to 2.1.y. 
