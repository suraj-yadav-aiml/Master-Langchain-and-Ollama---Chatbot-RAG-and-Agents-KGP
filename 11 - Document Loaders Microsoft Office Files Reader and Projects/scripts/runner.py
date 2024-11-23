from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from .llm import get_llama
from .prompts import system_prompt, human_prompt


messages = [system_prompt, human_prompt]

template = ChatPromptTemplate.from_messages(messages=messages)

llm = get_llama()

qna_chain = template | llm | StrOutputParser()

def ask_llm(context, question):
    return qna_chain.invoke(
        {
            'context': context,
            'question': question
        }
    )