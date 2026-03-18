import pandas as pd

DATA_FILE = "fb_ads_president_scored_anon.csv"

# ---------- Load Dataset ----------

df = pd.read_csv(DATA_FILE)

print("\nDATASET OVERVIEW")
print("-----------------")
print("Shape:", df.shape)


print("\nDATA TYPES")
print("-----------------")
print(df.dtypes)


print("\nDATASET INFO")
print("-----------------")
print(df.info())


# ---------- Summary Statistics ----------

print("\nSUMMARY STATISTICS")
print("-----------------")

print(df.describe(include='all'))


# ---------- Missing Values ----------

print("\nMISSING VALUES")
print("-----------------")

missing_counts = df.isnull().sum()
missing_percentage = (df.isnull().mean() * 100)

missing_table = pd.DataFrame({
    "Missing Count": missing_counts,
    "Missing Percentage": missing_percentage
})

print(missing_table)


# ---------- Categorical Analysis ----------

print("\nCATEGORICAL VALUE COUNTS")
print("-----------------")

categorical_columns = df.select_dtypes(include=['object']).columns

for col in categorical_columns[:5]:
    print(f"\nColumn: {col}")
    print(df[col].value_counts().head())


# ---------- Unique Value Counts ----------

print("\nUNIQUE VALUES PER COLUMN")
print("-----------------")

print(df.nunique())