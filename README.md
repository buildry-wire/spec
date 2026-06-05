# Wire SDK Spec

The source of truth for Wire payment SDKs. Defines the contract every SDK follows,
the public API description, and cross-SDK conformance vectors.

- [`CONTRACT.md`](CONTRACT.md) — the language-agnostic SDK contract
- [`openapi.yaml`](openapi.yaml) — the Wire Merchant API (OpenAPI 3.1)
- [`test-vectors/`](test-vectors/) — webhook signature conformance fixtures

## SDKs
| Language | Repo | Package |
|---|---|---|
| Go | [`wire-go`](https://github.com/buildry-wire/wire-go) | `github.com/buildry-wire/wire-go` |
| Python | [`wire-python`](https://github.com/buildry-wire/wire-python) | `wirepayment` (PyPI) |
| TypeScript | [`wire-node`](https://github.com/buildry-wire/wire-node) | `@buildry-wire/wire` (npm) |

## Regenerating test vectors
`python tools/gen_vectors.py && python tools/test_vectors.py`

## License
MIT
