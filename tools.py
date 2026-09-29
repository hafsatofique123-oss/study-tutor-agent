from crewai.tools import tool


@tool("Calculator Tool")
def calculator(expression: str) -> str:
    """
    Calculate a basic mathematical expression.

    Use this tool when the student asks for a mathematical
    calculation or when an exact calculation is needed.
    """

    try:
        allowed_characters = "0123456789+-*/().% "

        if not all(character in allowed_characters for character in expression):
            return "The expression contains unsupported characters."

        result = eval(expression, {"__builtins__": {}}, {})

        return f"Calculation result: {result}"

    except Exception:
        return "I could not calculate that expression."


@tool("Study Plan Tool")
def create_study_plan(topic: str, days: int) -> str:
    """
    Create a simple study plan for a topic.

    Use this when the student asks for a study schedule,
    revision plan, or preparation plan.
    """

    if days < 1:
        return "The number of days must be at least 1."

    if days > 30:
        return "Please create a study plan for 30 days or fewer."

    plan = []

    for day in range(1, days + 1):
        if day == 1:
            activity = "Learn the basic concepts."
        elif day == days:
            activity = "Review the topic and test yourself."
        else:
            activity = "Study the topic and practice what you learned."

        plan.append(f"Day {day}: {activity}")

    return f"Study plan for {topic}:\n" + "\n".join(plan)
