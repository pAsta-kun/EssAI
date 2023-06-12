import pinecone
from openai.embeddings_utils import get_embedding
from tqdm import tqdm
import docx
import os
import openai
from APIKeys import pineconeKey as pineconeKey
from APIKeys import openAIKey as openAIKey 

openai.api_key = openAIKey

docs_path = r"C:\Users\aliva\Desktop\EssAI\docs"

text_chunks = []
for f_name in os.listdir(docs_path):
  doc_path = os.path.join(docs_path, f_name)
  doc = docx.Document(doc_path)
  for para in doc.paragraphs:
    text_chunks.append(para.text)

# remove all chunks shorter than 10 words and strip the rest
text_chunks = [string.strip().strip('\n') for string in text_chunks if len(string.split()) >= 10]

chunks_with_embeddigns = []
for chunk in tqdm(text_chunks):
  embedding = get_embedding(chunk, engine='text-embedding-ada-002')
  chunks_with_embeddigns.append({"text": chunk, "embedding": embedding})

pinecone.init(
    api_key=pineconeKey,
    environment="us-west4-gcp-free"
)

# create or connect to index
index_name = "essai"

if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=1536)
# connect to index
index = pinecone.Index(index_name)

batch_size = 64  # process everything in batches of 64
for i in tqdm(range(0, len(chunks_with_embeddigns), batch_size)):
    data_batch = chunks_with_embeddigns[i: i+batch_size]
    # set end position of batch
    i_end = min(i+batch_size, len(chunks_with_embeddigns))
    # get batch meta
    text_batch = [item['text'] for item in data_batch]
    # get ids
    ids_batch = [str(n) for n in range(i, i_end)]
    # get embeddings
    embeds = [item['embedding'] for item in data_batch]
    # prep metadata and upsert batch
    meta = [{'text': text_batch} for text_batch in zip(text_batch)] # you can add more fields here
    to_upsert = zip(ids_batch, embeds, meta)
    # upsert to Pinecone
    index.upsert(vectors=list(to_upsert))
