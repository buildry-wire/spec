"""Reference webhook signature verifier — mirrors the Wire server scheme.

Header: WirePayment-Signature: t=<unix>,v1=<hex(HMAC-SHA256(secret, "<t>.<body>"))>
"""
import hashlib
import hmac


def _parse(header: str) -> tuple[int | None, str | None]:
    t, v1 = None, None
    for part in header.split(","):
        k, _, v = part.strip().partition("=")
        if k == "t":
            try:
                t = int(v)
            except ValueError:
                return None, None
        elif k == "v1":
            v1 = v
    return t, v1


def verify(secret: str, body: bytes, header: str, now: int, tolerance: int = 300) -> bool:
    t, v1 = _parse(header)
    if t is None or not v1:
        return False
    if abs(now - t) > tolerance:
        return False
    mac = hmac.new(secret.encode(), f"{t}.".encode() + body, hashlib.sha256)
    expected = mac.hexdigest()
    return hmac.compare_digest(expected, v1)
