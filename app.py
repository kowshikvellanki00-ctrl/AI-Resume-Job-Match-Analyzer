import streamlit as st
import google.generativeai as genai

st.title("AI Resume & Job Match Analyzer")

api_key = st.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-1.5-flash')

    resume = st.text_area("Paste Resume")

    job_description = st.text_area("Paste Job Description")

    if st.button("Analyze Resume"):

        prompt = f'''
        Analyze this resume against the job description.

        Give:
        - Match percentage
        - Missing skills
        - ATS suggestions
        - Final recommendation

        Resume:
        {resume}

        Job Description:
        {job_description}
        '''

        response = model.generate_content(prompt)

        st.write(response.text)
