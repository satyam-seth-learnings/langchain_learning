from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from decouple import config

SECRET_KEY = config("OPENAI_API_KEY")

# # Example 1

# # Load Document
# loader = TextLoader("./data/history.txt")
# history_doc = loader.load()

# # Split Document
# text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=0)
# history_document = text_splitter.split_documents(history_doc)

# # Embed Model Object
# embedding_function = OpenAIEmbeddings(api_key=SECRET_KEY)

# # Store
# db = Chroma.from_documents(history_document, embedding_function)

# query = "most eventful periods in history"

# # similar_docs = db.similarity_search(query)

# # Vector Store Retriever
# retriever = db.as_retriever()
# similar_docs = retriever.get_relevant_documents(query)

# print(similar_docs)
# print(similar_docs[0].page_content)


# # Example 2

# # Load Document
# loader = TextLoader("./data/history.txt")
# history_doc = loader.load()

# # Split Document
# text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=0)
# history_document = text_splitter.split_documents(history_doc)

# # Embed Model Object
# embedding_function = OpenAIEmbeddings(api_key=SECRET_KEY)

# # Store
# db = Chroma.from_documents(
#     history_document,
#     embedding_function,
#     persist_directory="./chro_db",
# )

# db.persist()

# # Read from ChromaDB
# db_connection = Chroma(
#     embedding_function=embedding_function, persist_directory="./chro_db"
# )

# query = "most eventful periods in history"

# # Vector Store Retriever
# # retriever = db_connection.as_retriever()
# # retriever = db_connection.as_retriever(search_kwargs={'k': 1})
# retriever = db_connection.as_retriever(search_kwargs={"k": 2})
# similar_docs = retriever.get_relevant_documents(query)

# # [Document(metadata={'source': './data/history.txt'}, page_content='The 20th century was one of the most eventful periods in history. It saw two world wars, the Cold War, the rise and fall of empires, civil rights movements, and the development of technology that connected the world. Events like the moon landing, the fall of the Berlin Wall, and the growth of the internet reshaped the modern world.'), Document(metadata={'source': './data/history.txt'}, page_content='The earliest known civilizations emerged around river valleys, such as Mesopotamia, Ancient Egypt, the Indus Valley, and China. These societies developed writing, agriculture, trade, and complex governments. Their innovations, like the wheel and early forms of writing like cuneiform and hieroglyphics, laid the foundation for human progress.\n\nThe Middle Ages, or medieval period, lasted from roughly the 5th to the late 15th century. It began after the fall of the Roman Empire and was marked by feudalism, the rise of the Catholic Church, and frequent warfare. Despite being labeled the "Dark Ages," this era also saw growth in art, learning, and the foundation of universities.'), Document(metadata={'source': './data/history.txt'}, page_content='Starting in the 14th century, the Renaissance was a period of renewed interest in art, science, and classical learning, especially in Europe. Thinkers like Leonardo da Vinci and Galileo made major advances, while artists like Michelangelo and Raphael created works that are still celebrated today. This era helped shape modern Western thought.\n\nIn the 18th and 19th centuries, the Industrial Revolution transformed economies and societies. It began in Britain with the invention of machines that revolutionized production. Urbanization increased, new transportation methods like railroads developed, and labor systems changed dramatically—though it also brought pollution and harsh working conditions.')]
# print(similar_docs)

# # The 20th century was one of the most eventful periods in history. It saw two world wars, the Cold War, the rise and fall of empires, civil rights movements, and the development of technology that connected the world. Events like the moon landing, the fall of the Berlin Wall, and the growth of the internet reshaped the modern world.
# print(similar_docs[0].page_content)


# Example 2

# Load Document
loader = TextLoader("./data/science.txt")
science_doc = loader.load()

# Split Document
text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=0)
science_document = text_splitter.split_documents(science_doc)

# Embed Model Object
embedding_function = OpenAIEmbeddings(api_key=SECRET_KEY)

# Store
db = Chroma.from_documents(
    science_document,
    embedding_function,
    persist_directory="./chro_db",
)

db.persist()

# Read from ChromaDB
db_connection = Chroma(
    embedding_function=embedding_function, persist_directory="./chro_db"
)

query = "Science is divided into"

# Vector Store Retriever
# retriever = db_connection.as_retriever()
# retriever = db_connection.as_retriever(search_kwargs={'k': 1})
retriever = db_connection.as_retriever(search_kwargs={"k": 2})
similar_docs = retriever.get_relevant_documents(query)

# [Document(metadata={'source': './data/science.txt'}, page_content='Science is the study of the natural world through observation and experimentation. It helps us understand how things work—from the smallest atoms to the vastness of the universe. Scientists use evidence and reasoning to form theories and solve problems that improve our lives.\n\nScience is divided into different branches. Physics explores energy, matter, and forces; chemistry studies substances and how they change; biology focuses on living organisms. Other branches include Earth science, astronomy, and environmental science, each helping us understand different parts of the world around us.'), Document(metadata={'source': './data/science.txt'}, page_content='At the heart of science is the scientific method—a step-by-step process that starts with asking a question, forming a hypothesis, testing it through experiments, and analyzing results. This method helps scientists discover reliable facts and avoid guessing or relying on beliefs alone.\n\nScience drives technology. From electricity and medicine to space travel and smartphones, many of the things we use daily came from scientific research. As scientists discover more, engineers and inventors use that knowledge to create new tools and solutions.')]
print(similar_docs)

"""
Science is the study of the natural world through observation and experimentation. It helps us understand how things work—from the smallest atoms to the vastness of the universe. Scientists use evidence and reasoning to form theories and solve problems that improve our lives.

Science is divided into different branches. Physics explores energy, matter, and forces; chemistry studies substances and how they change; biology focuses on living organisms. Other branches include Earth science, astronomy, and environmental science, each helping us understand different parts of the world around us.
"""
print(similar_docs[0].page_content)
