import streamlit as st
from chatta_app.handler import OllamaHandler


def main():
    # Global Parameters
    OH = OllamaHandler()

    # Header
    st.header("Chatta-ChatBot")

    # Chat Input
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            try:
                OH.add_message(content=prompt, role="user")
                response = st.write_stream(OH.stream_chat())
            except RuntimeError as e:
                st.error(f"RuntimeError: {e}")

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
