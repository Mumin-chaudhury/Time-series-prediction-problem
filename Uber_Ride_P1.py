import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv('ncr_ride_bookings.csv')
print(df.head())

# Data Preprocessing
df.drop_duplicates()
df_cleaned = df.dropna()
