
# importing pandas library
import pandas as pd
# import matplotlib library
import matplotlib.pyplot as plt
  
# creating dataframe
df = pd.DataFrame({
    'Name': ['John', 'Sammy', 'Joe'],
    'Age': [45, 38, 90],
    'Height(in cm)': [150, 180, 160]
})
df
# plotting graph
# df.plot(x="Name", y=["Age", "Height(in cm)"], kind="bar")