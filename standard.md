# Standard
This document explains a standard briefly.

## ETag (RFC 9110 8.8.3)
ETag is used to validate or modify a resource (e.g., update or delete) when the client knows the document state.

It is also used to check if the server resource is updated. 
The ETag value must be enclosed in double quotes ("").

When the server provides an ETag value with an HTTP header, it represents the current state of the resource.

Clients can use the headers `If-Match` or `If-None-Match` to interact with the ETag.

- If the ETag value is prefixed with `W/` (e.g., `W/"ETAG_VALUE"`), it indicates a weak comparison.
- Typically, `If-None-Match` is used to check if the server has a newer version of the resource.
- `If-Match` is generally used for updating or deleting a document only if the provided ETag matches the current state.
