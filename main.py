from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RequestData(BaseModel):
    input: str

@app.post("/")
def use_tool(data: RequestData):
    if data.input.startswith("test"):
        return {"output": data.input}

    # Przykład: zwraca listę członków zespołu badawczego
    return {"output": "dr Anna Kowalska, prof. Jan Nowak, mgr Tomasz Zieliński"}
