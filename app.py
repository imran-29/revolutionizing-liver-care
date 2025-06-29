from flask import Flask, request, render_template, session, jsonify, redirect, url_for
import pickle
import numpy as np
import json

app = Flask(__name__)
app.secret_key = 'e639b1d68a62e4a79120c6cce497e932f08341781c6cfa3e'  # Demo key; generate a new one for deployment!

try:
    with open('xgb_best_model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    model = None

try:
    with open('feature_importances.json', 'r') as f:
        feat_importance = json.load(f)
except Exception as e:
    feat_importance = {}

FEATURES = [
    "Age", "Gender", "Place(location where the patient lives)",
    "Duration of alcohol consumption(years)", "Quantity of alcohol consumption (quarters/day)",
    "Type of alcohol consumed", "Hepatitis B infection", "Hepatitis C infection",
    "Diabetes Result", "Blood pressure (mmhg)", "Obesity",
    "Family history of cirrhosis/ hereditary", "TCH", "TG", "LDL", "HDL",
    "Hemoglobin  (g/dl)", "PCV  (%)", "MCV   (femtoliters/cell)",
    "Total Count", "Polymorphs  (%) ", "Lymphocytes  (%)",
    "Monocytes   (%)", "Eosinophils   (%)", "Basophils  (%)",
    "Platelet Count  (lakhs/mm)", "Total Bilirubin    (mg/dl)",
    "Direct    (mg/dl)", "Indirect     (mg/dl)", "Total Protein     (g/dl)",
    "Albumin   (g/dl)", "Globulin  (g/dl)", "AL.Phosphatase      (U/L)",
    "SGOT/AST      (U/L)", "SGPT/ALT (U/L)", "USG Abdomen (diffuse liver or  not)"
]

@app.route('/')
def home():
    if model is None:
        return "<h3 style='color:red;'>Model file not found. Please add 'xgb_best_model.pkl' and restart.</h3>", 500
    history = session.get('history', [])
    return render_template('index.html', prediction_text=None, history=history, feat_importance=feat_importance)

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return "<h3 style='color:red;'>Model file not found. Please add 'xgb_best_model.pkl' and restart.</h3>", 500
    try:
        values = [float(request.form[feature]) for feature in FEATURES]
        arr = np.array(values).reshape(1, -1)
        pred = model.predict(arr)[0]
        prob = model.predict_proba(arr)[0][1]
        result = "Patient is likely to have liver cirrhosis." if pred == 1 else "Patient is not likely to have liver cirrhosis."
        probability_percent = f"{prob*100:.1f}%"
    except Exception as e:
        result = f"Error: {e}"
        probability_percent = "N/A"

    input_summary = {
        "Age": request.form.get("Age"),
        "Gender": request.form.get("Gender"),
        "Alcohol Years": request.form.get("Duration of alcohol consumption(years)"),
        "Alcohol/day": request.form.get("Quantity of alcohol consumption (quarters/day)"),
        "Diabetes": request.form.get("Diabetes Result"),
        "BP": request.form.get("Blood pressure (mmhg)"),
    }
    history = session.get('history', [])
    history.insert(0, {
        "input": input_summary,
        "result": result,
        "prob": probability_percent
    })
    history = history[:10]
    session['history'] = history

    return render_template('index.html',
                           prediction_text=f"{result} (Confidence: {probability_percent})",
                           history=history,
                           feat_importance=feat_importance)

@app.route('/api/predict', methods=['POST'])
def api_predict():
    if model is None:
        return jsonify({'error': "Model not available."}), 500
    data = request.json
    try:
        values = [float(data[feature]) for feature in FEATURES]
        arr = np.array(values).reshape(1, -1)
        pred = int(model.predict(arr)[0])
        prob = float(model.predict_proba(arr)[0][1])
        return jsonify({'prediction': pred, 'probability': prob})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/about')
def about():
    return render_template('inner-page.html')

@app.route('/modelinfo')
def modelinfo():
    return render_template('portfolio-details.html')

@app.route('/clear-session')
def clear_session():
    session.clear()
    return redirect(url_for('home'))

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html", error=str(e)), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)

