from litellm.integrations.custom_logger import CustomLogger

BEDROCK_UNSUPPORTED_PARAMS = {"context_management"}

class BedrockCompatHook(CustomLogger):
    async def async_pre_call_hook(self, user_api_key_dict, cache, data, call_type):
        thinking = data.get("thinking")
        if isinstance(thinking, dict) and thinking.get("type") == "adaptive":
            thinking["type"] = "enabled"
            thinking.setdefault("budget_tokens", 10000)
        for param in BEDROCK_UNSUPPORTED_PARAMS:
            data.pop(param, None)
        return data

proxy_handler_instance = BedrockCompatHook()
