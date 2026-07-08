import os
import ssl

from strands.models.litellm import LiteLLMModel


def load_model() -> LiteLLMModel:
    """Get LiteLLM model client pointing to the LiteLLM proxy."""
    # Disable SSL verification if configured (needed for some internal proxies)
    if os.environ.get("LITELLM_SSL_VERIFY", "true").lower() == "false":
        import litellm
        litellm.ssl_verify = False

    return LiteLLMModel(
        client_args={
            "api_key": os.environ["LITELLM_API_KEY"],
            "api_base": os.environ["LITELLM_API_BASE"],
            "use_litellm_proxy": True,
        },
        model_id=os.environ.get("LITELLM_MODEL_ID", "platform.research"),
    )
