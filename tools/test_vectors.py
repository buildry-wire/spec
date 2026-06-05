"""Self-test for the webhook signature vectors. Run: python tools/test_vectors.py"""
import json
import pathlib
import sys

from verify_vectors import verify  # noqa: E402

VECTORS = pathlib.Path(__file__).resolve().parent.parent / "test-vectors" / "webhook-signatures.json"


def main() -> int:
    data = json.loads(VECTORS.read_text())
    failures = []
    for case in data["cases"]:
        ok = verify(
            secret=data["secret"],
            body=case["body"].encode(),
            header=case["header"],
            now=data["now"],
            tolerance=data["tolerance_seconds"],
        )
        if ok != case["valid"]:
            failures.append(f"{case['name']}: expected valid={case['valid']}, got {ok}")
    if failures:
        print("FAIL:\n" + "\n".join(failures))
        return 1
    print(f"PASS: {len(data['cases'])} vector cases")
    return 0


if __name__ == "__main__":
    sys.exit(main())
