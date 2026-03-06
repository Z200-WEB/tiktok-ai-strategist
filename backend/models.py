from pydantic import BaseModel
from typing import Optional


class VideoData(BaseModel):
      title: str
      views: int
      likes: int
      watch_time: Optional[float] = None


class AnalyticsData(BaseModel):
      total_views: int
      followers: int
      likes: int
      comments: int
      shares: int
      videos: list[VideoData]
      posting_times: list[str]


class StrategyRequest(BaseModel):
      analytics: AnalyticsData
      user_idea: Optional[str] = None
  
