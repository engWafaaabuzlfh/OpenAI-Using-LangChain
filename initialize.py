from langchain_openai import OpenAI
from langchain_classic.chains import LLMChain
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

from prompt import SYSTEM_INSTRUCTIONS

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def prompt_template(system_instruction: str):
    prompt = PromptTemplate.from_template(
        f"{system_instruction}\n\n"
    )
    return prompt

def llm_chain(prompt: PromptTemplate):
    llm = OpenAI(model="gpt-3.5-turbo",
                temperature=0.7, 
                openai_api_key=OPENAI_API_KEY
                )
    prompt = prompt
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain


