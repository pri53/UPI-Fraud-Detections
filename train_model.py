
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier # type: ignore
# from sklearn.model_selection import train_test_split
# import joblib

# df = pd.read_csv('/Users/akshithgoud/Desktop/upi-fraud-detection/backend/data/fake_upi_dataset.csv')

# df['hour'] = pd.to_datetime(df['Time'], format='%H:%M').dt.hour
# df['is_foreign'] = df['From'].str[:2] != df['To'].str[:2]
# df['transaction_length'] = df['Transaction_ID'].apply(len)
# df['from_bank'] = df['From'].str.contains('bank', case=False).astype(int)
# df['to_bank'] = df['To'].str.contains('bank', case=False).astype(int)
# df['transaction_length'] = df['Transaction_ID'].apply(len)

# features = ['Amount', 'hour', 'is_foreign', 'transaction_length', 'from_bank', 'to_bank']
# X = df[features]
# y = df['label']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# model = RandomForestClassifier()
# model.fit(X_train, y_train)

# joblib.dump(model, 'model/model.pkl')
# print("✅ Model trained and saved.")



# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# import joblib
# import os

# # Load the dataset
# df = pd.read_csv('data/fake_upi_dataset.csv')  # adjust path if needed

# # Clean and normalize column names
# df.columns = df.columns.str.strip().str.lower()

# # Rename columns to match access pattern
# df.rename(columns={
#     'from': 'from_user',
#     'to': 'to_user',
#     'time': 'time',
#     'transaction_id': 'transaction_id',
#     'amount': 'amount',
#     'label': 'label'
# }, inplace=True)

# # Feature Engineering
# df['hour'] = pd.to_datetime(df['time'], format='%H:%M').dt.hour
# df['is_foreign'] = df['from_user'].str[:2] != df['to_user'].str[:2]
# df['transaction_length'] = df['transaction_id'].apply(len)
# df['from_bank'] = df['from_user'].str.contains('bank', case=False).astype(int)
# df['to_bank'] = df['to_user'].str.contains('bank', case=False).astype(int)

# # Define features and labels
# features = ['amount', 'hour', 'is_foreign', 'transaction_length', 'from_bank', 'to_bank']
# X = df[features]
# y = df['label']

# # Split the dataset
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train the model
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)

# # Ensure the model directory exists
# os.makedirs("model", exist_ok=True)

# # Save the trained model
# joblib.dump(model, 'model/model.pkl')
# print("✅ Model trained and saved to model/model.pkl")


# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# import joblib
# import os

# # Load dataset
# df = pd.read_csv('\/Users/akshithgoud/Desktop/upi-fraud-detection/backend/data/upi_transaction_dataset.csv')

# # Clean column names
# df.columns = df.columns.str.strip().str.lower()

# # Label encode categorical features
# le_sender = LabelEncoder()
# le_receiver = LabelEncoder()
# le_time = LabelEncoder()

# df['sender_domain'] = le_sender.fit_transform(df['sender_domain'])
# df['receiver_domain'] = le_receiver.fit_transform(df['receiver_domain'])
# df['time_of_day'] = le_time.fit_transform(df['time_of_day'])

# # Features to use
# features = [
#     'amount',
#     'hour',
#     'minute',
#     'sender_domain',
#     'receiver_domain',
#     'same_domain',
#     'time_of_day',
#     'log_amount'
# ]

# X = df[features]
# y = df['label']

# # Split data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train model
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)

# # Ensure model directory exists
# os.makedirs("model", exist_ok=True)

# # Save model
# joblib.dump(model, 'model/model.pkl')

# print("✅ Model trained and saved to model/model.pkl")



# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# import joblib
# import os

# # Load dataset
# df = pd.read_csv('/Users/akshithgoud/Desktop/upi-fraud-detection/backend/data/updated_location dataset.csv')  # Adjust path as needed

# # Clean column names
# df.columns = df.columns.str.strip().str.lower()

# encoders = {}

# # Label encode new fields
# le_from = LabelEncoder()
# le_to = LabelEncoder()
# le_location = LabelEncoder()
# le_area = LabelEncoder()
# le_time = LabelEncoder()


# df['from_upi'] = le_from.fit_transform(df['from_upi'])
# df['to_upi'] = le_to.fit_transform(df['to_upi'])
# df['location'] = le_location.fit_transform(df['location'])
# df['area'] = le_area.fit_transform(df['area'])
# df['time'] = le_time.fit_transform(df['time'])

# # Features and label
# features = ['from_upi', 'to_upi', 'time', 'location', 'area', 'amount']
# X = df[features]
# y = df['label']



# # Train/test split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train model
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)



# # Save model and encoders
# os.makedirs("model", exist_ok=True)
# joblib.dump(model, 'model/model.pkl')
# joblib.dump(le_from, 'model/le_from.pkl')
# joblib.dump(le_to, 'model/le_to.pkl')
# joblib.dump(le_location, 'model/le_location.pkl')
# joblib.dump(le_area, 'model/le_area.pkl')
# joblib.dump(le_time, 'model/le_time.pkl')

# print("✅ Model and encoders saved in /model")


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Load dataset
df = pd.read_csv('/Users/akshithgoud/Desktop/upi-fraud-detection/backend/data/updated_location dataset.csv')

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Ensure 'unknown' is in the data for all label encoders
def prepare_encoder(column_data):
    le = LabelEncoder()
    unique_values = column_data.astype(str).unique().tolist()
    if 'unknown' not in unique_values:
        unique_values.append('unknown')
    le.fit(unique_values)
    return le

# Initialize and fit encoders
le_from = prepare_encoder(df['from_upi'])
le_to = prepare_encoder(df['to_upi'])
le_location = prepare_encoder(df['location'])
le_area = prepare_encoder(df['area'])
le_time = prepare_encoder(df['time'])

# Apply encoding (replace unseen with 'unknown')
df['from_upi'] = df['from_upi'].apply(lambda x: x if x in le_from.classes_ else 'unknown')
df['to_upi'] = df['to_upi'].apply(lambda x: x if x in le_to.classes_ else 'unknown')
df['location'] = df['location'].apply(lambda x: x if x in le_location.classes_ else 'unknown')
df['area'] = df['area'].apply(lambda x: x if x in le_area.classes_ else 'unknown')
df['time'] = df['time'].apply(lambda x: x if x in le_time.classes_ else 'unknown')

# Transform columns
df['from_upi'] = le_from.transform(df['from_upi'])
df['to_upi'] = le_to.transform(df['to_upi'])
df['location'] = le_location.transform(df['location'])
df['area'] = le_area.transform(df['area'])
df['time'] = le_time.transform(df['time'])

# Features and label
features = ['from_upi', 'to_upi', 'time', 'location', 'area', 'amount']
X = df[features]
y = df['label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and encoders
os.makedirs("model", exist_ok=True)
joblib.dump(model, 'model/model.pkl')
joblib.dump(le_from, 'model/le_from.pkl')
joblib.dump(le_to, 'model/le_to.pkl')
joblib.dump(le_location, 'model/le_location.pkl')
joblib.dump(le_area, 'model/le_area.pkl')
joblib.dump(le_time, 'model/le_time.pkl')

print("✅ Model and encoders saved in /model")

