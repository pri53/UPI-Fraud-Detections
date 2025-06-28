
# from flask import Flask, request, jsonify
# import pandas as pd
# import joblib
# from datetime import datetime
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)
# model = joblib.load('model/model.pkl')

# def preprocess_data(transaction):
#     features = {
#         'amount': float(transaction['amount']),
#         'hour': datetime.strptime(transaction['time'], '%H:%M').hour,
#         'is_foreign': int(transaction['from'][:2] != transaction['to'][:2]),
#         'transaction_length': len(transaction['transaction_id']),
#         'from_bank': 1 if 'bank' in transaction['from'].lower() else 0,
#         'to_bank': 1 if 'bank' in transaction['to'].lower() else 0
#     }
#     return pd.DataFrame([features])

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     processed_data = preprocess_data(data)
#     prediction = model.predict(processed_data)
#     return jsonify({
#         'status': 'fraud' if prediction[0] == 1 else 'legitimate',
#         'confidence': float(model.predict_proba(processed_data)[0][1])
#     })

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, jsonify
# import pandas as pd
# import joblib
# from datetime import datetime
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app, resources={r"/predict": {"origins": "http://localhost:3002"}})


# model = joblib.load('model/model.pkl')


# # Load model with error handling
# try:
#     model = joblib.load('model/model.pkl')
#     print("✅ Model loaded successfully!", flush=True)
# except Exception as e:
#     print("❌ Model load failed:", e, flush=True)I
#     model = None

# def preprocess_data(transaction):
#     try:
#         print("🔍 Preprocessing input:", transaction, flush=True)
#         features = {
#             'amount': float(transaction['amount']),
#             'hour': datetime.strptime(transaction['time'], '%H:%M').hour,
#             'is_foreign': int(transaction['from'][:2] != transaction['to'][:2]),
#             'transaction_length': len(transaction['transaction_id']),
#             'from_bank': 1 if 'bank' in transaction['from'].lower() else 0,
#             'to_bank': 1 if 'bank' in transaction['to'].lower() else 0
#         }
#         print("✅ Preprocessing successful:", features, flush=True)
#         return pd.DataFrame([features])
#     except Exception as e:
#         print("❌ Preprocessing error:", e, flush=True)
#         return None

# @app.route('/predict', methods=['POST'])
# def predict():
#     print("📩 Received /predict POST request", flush=True)
#     if model is None:
#         print("❌ No model loaded", flush=True)
#         return jsonify({'prediction': 'error', 'confidence': 0.0})

#     try:
#         data = request.json
#         print("🧾 Incoming JSON data:", data, flush=True)
#         processed_data = preprocess_data(data)

#         if processed_data is None:
#             return jsonify({'prediction': 'error', 'confidence': 0.0})

#         prediction = model.predict(processed_data)[0]
#         confidence = model.predict_proba(processed_data)[0][1]

#         result = {
#             'prediction': 'Fraud' if prediction == 1 else 'Legit',
#             'confidence': round(confidence * 100, 2)
#         }

#         print("✅ Prediction result:", result, flush=True)
#         return jsonify(result)

#     except Exception as e:
#         print("❌ Prediction error:", e, flush=True)
#         return jsonify({'prediction': 'error', 'confidence': 0.0})

# # if __name__ == '__main__':
# #     print("🚀 Starting Flask server...", flush=True)
# #     app.run(debug=True)

# if __name__ == '__main__':
#     print("✅ Model loaded successfully!\n🚀 Starting Flask server...")
#     app.run(host='0.0.0.0', port=5050, debug=True)




# from flask import Flask, request, jsonify
# import pandas as pd
# import joblib
# from datetime import datetime
# from flask_cors import CORS
# import google.generativeai as genai
# import os

# app = Flask(__name__)
# CORS(app, resources={
#     r"/predict": {"origins": "http://localhost:3002"},
#     r"/chat": {"origins": "http://localhost:3002"}
# })

# # Load fraud detection model
# try:
#     model = joblib.load('model/model.pkl')
#     print("✅ Fraud detection model loaded successfully!", flush=True)
# except Exception as e:
#     print("❌ Fraud detection model load failed:", e, flush=True)
#     model = None

