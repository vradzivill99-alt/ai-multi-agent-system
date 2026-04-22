def retrieve_data(query: str):
    # simple mock RAG
    knowledge = [
        "AI automation reduces costs",
        "RAG improves context accuracy",
        "Agents can automate workflows"
    ]

    relevant = [k for k in knowledge if query.lower() in k.lower()]
    return relevant if relevant else knowledge
