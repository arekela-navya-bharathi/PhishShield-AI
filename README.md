# PhishShield-AI

# CyberSafe: Phishing URL Detector

🛡️ **CyberSafe: Phishing URL Detector** is an AI-powered web application designed to identify phishing websites by analyzing URLs using smart feature extraction and a Random Forest classification model.

---

## About the Project

This project was developed by **Arekela Navya Bharathi** as part of an AI + Cybersecurity initiative to build a real-time phishing detection tool. Phishing attacks are a major cybersecurity threat where attackers create fake websites to steal sensitive information. This tool helps users identify potentially dangerous URLs before they fall victim.

---

## How It Works

The detection model uses the following features extracted from the URL:

- **URL Length:** Phishing URLs tend to be longer to obfuscate malicious parts.  
- **Number of Dots:** Excessive subdomains can indicate phishing.  
- **Number of Hyphens:** Hyphens are often used in fake URLs to mimic legitimate ones.  
- **HTTPS Presence:** Legitimate sites usually use HTTPS; lack of it is suspicious.  
- **IP Address in URL:** Using an IP address instead of a domain name is a red flag.  
- **Suspicious Keywords:** Words like "login", "verify", "update", "secure", "account", "bank", "confirm", and "password" are often found in phishing URLs.

A Random Forest classifier was trained on a labeled dataset of phishing and safe URLs using these features. The model then predicts whether an input URL is safe or potentially phishing.

---

## How to Run

1. **Clone the repository**

```bash
git clone https://github.com/arekela-navya-bharathi/PhishShield-AI.git
cd PhishShield-AI


```
2.Install dependencies

Make sure you have Python installed (preferably 3.7 or above).

```bash

pip install -r requirements.txt

```

3.Run the Streamlit app

```bash
streamlit run app.py
```


4.Use the web app

Enter URLs in the input box to check if they are phishing or safe. The app provides real-time feedback with a clean, cyber-safe themed interface.




Sample URLs to Test
Safe:

https://www.google.com

https://github.com

https://openai.com

Phishing (likely flagged):

http://free-money-now.win

http://verify-account-secure.com

http://login-bank-account-update.info
