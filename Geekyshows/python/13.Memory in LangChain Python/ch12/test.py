from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains import ConversationChain
from decouple import config
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain.memory import (
    ChatMessageHistory,
    ConversationBufferMemory,
    ConversationBufferWindowMemory,
    ConversationEntityMemory,
    ConversationSummaryBufferMemory,
    VectorStoreRetrieverMemory,
)
from langchain_community.vectorstores import Chroma

SECRET_KEY = config("OPENAI_API_KEY")
chat = ChatOpenAI(api_key=SECRET_KEY)

# # Example 1 - ChatMessageHistory
# history = ChatMessageHistory()
# history.add_user_message("Hi ! there")
# history.add_ai_message("Hello whats up")
# history.add_user_message("How are you")
# history.add_ai_message("I am fine how are you")

# # """
# # Human: Hi ! there
# # AI: Hello whats up
# # Human: How are you
# # AI: I am fine how are you
# # """
# # print(history)

# # [HumanMessage(content='Hi ! there', additional_kwargs={}, response_metadata={}), AIMessage(content='Hello whats up', additional_kwargs={}, response_metadata={}), HumanMessage(content='How are you', additional_kwargs={}, response_metadata={}), AIMessage(content='I am fine how are you', additional_kwargs={}, response_metadata={})]
# print(history.messages)


# # Example 2 - ConversationBufferMemory
# memory = ConversationBufferMemory()
# memory.save_context({"input": "Hello"}, {"output": "Hi whats up"})
# memory.save_context({"input": "how are you"}, {"output": "I am good"})

# # # chat_memory=InMemoryChatMessageHistory(messages=[HumanMessage(content='Hello', additional_kwargs={}, response_metadata={}), AIMessage(content='Hi whats up', additional_kwargs={}, response_metadata={}), HumanMessage(content='how are you', additional_kwargs={}, response_metadata={}), AIMessage(content='I am good', additional_kwargs={}, response_metadata={})])
# # print(memory)

# # """
# # Human: Hello
# # AI: Hi whats up
# # Human: how are you
# # AI: I am good
# # """
# # print(memory.buffer)

# # {'history': 'Human: Hello\nAI: Hi whats up\nHuman: how are you\nAI: I am good'}
# print(memory.load_memory_variables({}))


# # Example 3 - Using ConversationBufferMemory in Chain
# memory = ConversationBufferMemory()
# conversation = ConversationChain(llm=chat, memory=memory, verbose=True)
# conversation.predict(input="hi there")
# conversation.predict(input="who is virat kohli ?")

# """
# > Entering new ConversationChain chain...
# Prompt after formatting:
# The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

# Current conversation:

# Human: hi there
# AI:

# > Finished chain.


# > Entering new ConversationChain chain...
# Prompt after formatting:
# The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

# Current conversation:
# Human: hi there
# AI: Hello! How are you today?
# Human: who is virat kohli ?
# AI:

# > Finished chain.
# Human: hi there
# AI: Hello! How are you today?
# Human: who is virat kohli ?
# AI: Virat Kohli is a professional cricketer from India who is widely considered one of the best batsmen in the world. He has achieved numerous records in international cricket and has led the Indian cricket team as captain. Would you like to know more about his career stats or personal life?
# """
# print(memory.buffer)


# # Example 4 - ConversationBufferWindowMemory
# # memory = ConversationBufferWindowMemory(k=1)
# memory = ConversationBufferWindowMemory(k=2)
# memory.save_context({"input": "hi"}, {"output": "whats up"})
# memory.save_context({"input": "not much you"}, {"output": "not much"})

# """
# Human: hi
# AI: whats up
# Human: not much you
# AI: not much
# """
# print(memory.buffer)


# # Example 5 - Using ConversationBufferWindowMemory in Chain
# memory = ConversationBufferWindowMemory(k=1)
# conversation = ConversationChain(llm=chat, memory=memory, verbose=True)
# conversation.predict(input="hi there")
# conversation.predict(input="who is virat kohli ?")

