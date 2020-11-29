import pandas as pd

dates=['April-10', 'April-11', 'April-12', 'April-13','April-14','April-16']
income1=[10,20,10,15,10,12]
income2=[20,30,10,5,40,13]

df=pd.DataFrame({"Date":dates,
                "Income_1":income1,
                "Income_2":income2})

for i in df.index: 
     print("Total income in "+ df["Date"][i]+ " is:"+str(df["Income_1"][i]+df["Income_2"][i]))

print(type(df))
