import pandas as pd

df = pd.read_csv("data/cleaned_logs/part-00000.csv", header=None, names=["timestamp", "user_id", "page"])

# Basic stats
session_counts = df["user_id"].value_counts()
most_visited = df["page"].value_counts()

print("Top Users by Session Count:")
print(session_counts.head())

print("Most Visited Pages:")
print(most_visited.head())
