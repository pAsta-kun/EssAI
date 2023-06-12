import pinecone
from openai.embeddings_utils import get_embedding
from tqdm import tqdm
import docx
import os
import openai
from APIKeys import pineconeKey as pineconeKey
from APIKeys import openAIKey as openAIKey 

openai.api_key = openAIKey

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

def search_docs(query):
    xq = openai.Embedding.create(input=query, engine="text-embedding-ada-002")['data'][0]['embedding']
    res = index.query([xq], top_k=5, include_metadata=True)
    chosen_text = []
    for match in res['matches']:
        chosen_text = match['metadata']
    return res['matches']

matches = search_docs("What are some essay tips?")

for match in matches:
    print(f"{match['score']:.2f}: {match['metadata']}")
print("******************")

def construct_prompt(query):
    matches = search_docs(query)

    chosen_text = []
    for match in matches:
        chosen_text.extend(match['metadata']['text'])
    #print(chosen_text)


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
        max_tokens=2000,
        temperature=0.0,
    )

    return res.choices[0].text

print(answer_question("What are some tips for my college personal statement?"))