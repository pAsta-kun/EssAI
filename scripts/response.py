from flask import Flask, request, jsonify
from flask_cors import CORS
import pinecone
from openai.embeddings_utils import get_embedding
from tqdm import tqdm
import docx
import os
import openai
from APIKeys import pineconeKey as pineconeKey
from APIKeys import openAIKey as openAIKey 

app = Flask(__name__)
CORS(app)

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

def construct_prompt(query):
    matches = search_docs(query)

    chosen_text = []
    for match in matches:
        chosen_text.extend(match['metadata']['text'])

    prompt = """You're an AI Chatbot called EssAI. You're purpose is to answer students questions and help them with their college essays. You'll be provided some context, make sure to use this in order to forumlate better responses. If you don't believe you can give a very strong response then inform the user and response in a way you see fit. When providing rersources, refrain from providing email adresses and links or usernames, only provide links.'"""
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
        temperature=0.3,
    )

    return res.choices[0].text

@app.route('/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'GET':
        return 'EssAI Server'
    elif request.method == 'POST':
        requestData = request.get_json()  # Get the data from the POST request
        query = requestData['message']  # Extract the 'message' field
        response = answer_question(query)  # Generate the response using your answer_question function
        return jsonify({'bot': response})  # Return the response as JSON

if __name__ == '__main__':
    app.run(port=5000)
