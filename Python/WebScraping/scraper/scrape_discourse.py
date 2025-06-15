import requests, json
from bs4 import BeautifulSoup

BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"
CATEGORY_ID = 34

def get_discourse_posts():
    all_posts = []
    for page in range(0, 5):
        url = f"{BASE_URL}/c/courses/tds-kb/{CATEGORY_ID}.json?page={page}"
        res = requests.get(url)
        topics = res.json().get("topic_list", {}).get("topics", [])
        for topic in topics:
            topic_id = topic["id"]
            topic_url = f"{BASE_URL}/t/{topic_id}.json"
            topic_data = requests.get(topic_url).json()
            for post in topic_data["post_stream"]["posts"]:
                soup = BeautifulSoup(post["cooked"], "html.parser")
                all_posts.append({
                    "text": soup.get_text(),
                    "url": f"{BASE_URL}/t/{topic_id}/{post['post_number']}"
                })
    return all_posts

with open("data/discourse_raw.json", "w") as f:
    json.dump(get_discourse_posts(), f, indent=2)
