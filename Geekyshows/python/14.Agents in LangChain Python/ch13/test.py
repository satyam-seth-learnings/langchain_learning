from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import (
    create_openai_functions_agent,
    AgentExecutor,
    create_react_agent,
)
from pydantic import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from langchain import hub
from langchain_openai import ChatOpenAI
from decouple import config

SECRET_KEY = config("OPENAI_API_KEY")
chat = ChatOpenAI(api_key=SECRET_KEY)

# # Example 1 - Agent Type - OpenAI Functions
# # Create Agent
# prompt = hub.pull("hwchase17/openai-functions-agent")

# # # input_variables=['agent_scratchpad', 'input'] optional_variables=['chat_history'] input_types={'chat_history': list[typing.Annotated[typing.Union[typing.Annotated[langchain_core.messages.ai.AIMessage, Tag(tag='ai')], typing.Annotated[langchain_core.messages.human.HumanMessage, Tag(tag='human')], typing.Annotated[langchain_core.messages.chat.ChatMessage, Tag(tag='chat')], typing.Annotated[langchain_core.messages.system.SystemMessage, Tag(tag='system')], typing.Annotated[langchain_core.messages.function.FunctionMessage, Tag(tag='function')], typing.Annotated[langchain_core.messages.tool.ToolMessage, Tag(tag='tool')], typing.Annotated[langchain_core.messages.ai.AIMessageChunk, Tag(tag='AIMessageChunk')], typing.Annotated[langchain_core.messages.human.HumanMessageChunk, Tag(tag='HumanMessageChunk')], typing.Annotated[langchain_core.messages.chat.ChatMessageChunk, Tag(tag='ChatMessageChunk')], typing.Annotated[langchain_core.messages.system.SystemMessageChunk, Tag(tag='SystemMessageChunk')], typing.Annotated[langchain_core.messages.function.FunctionMessageChunk, Tag(tag='FunctionMessageChunk')], typing.Annotated[langchain_core.messages.tool.ToolMessageChunk, Tag(tag='ToolMessageChunk')]], FieldInfo(annotation=NoneType, required=True, discriminator=Discriminator(discriminator=<function _get_type at 0x7f13ea9a1360>, custom_error_type=None, custom_error_message=None, custom_error_context=None))]], 'agent_scratchpad': list[typing.Annotated[typing.Union[typing.Annotated[langchain_core.messages.ai.AIMessage, Tag(tag='ai')], typing.Annotated[langchain_core.messages.human.HumanMessage, Tag(tag='human')], typing.Annotated[langchain_core.messages.chat.ChatMessage, Tag(tag='chat')], typing.Annotated[langchain_core.messages.system.SystemMessage, Tag(tag='system')], typing.Annotated[langchain_core.messages.function.FunctionMessage, Tag(tag='function')], typing.Annotated[langchain_core.messages.tool.ToolMessage, Tag(tag='tool')], typing.Annotated[langchain_core.messages.ai.AIMessageChunk, Tag(tag='AIMessageChunk')], typing.Annotated[langchain_core.messages.human.HumanMessageChunk, Tag(tag='HumanMessageChunk')], typing.Annotated[langchain_core.messages.chat.ChatMessageChunk, Tag(tag='ChatMessageChunk')], typing.Annotated[langchain_core.messages.system.SystemMessageChunk, Tag(tag='SystemMessageChunk')], typing.Annotated[langchain_core.messages.function.FunctionMessageChunk, Tag(tag='FunctionMessageChunk')], typing.Annotated[langchain_core.messages.tool.ToolMessageChunk, Tag(tag='ToolMessageChunk')]], FieldInfo(annotation=NoneType, required=True, discriminator=Discriminator(discriminator=<function _get_type at 0x7f13ea9a1360>, custom_error_type=None, custom_error_message=None, custom_error_context=None))]]} partial_variables={'chat_history': []} metadata={'lc_hub_owner': 'hwchase17', 'lc_hub_repo': 'openai-functions-agent', 'lc_hub_commit_hash': 'a1655024b06afbd95d17449f21316291e0726f13dcfaf990cc0d18087ad689a5'} messages=[SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables=[], input_types={}, partial_variables={}, template='You are a helpful assistant'), additional_kwargs={}), MessagesPlaceholder(variable_name='chat_history', optional=True), HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['input'], input_types={}, partial_variables={}, template='{input}'), additional_kwargs={}), MessagesPlaceholder(variable_name='agent_scratchpad')]
# # print(prompt)

# search = DuckDuckGoSearchRun()

# tools = [search]
# agent = create_openai_functions_agent(llm=chat, tools=tools, prompt=prompt)
# # Run Agent
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# response = agent_executor.invoke({"input": "Who is current Prime Minister of India?"})

