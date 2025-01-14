import streamlit as st
import re
import responses_chatbot.long_responses as long_responses
import pathlib

def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

css_path=pathlib.Path("assets/style.css")
load_css(css_path)

# Function to calculate message probability
def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Count how many words are present in predefined message
    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    # Calculate percent of recognized words in a user message
    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Response ---------------------------------------------------------------------------------------------------
    response('Hello', 
             ['hi', 'hello', 'ssup', 'hey', 'heyo'], single_response=True)
    response('Aww, thank you! You just made my circuits blush!', 
         ['I', 'love', 'you'], required_words=['you'])
    response('My name is Vansh. Nice to meet you!', 
             ['what', 'is', 'your', 'name'], single_response=True)

    response(long_responses.R_ABOUT, 
         ['what', 'do', 'you', 'do'], required_words=['do'])

    response(long_responses.R_COMPINQ,
         ['what', 'is', 'your', 'favorite', 'hobby'], required_words=['hobby'])

    response(long_responses.R_EDUCATION,
         ['what', 'are', 'you', 'studying'], required_words=['studying'])

    response(long_responses.R_FUTUREQUESTION,
         ['what', 'do', 'you', 'want', 'to', 'do', 'in', 'the', 'future'], required_words=['future'])

    response(long_responses.R_CURRENTSTATE,
         ['how', 'are', 'you', 'doing'], required_words=['how'])

    response(long_responses.R_INTEREST,
         ['why', 'are', 'you', 'interested', 'in', 'computers'], required_words=['interested'])

    response(long_responses.R_PURSUING,
         ['why', 'are', 'you', 'pursuing', 'a', 'bachelor\'s', 'degree'], required_words=['bachelor\'s'])

    response(long_responses.R_WHATSNEW,
         ['what', 'is', 'new', 'with', 'you'], required_words=['new'])

    response(long_responses.R_GOALS,
         ['where', 'do', 'you', 'see', 'yourself', 'in', 'five', 'years'], required_words=['five', 'years'])

    response(long_responses.R_EAT, ['what', 'you', 'eat'], required_words=['eat', 'you'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long_responses.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Streamlit Chatbot Interface

# Initialize the session state for storing chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the conversation history (old messages first)
for message in reversed(st.session_state.messages):  # Reverse order so old messages are on top
    with st.chat_message(message["role"], avatar="😊" if message["role"] == "user" else "🤖"):
        st.write(message["content"])

# Get the user's input
user_input = st.chat_input(placeholder="How can I help you?",key='chatbot_input')

# If the user inputs a message
if user_input:
    # Store the user input in session_state
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get the bot's response
    bot_response = get_response(user_input)

    # Store the bot's response in session_state
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    # Display the new user's message at the bottom (it will be the last in the list)
    with st.chat_message("user", avatar="😊"):
        st.write(user_input)

    with st.chat_message("assistant", avatar="🤖"):
        st.write(bot_response)

else:
    st.write("This bot is static and may not understand everything.")

