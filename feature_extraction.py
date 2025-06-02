import pandas as pd
import re
from urllib.parse import urlparse

# Load your dataset
df = pd.read_csv("phishing_dataset.csv")

# Function to check if a string contains an IP address
def has_ip(url):
    return 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0

# Function to check for suspicious keywords
def has_suspicious_words(url):
    suspicious_keywords = ['login', 'verify', 'update', 'secure', 'account', 'bank', 'confirm', 'password']
    return 1 if any(word in url.lower() for word in suspicious_keywords) else 0

# Feature extraction function
def extract_features(url):
    parsed = urlparse(url)
    return pd.Series({
        "url_length": len(url),
        "num_dots": url.count('.'),
        "num_hyphens": url.count('-'),
        "has_https": 1 if parsed.scheme == "https" else 0,
        "has_ip_address": has_ip(url),
        "has_suspicious_words": has_suspicious_words(url),
    })

# Apply feature extraction to all rows
features = df['url'].apply(extract_features)

# Combine original labels with new features
new_df = pd.concat([features, df['label']], axis=1)

# Save to new file
new_df.to_csv("phishing_features.csv", index=False)

print("✅ Smart features extracted and saved to 'phishing_features.csv'")
