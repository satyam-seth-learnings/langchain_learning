from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from decouple import config

HUGGINGFACEHUB_API_TOKEN = config("HUGGINGFACEHUB_API_TOKEN")

template = "<s>[INST]Write short answer of</s>{question}[/INST]"

prompt_template = PromptTemplate.from_template(template)
formatted_prompt_template = prompt_template.format(question="Who was Raja Hari Singh?")

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    task="text-generation",
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
)
response = llm.invoke(formatted_prompt_template)

# # Raja Hari Singh (full name: **Maharaja Hari Singh**) was the last ruling **Maharaja of the princely state of Jammu and Kashmir** in British India. He played a pivotal role in the events surrounding the partition of India in 1947 and the subsequent accession of Jammu and Kashmir to India.
# print(response)

# Streaming
response = llm.stream(formatted_prompt_template)
"""
Maharaja Hari Singh was the last ruling monarch of the princely state of Jammu and Kashmir, a region that would become one of the most contested territories in South Asia.
Born on September 23, 1895, into the Dogra dynasty, he ascended to the throne in 1925 and ruled until 1947. A complex and controversial figure, Hari Singh was known for his ambition to modernize his state while maintaining absolute authority.
His reign coincided with a period of immense political upheaval, as India moved toward independence from British rule. When the British left in 1947, princely states like Jammu and Kashmir were given the option to join either India or Pakistan or remain independent.
Hari Singh initially chose independence, aiming to keep his Muslim-majority state free from both emerging nations. However, this decision was short-lived. In October 1947, armed tribesmen from Pakistan invaded Kashmir, prompting a crisis. Faced with a threat he could not repel on his own, Hari Singh turned to India for military assistance. 
The Indian government agreed to send troops, but only after he signed the Instrument of Accession, formally integrating Jammu and Kashmir into India. He did so on October 26, 1947, a decision that laid the foundation for the long-standing conflict between India and Pakistan over the region.
After the accession, political pressure from Indian leaders, particularly Jawaharlal Nehru and the popular Kashmiri leader Sheikh Abdullah, led to Hari Singh being sidelined. By 1952, the monarchy was formally abolished, and Hari Singh was exiled to Bombay (now Mumbai), where he spent the remainder of his life until his death on April 26, 1961.
His legacy remains deeply intertwined with the history and politics of Kashmir, symbolizing both the end of princely rule in India and the beginning of a conflict that endures to this day.
"""
for res in response:
    print(res, end="", flush=True)
