import streamlit as st
from langchain.llms import Ollama
from prompts.task_summarization import get_task_summarization_prompt
from config.settings import LLM_MODEL

@st.cache_resource
def get_llm():
    """
    Initialize and cache LLM model
    
    Returns:
        Ollama or None: Initialized LLM model or None if initialization fails
    """
    try:
        return Ollama(model=LLM_MODEL)
    except Exception as e:
        st.error(f"Error initializing LLM: {e}")
        return None

def summarize_task(description):
    """
    Summarize a task description using the LLM
    
    Args:
        description (str): Task description to summarize
        
    Returns:
        str: Summarized task description, or original if summarization fails
    """
    llm = get_llm()
    if not llm or not description:
        return description
        
    try:
        prompt = get_task_summarization_prompt()
        summarize_chain = prompt | llm
        summary = summarize_chain.invoke({"description": description})
        return summary.strip()
    except Exception as e:
        st.warning(f"Error summarizing task: {e}")
        return description  # Fallback to original description