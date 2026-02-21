def create_study_plan(topic: str, days: int = 7) -> str:
    topic_lower = topic.lower()

    # Topic-specific modules
    if "python" in topic_lower:
        modules = [
            "Python basics and syntax",
            "Control flow and functions",
            "Data structures (lists, dicts, sets)",
            "File handling and exceptions",
            "Object-oriented programming",
            "Libraries (NumPy, pandas)",
            "Mini project"
        ]
    elif "machine learning" in topic_lower:
        modules = [
            "ML concepts and workflow",
            "Data preprocessing",
            "Supervised learning models",
            "Model evaluation",
            "Unsupervised learning",
            "Neural networks basics",
            "Mini project"
        ]
    else:
        modules = [
            "Core concepts",
            "Key terminology",
            "Practical exercises",
            "Applications",
            "Common challenges",
            "Advanced topics",
            "Mini project"
        ]

    plan = f"{days}-day study plan for {topic}:\n\n"

    for day in range(days):
        module = modules[day % len(modules)]
        plan += f"Day {day+1}: {module}\n"
        plan += "  • Study theory\n"
        plan += "  • Practice exercises\n"
        plan += "  • Review notes\n\n"

    plan += "Final step: Build a small project and review all concepts."

    return plan