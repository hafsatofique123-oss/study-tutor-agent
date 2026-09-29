from crewai import Agent, Crew, Task, Process, Memory

from config import get_llm
from tools import calculator, create_study_plan


def create_study_tutor():
    """Create the Study Tutor Agent and its memory."""

    llm = get_llm()

    memory = Memory(
        llm=llm,
        embedder={
            "provider": "huggingface",
            "config": {
                "model_name": "sentence-transformers/all-MiniLM-L6-v2"
            },
        },
    )

    study_tutor = Agent(
        role="Study Tutor Agent",

        goal=(
            "Help students understand academic topics clearly, "
            "adapt explanations to their level, provide examples, "
            "encourage practice, and give useful feedback."
        ),

        backstory=(
            "You are a patient and supportive academic tutor. "
            "You explain difficult concepts in simple language. "
            "You adapt your explanations to the student's level "
            "and encourage students to understand concepts instead "
            "of simply memorizing answers."
        ),

        llm=llm,

        tools=[
            calculator,
            create_study_plan,
        ],

        memory=memory,

        verbose=True,

        allow_delegation=False,
    )

    return study_tutor, memory


def run_study_tutor(
    study_tutor,
    memory,
    subject,
    level,
    question,
):
    """Run the Study Tutor Agent."""

    study_task = Task(
        description=f"""
        Help the student with this request.

        Subject:
        {subject}

        Student Level:
        {level}

        Student Question:
        {question}

        Instructions:

        - Explain the topic according to the student's level.
        - Use simple and clear language.
        - Give an example when useful.
        - Explain difficult terminology.
        - Highlight important points.
        - Use the Calculator Tool for calculations.
        - Use the Study Plan Tool when a study plan is requested.
        - Use relevant previous memory when available.
        - Encourage active learning.
        - Do not unnecessarily make the answer complicated.

        Format the response using these sections when appropriate:

        ## Explanation

        ## Example

        ## Key Points

        ## Practice
        """,

        expected_output=(
            "A clear, accurate and student-friendly educational response."
        ),

        agent=study_tutor,
    )

    crew = Crew(
        agents=[study_tutor],
        tasks=[study_task],
        process=Process.sequential,
        memory=memory,
        verbose=True,
    )

    result = crew.kickoff()

    return result
