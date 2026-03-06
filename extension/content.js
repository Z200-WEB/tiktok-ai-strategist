// content.js — reads TikTok Analytics DOM and extracts structured data

function parseNumber(str) {
    if (!str) return 0;
    const cleaned = str.trim();
    if (cleaned.includes('M')) return Math.round(parseFloat(cleaned) * 1_000_000);
    if (cleaned.includes('K')) return Math.round(parseFloat(cleaned) * 1_000);
    return parseInt(cleaned.replace(/,/g, ''), 10) || 0;
}

function extractVideoData() {
    const rows = document.querySelectorAll('[data-e2e="video-row"]');
    return Array.from(rows).slice(0, 10).map(row => ({
          title: row.querySelector('[data-e2e="video-title"]')?.innerText?.trim() || '',
          views: parseNumber(row.querySelector('[data-e2e="video-views"]')?.innerText),
          likes: parseNumber(row.querySelector('[data-e2e="video-likes"]')?.innerText),
          watch_time: null,
    }));
}

function extractPostingTimes() {
    const times = document.querySelectorAll('[data-e2e="post-time"]');
    return Array.from(times).map(t => t.innerText?.trim()).filter(Boolean);
}

function extractAnalytics() {
    return {
          total_views: parseNumber(
                  document.querySelector('[data-e2e="views-count"]')?.innerText
                ),
          followers: parseNumber(
                  document.querySelector('[data-e2e="followers-count"]')?.innerText
                ),
          likes: parseNumber(
                  document.querySelector('[data-e2e="likes-count"]')?.innerText
                ),
          comments: parseNumber(
                  document.querySelector('[data-e2e="comments-count"]')?.innerText
                ),
          shares: parseNumber(
                  document.querySelector('[data-e2e="shares-count"]')?.innerText
                ),
          videos: extractVideoData(),
          posting_times: extractPostingTimes(),
    };
}

chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
    if (msg.action === 'extract') {
          sendResponse(extractAnalytics());
    }
});
