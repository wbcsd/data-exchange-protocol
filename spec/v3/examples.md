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

