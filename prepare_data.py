
import openai
import os

import sys

sys.path.append('../..')

# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv()) # read local .env file

# openai.api_key  = os.environ['OPENAI_API_KEY']
openai.api_key = "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"

# PREPARATION LOAD & Embedding + STORAGE DB
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
embedding = OpenAIEmbeddings()

from langchain.vectorstores import Chroma
persist_directory = 'chroma/'

from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain.document_loaders import NotionDirectoryLoader
loader = NotionDirectoryLoader("docs/Notion_DB")
docs = loader.load()
txt = ' '.join([d.page_content for d in docs])

from langchain.text_splitter import MarkdownHeaderTextSplitter
# Split Headers MD
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]
markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)
md_header_splits = markdown_splitter.split_text(txt)
print(md_header_splits)

# Split
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1500,
    chunk_overlap = 150
)
splits = text_splitter.split_documents(md_header_splits)

vectordb = Chroma.from_documents(
documents=splits,
    embedding=embedding,
    persist_directory=persist_directory
)
vectordb.persist()