import os

class Ollama:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("STRING", {"default": "ollama/mistral"}),
                "api_type": ("STRING", {"default": "litellm"}),
                "base_url": ("STRING", {"default": "http://0.0.0.0:8000"})
            }
        }

    RETURN_TYPES = ("LLM",)
    FUNCTION = "execute"
    CATEGORY = "AutoGen/LLM"

    def execute(self, model, api_type, base_url):
        config_list = [
            {
                'model': model,
                'api_type': api_type,
                'base_url': base_url,

            }
        ]
        return ({"LLM": config_list, "llama-cpp": False},)

NODE_CLASS_MAPPINGS = {
    "Ollama": Ollama,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Ollama": "Ollama"
}
