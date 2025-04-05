from langchain_openai import ChatOpenAI
from langchain.output_parsers import (
    CommaSeparatedListOutputParser,
    DatetimeOutputParser,
    PydanticOutputParser,
)
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from decouple import config
from pydantic import BaseModel, Field

SECRET_KEY = config("OPENAI_API_KEY")
llm = ChatOpenAI(api_key=SECRET_KEY)

# Example 1
date_time_parser = DatetimeOutputParser()
"""
Write a datetime string that matches the following pattern: '%Y-%m-%dT%H:%M:%S.%fZ'.

Examples: 0734-02-10T15:39:48.908398Z, 1628-10-19T06:19:35.598419Z, 0350-08-19T15:21:12.957500Z

Return ONLY this string, no other words!
"""
print(date_time_parser.get_format_instructions())

comma_sep_parser = CommaSeparatedListOutputParser()
"""
Write a datetime string that matches the following pattern: '%Y-%m-%dT%H:%M:%S.%fZ'.

Examples: 0734-02-10T15:39:48.908398Z, 1628-10-19T06:19:35.598419Z, 0350-08-19T15:21:12.957500Z

Return ONLY this string, no other words!
"""
print(comma_sep_parser.get_format_instructions())


# # Example 2
# date_time_parser = DatetimeOutputParser()
# human_template = "{request}\n{format_instruction}"
# chat_prompt = ChatPromptTemplate.from_messages(
#     [HumanMessagePromptTemplate.from_template(human_template)]
# )

# # # Chat Prompt:  input_variables=['format_instruction', 'request'] input_types={} partial_variables={} messages=[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['format_instruction', 'request'], input_types={}, partial_variables={}, template='{request}\n{format_instruction}'), additional_kwargs={})]
# # print("Chat Prompt: ", chat_prompt)

# formatted_chat_prompt = chat_prompt.format_messages(
#     request="What date was when world war 2 declared",
#     format_instruction=date_time_parser.get_format_instructions(),
# )

# # # Formatted Chat Prompt:  [HumanMessage(content="What date was when world war 2 declared\nWrite a datetime string that matches the following pattern: '%Y-%m-%dT%H:%M:%S.%fZ'.\n\nExamples: 1789-09-12T05:06:03.245987Z, 0082-12-13T11:20:23.097101Z, 0058-12-18T13:00:12.971795Z\n\nReturn ONLY this string, no other words!", additional_kwargs={}, response_metadata={})]
# # print("Formatted Chat Prompt: ", formatted_chat_prompt)

# response = llm.invoke(formatted_chat_prompt)
# # Response Content: 1939-09-01T00:00:00:000000Z
# print("Response: ", response.content)
# # Response Content: 1939-09-01T00:00:00
# print("Response Content Parser: ", date_time_parser.parse(response.content))

# # Example - 3
# # Define your desired data structure


# class Cricketer(BaseModel):
#     name: str = Field(description="Name of Cricketer")
#     records: list = Field(description="Python list of records")


# parser = PydanticOutputParser(pydantic_object=Cricketer)

# # """
# # The output should be formatted as a JSON instance that conforms to the JSON schema below.

# # As an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}
# # the object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.

# # Here is the output schema:
# # ```
# # {"properties": {"name": {"description": "Name of Cricketer", "title": "Name", "type": "string"}, "records": {"description": "Python list of records", "items": {}, "title": "Records", "type": "array"}}, "required": ["name", "records"]}
# # ```
# # """
# # print(parser.get_format_instructions())

# human_template = "{request}\n{format_instruction}"
# chat_prompt = ChatPromptTemplate.from_messages(
#     [HumanMessagePromptTemplate.from_template(human_template)]
# )

# formatted_chat_prompt = chat_prompt.format_messages(
#     request="tell me about a cricketer",
#     format_instruction=parser.get_format_instructions(),
# )

# # # Formatted Chat Prompt:  [HumanMessage(content='tell me about a cricketer\nThe output should be formatted as a JSON instance that conforms to the JSON schema below.\n\nAs an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}\nthe object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.\n\nHere is the output schema:\n```\n{"properties": {"name": {"description": "Name of Cricketer", "title": "Name", "type": "string"}, "records": {"description": "Python list of records", "items": {}, "title": "Records", "type": "array"}}, "required": ["name", "records"]}\n```', additional_kwargs={}, response_metadata={})]
# # print("Formatted Chat Prompt: ", formatted_chat_prompt)

# response = llm.invoke(formatted_chat_prompt)
# print("Response: ", response.content)
# print("Response Content Parser: ", parser.parse(response.content))
