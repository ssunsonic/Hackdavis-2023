import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt

df = pd.read_csv('monthly_milk_production.csv')
date = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
col = []
for i in range(len(df)):
    col.append(date[i%7])
    
df['Date'] = pd.DataFrame(col)
df.to_csv('Day_m.csv', index=False)

# Read the dataset
df = pd.read_csv('Day_m.csv')

# Prepare the data
encoder = LabelEncoder()
df['Date'] = encoder.fit_transform(df['Date'])
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df.iloc[:, 1:])

# Split data into input (X) and output (y) variables
look_back = 7
X, y = [], []
for i in range(look_back, len(df)):
    X.append(scaled_data[i - look_back:i, :])
    y.append(scaled_data[i, :])
X, y = np.array(X), np.array(y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and train the LSTM model
model = Sequential()
model.add(LSTM(50, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(X.shape[2]))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X_train, y_train, epochs=50, batch_size=1, verbose=2)

# Predict future values
predicted = model.predict(X_test)

# Inverse transform the predicted values
predicted = scaler.inverse_transform(predicted)

# Inverse transform the actual test values for comparison
y_test_inverse = scaler.inverse_transform(y_test)

# Plot the predicted values and the actual test values
plt.figure(figsize=(10, 6))
plt.plot(y_test_inverse[:, 0], label='Actual')
plt.plot(predicted[:, 0], label='Predicted')
plt.xlabel('Day')
plt.ylabel('Footprints')
plt.title('LSTM Predictions')
plt.legend()
plt.show()