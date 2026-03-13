"""
Unit tests for Pydantic data models (models.py)
Tests run without OpenAI API key — no external calls needed.
"""
import sys
import os
import pytest

# Add backend directory to path so we can import models
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from models import VideoData, AnalyticsData, StrategyRequest


class TestVideoData:
      """Tests for VideoData model"""

    def test_valid_video_data(self):
              video = VideoData(title="Test video", views=10000, likes=500)
              assert video.title == "Test video"
              assert video.views == 10000
              assert video.likes == 500
              assert video.watch_time is None

    def test_video_data_with_watch_time(self):
              video = VideoData(title="Tutorial", views=50000, likes=2000, watch_time=35.5)
              assert video.watch_time == 35.5

    def test_video_data_requires_title(self):
              with pytest.raises(Exception):
                            VideoData(views=100, likes=10)

          def test_video_data_requires_views(self):
                    with pytest.raises(Exception):
                                  VideoData(title="Test", likes=10)

                def test_video_data_requires_likes(self):
                          with pytest.raises(Exception):
                                        VideoData(title="Test", views=100)


class TestAnalyticsData:
      """Tests for AnalyticsData model"""

    def _make_video(self):
              return VideoData(title="Video", views=1000, likes=50)

    def test_valid_analytics_data(self):
              analytics = AnalyticsData(
                            total_views=100000,
                            followers=5000,
                            likes=8000,
                            comments=200,
                            shares=150,
                            videos=[self._make_video()],
                            posting_times=["19:00", "21:00"],
              )
              assert analytics.total_views == 100000
              assert analytics.followers == 5000
              assert len(analytics.videos) == 1
              assert len(analytics.posting_times) == 2

    def test_analytics_with_multiple_videos(self):
              videos = [VideoData(title=f"Video {i}", views=i * 1000, likes=i * 50) for i in range(1, 4)]
              analytics = AnalyticsData(
                  total_views=6000,
                  followers=1000,
                  likes=300,
                  comments=50,
                  shares=30,
                  videos=videos,
                  posting_times=["20:00"],
              )
              assert len(analytics.videos) == 3

    def test_analytics_empty_posting_times(self):
              analytics = AnalyticsData(
                            total_views=0,
                            followers=0,
                            likes=0,
                            comments=0,
                            shares=0,
                            videos=[],
                            posting_times=[],
              )
              assert analytics.posting_times == []


class TestStrategyRequest:
      """Tests for StrategyRequest model"""

    def _make_analytics(self):
              video = VideoData(title="Test", views=5000, likes=200)
              return AnalyticsData(
                  total_views=5000,
                  followers=300,
                  likes=200,
                  comments=20,
                  shares=10,
                  videos=[video],
                  posting_times=["19:00"],
              )

    def test_strategy_request_without_user_idea(self):
              req = StrategyRequest(analytics=self._make_analytics())
              assert req.user_idea is None

    def test_strategy_request_with_user_idea(self):
              req = StrategyRequest(
                            analytics=self._make_analytics(),
                            user_idea="I want to make a tutorial about Python",
              )
              assert req.user_idea == "I want to make a tutorial about Python"

    def test_strategy_request_requires_analytics(self):
              with pytest.raises(Exception):
                            StrategyRequest()


class TestHealthEndpoint:
      """Tests for FastAPI health endpoint (no OpenAI needed)"""

    def test_health_endpoint(self):
              from fastapi.testclient import TestClient
              from main import app

        client = TestClient(app)
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