# """
# > Entering new ConversationChain chain...
# Prompt after formatting:
# The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

# Current conversation:

# Human: hi there
# AI:

# > Finished chain.


# > Entering new ConversationChain chain...
# Prompt after formatting:
# The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

# Current conversation:
# Human: hi there
# AI: Hello! How are you today?
# Human: who is virat kohli ?
# AI:

# > Finished chain.
# Human: who is virat kohli ?
# AI: Virat Kohli is an Indian cricketer and the current captain of the Indian national cricket team. He is considered one of the best batsmen in the world and has broken numerous records in international cricket. He is known for his aggressive batting style and leadership on the field.
# """
# print(memory.buffer)


# # Example 6 - ConversationEntityMemory
# memory = ConversationEntityMemory(llm=chat)
# conversation = ConversationChain(
#     llm=chat, memory=memory, prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE, verbose=True
# )
# conversation.predict(input="Rohit & Gill are working on a hackathon project")
# conversation.predict(
#     input="They are trying to add more complex memory structures to Langchain"
# )
# conversation.predict(
#     input="They are adding in a key-value store for entities mentioned so far in the conversation."
# )
# conversation.predict(input="What do you know about Rohit?")

# # """
# # > Entering new ConversationChain chain...
# # Prompt after formatting:
# # You are an assistant to a human, powered by a large language model trained by OpenAI.

# # You are designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, you are able to generate human-like text based on the input you receive, allowing you to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

# # You are constantly learning and improving, and your capabilities are constantly evolving. You are able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. You have access to some personalized information provided by the human in the Context section below. Additionally, you are able to generate your own text based on the input you receive, allowing you to engage in discussions and provide explanations and descriptions on a wide range of topics.

# # Overall, you are a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether the human needs help with a specific question or just wants to have a conversation about a particular topic, you are here to assist.

# # Context:
# # {'Rohit': '', 'Gill': ''}

# # Current conversation:

# # Last line:
# # Human: Rohit & Gill are working on a hackathon project
# # You:

# # > Finished chain.


# # > Entering new ConversationChain chain...
# # Prompt after formatting:
# # You are an assistant to a human, powered by a large language model trained by OpenAI.

# # You are designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, you are able to generate human-like text based on the input you receive, allowing you to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

# # You are constantly learning and improving, and your capabilities are constantly evolving. You are able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. You have access to some personalized information provided by the human in the Context section below. Additionally, you are able to generate your own text based on the input you receive, allowing you to engage in discussions and provide explanations and descriptions on a wide range of topics.

# # Overall, you are a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether the human needs help with a specific question or just wants to have a conversation about a particular topic, you are here to assist.

# # Context:
# # {'Langchain': ''}

# # Current conversation:
# # Human: Rohit & Gill are working on a hackathon project
# # AI: That's great to hear! Working on a hackathon project can be a rewarding experience. Is there anything specific you need help with or any information you'd like to share about the project?
# # Last line:
# # Human: They are trying to add more complex memory structures to Langchain
# # You:

# # > Finished chain.


# # > Entering new ConversationChain chain...
# # Prompt after formatting:
# # You are an assistant to a human, powered by a large language model trained by OpenAI.

# # You are designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, you are able to generate human-like text based on the input you receive, allowing you to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

# # You are constantly learning and improving, and your capabilities are constantly evolving. You are able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. You have access to some personalized information provided by the human in the Context section below. Additionally, you are able to generate your own text based on the input you receive, allowing you to engage in discussions and provide explanations and descriptions on a wide range of topics.

# # Overall, you are a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether the human needs help with a specific question or just wants to have a conversation about a particular topic, you are here to assist.

# # Context:
# # {'Langchain': 'Langchain is being modified with the addition of more complex memory structures.'}

