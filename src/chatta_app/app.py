import httpx
import streamlit as st
from chatta_app.handler import OllamaHandler

DESC = """
`Chatta` is a simple chatbot demo with `Ollama` and `Streamlit`.
Easy usage with `Docker Compose`and clear python code.

Visit Github Repository: [p513817/ollama-streamlit](https://github.com/p513817/ollama-streamlit)
"""

# Init
if "USER_LOGIN" not in st.session_state:
    st.session_state.USER_LOGIN = False
if "USER_NAME" not in st.session_state:
    st.session_state.USER_NAME = ""
if "USER_DEPT" not in st.session_state:
    st.session_state.USER_DEPT = ""
if "FIRST_TIME" not in st.session_state:
    st.session_state.FIRST_TIME = True


# Helper
def is_login() -> bool:
    return st.session_state.USER_LOGIN


@st.dialog("Register")
def department_user():
    name = st.text_input("Name *")
    dept = st.text_input("Dept.")
    is_form_complete = name
    if st.button("Submit", use_container_width=True, disabled=not is_form_complete):
        with st.spinner("Communicating"):
            # Call API Here
            resp = httpx.post(
                "http://10.204.16.84:8000/submit/",
                params={"username": name, "department": dept},
            )
        print(resp, flush=True)
        st.success("Done")
        st.session_state.USER_LOGIN = True
        st.session_state.USER_NAME = name
        st.session_state.USER_DEPT = dept


@st.dialog("Report")
def report_form():
    feedback = st.text_area("Your Feedback", height=300)
    if st.button("Submit", use_container_width=True):
        with st.spinner("Communicating"):
            resp = httpx.post(
                "http://10.204.16.84:8000/report/",
                params={
                    "username": st.session_state.USER_NAME,
                    "department": st.session_state.USER_DEPT,
                    "feedback": feedback,
                },
            )
        print(resp.text, flush=True)
        st.success("Done")


def main():
    # Global Parameters
    OH = OllamaHandler()

    # Header
    st.header("Chatta")

    # Sidebar
    if not is_login():
        department_user()

    with st.sidebar:
        if st.button("Login", use_container_width=True):
            department_user()
        if st.button("Feedback", use_container_width=True):
            report_form()

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
                if st.session_state.FIRST_TIME:
                    OH.add_message(
                        content=f"Please say hello to user friendly and the user is {st.session_state.USER_NAME} who is belong the department: {st.session_state.USER_DEPT}",
                        role="system",
                    )
                    st.session_state.FIRST_TIME = False

                OH.add_message(
                    content=f"You are a chatbot which name Chatta. {DESC}",
                    role="system",
                )
                OH.add_message(
                    content="If user didn't ask for more detail please answer question within 100 words",
                    role="system",
                )
                OH.add_message(
                    content="If you don't know just tell user I don't know",
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
