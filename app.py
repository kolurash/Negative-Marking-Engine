from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Negative Marking Engine",
    description="Backend API to calculate scores with negative marking.",
    version="1.0.0"
)


class ScoreRequest(BaseModel):
    correct: int
    wrong: int


@app.get("/")
def home():
    return {
        "message": "Welcome to the Negative Marking Engine API"
    }


@app.post("/calculate-score")
def calculate_score(data: ScoreRequest):

    if data.correct < 0 or data.wrong < 0:
        raise HTTPException(
            status_code=400,
            detail="Values cannot be negative"
        )

    final_score = data.correct - (data.wrong * 0.25)

    return {
        "final_score": final_score
    }