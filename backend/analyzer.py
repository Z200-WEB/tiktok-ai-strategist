import os
from openai import AsyncOpenAI
from models import AnalyticsData

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def build_prompt(analytics: AnalyticsData, user_idea: str | None) -> str:
      videos_summary = "\n".join([
                f"  - {v.title or 'Untitled'}: {v.views:,} views, {v.likes:,} likes"
                for v in analytics.videos[:10]
      ])

    prompt = f"""
    You are an expert TikTok content strategist. Analyze the following account analytics and provide concrete, actionable recommendations.

    ## Account Analytics (Last 7 days)
    - Total Views: {analytics.total_views:,}
    - Followers: {analytics.followers:,}
    - Total Likes: {analytics.likes:,}
    - Comments: {analytics.comments:,}
    - Shares: {analytics.shares:,}

    ## Recent Video Performance
    {videos_summary}

    ## Posting Times
    {', '.join(analytics.posting_times) if analytics.posting_times else 'No data'}

    ## Your Task
    1. Summarize key performance trends in 3 bullet points
    2. Identify what content is working and WHY (be specific)
    3. Recommend the next 3 content ideas with specific posting times
    4. Identify 1-2 things to stop or change
    """

    if user_idea:
              prompt += f"""
              ## Creator's Idea to Evaluate
              The creator is considering: "{user_idea}"

Please evaluate this idea against the analytics data and suggest specific optimizations.
"""

    prompt += "\nRespond in clear, direct language. Be specific with data when possible."
    return prompt


    async def generate_strategy(analytics: AnalyticsData, user_idea: str | None) -> str:
        prompt = build_prompt(analytics, user_idea)

            response = await client.chat.completions.create(
                    model="gpt-4o",
                            messages=[
                                        {
                                                        "role": "system",
                                                                        "content": "You are a data-driven TikTok content strategist. You give specific, actionable advice based on performance data."
            },
                        {
                                        "role": "user",
                                                        "content": prompt
                                                                    }
                                                                            ],
                                                                                    temperature=0.7,
                                                                                            max_tokens=1000,
                                                                                                )

                                                                                                    return response.choices[0].message.content
                                                                                                    
