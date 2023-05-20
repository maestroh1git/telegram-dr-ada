import openai
import random
from config import OPENAI_KEY

openai.api_key = OPENAI_KEY


def generate_response(prompt: str) -> str:
    try:
        response = openai.Completion.create(
            engine="text-davinci-003", prompt=prompt, max_tokens=256)
        return response.choices[0].text.strip()
    except openai.OpenAIError as open_ai_error:
        # Handle specific OpenAI API errors
        # return open_ai_error._message
        if "plan and billing" in open_ai_error._message.lower():
            quirky_errors = [
                "Sorry, my brain is buffering. Can you ask me something else?",
                "Oops! It seems my imagination has taken a coffee break. Please try another prompt.",
                "Looks like I've run out of creative juice. Could you give me a different topic?",
            ]
            return quirky_errors[random.randint(0, len(quirky_errors)-1)]
        else:
            return open_ai_error._message

    except openai.error.APIError as e:
        # Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        pass
    except openai.error.APIConnectionError as e:
        #Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        pass
    except openai.error.RateLimitError as e:
        #Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass

# def generate_response(prompt: str, engine: str = "text-davinci-002", max_tokens: int = 60) -> str:
#     response = openai.Completion.create(engine=engine, prompt=prompt, max_tokens=max_tokens)
#     return response.choices[0].text.strip()