# """
# > Entering new AgentExecutor chain...

# Invoking: `duckduckgo_search` with `{'query': 'current Prime Minister of India'}`


# List of all Prime Ministers of India till 2025: Narendra Modi is the current and 14th Prime Minister of India who assumed office on 10 June 2024. Jawaharlal Nehru is the first and the longest ... India follows a parliamentary system in which the prime minister is the presiding head of the government and chief of the executive of the government. In such systems, the head of state, or, the head of state's official representative (i.e., the monarch, president, or governor-general) usually holds a purely ceremonial position and acts—on most matters—only on the advice of the prime minister. Prime Minister, Shri Narendra Modi, today condoled the loss of lives in an accident in Nuh, Haryana. "The state government is making every possible effort for relief and rescue", Shri Modi said. ... Shri Narendra Modi was sworn-in as India's Prime Minister for the third time on 9th June 2024, following another decisive victory in the 2024 ... Narendra Modi (born September 17, 1950, Vadnagar, India) is an Indian politician and government official who rose to become a senior leader of the Bharatiya Janata Party (BJP). In 2014 he led his party to victory in elections to the Lok Sabha (lower chamber of the Indian parliament), after which he was sworn in as prime minister of India.Prior to that he had served (2001-14) as chief ... List of Prime Minister of India: 1947 to 2025. Narendra Modi is the current Prime Minister of India in 2025, serving the nation for the past 11 years since first taking office in 2014. The list of Indian Prime Ministers begins with Jawaharlal Nehru, who became the first Prime Minister in 1947 and consist . Jawaharlal Nehru is the longest-serving Prime Minister of India, holding office for 16 ...The current Prime Minister of India is Narendra Modi, who assumed office on 10th June 2024.

# > Finished chain.
# {'input': 'Who is current Prime Minister of India?', 'output': 'The current Prime Minister of India is Narendra Modi, who assumed office on 10th June 2024.'}
# """
# print(response)


# # Example 2 - Agent Type - ReAct
# # Create Agent
# prompt = hub.pull("hwchase17/react")
# # print(prompt)
# search = DuckDuckGoSearchRun()

# tools = [search]
# agent = create_react_agent(llm=chat, tools=tools, prompt=prompt)
# # Run Agent
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# response = agent_executor.invoke({"input": "Who is current Prime Minister of India?"})

# """
# > Entering new AgentExecutor chain...
# I should use the duckduckgo_search tool to find the answer.
# Action: duckduckgo_search
# Action Input: Current Prime Minister of IndiaList of all Prime Ministers of India till 2025: Narendra Modi is the current and 14th Prime Minister of India who assumed office on 10 June 2024. Jawaharlal Nehru is the first and the longest ... Prime Minister, Shri Narendra Modi, today condoled the loss of lives in an accident in Nuh, Haryana. "The state government is making every possible effort for relief and rescue", Shri Modi said. ... Shri Narendra Modi was sworn-in as India's Prime Minister for the third time on 9th June 2024, following another decisive victory in the 2024 ... India follows a parliamentary system in which the prime minister is the presiding head of the government and chief of the executive of the government. In such systems, the head of state, or, the head of state's official representative (i.e., the monarch, president, or governor-general) usually holds a purely ceremonial position and acts—on most matters—only on the advice of the prime minister. Narendra Modi (born September 17, 1950, Vadnagar, India) is an Indian politician and government official who rose to become a senior leader of the Bharatiya Janata Party (BJP). In 2014 he led his party to victory in elections to the Lok Sabha (lower chamber of the Indian parliament), after which he was sworn in as prime minister of India.Prior to that he had served (2001-14) as chief ... List of Prime Minister of India: 1947 to 2025. Narendra Modi is the current Prime Minister of India in 2025, serving the nation for the past 11 years since first taking office in 2014. The list of Indian Prime Ministers begins with Jawaharlal Nehru, who became the first Prime Minister in 1947 and consist . Jawaharlal Nehru is the longest-serving Prime Minister of India, holding office for 16 ...The search results clearly show that Narendra Modi is the current Prime Minister of India.
# Final Answer: Narendra Modi

# > Finished chain.
# {'input': 'Who is current Prime Minister of India?', 'output': 'Narendra Modi'}
# """
# print(response)


# # Example 3 - Custom Tool
# # Using Decorator
# class SearchInput(BaseModel):
#     query: str = Field(description="should be a search query")


# @tool("search-tool", args_schema=SearchInput, return_direct=True)
# def search(query: str) -> str:
#     """Look up things online"""
#     return "Langchain"


# # search-tool
# print(search.name)

# # Look up things online
# print(search.description)

# # {'query': {'description': 'should be a search query', 'title': 'Query', 'type': 'string'}}
# print(search.args)


