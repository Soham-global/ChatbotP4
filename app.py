import os
import json
import datetime
import csv
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# NLTK setup
ssl._create_default_https_context = ssl._create_unverified_context

# Load intents from the JSON file
file_path = os.path.abspath("./intents.json")
with open(file_path, "r") as file:
    intents = json.load(file)

# Create the vectorizer and classifier
vectorizer = TfidfVectorizer(ngram_range=(1, 4))
clf = LogisticRegression(random_state=0, max_iter=10000)

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# Train the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

# Chatbot response function
def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response
    return "I'm sorry, I didn't understand that."

# Streamlit application
def main():
    st.title("Hospital Chatbot")
    st.sidebar.header("Menu")
    menu = ["Home", "Conversation History", "About"]
    choice = st.sidebar.selectbox("Select an Option", menu)

    if choice == "Home":
        st.subheader("Chat with the Hospital Chatbot")
        st.write("Welcome to Apollo Hospital! How can we assist you today?")
        
        # Check if chat log exists, otherwise create it
        log_file = "chat_log.csv"
        if not os.path.exists(log_file):
            with open(log_file.csv, "w", newline='', encoding="utf-8") as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(["User Input", "Chatbot Response", "Timestamp"])
        
        user_input = st.text_input("You:")
        if user_input:
            response = chatbot(user_input)
            st.text_area("Chatbot:", value=response, height=120, max_chars=None)
            
            # Log the conversation
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(log_file, "a", newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([user_input, response, timestamp])

            if response.lower() in ["take care and stay healthy!", "goodbye! we're here if you need us."]:
                st.write("Thank you for chatting with us. Stay healthy!")
                st.stop()

    elif choice == "Conversation History":
        st.subheader("Conversation History")
        if os.path.exists("chat_log.csv"):
            with open("chat_log.csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)  # Skip the header
                for row in reader:
                    st.text(f"User: {row[0]}")
                    st.text(f"Chatbot: {row[1]}")
                    st.text(f"Timestamp: {row[2]}")
                    st.markdown("---")
        else:
            st.write("No conversation history found.")

    elif choice == "About":
        st.subheader("About the Hospital Chatbot")
        st.write("""
            The Hospital Chatbot is designed to assist patients with common queries, such as:
            - Booking appointments
            - Inquiring about doctors
            - Receiving health tips
            - Emergency contact information

            This chatbot leverages Natural Language Processing (NLP) and Machine Learning (ML) for intent recognition. It uses Streamlit to provide an intuitive user interface.
        """)

if __name__ == '__main__':
    main()
