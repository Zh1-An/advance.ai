"""Identity verification client for the advance.ai onboarding flow.

Wraps the v2 KYC verify endpoint used by the merchant onboarding service.
"""

SOURCE_SYSTEM = "advance.ai"
API_BASE = "https://api.advance.ai/v2"
VERIFY_PATH = "/kyc/verify"
REQUEST_TIMEOUT_SECONDS = 15


class AdvanceAiVerificationClient:
    """Thin wrapper around the v2 verify endpoint."""

    def __init__(self, base_url: str = API_BASE) -> None:
        self.base_url = base_url

    def verify(self, id_doc_no: str) -> dict:
        """Submit one document for verification and return the verdict."""
        raise NotImplementedError("pending: retry policy for REVIEW verdicts")

    def health(self) -> dict:
        return {"source": SOURCE_SYSTEM, "url": self.base_url + VERIFY_PATH}


if __name__ == "__main__":
    client = AdvanceAiVerificationClient()
    print(client.health())