# # Example 4 - Using StructuredTool
# class CalculatorInput(BaseModel):
#     a: int = Field(description="first number")
#     b: int = Field(description="second number")


# def multiply(a: int, b: int) -> int:
#     "Multiply two numbers"
#     return a * b


# calculator = StructuredTool.from_function(
#     func=multiply,
#     name="Calculator",
#     description="multiply numbers",
#     args_schema=CalculatorInput,
#     return_direct=True,
# )

# # Calculator
# print(calculator.name)

# # multiply numbers
# print(calculator.description)

# # {'a': {'description': 'first number', 'title': 'A', 'type': 'integer'}, 'b': {'description': 'second number', 'title': 'B', 'type': 'integer'}}
# print(calculator.args)


# # Example 5 - Using Custom Tool
# # Defining Custom Tool
# @tool
# def get_word_length(words: str) -> int:
#     """Returns the length of a word"""
#     return len(words)


# # Create Agent
# prompt = hub.pull("hwchase17/react")

# tools = [get_word_length]
# agent = create_react_agent(llm=chat, tools=tools, prompt=prompt)
# # Run Agent
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# response = agent_executor.invoke({"input": "Hello"})

# """
# > Entering new AgentExecutor chain...
# This is a word, so I should use the get_word_length function to determine its length.
# Action: get_word_length
# Action Input: "Hello"5I have found the length of the word "Hello".
# Final Answer: 5

# > Finished chain.
# {'input': 'Hello', 'output': '5'}
# """
# print(response)


# Example 6 - Multiple Tools
# Defining Custom Tool
@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    return len(word)


# Create Agent
prompt = hub.pull("hwchase17/react")
search = DuckDuckGoSearchRun()
tools = [get_word_length, search]
agent = create_react_agent(llm=chat, tools=tools, prompt=prompt)
# Run Agent
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
response = agent_executor.invoke(
    {
        "input": "What is LangChain ? What is the total word length of that including space ?"
    }
)

# """
# > Entering new AgentExecutor chain...
# I can use a search engine to look up information about LangChain and then calculate the total word length of the answer.
# Action: duckduckgo_search
# Action Input: "LangChain"LangChain is a powerful tool that can be used to build a wide range of LLM-powered applications. It is simple to use and has a large user and contributor community. Conversational Agents: Build chatbots and virtual assistants that can engage in meaningful, context-aware conversations with users. Why LangChain Matters in AI Development. LangChain simplifies the often-complex task of building applications that use LLMs. With its ability to chain multiple components together, developers can create solutions tailored to specific requirements without starting from scratch. Install LangChain and dependencies: pip install langchain openai python-dotenv 🪄 Your First LangChain Project: A Smart Q&A Bot from a Text File. Let's build a simple app that can read a text file and answer questions from it using an LLM. 🔹 Step 1: Setup Your API Key. Create a .env file in your project folder and add: What is LangChain, and why is it used? Answer: LangChain is a framework for building applications powered by language models. It simplifies tasks like connecting LLMs to data sources, managing conversational memory, and using external tools. Explain the concept of retrieval in LangChain. LangChain is a Python framework designed to streamline AI application development. It focuses on integrating large language models (LLMs) with real-time data processing. It offers features for data communication, generating vector embedding generation, and simplifying the interaction with LLMs, making it efficient for AI developers.I have gathered a lot of information about LangChain. Now I can calculate the total word length of this information including spaces.
# Action: get_word_length
# Action Input: "LangChain is a powerful tool that can be used to build a wide range of LLM-powered applications. It is simple to use and has a large user and contributor community. Conversational Agents: Build chatbots and virtual assistants that can engage in meaningful, context-aware conversations with users. Why LangChain Matters in AI Development. LangChain simplifies the often-complex task of building applications that use LLMs. With its ability to chain multiple components together, developers can create solutions tailored to specific requirements without starting from scratch. Install LangChain and dependencies: pip install langchain openai python-dotenv 🪄 Your First LangChain Project: A Smart Q&A Bot from a Text File. Let's build a simple app that can read a text file and answer questions from it using an LLM. 🔹 Step 1: Setup Your API Key. Create a .env file in your project folder and add: What is LangChain, and why is it used? Answer: LangChain is a framework for building applications powered by language models. It simplifies tasks like connecting LLMs to data sources, managing conversational memory, and using external tools. Explain the concept of retrieval in LangChain. LangChain is a Python framework designed to streamline AI application development. It focuses on integrating large language models (LLMs) with real-time data processing. It offers features for data communication, generating vector embedding generation, and simplifying the interaction with LLMs, making it efficient for AI developers."1518I have calculated the total word length of the information about LangChain.
# Final Answer: The total word length of the information about LangChain, including spaces, is 1518.

# > Finished chain.
# """
