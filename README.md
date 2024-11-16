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

## Steps
1. Clone the Repository
```sh
git clone https://github.com/princ0301/E-Commerce-Chatbot.git
cd /E-Commerce-Chatbot
```

2. Install Dependencies
```sh
pip install -r requirements.txt
```

3. Create a .env File In the project root directory, create a .env file to store sensitive credentials securely. Add the following keys:
```
HF_TOKEN="your huggingface API token"
GROQ_API_KEY="Enter your Groq API key"
ASTRA_DB_API_ENDPOINT="https://your-astra-db-endpoint"
ASTRA_DB_APPLICATION_TOKEN="your-astra-db-application-token"
ASTRA_DB_KEYSPACE="your-keyspace-name"
```
Replace the placeholders with your actual credentials.

4. Set Up Astra DB
- Create a new database in Astra DB.
- Obtain your API endpoint, application token, and keyspace name.

5. Run ingestion file
```
python ecommbot/ingest.py
```

6. Run the Chatbot
```
python run.py
```
## 🤖 Technologies Used
- LangChain: Conversational AI and chaining logic.
- Groq: High-performance AI acceleration.
- Astra DB: Cloud-native database for data storage.
- Flask: Backend framework for serving the chatbot.
- BeautifulSoup: Web scraping.
- Python Libraries: pandas, numpy, sklearn, etc.

## 🌟 Key Highlights
- Scalable and adaptable design for e-commerce platforms.
- Seamless integration with any dataset of customer reviews.
- High accuracy and response quality optimized for user satisfaction.
