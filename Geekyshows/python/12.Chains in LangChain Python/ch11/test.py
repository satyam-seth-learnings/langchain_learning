from operator import itemgetter
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

# from langchain.chains import LLMChain # deprecated

from decouple import config

SECRET_KEY = config("OPENAI_API_KEY")
chat = ChatOpenAI(api_key=SECRET_KEY)

# # Example 1 - Chain
# human_template = "tell me fact about {topic}"
# chat_prompt = ChatPromptTemplate.from_messages(
#     [HumanMessagePromptTemplate.from_template(human_template)]
# )

# # chain = LLMChain(llm=chat, prompt=chat_prompt) # deprecated

# # chain = chat_prompt | chat
# chain = chat_prompt | chat | StrOutputParser()

# # response = chain.invoke(input="javascript")
# response = chain.invoke({"topic": "python"})

# # content='Python is a widely used high-level, general-purpose programming language known for its easy readability and simple syntax. It was created by Guido van Rossum and first released in 1991. Python is often used for web development, data analysis, artificial intelligence, scientific computing, and more.' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 59, 'prompt_tokens': 12, 'total_tokens': 71, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-BQyEhx30C1mPBfETys3eW8INEI9iT', 'finish_reason': 'stop', 'logprobs': None} id='run-09cb62d6-bd65-4e7b-b0ba-5f6251f9fbd9-0' usage_metadata={'input_tokens': 12, 'output_tokens': 59, 'total_tokens': 71, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
# # Python is a widely used high-level, general-purpose programming language known for its easy readability and simple syntax. It was created by Guido van Rossum and first released in 1991. Python is often used for web development, data analysis, artificial intelligence, scientific computing, and more.
# print(response)


# Example 2 - Multiple Chains
chat_prompt1 = ChatPromptTemplate.from_template("what is the city {person} is from?")
chat_prompt2 = ChatPromptTemplate.from_template(
    "what country is the city {city} in? respond in {language}",
)

city_chain = chat_prompt1 | chat | StrOutputParser()

country_chain = (
    {"city": city_chain, "language": itemgetter("language")}
    | chat_prompt2
    | chat
    | StrOutputParser()
)

response = country_chain.invoke({"person": "virat kohli", "language": "english"})

# Virat Kohli is from Delhi, India.
print(response)
