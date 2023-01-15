# Stream lit is a service which running in background 
# it an host it online and deploy .
# its a ibraray to create web pages

import streamlit as st

st.title("String App ")
message =st.text_area("Enter some text")
button = st.button("Process Text")

if button:
    st.write(message)
if st.sidebar.checkbox("Show Words"):
    words = message.split()
    st.write(words)
if st.sidebar.checkbox("Character count"):
    for char in message:
        st.write(f'{char} : {message.count(char)}')
    