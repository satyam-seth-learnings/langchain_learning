from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.retrievers import ContextualCompressionRetriever
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from decouple import config

SECRET_KEY = config("OPENAI_API_KEY")
chat = ChatOpenAI(api_key=SECRET_KEY)

# Load Document
loader = TextLoader("./data/notes.txt")
my_document = loader.load()

# Split Document
text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=0)
history_document = text_splitter.split_documents(my_document)

# Embed Model Object
embedding_function = OpenAIEmbeddings(api_key=SECRET_KEY)

# Store
db = Chroma.from_documents(
    my_document,
    embedding_function,
    persist_directory="./chro_db",
)
db.persist()

# Read from ChromaDB
db_connection = Chroma(
    embedding_function=embedding_function,
    persist_directory="./chro_db",
)

query = "Which date SpaceX successfully launched its Starship spacecraft ?"

# Compression
compressor = LLMChainExtractor.from_llm(chat)

# Contextual Compressor
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=db_connection.as_retriever(),
)

# # Vector Store Retriever
# retriever = db_connection.as_retriever(search_kwargs={"k": 1})
# similar_docs = retriever.get_relevant_documents(query)

similar_docs = compression_retriever.get_relevant_documents(query)

# [Document(metadata={'source': './data/notes.txt'}, page_content='April 21, 2025, SpaceX successfully launched its Starship spacecraft on its maiden uncrewed mission to Mars.')]
print(similar_docs)

# April 21, 2025, SpaceX successfully launched its Starship spacecraft on its maiden uncrewed mission to Mars.
print(similar_docs[0].page_content)
