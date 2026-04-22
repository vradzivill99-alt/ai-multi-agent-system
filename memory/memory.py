memory_store = []

def save_memory(query, result):
    memory_store.append({
        "query": query,
        "result": result
    })

def get_memory():
    return memory_store
