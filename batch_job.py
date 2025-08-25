from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from uuid import uuid4


# Step-1: Load the Document
loader = PyPDFLoader("tcsannualreport.pdf")
documents = loader.load()
print("Documentaion loaded successfully.")
print(len(documents))
# print(documents[0])

# Step-2: Split the document into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 100
)
chunks = text_splitter.split_documents(documents)
# print(chunks)
print("No.of Chunks: ",len(chunks))
print("Successfully splitting the documentation into chunks.")

# Step-3: Build an Embedding Model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
print("Embedding model has created successfully.")

# Step-4: Creating Faiss Database
index = faiss.IndexFlatL2(len(embedding_model.embed_query("hello world")))

vector_store = FAISS(
    embedding_function=embedding_model,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)
print("Faiss Database has Created Successfully.")

# Step-5: Add chunks into faiss database

vector_store.add_documents(chunks)
print("Successfully added chunks into faiss database.")

# Step-6: Saving the Faiss database into local storage
vector_store.save_local("tcs_docu_faiss_index")
print("Successfully save the faiss database into local storage")