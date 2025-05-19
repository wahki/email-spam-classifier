# 🚀 Email Spam Classification App

![Streamlit](https://img.shields.io/badge/Streamlit-✨%20Awesome-orange)  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![License](https://img.shields.io/badge/License-MIT-green)  

**Email Spam Classification App** is a real-time email spam classification application developed with Streamlit. It employs TF–IDF vectorization for feature extraction, a Multinomial Naive Bayes classifier for prediction, and joblib for efficient model serialization and loading.

> Maintain the integrity of your inbox by accurately identifying and filtering unwanted messages.

---

## 🔍 Features

- **Instant Predictions**  
  TF–IDF + MultinomialNB pipeline delivers results in milliseconds.
- **Streamlit UI**  
  Clean, interactive front-end for one-click spam detection.
- **Modular Design**  
  Model and vectorizer serialized with `joblib` for easy updates.
- **Easy Setup**  
  All dependencies listed in `requirements.txt`:  
  ```bash
  pip install -r requirements.txt

- **Open Source**
  MIT-licensed - customize and extend as you like.

## 🛠️ Installation & Usage

1. Clone The Repo
    ```bash
    git clone https://github.com/fatimesevilgen/email-spam-classifier.git
    cd email-spam-classifier
    ```

2. Create and activate a virtual environment (optional but recommended)
    ```bash
    python -m venv venv
    # macOS/Linux
    source venv/bin/activate
    # Windows
    venv\Scripts\activate
    ```

3. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Run The App
    ```bash
    streamlit run app.py
    ```

## 📁 Project Structure

```bash
email-spam-classifier/
    ├── predict.py                   # Predict method with model & vectorizer
    ├── app.py                       # Streamlit application code
    ├── spam_model.joblib            # Trained MultinomialNB model
    ├── tfidf_vectorizer.joblib      # Trained TF–IDF vectorizer
    ├── requirements.txt             # Python dependencies
    └── README.md                    # This file
```

## 🤝 Contributing

1. Fork this repository

2. Create a feature branch (git checkout -b feature/awesome-new)

3. Commit your changes (git commit -m "Add awesome new feature")

4. Push to your branch (git push origin feature/awesome-new)

5. Open a Pull Request 🚀

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 📬 Contact
Questions, suggestions, or just want to say hi?

- [Email](fatimesevilen@gmail.com)
- [Linkedin](https://www.linkedin.com/in/fatimesevilgen1/)
- [Github](https://github.com/fatimesevilgen)