import streamlit as st
from chatbot_core import answer_question  
st.markdown("<h1 style='font-size: 24px; text-align: center;'>💬 Chatbot Code du Travail Marocain</h1>", unsafe_allow_html=True)

st.caption("🚀 A Streamlit chatbot powered by Abdelaali LAMRANI")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Posez votre question sur le code du travail marocain:"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("🕒 Le bot est en train de réfléchir..."):
            # Get the assistant's response
            response = answer_question(prompt)

    # Get the assistant's response
    response = answer_question(prompt)
    
    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
