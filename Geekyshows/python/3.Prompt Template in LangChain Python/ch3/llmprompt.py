from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from decouple import config

SECRET_KEY = config("OPENAI_API_KEY")
llm = OpenAI(api_key=SECRET_KEY)

# LLMs - Prompt Template

# Example 1 - Prompt having No Input Variable
no_input_prompt = PromptTemplate(input_variables=[], template="Tell me a Python Trick")
# no_input_prompt = PromptTemplate.from_template("Tell me a Python Trick")

# # input_variables=[] input_types={} partial_variables={} template='Tell me a Python Trick'
# print(no_input_prompt)

formatted_no_input_prompt = no_input_prompt.format()

# # No Input Prompt:  Tell me a Python Trick
# print("No Input Prompt: ", formatted_no_input_prompt)

response = llm.invoke(formatted_no_input_prompt)

"""
response:
One Python trick is to use list comprehension to create a list with a conditional statement. For example, you can create a list of even numbers from 1 to 10 using the code:

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

This will print the list [2, 4, 6, 8, 10]. This is a more concise and efficient way of creating a list compared to using a for loop and if statement.
"""
print("response: ", response)


# # Example 2 - Prompt having One Input Variable
# one_input_prompt = PromptTemplate(
#     input_variables=["language"], template="Tell me a {language} Trick"
# )
# # one_input_prompt = PromptTemplate.from_template("Tell me a {language} Trick")

# # # input_variables=['language'] input_types={} partial_variables={} template='Tell me a {language} Trick'
# # print(one_input_prompt)

# formatted_one_input_prompt = one_input_prompt.format(language="Javascript")

# # # One Input Prompt:  Tell me a Javascript Trick
# # print("One Input Prompt: ", formatted_one_input_prompt)

# response = llm.invoke(formatted_one_input_prompt)

# """
# response:

# One Javascript trick is using the spread operator to easily combine arrays. This can be done by using three dots (...) in front of an array variable when passing it as an argument to a function or when creating a new array. For example:

# ```
# let array1 = [1, 2, 3];
# let array2 = [4, 5, 6];
# let combinedArray = [...array1, ...array2]; // [1, 2, 3, 4, 5, 6]
# ```

# This can also be used to clone an array, instead of using the `slice()` method:

# ```
# let originalArray = [1, 2, 3];
# let cloneArray = [...originalArray]; // [1, 2, 3]
# ```

# The spread operator can also be used to pass elements of an array as arguments to a function:

# ```
# let numbers = [1, 2, 3];
# function sum(a, b, c) {
#   return a + b + c;
# }
# let result = sum(...numbers); // 6
# ```
# """
# print("response: ", response)


# # Example 3 - Prompt having Multiple Input Variable
# multiple_input_prompt = PromptTemplate(
#     input_variables=["language", "topic"], template="Tell me a {language} {topic} Trick"
# )
# # multiple_input_prompt = PromptTemplate.from_template("Tell me a {language} {topic} Trick")

# # # input_variables=['language'] input_types={} partial_variables={} template='Tell me a {language} Trick'
# # print(multiple_input_prompt)

# formatted_multiple_input_prompt = multiple_input_prompt.format(
#     language="C Programming", topic="function"
# )

# # # Multiple Input Prompt:  Tell me a Javascript Trick
# # print("Multiple Input Prompt: ", formatted_multiple_input_prompt)

# response = llm.invoke(formatted_multiple_input_prompt)
# print("response: ", response)


# # Example 4 - PromptTemplate - No input variable manually
# template = "Tell me a {language} {topic} Trick"
# prompt_template = PromptTemplate.from_template(template)
# # Prompt Template:  input_variables=['language', 'topic'] input_types={} partial_variables={} template='Tell me a {language} {topic} Trick
# print("Prompt Template: ", prompt_template)
# # Prompt Template:  ['language', 'topic']
# print("Prompt Template: ", prompt_template.input_variables)

# formatted_prompt_template = prompt_template.format(language="python", topic="array")
# print("Formatted Prompt Template: ", formatted_prompt_template)

# response = llm.invoke(formatted_prompt_template)
# print("response: ", response)