# # Configure Gemini AI
# try:
#     genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
#     gemini_model = genai.GenerativeModel('gemini-pro')
#     print("✅ Gemini AI configured successfully!", flush=True)
# except Exception as e:
#     print("❌ Gemini AI configuration failed:", e, flush=True)
#     gemini_model = None

# def preprocess_data(transaction):
#     try:
#         print("🔍 Preprocessing input:", transaction, flush=True)
#         features = {
#             'amount': float(transaction['amount']),
#             'hour': datetime.strptime(transaction['time'], '%H:%M').hour,
#             'is_foreign': int(transaction['from'][:2] != transaction['to'][:2]),
#             'transaction_length': len(transaction['transaction_id']),
#             'from_bank': 1 if 'bank' in transaction['from'].lower() else 0,
#             'to_bank': 1 if 'bank' in transaction['to'].lower() else 0
#         }
#         print("✅ Preprocessing successful:", features, flush=True)
#         return pd.DataFrame([features])
#     except Exception as e:
#         print("❌ Preprocessing error:", e, flush=True)
#         return None

# @app.route('/predict', methods=['POST'])
# def predict():
#     print("📩 Received /predict POST request", flush=True)
#     if model is None:
#         print("❌ No model loaded", flush=True)
#         return jsonify({'status': 'error', 'message': 'Model not loaded'}), 500

#     try:
#         data = request.json
#         print("🧾 Incoming JSON data:", data, flush=True)
#         processed_data = preprocess_data(data)

#         if processed_data is None:
#             return jsonify({'status': 'error', 'message': 'Data preprocessing failed'}), 400

#         prediction = model.predict(processed_data)[0]
#         confidence = model.predict_proba(processed_data)[0][1]

#         result = {
#             'status': 'success',
#             'prediction': 'fraud' if prediction == 1 else 'legitimate',
#             'confidence': round(float(confidence) * 100, 2)
#         }

#         print("✅ Prediction result:", result, flush=True)
#         return jsonify(result)

#     except Exception as e:
#         print("❌ Prediction error:", e, flush=True)
#         return jsonify({'status': 'error', 'message': str(e)}), 500

# @app.route('/chat', methods=['POST'])
# def chat():
#     if gemini_model is None:
#         return jsonify({'status': 'error', 'message': 'Chat service not available'}), 500
    
#     try:
#         data = request.json
#         prompt = data.get('prompt', '')
        
#         if not prompt.lower().strip():
#             return jsonify({'status': 'error', 'message': 'Empty prompt'}), 400
            
#         # Add context to only answer UPI-related questions
#         upi_context = """
#         You are a specialized assistant for UPI (Unified Payments Interface) transactions and fraud detection. 
#         Only answer questions related to UPI payments, transactions, security, and fraud prevention.
#         For any other topics, respond with: "I can only assist with UPI-related questions."
        
#         User question: """
        
#         response = gemini_model.generate_content(upi_context + prompt)
#         return jsonify({
#             'status': 'success',
#             'response': response.text
#         })
        
#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)}), 500

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5050, debug=True)




from flask import Flask, request, jsonify
import pandas as pd
import joblib
from datetime import datetime
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()  # Add this at the top



app = Flask(__name__)
CORS(app, resources={
    r"/predict": {"origins": "http://localhost:3000"},
    r"/chat": {"origins": "http://localhost:3000"}
})


# Load model and encoders
try:
    model = joblib.load('model/model.pkl')
    le_from = joblib.load('model/le_from.pkl')
    le_to = joblib.load('model/le_to.pkl')
    le_time = joblib.load('model/le_time.pkl')
    le_location = joblib.load('model/le_location.pkl')
    le_area = joblib.load('model/le_area.pkl')
    print("✅ Model and encoders loaded successfully!", flush=True)
except Exception as e:
    print("❌ Failed to load model or encoders:", e, flush=True)
    model = None


# Configure Gemini AI
# try:
#     load_dotenv()  # Add this at the top
#     genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
#     gemini_model = genai.GenerativeModel('gemini-pro')
#     print("✅ Gemini AI configured successfully!", flush=True)
# except Exception as e:
#     print("❌ Gemini AI configuration failed:", e, flush=True)
#     gemini_model = None

try:
    load_dotenv()
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
    gemini_model = genai.GenerativeModel(
        'gemini-2.0-flash',
        safety_settings=[
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
        ]
    )
    print("✅ Gemini AI configured successfully!", flush=True)
