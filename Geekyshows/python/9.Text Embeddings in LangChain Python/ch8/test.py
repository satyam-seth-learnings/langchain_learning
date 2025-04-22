from langchain_openai import OpenAIEmbeddings
from decouple import config

SECRET_KEY = config("OPENAI_API_KEY")
embeddings_model = OpenAIEmbeddings(api_key=SECRET_KEY)

# Example 1 - Embed Query
text = "This is sample text"
embedded_query = embeddings_model.embed_query(text)
print(embedded_query)


# # Example 2 - Embed Document
# text = [
#     "Hello Sonam",
#     "How are you ?",
#     "Where are you now ?",
# ]

# embedded_query = embeddings_model.embed_documents(text)
# print(embedded_query)
# print(len(embedded_query))  # 3
