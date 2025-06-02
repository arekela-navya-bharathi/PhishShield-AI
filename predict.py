import joblib
import pandas as pd
from urllib.parse import urlparse
import re

model = joblib.load("phishing_model.pkl")

def has_ip(url):
    return 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0

def has_suspicious_words(url):
    suspicious_keywords = ['login', 'verify', 'update', 'secure', 'account', 'bank', 'confirm', 'password']
    return 1 if any(word in url.lower() for word in suspicious_keywords) else 0

def extract_features(url):
    parsed = urlparse(url)
    return pd.DataFrame([{
        "url_length": len(url),
        "num_dots": url.count('.'),
        "num_hyphens": url.count('-'),
        "has_https": 1 if parsed.scheme == "https" else 0,
        "has_ip_address": has_ip(url),
        "has_suspicious_words": has_suspicious_words(url),
    }])

def predict_url(url):
    features = extract_features(url)
    prediction = model.predict(features)[0]
    return "Phishing Website" if prediction == 1 else "Safe Website"
