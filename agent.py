from crewai import Agent, Crew, Task, Process, Memory

from config import get_llm
from tools import calculator, create_study_plan


def create_memory(llm):
    """Create memory for the Study Tutor Agent."""

    return Memory(
        llm=llm,
        embedder={
            "provider": "huggingface",
            "config": {
                "model_name": "sentence-transformers/all-MiniLM-L6-v2"
            },
        },
    )


def create_study_tutor():
    """Create the Study Tutor Agent."""

    llm = get_llm()

    memory = create_memory(llm)

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


def create_study_crew(student_input):
    """Create the CrewAI crew for one study request."""

    study_tutor, memory = create_study_tutor()

    study_task = Task(
        description=f"""
        Help the student with the following request:

        Subject:
        {student_input["subject"]}

        Student Level:
        {student_input["level"]}

        Student Question:
        {student_input["question"]}

        Follow these rules:

        1. Explain the concept according to the student's level.
        2. Use simple and clear language.
        3. Give a practical or academic example when useful.
        4. Highlight the most important points.
        5. If the student asks for a calculation, use the Calculator Tool.
        6. If the student asks for a study plan, use the Study Plan Tool.
        7. If relevant, give a few practice questions.
        8. If previous memory is relevant, use it to personalize
           the explanation.
        9. Do not make the explanation unnecessarily complicated.
        10. Encourage the student to think and learn.

        Structure your response as:

        ## Explanation

        ## Example

        ## Key Points

        ## Practice

        Only include sections that are useful for the student's request.
        """,

        expected_output=(
            "A clear, accurate, student-friendly educational response "
            "with explanations, examples, key points, and practice "
            "when appropriate."
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

    return crew
