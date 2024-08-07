import streamlit as st
from chatta_app.handler import OllamaHandler

DESC = """
`Chatta` is a simple chatbot demo with `Ollama` and `Streamlit`.
Easy usage with `Docker Compose`and clear python code.

Visit Github Repository: [p513817/ollama-streamlit](https://github.com/p513817/ollama-streamlit)
"""


def main():
    # Global Parameters
    OH = OllamaHandler()

    # Header
    st.header("Chatta")
    with st.expander("More details ...", expanded=True, icon="👋"):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(DESC)
        with col2:
            try:
                st.image("assets/chatta-qrcode.png", width=100)
            except Exception:
                st.image(
                    "https://github.com/p513817/ollama-streamlit/blob/master/assets/chatta-qrcode.png?raw=true",
                    width=100,
                )

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
                OH.add_message(
                    content=f"You are a chatbot which name Chatta. {DESC}",
                    role="system",
                )
                OH.add_message(content=prompt, role="user")
                response = st.write_stream(OH.stream_chat())
            except RuntimeError as e:
                st.error(f"RuntimeError: {e}")

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
