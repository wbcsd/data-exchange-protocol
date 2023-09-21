# 23. Action Authenticate: Error Responses (Proposal #1)

Date: 2023-09-20

## Status

In Progress

## Context

The Tech. Specs. builds on existing standards for the overal Authentication flow. For the Action `Authenticate` specically, the Tech. Specs. refer to the standard 'The OAuth 2.0 Authorization Framework' (https://www.rfc-editor.org/rfc/rfc6749). However, the requirement to implement the Action `Authenticate` based on this standard conflicts with the requirements in the Error Responses (V1: 6.5, V2: 6.9). As a result, it is theoretically impossible to implement a conformant solution. 

#### Action Authenticate
* **Tech. Specs. (both V1 and V2), Section 6.4.1/6.5:** *"Host systems MUST implement this action in conformance with [rfc6749] Section 4.4 (OAuth2 Client Credentials)."*
* **RFC6749 (https://www.rfc-editor.org/rfc/rfc6749) Section 4.4:** *If the request failed client authentication or is invalid, the authorization server returns an error response as described in Section 5.2.*
  * **Section 5.2:** *"The authorization server responds with an HTTP 400 (Bad Request) status code (unless specified otherwise) and includes the following parameters with the response:"*
    *  "error (REQUIRED)"
    *  "error_description (OPTIONAL)"
    *  "error_uri (OPTIONAL)"

For example:
```javascript
     HTTP/1.1 400 Bad Request
     Content-Type: application/json;charset=UTF-8
     Cache-Control: no-store
     Pragma: no-cache

     {
       "error":"..."
     }   
```

#### Error Responses
* **Tech. Specs. (both V1 and V2), Section 6.5/6.9:**
  * *"Whenever a host system returns an error response, it MUST send a HTTP response such that:"*
    * *"with response body the error response"*
  * *"A error response is a JSON object with the following properties:*
    * *"code: a error response code encoded as a String"*
    * *"message: a error message encoded as a String"*

For example:
```javascript
     HTTP/1.1 400 Bad Request
     Content-Type: application/json;charset=UTF-8
     Cache-Control: no-store
     Pragma: no-cache

     {
       "code":"...",
       "message":"..."
     }   
```

As shown, these requirements conflict when it comes to the structure of the body of the error response. Therefore, the Tech. Specs. need an update to eliminate this conflict.

## Summary

In general, we propose to stick to standards as much as possible. Hence, we propose to adjust the specifications in the section `Error Responses` (6.5/6.9) in such a way that they do not conflict with a standard. In this specific case, that means that the specification for the error response can not apply to the `Action Authenticate`. 


## Decision

### Technical Specification

**6.9. Error Responses**

Whenever a host system returns an error response for any Action other than the `Action Authenticate`, it MUST send a HTTP response such that
* the HTTP Status Code equals the HTTP Status Code defined for the respective error response code (see Error Codes Table)
* with content type set to application/json, and
* with response body the error response

A error response is a JSON object with the following properties:
* code: a error response code encoded as a String
* message: a error message encoded as a String

A error response code is a value from column Error Response Code from the table below.

A error message is a human-readable error description. Example values are in column Example Message in the table below.

## Consequences

1. As this ADR is more a correction than a change,  the Tech Specs Version number can be updated from 2.0.x to 2.1.y.
2. This correction results in having multiple structures for `error responses` which might be undesirable. 
