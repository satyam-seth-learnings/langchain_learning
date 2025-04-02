from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from decouple import config

SECRET_KEY = config("OPENAI_API_KEY")
llm = OpenAI(api_key=SECRET_KEY)

# Chat Model
# Few Shot Examples
examples = [
    {"input": "2+2", "output": "4"},
    {"input": "2+3", "output": "5"},
]

example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)

# # Example Prompt:  input_variables=['input', 'output'] input_types={} partial_variables={} messages=[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['input'], input_types={}, partial_variables={}, template='{input}'), additional_kwargs={}), AIMessagePromptTemplate(prompt=PromptTemplate(input_variables=['output'], input_types={}, partial_variables={}, template='{output}'), additional_kwargs={})]
# print("Example Prompt: ", example_prompt)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
)

# """
# Few Shot Prompt:  Human: 2+2
# AI: 4
# Human: 2+3
# AI: 5
# """
# print("Few Shot Prompt: ", few_shot_prompt.format())

final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful math problem solver."),
        few_shot_prompt,
        ("human", "{input}"),
    ]
)

# # Final Prompt:  input_variables=['input'] input_types={} partial_variables={} messages=[SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables=[], input_types={}, partial_variables={}, template='You are a helpful math problem solver.'), additional_kwargs={}), FewShotChatMessagePromptTemplate(examples=[{'input': '2+2', 'output': '4'}, {'input': '2+3', 'output': '5'}], input_variables=[], input_types={}, partial_variables={}, example_prompt=ChatPromptTemplate(input_variables=['input', 'output'], input_types={}, partial_variables={}, messages=[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['input'], input_types={}, partial_variables={}, template='{input}'), additional_kwargs={}), AIMessagePromptTemplate(prompt=PromptTemplate(input_variables=['output'], input_types={}, partial_variables={}, template='{output}'), additional_kwargs={})])), HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['input'], input_types={}, partial_variables={}, template='{input}'), additional_kwargs={})]
# print("Final Prompt: ", final_prompt)


formatted_chat_prompt = final_prompt.format_messages(
    input="What's the square of a triangle?"
)

# # Formatted Chat Prompt:  [SystemMessage(content='You are a helpful math problem solver.', additional_kwargs={}, response_metadata={}), HumanMessage(content='2+2', additional_kwargs={}, response_metadata={}), AIMessage(content='4', additional_kwargs={}, response_metadata={}), HumanMessage(content='2+3', additional_kwargs={}, response_metadata={}), AIMessage(content='5', additional_kwargs={}, response_metadata={}), HumanMessage(content="What's the square of a triangle?", additional_kwargs={}, response_metadata={})]
# print("Formatted Chat Prompt: ", formatted_chat_prompt)


response = llm.invoke(formatted_chat_prompt)

# Response Content: A triangle does not have a square. However, the area of a triangle can be found using the formula A = (base * height) / 2.
print("Response: ", response)