except Exception as e:
    print("❌ Gemini AI configuration failed:", e, flush=True)
    gemini_model = None


# def preprocess_data(transaction):
#     try:
#         print("🔍 Preprocessing input:", transaction, flush=True)
#         features = {
#             'amount': float(transaction['amount']),
#             'hour': datetime.strptime(transaction['time'], '%H:%M').hour,
#             'is_foreign': int(transaction['from'][:2] != transaction['to'][:2]),
#             'transaction_length': len(transaction['transaction_id']),
#             'from_bank': 1 if 'bank' in transaction['from'].lower() else 0,
#             'to_bank': 1 if 'bank' in transaction['to'].lower() else 0
#         }

        
#         print("✅ Preprocessing successful:", features, flush=True)
#         return pd.DataFrame([features])
#     except Exception as e:
#         print("❌ Preprocessing error:", e, flush=True)
#         return None

# def preprocess_data(transaction):
#     try:
#         print("🔍 Preprocessing input:", transaction, flush=True)
#         features = {
#             'amount': float(transaction['amount']),
#             'hour': datetime.strptime(transaction['time'], '%H:%M').hour,
#             'is_foreign': int(transaction['from'][:2] != transaction['to'][:2]),
#             'transaction_length': len(transaction['transaction_id']),
#             'from_bank': 1 if 'bank' in transaction['from'].lower() else 0,
#             'to_bank': 1 if 'bank' in transaction['to'].lower() else 0
#         }

        
#         print("✅ Preprocessing successful:", features, flush=True)
#         return pd.DataFrame([features])
#     except Exception as e:
#         print("❌ Preprocessing error:", e, flush=True)

#         return None

def safe_transform(le, value, fallback='unknown'):
    # Add 'unknown' to encoder if it's not already there
    if fallback not in le.classes_:
        le.classes_ = list(le.classes_) + [fallback]
    # Use actual value if seen, else fallback
    return le.transform([value if value in le.classes_ else fallback])[0]


# def preprocess_data(transaction):
#     try:
#         print("🔍 Preprocessing input:", transaction, flush=True)

#         # Encode each categorical value using the label encoders
#         from_upi = le_from.transform([transaction['from']])[0]
#         to_upi = le_to.transform([transaction['to']])[0]
#         time = le_time.transform([transaction['time']])[0]
#         location = le_location.transform([transaction['location']])[0]
#         area = le_area.transform([transaction['area']])[0]
#         amount = float(transaction['amount'].replace("₹", "").replace(",", ""))

#         features = {
#             'from_upi': from_upi,
#             'to_upi': to_upi,
#             'time': time,
#             'location': location,
#             'area': area,
#             'amount': amount
#         }

#         print("✅ Preprocessing successful:", features, flush=True)
#         return pd.DataFrame([features])

#     except Exception as e:
#         print("❌ Preprocessing error:", e, flush=True)
#         return None

def preprocess_data(transaction):
    try:
        print("🔍 Preprocessing input:", transaction, flush=True)

        from_upi = safe_transform(le_from, transaction['from'])
        to_upi = safe_transform(le_to, transaction['to'])
        time = safe_transform(le_time, transaction['time'])
        location = safe_transform(le_location, transaction['location'])
        area = safe_transform(le_area, transaction['area'])
        amount = float(transaction['amount'].replace("₹", "").replace(",", ""))

        features = {
            'from_upi': from_upi,
            'to_upi': to_upi,
            'time': time,
            'location': location,
            'area': area,
            'amount': amount
        }

        print("✅ Preprocessing successful:", features, flush=True)
        return pd.DataFrame([features])

    except Exception as e:
        print("❌ Preprocessing error:", e, flush=True)
        return None


    
    
@app.route('/', methods=['GET'])
def home():
    return "<h1>UPI Fraud Detection API is running ✅</h1>"    


@app.route('/predict', methods=['POST'])

def predict():
    print("📩 Received /predict POST request", flush=True)

    if model is None:
        print("❌ No model loaded", flush=True)
        return jsonify({'status': 'error', 'message': 'Model not loaded'}), 500

    try:
        data = request.json
        print("🧾 Incoming JSON data:", data, flush=True)

        # Preprocess the input data
        processed_data = preprocess_data(data)  # assumes your function loads encoders inside

        if processed_data is None:
            return jsonify({'status': 'error', 'message': 'Data preprocessing failed'}), 400

        # Perform prediction
        prediction = model.predict(processed_data)[0]

        # Handle case when predict_proba is not available (some models might not support it)
        try:
            confidence = model.predict_proba(processed_data)[0][1]
        except AttributeError:
            confidence = 0.5  # default fallback confidence

        # Prepare result
        is_fraud = prediction == 1
        result = {
            'status': 'success',
            'prediction': 'fraud' if is_fraud else 'legitimate',
            'confidence': round(float(confidence) * 100, 2)
        }

        # Only show complaint-related steps for fraud
        if is_fraud:
            result['action_required'] = {
                'register_complaint': True,
                'complaint_links': {
                    'national_cyber_crime_portal': 'https://cybercrime.gov.in/',
                    'rbi_banking_ombudsman': 'https://rbi.org.in/Scripts/Complaints.aspx',
                    'upi_dispute_resolution': 'https://www.npci.org.in/what-we-do/upi/dispute-resolution-mechanism'
                },
                'steps_to_follow': [
                    "Immediately contact your bank",
                    "Freeze the affected account if necessary",
                    "Gather all transaction details",
                    "File a complaint with your bank first",
                    "Then file with the National Cyber Crime Portal"
                ]
            }

        print("✅ Prediction result:", result, flush=True)
        return jsonify(result)

    except Exception as e:
        print("❌ Prediction error:", e, flush=True)
        return jsonify({'status': 'error', 'message': str(e)}), 500


# def predict():
#     print("📩 Received /predict POST request", flush=True)

#     if model is None:
#         print("❌ No model loaded", flush=True)
#         return jsonify({'status': 'error', 'message': 'Model not loaded'}), 500

#     try:
#         data = request.json
#         print("🧾 Incoming JSON data:", data, flush=True)

#         # ✅ Preprocess after data is available
#         # processed_data = preprocess_data(
#         #     data, le_from, le_to, le_time, le_location, le_area
#         # )
#         processed_data = preprocess_data(data)


#         if processed_data is None:
#             return jsonify({'status': 'error', 'message': 'Data preprocessing failed'}), 400

#         # ✅ Run prediction
#         prediction = model.predict(processed_data)[0]
#         confidence = model.predict_proba(processed_data)[0][1]

#         # ✅ Prepare result
#         is_fraud = prediction == 1
#         result = {
#             'status': 'success',
#             'prediction': 'fraud' if is_fraud else 'legitimate',
#             'confidence': round(float(confidence) * 100, 2)
#         }

#         # ✅ Add complaint registration info if it's fraud
#         if is_fraud:
#             result['action_required'] = {
#                 'register_complaint': True,
#                 'complaint_links': {
#                     'national_cyber_crime_portal': 'https://cybercrime.gov.in/',
#                     'rbi_banking_ombudsman': 'https://rbi.org.in/Scripts/Complaints.aspx',
#                     'upi_dispute_resolution': 'https://www.npci.org.in/what-we-do/upi/dispute-resolution-mechanism'
#                 },
#                 'steps_to_follow': [
#                     "Immediately contact your bank",
#                     "Freeze the affected account if necessary",
#                     "Gather all transaction details",
#                     "File a complaint with your bank first",
#                     "Then file with the National Cyber Crime Portal"
#                 ]
#             }

#         print("✅ Prediction result:", result, flush=True)
#         return jsonify(result)

#     except Exception as e:
#         print("❌ Prediction error:", e, flush=True)
#         return jsonify({'status': 'error', 'message': str(e)}), 500

# def predict():
#     processed_data = preprocess_data(
#     data, le_from, le_to, le_time, le_location, le_area
# )

#     print("📩 Received /predict POST request", flush=True)
#     if model is None:
#         print("❌ No model loaded", flush=True)
#         return jsonify({'status': 'error', 'message': 'Model not loaded'}), 500

#     try:
#         data = request.json
#         print("🧾 Incoming JSON data:", data, flush=True)
#         processed_data = preprocess_data(data)

#         if processed_data is None:
#             return jsonify({'status': 'error', 'message': 'Data preprocessing failed'}), 400

#         prediction = model.predict(processed_data)[0]
#         confidence = model.predict_proba(processed_data)[0][1]


