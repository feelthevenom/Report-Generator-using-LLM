from langchain.prompts import PromptTemplate

# Prompt template for task summarization
TASK_SUMMARIZATION_TEMPLATE = """Summarize the following work description into a concise task that reflects an 8-hour effort.

Format requirements:
- For brief descriptions: Expand into a 3-4 line summary (max 30 words) with inferred subtasks
- For detailed descriptions: Condense into a 1-2 line summary (max 30 words)
- Include specific tools/steps relevant to the task (e.g., for coding: VSCode, Git, Docker, Anaconda)
- Use a professional, direct tone
- Avoid introductory phrases and unnecessary details like here is the summary
- Avoid format like *bullet points* or [brackets]
- Avoid lines and points make it a paragraph or single line
- The summary is for my daily work report and should be concise and professional.

Work description: {description}"""

def get_task_summarization_prompt():
    """
    Get the PromptTemplate for task summarization
    
    Returns:
        PromptTemplate: The task summarization prompt template
    """
    return PromptTemplate(
        input_variables=["description"],
        template=TASK_SUMMARIZATION_TEMPLATE
    )