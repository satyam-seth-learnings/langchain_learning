from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_community.document_loaders import (
    TextLoader,
    CSVLoader,
    BSHTMLLoader,
    PyPDFLoader,
)
from decouple import config

SECRET_KEY = config("OPENAI_API_KEY")
chat = ChatOpenAI(api_key=SECRET_KEY)

# # Example 1 Text File
# loader = TextLoader("./data/sample.txt")
# mydata = loader.load()

# # # My Data: [Document(metadata={'source': './data/sample.txt'}, page_content='This is sample line 1\nThis is sample line 2\nThis is sample line 3\nThis is sample line 4')]
# # print("My Data:", mydata)

# # """
# # My Data[0]: page_content='This is sample line 1
# # This is sample line 2
# # This is sample line 3
# # This is sample line 4' metadata={'source': './data/sample.txt'}
# # """
# # print("My Data[0]:", mydata[0])

# # """
# # My Data[0].page_content:
# #  This is sample line 1
# # This is sample line 2
# # This is sample line 3
# # This is sample line 4
# # """
# # print("My Data[0].page_content:\n", mydata[0].page_content)

# # My Metadata:  {'source': './data/sample.txt'}
# print("My Metadata: ", mydata[0].metadata)


# # Example 2 - CSV File
# loader = CSVLoader("./data/sample.csv")
# mydata = loader.load()

# # # My Data: [Document(metadata={'source': './data/sample.csv', 'row': 0}, page_content='name: sonam\nroll: 101'), Document(metadata={'source': './data/sample.csv', 'row': 1}, page_content='name: raj\nroll: 102'), Document(metadata={'source': './data/sample.csv', 'row': 2}, page_content='name: kunal\nroll: 103')]
# # print("My Data:", mydata)

# # """
# # My Data[0]: page_content='name: sonam
# # roll: 101' metadata={'source': './data/sample.csv', 'row': 0}
# # """
# # print("My Data[0]:", mydata[0])

# # """
# # My Data[0].page_content:
# #  name: sonam
# # roll: 101
# # """
# # print("My Data[0].page_content:\n", mydata[0].page_content)

# # My Metadata:  {'source': './data/sample.csv', 'row': 0}
# print("My Metadata: ", mydata[0].metadata)


# # Example 3 - HTML File
# loader = BSHTMLLoader("./data/sample.html")
# mydata = loader.load()

# # # My Data: [Document(metadata={'source': './data/sample.html', 'title': 'My Title'}, page_content='\n\n\n\nMy Title\n\n\nThis is sample line 1\n\n')]
# # print("My Data:", mydata)

# # """
# # My Data[0]: page_content='


# # My Title


# # This is sample line 1

# # ' metadata={'source': './data/sample.html', 'title': 'My Title'}
# # """
# # print("My Data[0]:", mydata[0])

# # """
# # My Data[0].page_content:


# # My Title


# # This is sample line 1

# # """
# # print("My Data[0].page_content:\n", mydata[0].page_content)

# # My Data[0].page_content:     My Title   This is sample line 1
# print("My Data[0].page_content:", mydata[0].page_content.replace("\n", " "))


# # Example 4 - PDF File
# loader = PyPDFLoader("./data/sample.pdf")
# mydata = loader.load()

# # # My Data: [Document(metadata={'producer': 'Microsoft® Word 2019', 'creator': 'Microsoft® Word 2019', 'creationdate': '2025-04-21T20:36:49+05:30', 'author': 'Satyam Seth', 'moddate': '2025-04-21T20:36:49+05:30', 'source': './data/sample.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}, page_content='This is sample line 1 \nThis is sample line 2')]
# # print("My Data:", mydata)

# # """
# # My Data[0]: page_content='This is sample line 1
# # This is sample line 2' metadata={'producer': 'Microsoft® Word 2019', 'creator': 'Microsoft® Word 2019', 'creationdate': '2025-04-21T20:36:49+05:30', 'author': 'Satyam Seth', 'moddate': '2025-04-21T20:36:49+05:30', 'source': './data/sample.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}
# # """
# # print("My Data[0]:", mydata[0])

# # """
# # My Data[0].page_content:
# #  This is sample line 1
# # This is sample line 2
# # """
# # print("My Data[0].page_content:\n", mydata[0].page_content)

# # My Metadata:  {'producer': 'Microsoft® Word 2019', 'creator': 'Microsoft® Word 2019', 'creationdate': '2025-04-21T20:36:49+05:30', 'author': 'Satyam Seth', 'moddate': '2025-04-21T20:36:49+05:30', 'source': './data/sample.pdf', 'total_pages': 1, 'page': 0, 'page_label': '1'}
# print("My Metadata: ", mydata[0].metadata)


# Example 5
loader = TextLoader("./data/legal.txt")
my_context = loader.load()[0].page_content
human_template = "{question}\n{company_legal_doc}"
chat_prompt = ChatPromptTemplate.from_messages(
    [HumanMessagePromptTemplate.from_template(human_template)]
)
formatted_chat_prompt = chat_prompt.format_messages(
    question="How can i apply for PAN Card",
    company_legal_doc=my_context,
)

# # ormatted Chat Prompt:  [HumanMessage(content='How can i apply for PAN Card\nWe are running an IT Company name "Opsmit Tech" in India which is not yet registered.', additional_kwargs={}, response_metadata={})]
# print("Formatted Chat Prompt: ", formatted_chat_prompt)

response = chat.invoke(formatted_chat_prompt)
print("Response Content: ", response.content)
