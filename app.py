from flask import Flask,jsonify,request
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os
from openai import OpenAI
import openai
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

@app.route("/tcs", methods=["POST"])
def home():
    data = request.get_json()
    question = data.get('question')
    print("Question is: ",question)
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    new_vector_store = FAISS.load_local(
    "tcs_docu_faiss_index", embeddings, allow_dangerous_deserialization=True
    )
    
    context = new_vector_store.similarity_search(question)
    actual_context = context[0].page_content
    
    prompt = f''' I am going to ask a question. please answer based on the given context.
    If you don't get answer from the context don't give answer and don't search on internet.
    my question : {question}
    context : {actual_context}
    '''
    
    os.environ["OPENAI_API_KEY"] = "insert your openai api key here"
    
    client = OpenAI()

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt)
    print(response.output_text)

    return jsonify({
        "message": response.output_text
    }),200
    
    
app.run(debug=True)