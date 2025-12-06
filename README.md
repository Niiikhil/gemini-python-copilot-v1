python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install --upgrade pip
pip install langchain langchain-google-genai langchain-core langchain-community
pip install streamlit python-dotenv


source .venv/bin/activate && streamlit run main.py
