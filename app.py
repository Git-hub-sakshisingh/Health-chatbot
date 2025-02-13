import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load a pre-trained Hugging Face model 
chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    # Rule-based filtering for medical-related queries
    if "symptom" in user_input:
        return "Please consult a doctor for accurate medical advice."
    elif "appointment" in user_input:
        return "Would you like to schedule an appointment with the doctor?"
    elif "medication" in user_input:
        return "It's important to take prescribed medicines regularly. If you have concerns, consult your doctor."
    elif "heart attack" in user_input:
        return "If you suspect a heart attack, call emergency services immediately. While waiting for help, keep the person calm and seated. Offer aspirin if they are not allergic. If unconscious, start CPR and use an AED if available."
    elif "cough" in user_input:
        return "For a cough, drink warm liquids, use lozenges, inhale steam, and avoid irritants. If persistent or severe, seek medical advice."
    elif "diabetes" in user_input:
        return "Managing diabetes involves maintaining a balanced diet, regular exercise, monitoring blood sugar levels, and following prescribed medication. If you have concerns, consult your healthcare provider."
    elif "fever" in user_input:
        return "Fever is a sign of infection. Stay hydrated, rest, and take fever-reducing medications if needed. If fever is high or persistent, consult a doctor."
    elif "blood pressure" in user_input:
        return "Maintaining normal blood pressure requires a healthy diet, reduced salt intake, exercise, and stress management. Regular check-ups are advised."
    elif "flu" in user_input:
        return "Flu symptoms include fever, body aches, and fatigue. Stay hydrated, rest, and take flu medication if necessary. Seek medical advice if symptoms worsen."
    else:
        response = chatbot(user_input, max_length=500, num_return_sequences=1)
        return response[0]['generated_text']

# Streamlit web app interface
def main():
    st.title("Healthcare Assistant Chatbot")
    
    user_input = st.text_input("How can I assist you today?")

    if st.button("Submit"):
        if user_input:
            st.write("User:", user_input)
            with st.spinner("Processing your query, Please wait..."):
                response = healthcare_chatbot(user_input)
                st.write("Healthcare Assistant:", response)
                print(response)
        else:
            st.write("Please enter a message to get a response.")

if __name__ == "__main__":
    main()




# import streamlit as st
# from transformers import pipeline
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize

# #Download necessary NLTK data
# nltk.download('punkt')
# nltk.download('stopwords')

# # Load a pre-trained Hugging Face model for conversational AI (DialoGPT)
# chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# def healthcare_chatbot(user_input):
#     if "symptom" in user_input:
#         return "Please consult Doctor for accurate advice"
#     elif "appointment" in user_input:
#         return "Would you like to schedule an appointment with the Doctor?"
#     elif "medication" in user_input:
#         return "It's important to take prescribed medicines regularly. If you have concerns, consult your doctor."
#     else:
#         response = chatbot(user_input)
#         return response[0]['generated_text']

# # Streamlit web app interface
# def main():
#     # Set up the web app title and input area
#     st.title("Healthcare Assistant Chatbot")
    
#     # Display a simple text input for user queries
#     user_input = st.text_input("How can I assist you today?")

#     # Display chatbot response
#     if st.button("Submit"):
#         if user_input:
#             st.write("User : ", user_input)
#             with st.spinner("Processing your query, Please wait..."):
#                response = healthcare_chatbot(user_input)
#                st.write("Healthcare Assistant : ", response)
#                print(response)
#         else:
#             st.write("Please enter a message to get a response.")

# if __name__ == "__main__":
#     main()



