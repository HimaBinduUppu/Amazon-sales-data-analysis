#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Import pandas
import pandas as pd

# Update the file path
file_path = r"C:\Users\vmani\OneDrive\Documents\amazon.csv"

# Step 1: Load the dataset
try:
    df = pd.read_csv(file_path, encoding='utf-8-sig', on_bad_lines='skip')  # Skip problematic lines
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='latin1', on_bad_lines='skip')  # Alternative encoding

# Inspect the dataset
print("First 5 rows:")
print(df.head())


# In[5]:


print(df.head())


# In[7]:


print(df.info())
print(df.describe())
print(df.isnull().sum())  # Check for missing values


# In[11]:


print(df.columns)


# In[13]:


df.columns = df.columns.str.strip()


# In[15]:


df.rename(columns={"IncorrectName": "correct_name"}, inplace=True)


# In[17]:


df['column_name'] = "Unknown"


# In[21]:


# Check columns
print("Available columns:")
print(df.columns)

# Ensure no extra spaces or case mismatches
df.columns = df.columns.str.strip()

# Example: Handling missing or incorrectly named column
if 'column_name' in df.columns:
    df['column_name'] = df['column_name'].fillna("Unknown")
else:
    print("Column 'column_name' not found. Adding it with default values.")
    df['column_name'] = "Unknown"


# In[29]:


for col in df.select_dtypes(include='object').columns:  # Select only string (object) columns
    df[col] = df[col].apply(lambda x: x.encode('utf-8', 'ignore').decode('utf-8', 'ignore') if isinstance(x, str) else x)



# In[27]:


# Step 1: Check column names
print("Columns before stripping:")
print(df.columns)

# Step 2: Strip whitespace or hidden characters
df.columns = df.columns.str.strip()

# Step 3: Verify column names
print("Columns after stripping:")
print(df.columns)

# Step 4: Handle missing values
if 'column_name' in df.columns:
    df['column_name'] = df['column_name'].fillna("Unknown")
else:
    print("Column 'column_name' not found. Renaming or skipping this step.")


# In[31]:


df = df.drop_duplicates()


# In[37]:


output_path = r"C:\Users\vmani\OneDrive\Documents\amazon_cleaned.csv"
df.to_csv(output_path, index=False, encoding='utf-8')
print(f"Cleaned data saved to {output_path}")


# In[ ]:




