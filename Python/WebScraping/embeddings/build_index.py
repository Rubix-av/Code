import faiss, json
import numpy as np
from aipipe_utils import get_embedding

data_files = ["data/discourse_raw.json", "data/course_raw.json"]

texts, meta, vectors = [], [], []

for file in data_files:
    with open(file) as f:
        items = json.load(f)
        for item in items:
            text = item["text"]
            url = item["url"]
            embedding = get_embedding(text)
            vectors.append(embedding)
            texts.append(text)
            meta.append({"text": text, "source": url})

vecs_np = np.array(vectors).astype("float32")
index = faiss.IndexFlatL2(len(vecs_np[0]))
index.add(vecs_np)
faiss.write_index(index, "embeddings/index.faiss")

with open("data/metadata.json", "w") as f:
    json.dump(meta, f, indent=2)
