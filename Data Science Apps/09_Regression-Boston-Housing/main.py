import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# Streamlit app title
st.write("""
# Boston House Price Prediction App
This app predicts the **Boston House Price**!
""")
st.write('---')

# Load the Boston Housing dataset from CSV
boston = pd.read_csv('BostonHousing.csv')
st.write(boston)

# Define the feature columns and target column
X = boston.drop(columns=["medv"])  # Adjust 'MEDV' to match your dataset's column name for the target
Y = boston["medv"]

# Sidebar input parameters
st.sidebar.header('Specify Input Parameters')

def user_input_features():
    input_data = {}
    for col in X.columns:
        input_data[col] = st.sidebar.slider(
            col, 
            float(X[col].min()), 
            float(X[col].max()), 
            float(X[col].mean())
        )
    return pd.DataFrame(input_data, index=[0])

df = user_input_features()

# Main panel
st.header('Specified Input parameters')
st.write(df)
st.write('---')

# Build the regression model
model = RandomForestRegressor()
model.fit(X, Y)

# Make a prediction
prediction = model.predict(df)

st.header('Prediction of MEDV')
st.write(prediction)
st.write('---')

# Explain the model's predictions using SHAP values
explainer = shap.Explainer(model, X)
shap_values = explainer(X)

st.header('Feature Importance')
fig1, ax1 = plt.subplots()
shap.summary_plot(shap_values, X, show=False)
st.pyplot(fig1, bbox_inches='tight')
st.write('---')

fig2, ax2 = plt.subplots()
shap.summary_plot(shap_values, X, plot_type="bar", show=False)
st.pyplot(fig2, bbox_inches='tight')
