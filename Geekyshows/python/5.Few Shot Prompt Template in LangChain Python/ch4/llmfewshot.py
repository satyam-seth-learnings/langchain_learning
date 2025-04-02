from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from decouple import config

SECRET_KEY = config("OPENAI_API_KEY")
llm = OpenAI(api_key=SECRET_KEY)

# LLMs
# Few Shot Examples
examples = [
    {
        "input": "The patient presented with acute exacerbation of chronic obstructive pulmonary disease, manifesting symptoms such as dyspnea, increased respiratory rate, and use of accessory muscles for breathing.",
        "output": "The patient is having a sudden worsening of chronic lung disease. This shows with difficulty breathing, faster breathing, and using extra muscles to breathe.",
    },
    {
        "input": "patient is experiencing hyperlipidemia, characterized by elevated levels of low-density lipoprotein cholesterol and triglycerides, along with reduced high-density lipoprotein cholesterol, putting them at Increased rlSk for cardiovascular disease",
        "output": "The patient has hi h cholesterol with too much of the 'bad' kind and triglycerides, and not enough of the 'good' kind. This increases the risk of heart problems.",
    },
]

example_prompt = PromptTemplate(
    input_variables=["input", "output"], template="{input}\n{output}"
)

# """
# The patient presented with acute exacerbation of chronic obstructive pulmonary disease, manifesting symptoms such as dyspnea, increased respiratory rate, and use of accessory muscles for breathing.
# The patient is having a sudden worsening of chronic lung disease. This shows with difficulty breathing, faster breathing, and using extra muscles to breathe.
# """
# myprompt = example_prompt.format(**examples[0])
# print(myprompt)


prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="{myinput}",
    input_variables=["myinput"],
)

myprompt = prompt.format(
    myinput="The patient has been diagnosed with hypertension, evidenced by consistently elevated blood pressure readings, indicating s!stained systolic and diastolic pressures above the normal range."
)

# """"
# My Prompt:  The patient presented with acute exacerbation of chronic obstructive pulmonary disease, manifesting symptoms such as dyspnea, increased respiratory rate, and use of accessory muscles for breathing.
# The patient is having a sudden worsening of chronic lung disease. This shows with difficulty breathing, faster breathing, and using extra muscles to breathe.

# patient is experiencing hyperlipidemia, characterized by elevated levels of low-density lipoprotein cholesterol and triglycerides, along with reduced high-density lipoprotein cholesterol, putting them at Increased rlSk for cardiovascular disease
# The patient has hi h cholesterol with too much of the 'bad' kind and triglycerides, and not enough of the 'good' kind. This increases the risk of heart problems.


# The patient has been diagnosed with hypertension, evidenced by consistently elevated blood pressure readings, indicating s!stained systolic and diastolic pressures above the normal range.
# """
# print("My Prompt: ", myprompt)

response = llm.invoke(myprompt)

"""
Response: This puts the patient at increased risk for cardiovascular complications .
The patient has high blood pressure, with readings consistently above the normal range. This increases the risk of cardiovascular problems.
"""
print("Response: ", response)
