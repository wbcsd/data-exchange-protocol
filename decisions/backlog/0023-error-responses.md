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

In general, we propose to stick standards as much as possible. Hence, we propose to make the requirements under `Error Responses` (6.5/6.9) apply to 'actions' that are not covered by a standard. That is, all actions excluding the `Action Authenticate`. 

## Example 1:
?

## Decision

### Technical Specification

6.9. Error Responses
*"Whenever a host system returns an error response for , it MUST send a HTTP response such that"


## Consequences

1. As this ADR changes the overall functionality in a critical aspect (authentication flow),  the Tech Specs Version number must be updated from 2.0.x to 2.1.y.
2. The OpenId Connect Discovery mechanism is tied to a domain name where the `.well-known/openid-configuration` file is hosted (the `OpenId Connect Issuer`)
    1. For data security and data consistency reasons, any change to the domain name needs to be communicated and synchronized with data recipients in an appropriate fashion
    2. Data owners need to understand that the URL used to construct the full URL to the `.well-known/openid-configuration` cannot be changed easily later on, and that they consider e.g. the usage of their own domain name or other strategies to maintain sovereignty over this aspect
3. Solution Providers need to operate an OpenId Connect-conforming authentication implementation if they plan on supporting the `OpenId Connected-based Authentication Mechanism`
    1. OpenId Connect goes beyond the mandatory technical requirements of the V1 and V2.0.x tech specs. 
4. Data Recipients are strongly encouraged to update their implementation soon to support this ADR’s Authentication approach if they want to be fully interoperable with 2.1 series Host Systems.
