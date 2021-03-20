# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Sparks Foundations #gripmar21
# ## Task3-‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore’
# ## Author- Gaurav Sahu
# %% [markdown]
# ## Importing the required modules 

# %%
import numpy as np # linear algebra
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# ## Importing and reading csv file

# %%
file_name = open('SampleSuperstore.csv')
df = pd.read_csv(file_name)

# %% [markdown]
# ## Checking if the file has been imported and read properly

# %%
df.sample(9)

# %% [markdown]
# ## viewing the last 5 data points

# %%
df.tail()

# %% [markdown]
# 
# %% [markdown]
# ## To check the number of rows and columns 

# %%
df.shape

# %% [markdown]
# ## Checking for missing values in each attribute

# %%
df.isnull().sum()

# %% [markdown]
# ## total number of missing values if any

# %%
print("total number of null values = ",df.isnull().sum().sum())

# %% [markdown]
# ## A short info for all the attributes

# %%
print(df.info()) 

# %% [markdown]
# ## Statistical description of the data set

# %%
df.describe()

# %% [markdown]
# ## Checking for the repeated rows

# %%
df.duplicated().sum()

# %% [markdown]
# ## Droping the repeated rows

# %%
df.drop_duplicates()

# %% [markdown]
# ## Checking the number of unique values in each column

# %%
df.nunique()

# %% [markdown]
# ## Correlation between the numerical attributes

# %%
df.corr()

# %% [markdown]
# ## Droping an attribute which is of no use

# %%
col=['Postal Code']
df1=df.drop(columns=col,axis=1)

# %% [markdown]
# ## Graphical representation of the various attributes

# %%
plt.figure(figsize=(16,8))
plt.bar('Sub-Category','Category', data=df)
plt.show()


# %%
print(df1['State'].value_counts())
plt.figure(figsize=(15,8))
sns.countplot(x=df1['State'])
plt.xticks(rotation=90)
plt.show()


# %%
print(df['Sub-Category'].value_counts())
plt.figure(figsize=(12,6))
sns.countplot(x=df['Sub-Category'])
plt.xticks(rotation=90)
plt.show()


# %%
fig,axes = plt.subplots(1,1,figsize=(9,6))
sns.heatmap(df.corr(), annot= True)
plt.show()

# %% [markdown]
# ## Behaviour of 'Profit' w.r.t. 'Discount'

# %%
plt.figure(figsize = (10,4))
sns.lineplot('Discount', 'Profit', data = df, color = 'r', label= 'Discount')
plt.legend()


# %%
fig, ax = plt.subplots(figsize = (10 , 6))
ax.scatter(df["Sales"] , df["Profit"])
ax.set_xlabel('Sales')
ax.set_ylabel('Profit')
plt.show()

# %% [markdown]
# ## So now we grouped or sum the sales ,profit,discount,quantity according to every state of region and also according to sub-categories sales

# %%
grouped=pd.DataFrame(df.groupby(['Ship Mode','Segment','Category','Sub-Category','State','Region'])['Quantity','Discount','Sales','Profit'].sum().reset_index())
grouped

# %% [markdown]
# ## sum,mean,min,max,count median,standard deviation,Variance of each states of Profit

# %%
df.groupby("State").Profit.agg(["sum","mean","min","max","count","median","std","var"])


