from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from langchain.prompts import PromptTemplate

llm = HuggingFacePipeline.from_model_id(
    model_id="gpt2",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 50},
)
template = "{question}"
prompt_template = PromptTemplate.from_template(template)
formatted_prompt_template = prompt_template.format(question="What is Javascript ?")
response = llm.invoke(formatted_prompt_template)

"""
Device set to use cpu
What is Javascript ?

In my opinion Javascript is one of the best technologies out there

It can easily replace other websites with HTML5 or CSS3, make web development faster with CSS3 and other web features -

HTML5 (and other modern mobile
"""
print(response)
