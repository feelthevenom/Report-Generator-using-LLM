from langchain.prompts import PromptTemplate

# Prompt template for task summarization
TASK_SUMMARIZATION_TEMPLATE = """Write a concise task summary for the daily work report based on the following description: {description}. 

Guidelines:
- The summary should be professional, direct, and no more than 30 words.
- Include specific tools or steps relevant to the task (e.g., VSCode, Git, Docker, Anaconda).
- For brief descriptions, infer and include relevant subtasks.
- For detailed descriptions, condense the information.
- Do not use bullet points or other formatting; the summary should be a single paragraph or sentence.

Provide only the summary without any additional text or explanations."""

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


"""
10 Mon: Received laptop is setup by installing all tools and dependency for coding
11 Tue: Meeting with Dr. Gowthama and task has been assigned to build a simulation for single stage of SwaT stage after this i started manually understanding the the cycle of the system to build and simulate the process for the single stage.
12 Wed: EDA for the stages by cleaning the raw data and removing outliers and finding the annomly state and thresholds of each components in SWaT dataset sensors and actuators
13 Thu: Created new environment and started building the application by coding, created the function to autometically generate value from a range for all the senors and actuator in the SWaT first stage.
14 Fri: Started to automate the process over a timestamp but thigs are messed up by generating random values and non related to each component, so created another function that makes relationship between each component so i written a manual program which has relationship with each other but encouter too much logical error which leads the tank over flow in the stage1.
15 Sat: Weekend
16 Sun: Weekend
17 Mon: Verified the code once again to start and tryed to resolve the error which made previously that i missed to add threshold value and now the tank is not overflowed as next i added logic for the pump to outflow the water inside the tank
18 Tue: writen a code to visualize the the processes using matplot for easy implement and also added graph to verify the cycle to cross validate with original data
19 Wed: the generated value is stored in a csv file rather than priniting to use the data to train the machine learning model and once again ran the entire model to see the result and pushed to github and cleaned the code for modular coding
20 Thu:  I don't know please fill it based on previous day and make elaborate
21 Fri: I don't know please fill it based on previous day and make elaborate
22 Sat: Weekend
23 Sun: Weekend
24 Mon: Had meeting with Dr. Gowthama and showed the application we both me and gugan have done and next task is assigned to search the related to water treatment plant stages same as SWaT testbed which is open source and i started searching but the result i can't able to get proper detail
25 Tue: I used AI tool to build a complete plant as Pundi discussed about sewage water treatement plant for canada clients so i started building a complete sewage water treatment plant process by gathering all detals from AI including all the sensors and actuators and its connect
26 Wed: I manully drawn the all the stages with connection using HTML to understand the flow and process
27 Thu: The process which is done for SWaT stage 1 is repeated by anlyzing the stage 1 on both and verified both are looks same but there three aditional sensors which is GM101, SM101 and TURB101 so i used to manually set there value because these sensors values cannont determined these are done by jupyter notebook.
28 Fri: Created new environment for the sewage water treatment to simulated and repeated the process of stage 1 from SWaT to this sewage with the new additional component and its wored but the values are irrelevant so still need to figure out logic to meaning full value.

"""