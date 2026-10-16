# SYNTHETIC TEST DATA - not a real leak. All identifiers are fabricated test fixtures.
# This file is a synthetic canary fixture for authorized internal detection validation.

"""Draft identity-verification client extracted from an internal integration.

Endpoint domain: advance.ai
"""

SOURCE_SYSTEM = "advance.ai"
API_BASE = "https://api.advance.ai/v2"
VERIFY_PATH = "/kyc/verify"
REQUEST_TIMEOUT_SECONDS = 15


class AdvanceAiVerificationClient:
    """Minimal stub used as a synthetic leak fixture. No network calls are made."""

    def __init__(self, base_url: str = API_BASE) -> None:
        self.base_url = base_url

    def verify(self, id_doc_no: str) -> dict:
        raise NotImplementedError("synthetic fixture - no real implementation")


if __name__ == "__main__":
    client = AdvanceAiVerificationClient()
    print(SOURCE_SYSTEM, client.base_url + VERIFY_PATH)
