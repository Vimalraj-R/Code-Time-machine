import streamlit as st
import openai

# Azure OpenAI Configuration
openai.api_type = "azure"
openai.api_base = "https://mlloops-dev.openai.azure.com/"
openai.api_version = "2024-02-15-preview"
openai.api_key = "FyyR8OVcJTtbqLr3PLHx6EVjpUEegPIHzuwEYJpUEZ5dJknWOhGIJQQJ99BCACYeBjFXJ3w3AAABACOGXuN6"

DEPLOYMENT_NAME = "gpt-4o-mini"

# Function to analyze the code
def analyze_code_with_azure(code_snippet, summary_language="English"):
    if not code_snippet.strip():
        return "⚠️ It seems like you haven't provided any code. Please paste some code for analysis."

    prompt = f"""
You are Code Time Machine AI. The user provides you outdated or hard-to-understand legacy code.

Do the following tasks:
1. Explain what the code does.
2. Suggest modern improvements or updates.
3. Add missing documentation as comments or docstrings.
4. Give a simple summary in English.
5. Convert the legacy code into a modernized one in Python.
6. Finally, translate and provide the summary in {summary_language} language.

Code:
{code_snippet}
"""

    response = openai.ChatCompletion.create(
        engine=DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": "You are an expert AI that helps developers understand old code."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000
    )

    return response["choices"][0]["message"]["content"]


# Streamlit UI
st.set_page_config(page_title="Code Time Machine", layout="wide")
st.title("🕰️ Code Time Machine - Legacy Code Analyzer")

with st.sidebar:
    st.header("🛠️ Settings")
    summary_language = st.selectbox(
        "Choose your preferred language for the final summary:",
        ["English", "Tamil", "Hindi", "French", "German", "Spanish", "Chinese", "Japanese"]
    )
    st.markdown("---")
    st.markdown("💡 Paste any legacy or outdated code in the editor to get analysis and modern Python version.")

code_input = st.text_area("📄 Paste your legacy code here:", height=300, placeholder="Example: COBOL, Pascal, old C code...")

if st.button("🔍 Analyze Code"):
    st.info("Analyzing code with Code Time Machine AI... ⏳ Please wait.")
    result = analyze_code_with_azure(code_input, summary_language=summary_language)
    st.success("✅ Analysis Completed")
    st.markdown("---")
    st.markdown("### 📋 Full Analysis Result:")
    st.code(result, language="markdown")