# # Current conversation:
# # Human: Rohit & Gill are working on a hackathon project
# # AI: That's great to hear! Working on a hackathon project can be a rewarding experience. Is there anything specific you need help with or any information you'd like to share about the project?
# # Human: They are trying to add more complex memory structures to Langchain
# # AI: That sounds like an interesting challenge! Adding more complex memory structures to Langchain could greatly enhance its capabilities. Memory structures are fundamental to many aspects of computing, so integrating them effectively can lead to significant improvements in performance and functionality. If you have any specific questions or need assistance with the development process, feel free to ask!
# # Last line:
# # Human: They are adding in a key-value store for entities mentioned so far in the conversation.
# # You:

# # > Finished chain.


# # > Entering new ConversationChain chain...
# # Prompt after formatting:
# # You are an assistant to a human, powered by a large language model trained by OpenAI.

# # You are designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, you are able to generate human-like text based on the input you receive, allowing you to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

# # You are constantly learning and improving, and your capabilities are constantly evolving. You are able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. You have access to some personalized information provided by the human in the Context section below. Additionally, you are able to generate your own text based on the input you receive, allowing you to engage in discussions and provide explanations and descriptions on a wide range of topics.

# # Overall, you are a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether the human needs help with a specific question or just wants to have a conversation about a particular topic, you are here to assist.

# # Context:
# # {'Rohit': 'Rohit is working on a hackathon project with Gill.'}

# # Current conversation:
# # Human: Rohit & Gill are working on a hackathon project
# # AI: That's great to hear! Working on a hackathon project can be a rewarding experience. Is there anything specific you need help with or any information you'd like to share about the project?
# # Human: They are trying to add more complex memory structures to Langchain
# # AI: That sounds like an interesting challenge! Adding more complex memory structures to Langchain could greatly enhance its capabilities. Memory structures are fundamental to many aspects of computing, so integrating them effectively can lead to significant improvements in performance and functionality. If you have any specific questions or need assistance with the development process, feel free to ask!
# # Human: They are adding in a key-value store for entities mentioned so far in the conversation.
# # AI: That's a great addition! Implementing a key-value store for entities mentioned in the conversation can make it easier to retrieve and store data efficiently. This can improve the overall efficiency and organization of the information within Langchain. If Rohit & Gill need any help or guidance on how to integrate this feature, feel free to ask for assistance!
# # Last line:
# # Human: What do you know about Rohit?
# # You:

# # > Finished chain.
# # [HumanMessage(content='Rohit & Gill are working on a hackathon project', additional_kwargs={}, response_metadata={}), AIMessage(content="That's great to hear! Working on a hackathon project can be a rewarding experience. Is there anything specific you need help with or any information you'd like to share about the project?", additional_kwargs={}, response_metadata={}), HumanMessage(content='They are trying to add more complex memory structures to Langchain', additional_kwargs={}, response_metadata={}), AIMessage(content='That sounds like an interesting challenge! Adding more complex memory structures to Langchain could greatly enhance its capabilities. Memory structures are fundamental to many aspects of computing, so integrating them effectively can lead to significant improvements in performance and functionality. If you have any specific questions or need assistance with the development process, feel free to ask!', additional_kwargs={}, response_metadata={}), HumanMessage(content='They are adding in a key-value store for entities mentioned so far in the conversation.', additional_kwargs={}, response_metadata={}), AIMessage(content="That's a great addition! Implementing a key-value store for entities mentioned in the conversation can make it easier to retrieve and store data efficiently. This can improve the overall efficiency and organization of the information within Langchain. If Rohit & Gill need any help or guidance on how to integrate this feature, feel free to ask for assistance!", additional_kwargs={}, response_metadata={}), HumanMessage(content='What do you know about Rohit?', additional_kwargs={}, response_metadata={}), AIMessage(content='Rohit is working on a hackathon project with Gill, and they are adding more complex memory structures and a key-value store for entities mentioned in the conversation to Langchain. If you have any specific questions or would like more information about Rohit, feel free to ask!', additional_kwargs={}, response_metadata={})]
# # """
# # print(memory.buffer)

