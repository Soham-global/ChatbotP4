# Implementation of Chatbot by NLP Project 4

## Overview
This project implements a chatbot using Natural Language Processing (NLP) techniques. The chatbot is designed to assist patients and visitors of Apollo Hospital by understanding user intents and providing appropriate responses. It uses the `nltk` library for natural language processing, `scikit-learn` for machine learning, and `streamlit` for creating an interactive web interface.

## Features
- Understands various user intents such as greetings, appointment scheduling, doctor inquiries, health tips, and more.
- Provides relevant responses based on user input.
- Maintains a conversation history that can be viewed by the user.
- Built using Python and leverages popular libraries for NLP and machine learning.

## Technologies Used
- Python
- NLTK
- Scikit-learn
- Streamlit
- JSON for intents data

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Soham-global/ChatbotP4.git
cd <repository-directory>
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Download NLTK Data
```bash
import nltk
nltk.download('punkt')
```

### Usage
To run the chatbot application, execute the following command:
```bash
streamlit run app.py
```

Once the application is running, you can interact with the chatbot through the web interface. Type your message in the input box and press Enter to see the chatbot's response.

### Intents Data
The chatbot's behavior is defined by the intents.json file, which contains various tags, patterns, and responses. You can modify this file to add new intents or update existing ones.

### Conversation History
The chatbot saves the conversation history in a CSV file (chat_log.csv). You can view past interactions by selecting the "Conversation History" option in the sidebar.

### Contributing
Contributions to this project are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

### Acknowledgments
NLTK for natural language processing.
Scikit-learn for machine learning algorithms.
Streamlit for building the web interface.
Apollo Hospital for inspiring the chatbot's use case.








