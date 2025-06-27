import pandas as pd

# Read the CSV file with pipe delimiter
df = pd.read_csv('data.csv', delimiter='|')

# Remove rows with any NaN values and copy to avoid SettingWithCopyWarning
df_cleaned = df.dropna().copy()

# Convert 'Business Effective Date' to dd/mm/yyyy format
df_cleaned['Business Effective Date'] = pd.to_datetime(
    df_cleaned['Business Effective Date']
).dt.strftime('%d/%m/%Y')

# Save cleaned data to a new CSV file with comma delimiter
df_cleaned.to_csv('cleaned_data.csv', index=False)

print("✅ Cleaned data saved to 'cleaned_data.csv'")
