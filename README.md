# TikTok AI Strategist 🎯

> **Your personal AI content strategist for TikTok — built from real experience.**
>
> [![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
> [![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green?logo=fastapi)](https://fastapi.tiangolo.com)
> [![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-orange?logo=openai)](https://openai.com)
> [![Chrome Extension](https://img.shields.io/badge/Chrome-Extension-yellow?logo=googlechrome)](https://developer.chrome.com/docs/extensions)
>
> ---
>
> ## 💡 Background
>
> I grew my TikTok account to **300K+ views per video** by using AI to analyze my content performance and refine my strategy.
>
> The original workflow was manual — I would open TikTok Analytics, copy the data, paste it into Claude, wait for analysis, then combine the insights with my own ideas to decide the next post. It worked, but it was slow.
>
> This tool **automates that entire workflow**:
>
> | Before | After |
> |---|---|
> | Manually copy-pasting analytics (~30 min) | One click — done in seconds |
> | Subjective interpretation of data | AI-driven pattern recognition |
> | Ideas developed in isolation | Ideas validated against real performance data |
>
> ---
>
> ## 🚀 Features
>
> - **Auto Data Extraction** — Reads your TikTok Analytics page directly via Chrome Extension (no copy-paste needed)
> - - **AI-Powered Analysis** — Sends structured data to GPT-4o for deep performance analysis
>   - - **Strategy Generation** — Returns concrete next-post recommendations with posting times
>     - - **Idea Collaboration** — Input your own content ideas and get instant AI feedback
>      
>       - ---
>
> ## 🛠 Tech Stack
>
> | Layer | Technology |
> |---|---|
> | Chrome Extension | JavaScript (Manifest V3), Chrome Extensions API |
> | Backend | Python 3.11, FastAPI |
> | AI | OpenAI API (GPT-4o) |
> | Data Modeling | Pydantic |
> | Data Source | TikTok Analytics DOM scraping |
>
> ---
>
> ## 📐 Architecture
>
> ```
> TikTok Analytics Page (Chrome)
>         ↓  content.js reads DOM
> Chrome Extension Popup (popup.js)
>         ↓  HTTP POST /analyze
> FastAPI Backend (main.py)
>         ↓  builds prompt
> analyzer.py → OpenAI GPT-4o
>         ↓  returns strategy
> Extension Popup → displays result
> ```
>
> ---
>
> ## 📁 Project Structure
>
> ```
> tiktok-ai-strategist/
> ├── extension/
> │   ├── manifest.json     # Chrome Extension config (Manifest V3)
> │   ├── popup.html        # Extension UI
> │   ├── popup.js          # Sends data to backend, displays result
> │   ├── content.js        # Reads TikTok Analytics DOM
> │   └── styles.css
> ├── backend/
> │   ├── main.py           # FastAPI app & routes
> │   ├── analyzer.py       # LLM prompt engineering & OpenAI calls
> │   ├── models.py         # Pydantic data models
> │   └── requirements.txt
> └── README.md
> ```
>
> ---
>
> ## ⚙️ Setup
>
> ### Backend
>
> ```bash
> cd backend
> pip install -r requirements.txt
> cp .env.example .env      # Add your OPENAI_API_KEY
> uvicorn main:app --reload
> ```
>
> ### Chrome Extension
>
> 1. Open Chrome → navigate to `chrome://extensions`
> 2. 2. Enable **Developer mode** (top right toggle)
>    3. 3. Click **Load unpacked** → select the `extension/` folder
>       4. 4. Navigate to your **TikTok Analytics** page
>          5. 5. Click the **ZZH Strategist** icon → hit **Analyze**
>            
>             6. ---
>            
>             7. ## 📊 Example Output
>            
>             8. ```
> 📈 Performance Summary (Last 7 days)
> - Avg views: 280,000
> - - Best performing hook type: "Question opener"
>   - - Peak posting time: 19:00–21:00 JST
>     - - Completion rate trend: +12% vs previous week
>      
>       - 🎯 Next Content Recommendations
>       - 1. Post a "Question opener" video on Wednesday at 20:00
>         2. 2. Tutorial-style videos outperform trend videos by 3x — lean into tutorials
>            3. 3. Videos under 30s show 40% higher completion rate — keep it tight
>              
>               4. 💡 Your Idea Validation
>               5. [Your idea] → Strong concept.
>               6. Suggest adding a hook in the first 2 seconds to boost completion rate.
>               7. ```
>
>                  ---
>
>                  ## 🗺 Roadmap
>
>                  - [ ] TikTok API integration (replace DOM scraping)
>                  - [ ] Weekly auto-report via email
>                  - [ ] Multi-account support
>                  - [ ] Japanese language support for strategy output
>
>                  ---
>
>                  ## 📝 License
>
>                  MIT
>
>                  ---
>
>                  *Built by [ZAWE ZAW HTET](https://z200-web.github.io/my-portofilo/) — IT Student, Japan*
