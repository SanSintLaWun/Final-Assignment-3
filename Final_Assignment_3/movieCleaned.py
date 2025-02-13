# Import necessary libraries
# python version 3.8.2 64 bit
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Step 1: Dataset Selection
# Load your dataset (replace 'your_dataset.csv' with the actual file path or URL)
dataset = pd.read_csv('movieCleaned.csv')

# Step 2: Data Preprocessing
# Handle missing values, scale features, and encode categorical variables as needed

# Step 3: Linear Regression Model
# Extract features and target variable
X = dataset[['proBudget']]
y = dataset['gross']

# Initialize the Linear Regression model
model = LinearRegression()

# Step 4: Data Splitting
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Training the Model
# Train the linear regression model using the training dataset
model.fit(X_train, y_train)

# Monitor and record relevant metrics
coefficients = model.coef_
intercept = model.intercept_

# Step 6: Model Evaluation
# Evaluate the model's performance on the testing dataset
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Step 7: Visualization
# Visualize the regression line along with actual and predicted values
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('ProBudget')
plt.ylabel('Gross $')
plt.title('Linear Regression: Actual vs Predicted')
plt.show()

# Step 8: Prediction
# Accept user input for relevant features and make predictions
#user_input = np.array([proBudget, gross]).reshape(1, -1)
#prediction = model.predict(user_input)
#print(f'Predicted Output: {prediction[0]}')



# Step 10: Parameter Tuning
# Experiment with different hyperparameters or features and discuss observations

# Step 11: Challenges and Limitations
# Discuss challenges faced and identify potential limitations or assumptions

# Step 12: Future Improvements
# Suggest possible improvements or extensions to enhance the predictive model