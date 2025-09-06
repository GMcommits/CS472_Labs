import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#path to file
path = 'file path'

df = pd.read_csv(path)

#setup for weeks data
df['Date'] = pd.to_datetime(df['Date'])

df['Week'] = (df['Date'] - df['Date'].min())/ 7
df['Week'] = df['Week'].dt.days

#getting unique value for file names and authors
authors = df['Authors'].unique()
filenames = df['Filename'].unique()

#color
colors = {author: i for i, author in enumerate(authors)}
files ={file: i for i, file in enumerate(filenames)}

df['Col_ID'] = df['Authors'].map(colors)
df['File_ID'] = df['Filename'].map(files)

plt.xlabel('Files')
plt.ylabel('Weeks')

#plotting
plt.scatter(df['File_ID'], df['Week'], c = df['Col_ID'], cmap ='tab10')

plt.show()
