from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import StrategyRequest
from analyzer import generate_strategy

app = FastAPI(title="TikTok AI Strategist", version="1.0.0")

app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],
      allow_methods=["*"],
      allow_headers=["*"],
)


@app.post("/analyze")
async def analyze(request: StrategyRequest):
      strategy = await generate_strategy(
                analytics=request.analytics,
                user_idea=request.user_idea
      )
      return {"strategy": strategy}


@app.get("/health")
def health():
      return {"status": "ok"}
  
