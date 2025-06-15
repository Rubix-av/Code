from playwright.sync_api import sync_playwright
import json

URL = "https://tds.s-anand.net/#/2025-01/"

def scrape():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(URL)
        page.wait_for_timeout(5000)  # wait 5s
        texts = page.locator("main").all_text_contents()
        browser.close()
        return [{"text": t, "url": URL} for t in texts if len(t.strip()) > 50]

with open("data/course_raw.json", "w") as f:
    json.dump(scrape(), f, indent=2)
