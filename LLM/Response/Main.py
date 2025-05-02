from Constants.LLM import LLMProvider
from LinkLens.settings import CURRENT_LLM_PROVIDER
from LLM.Response.Provider.Providers import AIResponseProvider


def generate_ai_response(query, context):
    """
    Generates AI response based on current LLM provider
    """
    ai_response = AIResponseProvider()

    if CURRENT_LLM_PROVIDER == LLMProvider.ai21:
        response = ai_response.generate_ai21_response(query, context)

    elif CURRENT_LLM_PROVIDER == LLMProvider.open_ai:
        response = ai_response.generate_openai_response(query, context)

    return response
