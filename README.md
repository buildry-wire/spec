# Wire SDK Spec

The source of truth for Wire payment SDKs. Defines the contract every SDK follows,
the public API description, and cross-SDK conformance vectors.

- [`CONTRACT.md`](CONTRACT.md) — the language-agnostic SDK contract
- [`openapi.yaml`](openapi.yaml) — the Wire Merchant API (OpenAPI 3.1)
- [`test-vectors/`](test-vectors/) — webhook signature conformance fixtures

## Server SDKs
| Language | Repo | Package |
|---|---|---|
| Go | [`wire-go`](https://github.com/buildry-wire/wire-go) | `github.com/buildry-wire/wire-go` |
| Python | [`wire-python`](https://github.com/buildry-wire/wire-python) | `wirepayment` (PyPI) |
| TypeScript | [`wire-node`](https://github.com/buildry-wire/wire-node) | `@buildry-wire/wire` (npm) |
| PHP | [`wire-php`](https://github.com/buildry-wire/wire-php) | `buildry-wire/wire-php` (Packagist) |
| Ruby | [`wire-ruby`](https://github.com/buildry-wire/wire-ruby) | `wirepayment` (RubyGems) |
| Java | [`wire-java`](https://github.com/buildry-wire/wire-java) | `mn.wire:wire-java` (Maven Central) |
| .NET / C# | [`wire-dotnet`](https://github.com/buildry-wire/wire-dotnet) | `Wirepayment` (NuGet) |

## Client checkout SDKs
Present a Wire-hosted checkout session in the buyer's app or browser. Client-side
only — no secret key.

| Platform | Repo | Package |
|---|---|---|
| Browser / JS | [`wire-checkout-js`](https://github.com/buildry-wire/wire-checkout-js) | `@buildry-wire/checkout` (npm) |
| iOS / Swift | [`wire-checkout-ios`](https://github.com/buildry-wire/wire-checkout-ios) | `WireCheckout` (SwiftPM / CocoaPods) |
| Android / Kotlin | [`wire-checkout-android`](https://github.com/buildry-wire/wire-checkout-android) | `mn.wire:wire-checkout-android` (Maven Central) |

## Regenerating test vectors
`python tools/gen_vectors.py && python tools/test_vectors.py`

## License
MIT
