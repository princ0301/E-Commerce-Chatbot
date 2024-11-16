from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
from ecommbot.ingest import ingestdata
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

def generation(vstore):
    retriever = vstore.as_retriever(search_kwargs={"k": 3})
    
    PRODUCT_BOT_TEMPLATE = """
    Your ecommercebot bot is an expert in product recommendations and customer queries.
    It analyzes product titles and reviews to provide accurate and helpful responses.
    Ensure your answers are relevant to the product context and refrain from straying off-topic.
    Your responses should be concise and informative.

    CONTEXT:
    {context}

    QUESTION: {question}

    YOUR ANSWER:
    
    """
    
    prompt = ChatPromptTemplate.from_template(PRODUCT_BOT_TEMPLATE)
    
    llm = ChatGroq(model='llama3-70b-8192', api_key=groq_api_key)
    
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return chain

if __name__=="__main__":
    vstore = ingestdata("done")
    chain = generation(vstore)
    print(chain.invoke("Can you tell me the best bluetooth buds?"))