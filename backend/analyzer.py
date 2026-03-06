import os
from openai import AsyncOpenAI
from models import AnalyticsData

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def build_prompt(analytics: AnalyticsData, user_idea: str | None) -> str:
    videos_summary = "\n".join([
        f"  - {v.title or 'Untitled'}: {v.views:,} views, {v.likes:,} likes"
        for v in analytics.videos[:10]
    ])

    prompt = (
        "You are an expert TikTok content strategist. "
        "Analyze the following account analytics and provide concrete, actionable recommendations.\n\n"
        "## Account Analytics (Last 7 days)\n"
        f"- Total Views: {analytics.total_views:,}\n"
        f"- Followers: {analytics.followers:,}\n"
        f"- Total Likes: {analytics.likes:,}\n"
        f"- Comments: {analytics.comments:,}\n"
        f"- Shares: {analytics.shares:,}\n\n"
        "## Recent Video Performance\n"
        f"{videos_summary}\n\n"
        "## Posting Times\n"
        f"{', '.join(analytics.posting_times) if analytics.posting_times else 'No data'}\n\n"
        "## Your Task\n"
        "1. Summarize key performance trends in 3 bullet points\n"
        "2. Identify what content is working and WHY (be specific)\n"
        "3. Recommend the next 3 content ideas with specific posting times\n"
        "4. Identify 1-2 things to stop or change\n"
    )

    if user_idea:
        prompt += (
            "\n## Creator's Idea to Evaluate\n"
            f'The creator is considering: "{user_idea}"\n\n'
            "Please evaluate this idea against the analytics data and suggest specific optimizations.\n"
        )

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
