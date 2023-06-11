import pinecone
from openai.embeddings_utils import get_embedding
from tqdm import tqdm
import docx
import os
import openai

openai.api_key = ""

docs_path = 'C:\\Users\\aliva\\Desktop\\EssAI\\EssAIInfo.docx'

text_chunks = []

doc = docx.Document(docs_path)
for para in doc.paragraphs:
    text_chunks.append(para.text)

# remove all chunks shorter than 10 words and strip the rest
text_chunks = [string.strip().strip('\n') for string in text_chunks if len(string.split()) >= 10]

# remove all chunks shorter than 10 words and strip the rest
text_chunks = [string.strip().strip('\n') for string in text_chunks if len(string.split()) >= 10]

chunks_with_embeddings = []
for chunk in text_chunks:
    response = openai.Embedding.create(
        input= "idfk",
        model="text-embedding-ada-002",
        texts=[chunk]
    )
    embedding = response["embeddings"][0]["embedding"]
    chunks_with_embeddings.append({
        'text': chunk,
        'embedding': embedding
    })

pinecone.init(
    api_key="f6d7a4a5-8ca8-428b-bb4e-2ca554886b20",
    environment="us-west4-gcp-free"
)

# create or connect to index
index_name = "Essay-AI"

if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=1536)
# connect to index
index = pinecone.Index(index_name)

batch_size = 64  # process everything in batches of 64
for i in tqdm(range(0, len(chunks_with_embeddings), batch_size)):
    data_batch = chunks_with_embeddings.iloc[i: i+batch_size]
    # set end position of batch
    i_end = min(i+batch_size, len(chunks_with_embeddings))
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

def search_docs(query):
  xq = openai.Embedding.create(input=query, engine="text-embedding-ada-002")['data'][0]['embedding']
  res = index.query([xq], top_k=5, include_metadata=True)
  chosen_text = []
  for match in res['matches']:
    chosen_text = match['metadata']
  return res['matches']

matches = search_docs("What are some college essay tips?")
for match in matches:
    print(f"{match['score']:.2f}: {match['metadata']}")

def construct_prompt(query):
  matches = search_docs(query)

  chosen_text = []
  for match in matches:
    chosen_text.append(match['metadata']['text'])

  prompt = """Answer the question as truthfully as possible using the context below, and if the answer is no within the context, say 'I don't know.'"""
  prompt += "\n\n"
  prompt += "Context: " + "\n".join(chosen_text)
  prompt += "\n\n"
  prompt += "Question: " + query
  prompt += "\n"
  prompt += "Answer: "
  return prompt

def answer_question(query):
  prompt = construct_prompt(query)
  res = openai.Completion.create(
      prompt=prompt,
      model="text-davinci-003",
      max_tokens=500,
      temperature=0.0,
  )
  
  return res.choices[0].message

print(answer_question("What are some college essay tips?"))