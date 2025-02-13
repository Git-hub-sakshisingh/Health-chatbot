import streamlit as st
import google.generativeai as genai
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Configure Gemini API (Replace 'YOUR_GEMINI_API_KEY' with your actual API key)
genai.configure(api_key='your_gemini_api_key')
model = genai.GenerativeModel("gemini-pro")

def healthcare_chatbot(user_input):
    # Rule-based filtering for medical-related queries
    medical_responses = {
        "symptom": "Please consult a doctor for accurate medical advice.",
        "appointment": "Would you like to schedule an appointment with the doctor?",
        "medication": "It's important to take prescribed medicines regularly. If you have concerns, consult your doctor.",
        "heart attack": "If you suspect a heart attack, call emergency services immediately. While waiting for help, keep the person calm and seated. Offer aspirin if they are not allergic. If unconscious, start CPR and use an AED if available.",
        "cough": "For a cough, drink warm liquids, use lozenges, inhale steam, and avoid irritants. If persistent or severe, seek medical advice.",
        "diabetes": "Managing diabetes involves maintaining a balanced diet, regular exercise, monitoring blood sugar levels, and following prescribed medication. If you have concerns, consult your healthcare provider.",
        "fever": "Fever is a sign of infection. Stay hydrated, rest, and take fever-reducing medications if needed. If fever is high or persistent, consult a doctor.",
        "blood pressure": "Maintaining normal blood pressure requires a healthy diet, reduced salt intake, exercise, and stress management. Regular check-ups are advised.",
        "flu": "Flu symptoms include fever, body aches, and fatigue. Stay hydrated, rest, and take flu medication if necessary. Seek medical advice if symptoms worsen."
    }
    
    for key, response in medical_responses.items():
        if key in user_input.lower():
            return response
    
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return "Error processing request: " + str(e)
    
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


# Command-line interface
# if __name__ == "__main__":
    # print("Welcome to the Healthcare Assistant Chatbot! Type 'exit' to end the session.")
    # while True:
    #     user_input = input("You: ")
    #     if user_input.lower() == "exit":
    #         print("Goodbye! Stay healthy.")
    #         break
    #     response = healthcare_chatbot(user_input)
    #     print("Healthcare Assistant:", response)























