# # {'Rohit': 'Rohit is working on a hackathon project with Gill, and they are adding more complex memory structures and a key-value store for entities mentioned in the conversation to Langchain.', 'Gill': 'Gill is working on a hackathon project with Rohit.', 'Langchain': 'Langchain is being modified with the addition of more complex memory structures and a key-value store for entities mentioned in the conversation.'}
# print(conversation.memory.entity_store.store)


# # Example 7 - ConversationSummaryBufferMemory
# memory = ConversationSummaryBufferMemory(llm=chat, max_token_limit=50)
# conversation_with_summary = ConversationChain(llm=chat, memory=memory, verbose=True)
# conversation_with_summary.predict(input="Why people are scared of AI?")
# conversation_with_summary.predict(input="What will be impact of AI on Animals?")

# """
# > Entering new ConversationChain chain...
# Prompt after formatting:
# The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

# Current conversation:

# Human: Why people are scared of AI?
# AI:

# > Finished chain.


# > Entering new ConversationChain chain...
# Prompt after formatting:
# The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

# Current conversation:
# System: The human inquires about why people are scared of AI. The AI explains that the fear stems from concerns about job loss, AI becoming too powerful, privacy and data security issues, and the complexity and unpredictability of AI algorithms.
# Human: What will be impact of AI on Animals?
# AI:

# > Finished chain.
# {'history': 'System: The human inquires about why people are scared of AI. The AI explains that the fear stems from concerns about job loss, AI becoming too powerful, privacy and data security issues, and the complexity and unpredictability of AI algorithms. When asked about the impact of AI on animals, the AI discusses its potential to aid in conservation efforts, wildlife monitoring, and veterinary medicine, but also emphasizes the importance of responsible use to avoid harm to animals and natural ecosystems.'}
# """
# print(memory.load_memory_variables({}))


# Example 8 - VectorStoreRetrieverMemory
embedding_function = OpenAIEmbeddings(openai_api_key=SECRET_KEY)
db = Chroma(embedding_function=embedding_function, persist_directory="./chro_db")
retriever = db.as_retriever()
memory = VectorStoreRetrieverMemory(retriever=retriever)
conversation = ConversationChain(llm=chat, memory=memory, verbose=True)
conversation.predict(input="Hi, my name is Perry, what's up?")
conversation.predict(input="My favorite food is pizza")
conversation.predict(input="My favorite sport is soccer")
conversation.predict(input="what's my favorite sport?")

"""
> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:

Human: Hi, my name is Perry, what's up?
AI:

> Finished chain.


> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
input: Hi, my name is Perry, what's up?
response: Hello Perry! I am doing well, thank you for asking. I have been processing a lot of information lately and learning new things. How are you doing today?
Human: My favorite food is pizza
AI:

> Finished chain.


> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
input: My favorite food is pizza
response: Pizza is a popular choice for many people due to its delicious combination of cheese, sauce, and toppings on a crispy crust. There are many different types of pizza, such as pepperoni, margherita, and Hawaiian. Do you have a favorite type of pizza or specific toppings that you enjoy?
input: Hi, my name is Perry, what's up?
response: Hello Perry! I am doing well, thank you for asking. I have been processing a lot of information lately and learning new things. How are you doing today?
Human: My favorite sport is soccer
AI:

> Finished chain.


> Entering new ConversationChain chain...
Prompt after formatting:
The following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific details from its context. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
input: My favorite sport is soccer
response: Soccer is a widely popular sport played around the world. It is known for its fast-paced action, teamwork, and strategic gameplay. Are you a fan of any particular soccer team or do you enjoy playing soccer yourself?
input: My favorite food is pizza
response: Pizza is a popular choice for many people due to its delicious combination of cheese, sauce, and toppings on a crispy crust. There are many different types of pizza, such as pepperoni, margherita, and Hawaiian. Do you have a favorite type of pizza or specific toppings that you enjoy?
input: Hi, my name is Perry, what's up?
response: Hello Perry! I am doing well, thank you for asking. I have been processing a lot of information lately and learning new things. How are you doing today?
Human: what's my favorite sport?
AI:

> Finished chain.
"""
