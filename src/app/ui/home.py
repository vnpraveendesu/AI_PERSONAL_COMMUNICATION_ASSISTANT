import streamlit as st


def main():
    st.set_page_config(
        page_title="AI Personal Communication Assistant", page_icon="🤖", layout="wide"
    )

    st.title("AI Personal Communication Assistant")

    st.write("""
        Foundation setup completed.

        Planned modules:

        - Gmail Integration
        - Microsoft Outlook Integration
        - Conversation Intelligence
        - Local AI Assistant
        - Analytics Dashboard
        - Reported Leave Intelligence
        - Voice Assistant
        """)


if __name__ == "__main__":
    main()
