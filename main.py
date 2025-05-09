from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RequestData(BaseModel):
    input: str

@app.post("/tool1")
def tool1(data: RequestData):
    if data.input.startswith("test"):
        return {"output": data.input}
    return {"output": "dr Anna Kowalska, prof. Jan Nowak, mgr Tomasz Zieliński"}

@app.post("/tool2")
def tool2(data: RequestData):
    if data.input.startswith("test"):
        return {"output": data.input}
    return {"output": "Politechnika Warszawska, sponsor: FutureTech Foundation"}

@app.get("/")
def root():
    return {"message": "health check 🚀"}
