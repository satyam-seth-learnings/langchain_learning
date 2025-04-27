from langchain import hub
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.output_parsers import StrOutputParser
from decouple import config
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_community.tools import DuckDuckGoSearchRun

SECRET_KEY = config("OPENAI_API_KEY")

# # Example 1 - Basic Streaming 1
# chat = ChatOpenAI(
#     api_key=SECRET_KEY,
#     streaming=True,
#     callbacks=[StreamingStdOutCallbackHandler()],
# )
# chat_prompt = ChatPromptTemplate.from_messages(
#     [HumanMessagePromptTemplate.from_template("Tell me a long story about {topic}")]
# )
# formatted_chat_prompt = chat_prompt.format_messages(topic="king arthur")
# response = chat.invoke(formatted_chat_prompt)

# """
# In the land of Camelot, there once lived a noble and just king named Arthur. Born as the son of King Uther Pendragon and Queen Igraine, Arthur was destined for greatness from the moment he entered the world. However, his true lineage was kept a secret, as he was raised by the wizard Merlin in a small village far away from the castle.

# As Arthur grew older, it became clear that he possessed a rare and noble spirit. He was kind-hearted, brave, and wise beyond his years. It was not long before he was discovered to be the true heir to the throne of Camelot, and he was crowned king at the tender age of sixteen.

# Under Arthur's rule, Camelot prospered. The people flourished, and peace reigned throughout the land. His knights, known as the Knights of the Round Table, were the bravest and most chivalrous in all the realm. Among them were Sir Lancelot, the greatest knight of them all, Sir Gawain, Sir Percival, Sir Galahad, and many others.

# But Arthur's reign was not without its challenges. His half-sister, the sorceress Morgan le Fay, sought to overthrow him and claim the throne for herself. She conspired with Mordred, Arthur's illegitimate son, to bring about his downfall. Betrayal and treachery threatened to tear Camelot apart from within.

# In the midst of this turmoil, Arthur embarked on a quest to find the Holy Grail, a sacred relic said to hold the key to eternal life. With his knights by his side, he faced many trials and tribulations, but ultimately proved himself worthy of the Grail's power.

# However, the greatest challenge still lay ahead. In a fateful battle against Mordred and his forces, Arthur was mortally wounded. As he lay dying on the battlefield, he instructed his loyal knight, Sir Bedivere, to return Excalibur, his legendary sword, to the Lady of the Lake.

# And so, with tears in his eyes, Sir Bedivere cast the sword into the waters, where a hand rose up to catch it before disappearing beneath the surface. With his duty fulfilled, Sir Bedivere returned to find that Arthur had passed into legend, leaving behind a legacy that would never be forgotten.

# The tale of King Arthur and Camelot has endured through the ages, a shining example of courage, honor, and sacrifice. And though his kingdom may have fallen, the spirit of Arthur lives on in the hearts of those who still believe in the ideals of chivalry and justice.In the land of Camelot, there once lived a noble and just king named Arthur. Born as the son of King Uther Pendragon and Queen Igraine, Arthur was destined for greatness from the moment he entered the world. However, his true lineage was kept a secret, as he was raised by the wizard Merlin in a small village far away from the castle.

# As Arthur grew older, it became clear that he possessed a rare and noble spirit. He was kind-hearted, brave, and wise beyond his years. It was not long before he was discovered to be the true heir to the throne of Camelot, and he was crowned king at the tender age of sixteen.

# Under Arthur's rule, Camelot prospered. The people flourished, and peace reigned throughout the land. His knights, known as the Knights of the Round Table, were the bravest and most chivalrous in all the realm. Among them were Sir Lancelot, the greatest knight of them all, Sir Gawain, Sir Percival, Sir Galahad, and many others.

# But Arthur's reign was not without its challenges. His half-sister, the sorceress Morgan le Fay, sought to overthrow him and claim the throne for herself. She conspired with Mordred, Arthur's illegitimate son, to bring about his downfall. Betrayal and treachery threatened to tear Camelot apart from within.

# In the midst of this turmoil, Arthur embarked on a quest to find the Holy Grail, a sacred relic said to hold the key to eternal life. With his knights by his side, he faced many trials and tribulations, but ultimately proved himself worthy of the Grail's power.

# However, the greatest challenge still lay ahead. In a fateful battle against Mordred and his forces, Arthur was mortally wounded. As he lay dying on the battlefield, he instructed his loyal knight, Sir Bedivere, to return Excalibur, his legendary sword, to the Lady of the Lake.

