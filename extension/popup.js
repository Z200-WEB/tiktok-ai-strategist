// popup.js — handles UI interactions and communicates with backend

const BACKEND_URL = 'http://localhost:8000';

document.addEventListener('DOMContentLoaded', () => {
    const analyzeBtn = document.getElementById('analyze-btn');
    const statusEl = document.getElementById('status');
    const resultEl = document.getElementById('result');
    const userIdeaEl = document.getElementById('user-idea');
    const loadingEl = document.getElementById('loading');

                            analyzeBtn.addEventListener('click', async () => {
                                  try {
                                          analyzeBtn.disabled = true;
                                          loadingEl.style.display = 'block';
                                          resultEl.textContent = '';
                                          statusEl.textContent = 'Extracting analytics from TikTok...';

                                    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

                                    if (!tab.url.includes('tiktok.com')) {
                                              statusEl.textContent = 'Please navigate to TikTok Analytics first.';
                                              return;
                                    }

                                    // Inject content script and extract data
                                    const [result] = await chrome.scripting.executeScript({
                                              target: { tabId: tab.id },
                                              func: () => {
                                                          // Re-run extraction inline for reliability
                                                function parseNumber(str) {
                                                              if (!str) return 0;
                                                              const cleaned = str.trim();
                                                              if (cleaned.includes('M')) return Math.round(parseFloat(cleaned) * 1_000_000);
                                                              if (cleaned.includes('K')) return Math.round(parseFloat(cleaned) * 1_000);
                                                              return parseInt(cleaned.replace(/,/g, ''), 10) || 0;
                                                }
                                                          return {
                                                                        total_views: parseNumber(document.querySelector('[data-e2e="views-count"]')?.innerText),
                                                                        followers: parseNumber(document.querySelector('[data-e2e="followers-count"]')?.innerText),
                                                                        likes: parseNumber(document.querySelector('[data-e2e="likes-count"]')?.innerText),
                                                                        comments: parseNumber(document.querySelector('[data-e2e="comments-count"]')?.innerText),
                                                                        shares: parseNumber(document.querySelector('[data-e2e="shares-count"]')?.innerText),
                                                                        videos: [],
                                                                        posting_times: [],
                                                          };
                                              },
                                    });

                                    const analytics = result.result;
                                          statusEl.textContent = 'Sending to AI for analysis...';

                                    const response = await fetch(`${BACKEND_URL}/analyze`, {
                                              method: 'POST',
                                              headers: { 'Content-Type': 'application/json' },
                                              body: JSON.stringify({
                                                          analytics,
                                                          user_idea: userIdeaEl.value.trim() || null,
                                              }),
                                    });

                                    if (!response.ok) throw new Error(`Server error: ${response.status}`);

                                    const data = await response.json();
                                          statusEl.textContent = 'Done!';
                                          resultEl.textContent = data.strategy;

                                  } catch (err) {
                                          statusEl.textContent = `Error: ${err.message}`;
                                  } finally {
                                          analyzeBtn.disabled = false;
                                          loadingEl.style.display = 'none';
                                  }
                            });
});
