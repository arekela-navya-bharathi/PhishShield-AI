import streamlit as st
from predict import predict_url

st.set_page_config(page_title="PhishShield-AI url scanner", page_icon="🛡️", layout="centered")

st.markdown("<h1 style='text-align: center; color: #0ff; text-shadow: 1px 1px 2px #000;'>🛡️ PhishShield-AI: Phishing URL Detector</h1>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: #ccc;'>Be Aware. Stay Secure.</h4>", unsafe_allow_html=True)

url_input = st.text_input("🔗 Enter a URL to check:", placeholder="e.g. http://free-money-now.win")

if st.button("🔍 Scan"):
    if url_input.strip() == "":
        st.warning("Please enter a URL.")
    else:
        result = predict_url(url_input)
        if "Phishing" in result:
            st.error(f"🚨 {result}")
        else:
            st.success(f"🟢 {result}")


st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 13px; color: gray;'>Built with ❤️ by Navya | AI + Cybersecurity Project</p>", unsafe_allow_html=True)