# And so, with tears in his eyes, Sir Bedivere cast the sword into the waters, where a hand rose up to catch it before disappearing beneath the surface. With his duty fulfilled, Sir Bedivere returned to find that Arthur had passed into legend, leaving behind a legacy that would never be forgotten.

# The tale of King Arthur and Camelot has endured through the ages, a shining example of courage, honor, and sacrifice. And though his kingdom may have fallen, the spirit of Arthur lives on in the hearts of those who still believe in the ideals of chivalry and justice.
# """
# print(response.content)


# # Example 2 - Basic Streaming 2
# chat = ChatOpenAI(api_key=SECRET_KEY)
# chat_prompt = ChatPromptTemplate.from_messages(
#     [HumanMessagePromptTemplate.from_template("Tell me a fact about {topic}")]
# )
# formatted_chat_prompt = chat_prompt.format_messages(topic="king arthur")
# response = chat.stream(formatted_chat_prompt)

# # One fact about King Arthur is that he is a legendary British leader who is said to have led the defense of Britain against the Saxon invaders in the late 5th and early 6th centuries. His story has been passed down through folklore and literature, with many different versions of his life and adventures.%
# for res in response:
#     print(res.content, end="", flush=True)


# # Example 3 - Streaming in Chain
# chat = ChatOpenAI(openai_api_key=SECRET_KEY)
# chat_prompt = ChatPromptTemplate.from_template("Tell me a fact about {topic}")
# chain = chat_prompt | chat | StrOutputParser()
# response = chain.stream({"topic": "Python"})

# # Python is named after the British comedy television show Monty Python's Flying Circus, not the snake.%
# for res in response:
#     print(res, end="", flush=True)

# Example 4 - Streaming with Agents
chat = ChatOpenAI(openai_api_key=SECRET_KEY)
# Create Agent
prompt = hub.pull("hwchase17/openai-functions-agent")

search = DuckDuckGoSearchRun()

tools = [search]
agent = create_openai_functions_agent(llm=chat, tools=tools, prompt=prompt)
# Run Agent
agent_executor = AgentExecutor(agent=agent, tools=tools)
response = agent_executor.stream({"input": "Who is current Prime Minister of India?"})

"""
Calling Tool: `duckduckgo_search` with input `{'query': 'Current Prime Minister of India'}`
---
Tool Result: `List of all Prime Ministers of India till 2025: Narendra Modi is the current and 14th Prime Minister of India who assumed office on 10 June 2024. Jawaharlal Nehru is the first and the longest ... India follows a parliamentary system in which the prime minister is the presiding head of the government and chief of the executive of the government. In such systems, the head of state, or, the head of state's official representative (i.e., the monarch, president, or governor-general) usually holds a purely ceremonial position and acts—on most matters—only on the advice of the prime minister. Prime Minister, Shri Narendra Modi, today condoled the loss of lives in an accident in Nuh, Haryana. "The state government is making every possible effort for relief and rescue", Shri Modi said. ... Shri Narendra Modi was sworn-in as India's Prime Minister for the third time on 9th June 2024, following another decisive victory in the 2024 ... Narendra Modi (born September 17, 1950, Vadnagar, India) is an Indian politician and government official who rose to become a senior leader of the Bharatiya Janata Party (BJP). In 2014 he led his party to victory in elections to the Lok Sabha (lower chamber of the Indian parliament), after which he was sworn in as prime minister of India.Prior to that he had served (2001-14) as chief ... List of Prime Minister of India: 1947 to 2025. Narendra Modi is the current Prime Minister of India in 2025, serving the nation for the past 11 years since first taking office in 2014. The list of Indian Prime Ministers begins with Jawaharlal Nehru, who became the first Prime Minister in 1947 and consist . Jawaharlal Nehru is the longest-serving Prime Minister of India, holding office for 16 ...`
---
Final Output: The current Prime Minister of India is Narendra Modi. He assumed office on June 10, 2024.
---
"""
for res in response:
    # Agent Action
    if "actions" in res:
        for action in res["actions"]:
            print(f"Calling Tool: `{action.tool}` with input `{action.tool_input}`")
    # Observation
    elif "steps" in res:
        for step in res["steps"]:
            print(f"Tool Result: `{step.observation}`")
    # Final result
    elif "output" in res:
        print(f'Final Output: {res["output"]}')
    else:
        raise ValueError()
    print("---")
