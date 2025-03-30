from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    PromptTemplate,
)
from decouple import config

SECRET_KEY = config("OPENAI_API_KEY")
chat = ChatOpenAI(api_key=SECRET_KEY)

# Chat Model - Prompt Template

# Example 1 - Message Prompt Template as Tuples
chat_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}",
        ),
        ("human", "{text}"),
    ]
)

# # Chat Prompt:  input_variables=['input_language', 'output_language', 'text'] input_types={} partial_variables={} messages=[SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables=['input_language', 'output_language'], input_types={}, partial_variables={}, template='You are a helpful assistant that translates {input_language} to {output_language}'), additional_kwargs={}), HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['text'], input_types={}, partial_variables={}, template='{text}'), additional_kwargs={})]
# print("Chat Prompt: ", chat_prompt)
# # Chat Prompt Input Variables:  ['input_language', 'output_language', 'text']
# print("Chat Prompt Input Variables: ", chat_prompt.input_variables)

formatted_chat_prompt = chat_prompt.format_messages(
    input_language="English",
    output_language="French",
    text="I am leaning LangChain JS from GeekyShows YT",
)

# # Formatted Chat Prompt:  [SystemMessage(content='You are a helpful assistant that translates English to French', additional_kwargs={}, response_metadata={}), HumanMessage(content='I am leaning LangChain JS from GeekyShows YT', additional_kwargs={}, response_metadata={})]
# print("Formatted Chat Prompt: ", formatted_chat_prompt)

response = chat.invoke(formatted_chat_prompt)
# print("Response: ", response)

"""
Resoonse Content:
Je suis en train d'aoorendre LaneChain JS sur la chaine YouTube GeekyShows.
"""
print("Response Content: ", response.content)


# # Example 2 - Using Message Classes
# sys_template = (
#     "You are a helpful assistant that translates {input_language} to {output_language}."
# )
# human_template = "{text}"

# chat_prompt = ChatPromptTemplate.from_messages(
#     [
#         SystemMessagePromptTemplate.from_template(sys_template),
#         HumanMessagePromptTemplate.from_template(human_template),
#     ]
# )
# # # Chat Prompt:  input_variables=['input_language', 'output_language', 'text'] input_types={} partial_variables={} messages=[SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables=['input_language', 'output_language'], input_types={}, partial_variables={}, template='You are a helpful assistant that translates {input_language} to {output_language}.'), additional_kwargs={}), HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['text'], input_types={}, partial_variables={}, template='{text}'), additional_kwargs={})]
# # print("Chat Prompt: ", chat_prompt)

# # # Chat Prompt Input Variables:  ['input_language', 'output_language', 'text']
# # print("Chat Prompt Input Variables: ", chat_prompt.input_variables)

# formatted_chat_prompt = chat_prompt.format_messages(
#     input_language="English",
#     output_language="French",
#     text="I am learning LangChain JS from GeekyShows YT",
# )
# # print("Formatted Chat Prompt: ", formatted_chat_prompt)


# response = chat.invoke(formatted_chat_prompt)
# print("Response: ", response)
# print("Response: ", response.content)


# # Example 3 - Using PromptTemplate
# # system_prompt = PromptTemplate(
# #     input_variables=["input_language", "output_language"],
# #     template="You are a helpful assistant that translates {input_language} to {output_language}.",
# # )
# system_prompt = PromptTemplate.from_template(
#     "You are a helpful assistant that translates {input_language} to {output_language}.",
# )
# # input_variables=['input_language', 'output_language'] input_types={} partial_variables={} template='You are a helpful assistant that translates {input_language} to {output_language}.'
# # print(system_prompt)

# human_prompt = PromptTemplate.from_template("{text}")

# system_message_prompt = SystemMessagePromptTemplate(prompt=system_prompt)
# human_message_prompt = HumanMessagePromptTemplate(prompt=human_prompt)

# chat_prompt = ChatPromptTemplate.from_messages(
#     [
#         system_message_prompt,
#         human_message_prompt,
#     ]
# )
# print("Chat Prompt: ", chat_prompt)
# print("Chat Prompt Input Variable: ", chat_prompt.input_variables)

# formatted_chat_prompt = chat_prompt.format_messages(
#     input_language="English",
#     output_language="French",
#     text="I love programming",
# )
# print("Formatter Chat Prompt: ", formatted_chat_prompt)
