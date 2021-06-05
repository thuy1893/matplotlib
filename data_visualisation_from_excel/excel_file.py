#from youtube video: https://www.youtube.com/watch?v=eVwqIFf4eIY&list=TLPQMDUwNjIwMjE6CKFE3IrtsQ&index=3
import os 
os.chdir("C:\\Users\\nttdo\\learning.python\\atom")
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("Financial Sample.xlsx")
#print(df)

df_vtt_canada = df.loc[(df['Country']== 'Canada') & (df['Product']=='VTT') & (df['Segment']=='Government')]
df_vtt_canada = df_vtt_canada.sort_values(by=['Date'])
#df_vtt_canada.plot(x='Date', y='Profit')
#plt.show()
df_products = df.groupby(['Product']).sum()
#df_products['Units Sold'].plot.bar()
df_products['Units Sold'].plot.pie()
plt.show()
