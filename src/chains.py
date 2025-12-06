from langchain_core.output_parsers import StrOutputParser
from .config import get_llm
from .prompts import get_chat_prompt

_llm = None
_chain = None

def get_chat_chain():
    global _llm, _chain
    if _chain is None:
        _llm = get_llm()
        prompt = get_chat_prompt()
        _chain = prompt | _llm | StrOutputParser()
    return _chain

def ask_gemini(user_input: str) -> str:
    chain = get_chat_chain()
    return chain.invoke({"user_input": user_input})
