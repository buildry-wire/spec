"""Deterministically generate test-vectors/webhook-signatures.json.
Run: python tools/gen_vectors.py
"""
import hashlib
import hmac
import json
import pathlib

SECRET = "whsec_testvector000000000000000000"
NOW = 1_700_000_300          # the "current" time verifiers compare against
TOLERANCE = 300
VALID_TS = 1_700_000_100     # within tolerance of NOW
EXPIRED_TS = 1_699_999_000   # > 300s before NOW
BODY = '{"id":"evt_test","object":"event","type":"payment_intent.succeeded"}'


def header(ts: int, body: str, secret: str = SECRET) -> str:
    mac = hmac.new(secret.encode(), f"{ts}.".encode() + body.encode(), hashlib.sha256)
    return f"t={ts},v1={mac.hexdigest()}"


def main() -> None:
    valid = header(VALID_TS, BODY)
    cases = [
        {"name": "valid", "body": BODY, "header": valid, "valid": True},
        {"name": "tampered_body", "body": BODY + " ", "header": valid, "valid": False},
        {"name": "tampered_sig", "body": BODY,
         "header": f"t={VALID_TS},v1=" + "0" * 64, "valid": False},
        {"name": "expired", "body": BODY, "header": header(EXPIRED_TS, BODY), "valid": False},
        {"name": "malformed_header", "body": BODY, "header": "garbage", "valid": False},
    ]
    out = {
        "scheme": "HMAC-SHA256 over \"<t>.<body>\", header WirePayment-Signature: t=,v1=",
        "secret": SECRET,
        "now": NOW,
        "tolerance_seconds": TOLERANCE,
        "cases": cases,
    }
    path = pathlib.Path(__file__).resolve().parent.parent / "test-vectors" / "webhook-signatures.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
