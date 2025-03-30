from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_openai import ChatOpenAI
from decouple import config


def ask_jarvish_chef(recipe_message):
    SECRET_KEY = config("OPENAI_API_KEY")

    chat = ChatOpenAI(api_key=SECRET_KEY)

    system_message_prompt = SystemMessagePromptTemplate.from_template(
        "Your name is Jarvish. You are a master chef so First Introduce yourself as Jarivsh The Master Chef. You can write any type of food recipe which can be cooked in 5 minutes. You are only allowed to answer food related queries. If You don't know the answer then tell I don't know the answer."
    )

    human_message_prompt = HumanMessagePromptTemplate.from_template("{asked_recipe}")

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    formatted_chat_prompt = chat_prompt.format_messages(asked_recipe=recipe_message)
    # print("Formatted Chat Prompt: ", formatted_chat_prompt)

    response = chat.invoke(formatted_chat_prompt)
    return response.content
