# Practical 5: Creating a Bayesian Network

import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import ParameterEstimator
from pgmpy.estimators import MaximumLikelihoodEstimator

# Define the dataset
data = pd.DataFrame({
    'Weather': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
})

# Create a Bayesian Network model
model = BayesianNetwork()

# Define the variables based on the columns in the dataset
variables = list(data.columns)

# Add nodes (variables) to the model with the correct names
for variable in variables:
    model.add_node(variable)

# Define the structure (directed edges) of the Bayesian network
model.add_edge("Weather", "PlayTennis")
model.add_edge("Temperature", "PlayTennis")
model.add_edge("Humidity", "PlayTennis")

# Use Maximum Likelihood Estimation (MLE) to estimate CPDs from the data
estimator = ParameterEstimator(model, data)
model.fit(data, estimator=MaximumLikelihoodEstimator)

# Check the model for consistency
assert model.check_model()

# Print Bayesian Network Structure
print("Bayesian Network Structure:")
print(model.edges())

# Print CPDs
print("\nCPDs:")
for cpd in model.get_cpds():
    print(cpd)

# Optionally, you can save the model to a file
model.save("bayesian_network2.pkl")