#         result = {
#             'status': 'success',
#             'prediction': 'fraud' if prediction == 1 else 'legitimate',
#             'confidence': round(float(confidence) * 100, 2)
#         }

#         # Define is_fraud before using it
#         is_fraud = prediction == 1
#         result = {
#             'status': 'success',
#             'prediction': 'fraud' if is_fraud else 'legitimate',
#             'confidence': round(float(confidence) * 100, 2)
#         }

#         # Add complaint registration info if fraud is detected
#         if is_fraud:
#             result['action_required'] = {
#                 'register_complaint': True,
#                 'complaint_links': {
#                     'national_cyber_crime_portal': 'https://cybercrime.gov.in/',
#                     'rbi_banking_ombudsman': 'https://rbi.org.in/Scripts/Complaints.aspx',
#                     'upi_dispute_resolution': 'https://www.npci.org.in/what-we-do/upi/dispute-resolution-mechanism'
#                 },
#                 'steps_to_follow': [
#                     "Immediately contact your bank",
#                     "Freeze the affected account if necessary",
#                     "Gather all transaction details",
#                     "File a complaint with your bank first",
#                     "Then file with the National Cyber Crime Portal"
#                 ]
#             }

        

#         print("✅ Prediction result:", result, flush=True)
#         return jsonify(result)

#     except Exception as e:
#         print("❌ Prediction error:", e, flush=True)
#         return jsonify({'status': 'error', 'message': str(e)}), 500
    

    

# @app.route('/chat', methods=['POST'])
# def chat():
#     if gemini_model is None:
#         return jsonify({'status': 'error', 'message': 'Chat service not available'}), 500
    
#     try:
#         data = request.json
#         prompt = data.get('prompt', '')
        
#         if not prompt.lower().strip():
#             return jsonify({'status': 'error', 'message': 'Empty prompt'}), 400
            
#         # Add context to only answer UPI-related questions
#         upi_context = """
#         You are a specialized assistant for UPI (Unified Payments Interface) transactions and fraud detection. 
#         Only answer questions related to UPI payments, transactions, security, and fraud prevention.
#         For any other topics, respond with: "I can only assist with UPI-related questions."
        
#         User question: """
        
#         response = gemini_model.generate_content(upi_context + prompt)
#         return jsonify({
#             'status': 'success',
#             'response': response.text
#         })
        
    # except Exception as e:
    #     return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/chat', methods=['POST'])
def chat():
    if gemini_model is None:
        return jsonify({
            'status': 'error',
            'message': 'Chat service not available - check Gemini API configuration'
        }), 500
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                'status': 'error',
                'message': 'No JSON data received'
            }), 400
            
        prompt = data.get('prompt', '').strip()
        if not prompt:
            return jsonify({
                'status': 'error',
                'message': 'Empty prompt received'
            }), 400
        
        upi_context = """You are a UPI expert. Only answer UPI-related questions about:
        - Transactions
        - Fraud prevention
        - Payment issues
        - Security
        
        For other topics, respond: "I specialize in UPI questions only."
        
        Question: """
        
        response = gemini_model.generate_content(
            upi_context + prompt,
            safety_settings={
                'HARM_CATEGORY_HARASSMENT': 'BLOCK_NONE',
                'HARM_CATEGORY_HATE_SPEECH': 'BLOCK_NONE',
                'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'BLOCK_NONE',
                'HARM_CATEGORY_DANGEROUS_CONTENT': 'BLOCK_NONE'
            }
        )
        
        return jsonify({
            'status': 'success',
            'response': response.text
        })
        
    except Exception as e:
        print(f"❌ Chat error: {str(e)}", flush=True)
        return jsonify({
            'status': 'error',
            'message': f"Chat processing failed: {str(e)}"
        }), 500   

if __name__ == '__main__':
     if not os.path.exists('model/model.pkl'):
        print("❌ Model file not found at 'model/model.pkl'", flush=True)
    
    # Verify .env exists 
    
     if not os.path.exists('.env'):
        print("❌ .env file not found in root directory", flush=True)
    
     else:
        print("✅ .env file found", flush=True)
        if not os.getenv('GEMINI_API_KEY'):
            print("❌ GEMINI_API_KEY not found in .env", flush=True)
    
    
     app.run(host='0.0.0.0', port=5051, debug=True)