import streamlit as st

st.title("🎈 My new Streamlit app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
key = int(input("Enter the key"))
message = input("Enter the message")
alphabet = "abcdefghijklmnopqrstuvwxyz"
new_message = ""
for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position + key)
        new_character = alphabet[new_position]
        new_message += new_character
print(new_message)