```python
from crewai import Agent, Crew, Task, Process

from config import get_llm
from tools import calculator, create_study_plan


def create_study_tutor():
    """Create the Study Tutor Agent."""

    llm = get_llm()

    study_tutor = Agent(
        role="Study Tutor Agent",

        goal=(
            "Help students understand academic topics clearly, "
            "adapt explanations to their learning level, "
            "provide useful examples, create study plans, "
            "and encourage active learning."
        ),

        backstory=(
            "You are a patient and supportive academic tutor. "
            "You explain difficult concepts in simple language. "
            "You adapt explanations to the student's level. "
            "You use examples and practice questions to help "
            "students understand concepts instead of memorizing them."
        ),

        llm=llm,

        tools=[
            calculator,
            create_study_plan,
        ],

        verbose=False,

        allow_delegation=False,
    )

    return study_tutor


def run_study_tutor(
    study_tutor,
    subject,
    level,
    question,
    conversation_history=None,
):
    """Run the Study Tutor Agent with conversation context."""

    if conversation_history is None:
        conversation_history = []

    previous_context = ""

    if conversation_history:

        previous_context = "\n\nPrevious conversation:\n"

        for item in conversation_history[-6:]:

            previous_context += (
                f"Student: {item['question']}\n"
                f"Tutor: {item['answer']}\n\n"
            )

    study_task = Task(
        description=f"""
You are helping a student learn.

Subject:
{subject}

Student Learning Level:
{level}

Current Student Question:
{question}

{previous_context}

Instructions:

1. Answer the student's current question directly.
2. Adapt the explanation to the student's level.
3. Use simple and clear language.
4. Explain difficult terminology.
5. Give examples when useful.
6. Use the Calculator Tool when calculations are required.
7. Use the Study Plan Tool when the student requests a study plan.
8. Use previous conversation context when it is relevant.
9. Encourage active learning.
10. Do not unnecessarily make the answer complicated.
11. Do not invent facts.
12. If the question is unclear, explain what information is needed.

When appropriate, structure the response using:

## Explanation

## Example

## Key Points

## Practice

Only include sections that are useful for the question.
""",

        expected_output=(
            "A clear, accurate, concise and student-friendly "
            "educational response."
        ),

        agent=study_tutor,
    )

    crew = Crew(
        agents=[study_tutor],
        tasks=[study_task],
        process=Process.sequential,
        verbose=False,
    )

    result = crew.kickoff()

    return str(result)
```


