import pandas as pd

# Read the dataset
df = pd.read_csv("data/messy_students.csv")

# Keep a copy of the original dataset
original_df = df.copy()

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Remove duplicate rows
df = df.drop_duplicates()

# Clean City column
df["City"] = df["City"].str.strip()
df["City"] = df["City"].str.title()

# Reset index
df = df.reset_index(drop=True)

# Save cleaned dataset
df.to_csv("data/cleaned_students.csv", index=False)

# Display results
print("========== BEFORE CLEANING ==========")
print(original_df)

print("\n========== AFTER CLEANING ==========")
print(df)

print("\n========== DATA INFORMATION ==========")
df.info()

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== CLEANING SUMMARY ==========")
print("✅ Missing Age values filled")
print("✅ Missing Marks values filled")
print("✅ Duplicate rows removed")
print("✅ Extra spaces removed from City")
print("✅ City names standardized")
print("✅ Index reset")
print("✅ Cleaned dataset saved as data/cleaned_students.csv")