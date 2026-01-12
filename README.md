🍽️ Restaurant Rating Prediction & Deployment
An end-to-end Machine Learning application designed to predict restaurant rating classes based on service features and cost parameters. This project transitions from a detailed research-oriented Jupyter Notebook to a production-ready Streamlit web application.

🚀 Live Demo
[https://restaurant-rating-predictor.streamlit.app/]

🛠️ Tech Stack
Language: Python 3.10+

Machine Learning: Scikit-learn, Random Forest Regressor

Optimization: GridSearchCV (Hyperparameter Tuning)

Deployment: Streamlit

Data Pipelines: Joblib (Model & Scaler Serialization)

Visualization: Seaborn, Matplotlib

📊 Key Features
Hyperparameter Optimization: Utilized GridSearchCV to fine-tune the Random Forest model, resulting in a significantly reduced RMSE of 0.45.

Robust Preprocessing: Implemented a consistent scaling pipeline using StandardScaler to ensure numerical stability across cost and price-range features.

Production-Ready Pipeline: Serialized both the trained model (mlmodel.pkl) and the feature scaler (scaler.pkl) to prevent data leakage during real-time inference.

Interactive UI: A user-friendly Streamlit dashboard allowing users to toggle features like "Table Booking" and "Online Delivery" to see immediate impact on restaurant ratings.

📈 Performance Metrics
Mean Absolute Error (MAE): 0.35

Root Mean Squared Error (RMSE): 0.45

Feature Importance: Price range and Average Cost were identified as the primary drivers for restaurant rating predictions.
