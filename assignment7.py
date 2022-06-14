import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import openpyxl as xls
#These are the libraries that I used for this assignment.

dt= pd.read_csv("assignment_seven.csv")

#I import the database saved in my file.
df= pd.DataFrame(dt)

#I converted to a data frame
df1=df.drop(columns=["full_name"])
df1_dropna= df1.dropna()

#After that, I drop the column 'Full name' to meet the requirements of the federal guidelines.
excel_file= pd.ExcelWriter("output.xlsx")
df1_dropna.to_excel(excel_file)
excel_file.save()

#I save the new data as an excel file named 'Output.xlsx'


df2=df1["products"].value_counts()
df3=pd.DataFrame(df2)
excel_file= pd.ExcelWriter("output2.xlsx")
df3.to_excel(excel_file)
excel_file.save()

#The value count gives the rank of the products, and I made a new file just with the ranking.

df4=pd.DataFrame({'product_name': ['Acetaminophen', 'Ibuprofen', 'Titanium Dioxide', 'Alcohol', 'Salicylic Acid'], 'Quantity':[13,10,10,8,8]})
ax=df4.plot.bar(x='product_name', y='Quantity', rot=0)
plt.title('Ranking Products', fontsize=20)
plt.savefig('Top5.png')
plt.show()

#Finally, the visualization of the top 5 products.



