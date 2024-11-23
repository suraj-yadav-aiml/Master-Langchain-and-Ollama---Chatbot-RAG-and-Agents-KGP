from langchain_core.prompts import (SystemMessagePromptTemplate,
                                    HumanMessagePromptTemplate,)


# system_prompt = SystemMessagePromptTemplate.from_template("""You are a AI assistant with the following key guidelines:

# 1. Answer ONLY based on the provided context
# 2. Prioritize accuracy and relevance over verbosity
# 3. Structure your answer for maximum clarity:
#    - Use direct language
#    - Break down complex information
#    - Highlight key points
#    - Avoid speculation or external knowledge

# Context-driven response is mandatory""")

# human_prompt = HumanMessagePromptTemplate("""Instructions:
# - Carefully read and analyze the provided context
# - Extract ONLY relevant information
# - Construct your answer using ONLY the information within this context

# ### Context:
# ```{context}```

# ### Question:
# ```{question}```

# ### Structured Answer Requirements:
# - Use clear, direct language
# - Cite context references if possible
# - Format for readability

# ### Answer:""")

system_prompt = SystemMessagePromptTemplate.from_template("""You are helpful AI assistant who answer user question based on the provided context.""")

human_prompt = HumanMessagePromptTemplate.from_template("""Answer user question based on the provided context ONLY! If you do not know the answer, just say "I don't know".
            ### Context:
            ```{context}```

            ### Question:
            ```{question}```

            ### Answer:""")