# https://python.langchain.com/docs/langserve#server
from fastapi import FastAPI
from langchain_nvidia_ai_endpoints import ChatNVIDIA, NVIDIAEmbeddings
from langserve import add_routes

## May be useful later
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.prompt_values import ChatPromptValue
from langchain_core.runnables import RunnableLambda, RunnableBranch, RunnablePassthrough
from langchain_core.runnables.passthrough import RunnableAssign
from langchain_community.document_transformers import LongContextReorder
from functools import partial
from operator import itemgetter

from langchain_community.vectorstores import FAISS

## TODO: Make sure to pick your LLM and do your prompt engineering as necessary for the final assessment
embedder = NVIDIAEmbeddings(model="nvidia/nv-embed-v1", truncate="END")
instruct_llm = ChatNVIDIA(model="meta/llama3-8b-instruct")

app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple api server using Langchain's Runnable interfaces",
)

## PRE-ASSESSMENT: Run as-is and see the basic chain in action

add_routes(
    app,
    instruct_llm,
    path="/basic_chat",
)

## ASSESSMENT TODO: Implement these components as appropriate

# Load the vector store (Make sure this path is correct)
db = FAISS.load_local("faiss_index_nvidia", embedder, allow_dangerous_deserialization=True)
retriever = db.as_retriever()

# Define the generator prompt and chain
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Use the context provided to answer the user's question. Be concise and cite the sources from the context."),
    ("user", "Context:\n{context}\n\nQuestion:\n{question}")
])

generator_chain = (
    {"context": itemgetter("context"), "question": itemgetter("input")}
    | prompt_template
    | instruct_llm
    | StrOutputParser()
)

# Add the final routes to the app
add_routes(
    app,
    generator_chain,
    path="/generator",
)

add_routes(
    app,
    retriever,
    path="/retriever",
)

## Might be encountered if this were for a standalone python file...
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9012)
