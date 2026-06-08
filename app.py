import streamlit as st
import requests

# create the title for the page
st.title("🤝 Your Personal Assistant")

# add subheader
st.subheader("What can your personal assistant do?")

# create a list of that our assistant can do
st.markdown("""
            1. Answer questions on various topics.   
            2. Arrange Calendar events and meetings.  
            3. Read your emails and send replies, can even summarize them for you.
            4. Manage your tasks and to-do lists.
            5. Take quick notes for you.
            6. Track your expenses and budgeting.
            """)

# add chats subheader
st.subheader("💬 Chat with your assistant")

# create a session state for message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# show the messages in chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# create a chat input box
user_message = st.chat_input()

# if user sends a message
if user_message:
    with st.chat_message("user"):
        st.markdown(user_message)
        st.session_state.messages.append({"role": "user", "content": user_message})

    try:
        response = requests.post(
            "http://localhost:5678/webhook/07f60269-d048-4724-b45a-64d999af8f84",
            json={"message": user_message},
            timeout=60
        )

        # Debug info 

        if response.text.strip():
            try:
                response_data = response.json()
                if isinstance(response_data, list):
                    ai_response = response_data[0].get("output") or response_data[0].get("text") or str(response_data[0])
                elif isinstance(response_data, dict):
                    ai_response = response_data.get("output") or response_data.get("text") or response_data.get("message") or str(response_data)
                else:
                    ai_response = str(response_data)
            except Exception:
                ai_response = response.text  # use raw text if not JSON
        else:
            ai_response = f"Empty response from n8n (status: {response.status_code})"

    except requests.exceptions.Timeout:
        ai_response = "Timed out — n8n took too long to respond"
    except requests.exceptions.ConnectionError:
        ai_response = "Cannot connect to n8n — is it running on port 5678?"
    except Exception as e:
        ai_response = f"Error: {str(e)}"

    with st.chat_message("assistant"):
        st.markdown(ai_response)
        st.session_state.messages.append({"role": "assistant", "content": ai_response})