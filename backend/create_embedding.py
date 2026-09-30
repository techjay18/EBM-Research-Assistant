import os
import pandas as pd
from sqlalchemy import create_engine
import faiss
import numpy as np

engine = create_engine(
    "postgresql://postgres:jay1873@localhost/ebm_db"
)

query = '''
SELECT *
FROM papers
'''

df = pd.read_sql(query, engine)  # type: ignore[arg-type]

print(df.head())
print(df.columns)
print(df.shape)
df["content"] = (
    df[["Title", "Summary", "Topics", "Source"]]
    .fillna("")
    .astype(str)
    .agg(" ".join, axis=1)
)

print(df["content"][0])

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "pritamdeka/BioBERT-mnli-snli-scinli-scitail-mednli-stsb"
)

embeddings = model.encode(
    df["content"].tolist(),
    show_progress_bar=True
)
print(embeddings.shape)


embeddings = np.array(
    embeddings,
    dtype="float32"
)


index = faiss.IndexFlatL2(
    embeddings.shape[1]
)




index.add(embeddings)

print("FAISS Index Created")

os.makedirs("faiss_index", exist_ok=True)

faiss.write_index(
    index,
    "faiss_index/oncology.faiss"
)

df.to_pickle(
    "faiss_index/papers.pkl"
)

print("Files Saved Successfully")