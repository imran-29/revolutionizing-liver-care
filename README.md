# liver-cirrhosis-app
# 🩺 Liver Cirrhosis Prediction App

A machine learning-powered web application to predict the likelihood of **Liver Cirrhosis** using patient medical data.  
Built with Flask and an XGBoost model, the app provides real-time predictions with visual insights.

---

## 🚀 Key Features

- 🧠 **ML-Based Prediction**: Uses an XGBoost model trained on medical data.
- 🧾 **User-Friendly Form**: Collects patient info via an interactive web interface.
- 📊 **Feature Importance Visualization**: Understand which features influenced the result.
- 📋 **PDF & CSV Export**: Save prediction results for future reference.
- 📈 **Liver Enzyme Chart**: Visualize SGOT, SGPT, and ALP enzyme levels.
- 🧩 **Session History**: View past predictions in your session.

---

## 💻 Tech Stack

| Component     | Technology         |
|---------------|--------------------|
| Backend       | Python (Flask)     |
| Frontend      | HTML, Bootstrap 5  |
| ML Model      | XGBoost            |
| Libraries     | NumPy, Pandas, scikit-learn |

---

## 📂 Project Structure

📦 liver-cirrhosis-predictor/
├── app.py
├── xgb_best_model.pkl
├── feature_importances.json
├── requirements.txt
├── templates/
│ ├── index.html
│ ├── form_section.html
│ ├── charts_section.html
│ ├── result_section.html
│ ├── base.html
│ ├── inner-page.html
│ └── portfolio-details.html

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/imran-29/revolutionizing-liver-care.git
cd revolutionizing-liver-care
2. Create and Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # macOS/Linux
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the App
bash
Copy
Edit
python app.py
Then open your browser at 👉 http://localhost:5000

🔍 Model Details
Model: XGBoost Classifier

File: xgb_best_model.pkl

Feature Importance loaded from: feature_importances.json

📈 Visual Output
Bar charts showing liver enzyme levels and most influential features.

Prediction output with confidence level.

Example autofill data for quick testing.

✨ Example Prediction
Prediction: Patient is likely to have liver cirrhosis.

Confidence: 97.6%

Key Factors: Duration of alcohol consumption, Total Bilirubin, USG results.
