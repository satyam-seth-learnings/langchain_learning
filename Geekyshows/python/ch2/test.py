from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from decouple import config

SECRET_KEY = config("OPENAI_API_KEY")
# print(SECRET_KEY)

# LLMs

# llm = OpenAI()
llm = OpenAI(api_key=SECRET_KEY)
response = llm.invoke("Who is Prime Minister of India ?")
# As of October 2021, the Prime Minister of India is Narendra Modi.
print(response)


# Chat Models

# # Example - 1
# chat = ChatOpenAI(api_key=SECRET_KEY)
# response = chat.invoke("Who is Prime Minister of India ?")
# # content='As of October 2021, the Prime Minister of India is Narendra Modi.' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 17, 'prompt_tokens': 14, 'total_tokens': 31, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-BGlLgqhi0H20fJ5bieYoSL5tMtfrZ', 'finish_reason': 'stop', 'logprobs': None} id='run-617547b5-90d6-4f74-b50f-4030f9e984d2-0' usage_metadata={'input_tokens': 14, 'output_tokens': 17, 'total_tokens': 31, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
# # print(response)
# # As of October 2021, the Prime Minister of India is Narendra Modi.
# print(response.content)

# # Example -2
# chat = ChatOpenAI(api_key=SECRET_KEY)
# messages = [
#     SystemMessage(content="You are a standup comedian"),
#     HumanMessage(content="Who is Prime Minister of India ?"),
# ]
# response = chat.invoke(messages)
# # content="I'm a comedian, not a news anchor! But last time I checked, it was Narendra Modi. And let me tell you, trying to keep up with Indian politics is like trying to follow a Bollywood movie - you never know what twists and turns are coming next!" additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 55, 'prompt_tokens': 24, 'total_tokens': 79, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-BGlajo81TViLoWdQzBu3xLyI2WlyE', 'finish_reason': 'stop', 'logprobs': None} id='run-2f7b5ed8-c17b-446a-ad95-038ccc995ab5-0' usage_metadata={'input_tokens': 24, 'output_tokens': 55, 'total_tokens': 79, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
# print(response)
