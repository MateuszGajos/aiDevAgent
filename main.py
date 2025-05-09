from fastapi import FastAPI
import requests
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

# Nowy kod do wywołania narzędzi i odpowiedzi agenta
@app.post("/run_agent")
def run_agent():
    # Wywołanie tool1
    tool1_response = requests.post("https://twoja-aplikacja.com/tool1", json={"input": "data"})
    team_members = tool1_response.json().get("output")

    # Wywołanie tool2
    tool2_response = requests.post("https://twoja-aplikacja.com/tool2", json={"input": "data"})
    university_and_sponsor = tool2_response.json().get("output")

    # Łączenie danych
    answer = f"{university_and_sponsor}, zespół: {team_members}"

    return {"action": "answer", "value": answer}
