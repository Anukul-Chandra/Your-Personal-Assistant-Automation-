# import streamlit as st
# import requests

# # create the title for the page
# st.title("🤝 Your Personal Assistant")

# # add subheader
# st.subheader("What can your personal assistant do?")

# # create a list of what your assistant can do
# st.markdown("""
#             1. Answer questions on various topics.   
#             2. Arrange Calendar events and meetings.  
#             3. Read your emails and send replies, can even summarize them for you.
#             4. Manage your tasks and to-do lists.
#             5. Take quick notes for you.
#             6. Track your expenses and budgeting.
#             """)

# # add chats subheader
# st.subheader("💬 Chat with your assistant")

# # create a session state for message history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # show the messages in chat history
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # create a chat input box
# user_message = st.chat_input()

      
# # if user sends a message
# if user_message:
#     with st.chat_message("user"):
#         st.markdown(user_message)
#         # append the user message to message history
#         st.session_state.messages.append({"role": "user", "content": user_message})
    
#     # send the user message to the n8n webhook
#     response = requests.post(
#         "http://localhost:5678/webhook-test/df442a97-fe2a-4d06-99bf-282768a4c3e6",  # replace with your n8n webhook URL
#         json={"message": user_message}
#     )
    
#     # get the AI response from webhook
#     ai_response = response.json()["output"]
    
#     # display the AI response in chat
#     with st.chat_message("assistant"):
#         st.markdown(ai_response)
#         # append the AI response to message history
#         st.session_state.messages.append({"role": "assistant", "content": ai_response})


import streamlit as st
import requests

# ---------------------------
# Page Title
# ---------------------------
st.title("🤝 Your Personal Assistant")

st.subheader("What can your personal assistant do?")

st.markdown("""
1. Answer questions on various topics  
2. Arrange calendar events and meetings  
3. Read your emails and send replies, even summarize them  
4. Manage your tasks and to-do lists  
5. Take quick notes for you  
6. Track your expenses and budgeting  
""")

st.subheader("💬 Chat with your assistant")

# ---------------------------
# Session state for chat
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# Show previous messages
# ---------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------
# Chat input
# ---------------------------
user_message = st.chat_input("Type your message...")

# ---------------------------
# If user sends message
# ---------------------------
if user_message:

    # show user message
    with st.chat_message("user"):
        st.markdown(user_message)

    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    try:
        # send request to n8n webhook
        response = requests.post(
            "http://localhost:5678/webhook/df442a97-fe2a-4d06-99bf-282768a4c3e6",
            json={"message": user_message},
            timeout=30
        )

        data = response.json()

        # handle different response structures
        if isinstance(data, list):
            ai_response = data[0].get("output", str(data))
        elif isinstance(data, dict):
            ai_response = data.get("output", str(data))
        else:
            ai_response = str(data)

    except Exception as e:
        ai_response = f"⚠️ Error connecting to assistant: {e}"

    # show assistant response
    with st.chat_message("assistant"):
        st.markdown(ai_response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })