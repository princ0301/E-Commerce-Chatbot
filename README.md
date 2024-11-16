# 🛍️ Flipkart E-Commerce Chatbot

An intelligent, conversational chatbot built using LangChain, Groq, and Astra DB, trained on Flipkart customer review data. This chatbot provides personalized responses to user queries about products, offering insights derived from real customer reviews.

## 🚀 Features
- Customer Review Insights: Provides product insights based on scraped Flipkart reviews.
- Natural Language Understanding: Powered by LangChain for advanced conversational abilities.
- Real-time Performance: Efficient processing using Groq technology for faster response times.
- Database Integration: Uses Astra DB for scalable and secure data storage.
- Customizable: Extend the chatbot to other domains or datasets with minimal effort.

## 📂 Project Structure
```sh
E-Commerce-Chatbot/                                                                             
│
├── data/                                                                                       
│   ├── flipkart_reviews.csv               # Scraped reviews dataset                            
│
├── ecommbot/                                                                                   
│   ├── __init__.py                                                                             
│   ├── data_converter.py                  # Convert data into JSON File                        
│   ├── ingest.py                          # Ingestion of data to AstraDB                       
│   ├── retrieval_generation.py            # Retrieval Generation (RAG)                         
│
├── notebook/                                                                                   
│   ├── trial.ipynb                        # Experiment notebook                                
│
├── templates/                                                                                  
│   ├── chat.html                          # Web interface for the chatbot                      
│
├── static/                                                                                    
│   └── style.css                          # CSS files for UI                                  
│
├── requirements.txt                # Python dependencies                                       
├── .env                            # Environment variables                                     
├── app.py                          # Flask app entry point                                    
└── README.md                       # Project documentation
```                 

## 🛠️ Installation

## Prerequisites
- Ensure you have the following installed:
- Python 3.8 or higher
- Groq runtime environment
- Astra DB account
- HuggingFace API token
