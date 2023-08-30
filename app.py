from flask import Flask, request, jsonify
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import os
import openai

app = Flask(__name__)
openai.api_key  = os.environ['OPENAI_API_KEY']

# Initialize ChatOpenAI model
llm_name = "gpt-3.5-turbo"
# llm = ChatOpenAI(model_name=llm_name, temperature=0, openai_api_key=os.environ["OPENAI_API_KEY"])
llm = ChatOpenAI(model_name=llm_name, temperature=0)

# Initialize Chroma for embeddings
persist_directory = 'chroma/'
embedding = OpenAIEmbeddings()
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

def run_qa_chain(template: str, question: str):
    # Build prompt
    QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"], template=template)
    
    # Run chain
    qa_chain = RetrievalQA.from_chain_type(llm,
                                           retriever=vectordb.as_retriever(),
                                           return_source_documents=True,
                                           chain_type_kwargs={"prompt": QA_CHAIN_PROMPT})
    
    result = qa_chain({"query": question})
    
    return result["result"]

@app.route('/health', methods=['GET'])
def health_check():
    return "pong"

@app.route('/api/v1/search', methods=['POST'])
def get_qa_result():
    api_key = request.headers.get('Authorization')
    if api_key != os.environ["DESIRED_API_KEY"]:
        return jsonify({"error": "unauthorized"}), 401
    

    data = request.json
    
    if not data:
        return jsonify({"error": "Request body is empty or not a valid JSON object"}), 400

    template = data.get('template')
    question = data.get('question')
    
    if not template or not question:
        return jsonify({"error": "Both template and question fields are required in the request body"}), 400
    
    result = run_qa_chain(template, question)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)