import streamlit as st
from transformers import pipeline

# Initialize the summarizer pipeline
summarizer = pipeline('text2text-generation', model='describeai/gemini-small')

# Streamlit app title
st.title("Code Summarizer")

# Text area for user to input code
code = st.text_area("Enter your code here:", height=300)

# Summarize button
if st.button("Summarize Code"):
    if code:
        with st.spinner("Summarizing..."):
            response = summarizer(code, max_length=500, num_beams=3)
            summarized_code = response[0]['generated_text']
        st.success("Code Summarized!")
        st.text_area("Summarized Code:", value=summarized_code, height=200)
    else:
        st.warning("Please enter some code to summarize.")


