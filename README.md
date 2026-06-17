# 🔐 Password Strength Checker

> A smart, interactive password security analyzer built with Python and Streamlit. Evaluates password strength in real-time, estimates brute-force crack time, and tracks your password history — all in a clean web UI.

🔗 **Live Demo:** [password-strength-checker-ayesha-shahzaib.streamlit.app](https://password-strength-checker-ayesha-shahzaib.streamlit.app/)

---

## ✨ Features

- 🔍 **Real-time strength analysis** — checks length, uppercase, lowercase, digits, and special characters
- ⏱️ **Crack time estimator** — calculates how long a brute-force attack would take (from seconds to centuries)
- 📋 **Password history table** — tracks previously tested passwords using masked display for privacy
- 🔒 **Privacy-first** — passwords are masked, never stored in plain text
- 📊 **Interactive data grid** — sortable, filterable history table powered by AgGrid

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core logic & backend |
| Streamlit | Web UI framework |
| Pandas | Data handling & history table |
| st-aggrid | Interactive data grid |
| Regex | Pattern matching for character validation |

---

## 🧠 How It Works

1. User enters a password in the secure input field
2. The app checks against 5 security criteria (length, uppercase, lowercase, digits, special chars)
3. If all pass → password is marked **Strong** with an estimated crack time
4. Crack time is calculated based on charset size and brute-force speed (1 trillion guesses/sec)
5. The masked password and crack time are logged to the history table

---

## 🚀 Run Locally

```bash
git clone https://github.com/AyeshaShahzaib/Password-Strength-Checker.git
cd Password-Strength-Checker
pip install -r requirements.txt
streamlit run app.py
```

---

## 👩‍💻 Author

**Ayesha Shahzaib**
- GitHub: [@AyeshaShahzaib](https://github.com/AyeshaShahzaib)
- Email: ayeshashahzaib007@gmail.com

---

⭐ Found this useful? Give it a star!
