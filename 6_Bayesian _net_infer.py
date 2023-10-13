import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import ParameterEstimator
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

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

# Create an inference object using Variable Elimination
inference = VariableElimination(model)

# Perform inference to calculate probabilities

# Calculate the probability of playing tennis given certain conditions
result = inference.query(variables=['PlayTennis'], evidence={'Weather': 'Sunny'})
print("Probability of playing tennis given Sunny weather:")
print(result)

result = inference.query(variables=['PlayTennis'], evidence={'Temperature': 'Mild', 'Humidity': 'Normal'})
print("\nProbability of playing tennis given Mild temperature and Normal humidity:")
print(result)

# You can perform more inference queries as needed
# Calculate the probability of playing tennis given Rainy weather
result = inference.query(variables=['PlayTennis'], evidence={'Weather': 'Rainy'})
print("\nProbability of playing tennis given Rainy weather:")
print(result)

# Calculate the probability of playing tennis given Cool temperature
result = inference.query(variables=['PlayTennis'], evidence={'Temperature': 'Cool'})
print("\nProbability of playing tennis given Cool temperature:")
print(result)

# Calculate the probability of playing tennis given Overcast weather and High humidity
result = inference.query(variables=['PlayTennis'], evidence={'Weather': 'Overcast', 'Humidity': 'High'})
print("\nProbability of playing tennis given Overcast weather and High humidity:")
print(result)
