import streamlit as st

def signin():
    st.title("Sign In")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin":  # Simple authentication
            st.success("Logged in successfully!")
            st.experimental_rerun()  # Redirect to the book recommendation app
        else:
            st.error
            ("Invalid username or password")

if __name__ == "__main__":
    signin()
