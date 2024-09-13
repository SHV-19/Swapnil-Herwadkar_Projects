# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Data Load
data = pd.read_csv('D:/Swapnil/Swapnil/Work/Personal Projects/Sustainibillity Index Tableau/sustainable_fashion_trends_2024_cleaned.csv')

# Data Preparation
# Map Sustainability Ratings (A=4, B=3, C=2, D=1)
sustainability_map = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
data['Sustainability_Rating_Encoded'] = data['Sustainability_Rating'].map(sustainability_map)

# Encoding categorical variables such as Material_Type and Country
label_encoder = LabelEncoder()
data['Material_Type_Encoded'] = label_encoder.fit_transform(data['Material_Type'])
data['Country_Encoded'] = label_encoder.fit_transform(data['Country'])

# Define features and target
features_emissions = ['Country_Encoded', 'Year', 'Material_Type_Encoded', 'Water_Usage_Liters', 
                      'Waste_Production_KG', 'Average_Price_USD', 'Carbon_Footprint_MT']
target_sustainability = 'Sustainability_Rating_Encoded'

# Split the data for training
X_train_ratings, X_test_ratings, y_train_ratings, y_test_ratings = train_test_split(
    data[features_emissions], data[target_sustainability], test_size=0.2, random_state=42)

# Train the RandomForestRegressor model
model_ratings = RandomForestRegressor(random_state=42)
model_ratings.fit(X_train_ratings, y_train_ratings)

# Predict on the test set and calculate MSE for Sustainability Ratings
y_pred_ratings = model_ratings.predict(X_test_ratings)
ratings_mse = mean_squared_error(y_test_ratings, y_pred_ratings)

# Print MSE for Sustainability Ratings Prediction
print(f"Mean Squared Error for Sustainability Ratings Prediction: {ratings_mse}")

# Calculate RMSE
rmse_ratings = np.sqrt(ratings_mse)
print(f"Root Mean Squared Error for Sustainability Ratings Prediction: {rmse_ratings}")

Mean Squared Error for Sustainability Ratings Prediction: 1.3677109
Root Mean Squared Error for Sustainability Ratings Prediction: 1.1694917272046006

# Correlation Analysis
# Calculate correlations between sustainability ratings, average price, water usage, waste production, and material type
correlation_matrix = data[['Sustainability_Rating_Encoded', 'Average_Price_USD', 
                           'Water_Usage_Liters', 'Waste_Production_KG', 'Material_Type_Encoded', 
                           'Carbon_Footprint_MT']].corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Sustainability Ratings and Other Variables')
plt.show()
