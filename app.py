import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

chatbot = pipeline("text-generation",model ="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "It's like you are experincing symptoms. Please consult Doctor for accurate advice"
    elif "appointment" in user_input:
        return "Would you like to schedule appointement with the Doctor"
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly. If you have concerns, consult your doctor. "
    else:
        #for other inputs, use the Hugging face model to generate a response
        response = chatbot(user_input,max_length = 500,num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("Healthcare Assistant Chatbot")
    user_input=st.text_input("How can I assist you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User : ",user_input)
            with st.spinner("Processing your query, Please wait..."):
               response = healthcare_chatbot(user_input)
               st.write("Healthcare Assistant : ",response)
               print(response)
        else:
            st.write("Please enter a message to get a response.")


if __name__=="__main__":
    main()

