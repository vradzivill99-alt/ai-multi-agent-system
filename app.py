import os
from fastapi import FastAPI
from pydantic import BaseModel

from agents.planner import plan_task
from agents.retriever import retrieve_data
from agents.executor import execute_task
from memory.memory import save_memory

app = FastAPI()

class Task(BaseModel):
    query: str

@app.post("/run-agent")
def run_agent(task: Task):
    plan = plan_task(task.query)
    data = retrieve_data(task.query)
    result = execute_task(plan, data)
    
    save_memory(task.query, result)

    return {
        "plan": plan,
        "data": data,
        "result": result
    }
