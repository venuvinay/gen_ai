# you are importing lang chain for prompts and models and output
from fastapi import FastAPI
import uvicorn
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
# api server creation of two models one for essay and another for poem
from langserve import add_routes
#you are creatinfg a prompt message for gpt including two message one for eassay and another for poem
eassy=ChatPromptTemplate.from_messages(
    [
    ("system","listen to user carefully"),
    ("user","write an essay of exact 100 words on topic{topic}")
    ]
)
#from template form
poem=ChatPromptTemplate.from_template(
    '''
    write a poem of excat 50 words on topic{topic}

    '''
)
model=Ollama(model="llama2")
app = FastAPI(server="langserver",version=1.0)
add_routes(
    app,
    eassy|model,
    path="/essay"
)
add_routes(
    app,
    poem|model,
    path="/poem"
)
uvicorn.run(app,host="localhost",port=8000)