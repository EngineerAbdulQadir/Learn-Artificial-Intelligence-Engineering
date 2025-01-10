

# LangChain Series - Class 03

## **Introduction**

Welcome to the third class of the LangChain Series! In this session, we will focus on **Prompt Engineering and working with Large Language Models (LLMs)** using **LangChain**. By the end of this class, you'll have a deeper understanding of how to structure prompts effectively and interact with models such as OpenAI through LangChain.

---

## **Step 1: Basic Prompt Setup**

We start by creating a basic **PromptTemplate** and using it to structure prompts. Below is the code for defining a financial advisor prompt:

```python
import os
from langchain import PromptTemplate

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

# Define the prompt template
demo_template = '''I want you to act as a financial advisor for people.
In an easy way, explain the basics of {financial_concept}.'''

# Create the prompt
prompt = PromptTemplate(
    input_variables=['financial_concept'],
    template=demo_template
)

# Test the prompt with a financial concept
print(prompt.format(financial_concept='income tax'))
```

---

## **Step 2: Using OpenAI Model with LangChain**

Next, we integrate **LangChain** with **OpenAI's LLM** to process the input and return the result. Here's the code to initiate the OpenAI model and use the prompt template created earlier:

```python
from langchain.llms import OpenAI
from langchain.chains import LLMChain

# Initialize the OpenAI model with a specified temperature for creativity
llm = OpenAI(temperature=0.7)

# Create a chain to process the prompt using the OpenAI model
chain1 = LLMChain(llm=llm, prompt=prompt)

# Run the chain with an example input
print(chain1.run('GDP'))
```

---

## **Step 3: Language Translation with LangChain**

In this step, we will demonstrate how to build a **language translation** chain using LangChain's **PromptTemplate**.

```python
from langchain import PromptTemplate

# Define the translation prompt template
template = '''In an easy way translate the following sentence '{sentence}' into {target_language}'''
language_prompt = PromptTemplate(
    input_variables=["sentence", "target_language"],
    template=template,
)

# Format the prompt with a sentence and target language
print(language_prompt.format(sentence="How are you", target_language='hindi'))
```

Next, use LangChain to process the translation:

```python
from langchain.chains import LLMChain

# Create a chain for language translation
chain2 = LLMChain(llm=llm, prompt=language_prompt)

# Translate a sentence
print(chain2({'sentence': "Hello How are you", 'target_language': 'hindi'}))
```

---

## **Step 4: Using Few-Shot Learning in LangChain**

LangChain allows for **Few-Shot Learning**, where we provide a few examples for the model to learn from. Here's how you can create a few-shot prompt template:

```python
from langchain import PromptTemplate, FewShotPromptTemplate

# Define a few-shot learning example
examples = [
    {"word": "happy", "antonym": "sad"},
    {"word": "tall", "antonym": "short"},
]

# Define the prompt template for few-shot learning
example_formatter_template = """Word: {word}
Antonym: {antonym}
"""

example_prompt = PromptTemplate(
    input_variables=["word", "antonym"],
    template=example_formatter_template,
)

# Create a FewShotPromptTemplate
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Give the antonym of every input\n",
    suffix="Word: {input}\nAntonym: ",
    input_variables=["input"],
    example_separator="\n",
)

# Test the few-shot prompt
print(few_shot_prompt.format(input='big'))
```

---

## **Step 5: Running Few-Shot Prompt with LangChain**

Once the few-shot prompt template is created, you can integrate it into an **LLMChain** to generate the output:

```python
# Create an LLMChain with the few-shot prompt
chain = LLMChain(llm=llm, prompt=few_shot_prompt)

# Run the chain to get the antonym of a word
print(chain({'input': "big"}))
```

---

## **Conclusion**

In this class, we learned the fundamentals of **Prompt Engineering** and how to work with **Large Language Models (LLMs)** using **LangChain**. We covered a variety of use cases including financial advisory, language translation, and few-shot learning for generating antonyms. These techniques can be applied to various natural language processing tasks to build intelligent and dynamic applications with LangChain.