# Wire SDK Contract

Every Wire SDK (Go, Python, TypeScript, …) conforms to this contract so merchants
get the same surface and the same security guarantees in any language.

## Client
- Constructor takes an API key (`sk_live_…`) and optional config:
  `baseURL` (default `https://api.wire.mn`), `timeout` (30s), `maxRetries` (2),
  injectable HTTP client.
- The SDK never logs the key and never returns it in error messages.

## Resources (V1)
| Resource | Methods |
|---|---|
| PaymentIntents | create, retrieve, confirm, cancel, list |
| Charges | retrieve, list |
| Events | retrieve, list |
| WebhookEndpoints | create, retrieve, update, delete, list |

(`operator_connections` is V2.)

## Auth
`Authorization: Bearer <apiKey>` on every request.

## Idempotency
Every POST sends an `Idempotency-Key` header. If the caller does not supply one,
the SDK generates a random key.

## Pagination
Cursor-based: `starting_after`, `ending_before`, `limit` (1–100). List responses
are `{ object: "list", data: [...], has_more }`. Every SDK exposes an
auto-pagination iterator that follows `has_more` via `starting_after`.

## Errors
Server returns `{ "error": { "type", "code", "message", "param", "request_id" } }`
with an HTTP status. SDKs map this to a typed error carrying
`type, code, message, param, requestId, statusCode`. Network/timeout is a distinct
error type. `request_id` is always preserved.

## Retries
Exponential backoff with jitter on 429, 5xx, and network errors, up to `maxRetries`.
Honor `Retry-After`. The same `Idempotency-Key` is reused across retries. Other 4xx
are not retried.

## Webhook signature verification
Header `WirePayment-Signature: t=<unix>,v1=<hex>` where
`hex = HMAC-SHA256(secret, "<t>.<rawBody>")`.
`verify(rawBody, signatureHeader, secret, tolerance=300s)`:
1. Parse `t` and `v1`.
2. Recompute `HMAC-SHA256(secret, t + "." + rawBody)`; compare to `v1` in constant time.
3. Reject if `|now - t| > tolerance`.
4. Fail closed on any parse/mismatch.
Verification runs on the RAW request body, before any JSON parsing.

Conformance vectors: `test-vectors/webhook-signatures.json`.
