# Import streamlit
import streamlit as st

# Necessary for streamlit sharing
st.set_page_config(page_title="Faithbot", page_icon="🙏", layout="centered", initial_sidebar_state="auto")

# Import necessary libraries
from src import vector_store
from src import rag_faithbot


def init():
    # Load the documents
    documents = vector_store.load_documents()

    # Split the documents
    chunks = vector_store.split_documents(documents)

    # Save the documents to Chroma
    vector_store.save_to_chroma(chunks)


# Run the app
def run():
    st.title("Faithbot with :parrot: :link: Langchain")
    st.write("Welcome to Faithbot! Faithbot is a chatbot that can help you with your faith. You can ask Faithbot about the Bible, Christianity, and more. Faithbot is here to help you with your faith journey.")
    st.write("To get started, type a question or message in the text box below and press Enter.")
    st.write("If you need help, type 'help' in the text box.")
    st.write("If you want to exit, type 'exit' in the text box.")
    st.write("Enjoy your conversation with Faithbot!")
    st.write("")

    # Initialize the app
    init()
    st.write("Faithbot is ready to help you with your faith. Please type a question or message in the text box below and press Enter.")

    # Chatbot
    user_input = st.text_input("You: ", "")
    if user_input:
        if user_input.lower() == "help":
            st.write("Faithbot: I am here to help you with your faith. You can ask me questions about the Bible, Christianity, and more. If you need help, just type 'help'. If you want to exit, type 'exit'. Enjoy your conversation with Faithbot!")
        elif user_input.lower() == "exit":
            st.write("Faithbot: Goodbye! Have a blessed day!")

        elif user_input:
            st.write(f"You: {user_input}")
            print(rag_faithbot.query_chroma(user_input))

        else:
            st.write("Faithbot: I am sorry, I do not understand. Please type 'help' for assistance or 'exit' to exit.")
    else:
        st.write("Faithbot: Hello! How can I help you today?")


# Run the app
if __name__ == "__main__":
    run()
