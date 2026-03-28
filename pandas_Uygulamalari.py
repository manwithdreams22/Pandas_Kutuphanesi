#import pandas as pd
#import numpy as np
 
             ## 1. Uygulama
#liste=[1,2,3,"a","b","c"]
#df=pd.DataFrame(liste)
#df=pd.DataFrame(liste, columns=["Veriler"])
#data = [['Ali',10],['Ayşe',12],['Mehmet',13]]
#df = pd.DataFrame(data,columns=['Ad','Yaş'])
#data = {'Ad':['Ali', 'Ayşe', 'Mehmet'],'Yaş':[10,12,13]}
#df = pd.DataFrame(data)
#df = pd.DataFrame(data,index=['Ogrenci1','Ogrenci2','Ogrenci3'])
#print(df)
             # 2. Uygulama
##data=np.random.randint(1,100,size=(3,3))
##df=pd.DataFrame(data, columns=["x1","x2","x3"])
##df.info()
##df.axes
##df.shape
##df.ndim
##df.size
##df.values
##df.head()
##df.tail()

#             # 3. Uygulama

# d1 = np.random.randint(0,100, size = 10)
# d2 = np.random.randint(0,100, size = 10)
# d3 = np.random.randint(0,100, size = 10)
# d4 = np.random.randint(0,100, size = 10)
 
# dict = {"seri1":d1,"seri2":d2,"seri3":d3,"seri4":d4}

# df = pd.DataFrame(dict)

# #print(df[2:4])

# #print(df["seri1"])

# #print(df.seri1)

# #print(df[["seri1","seri4"]])

# #print(df.iloc[0])
# #print(df.iloc[1])
# #print(df.iloc[-1])
# #print(df.iloc[0:3])

# #print( df.iloc[:,0])
# #print(df.iloc[:,1])
# #print(df.iloc[:,-1])

# #print(df.iloc[0:3])
# #print(df.iloc[: , 0:2])
# #print(df.iloc[[0,2,6,8] , [0,2,3]])
# #print(df.iloc[0:5, 2:4])

# #print(df.loc[0])
# #print(df.loc[1])
# #print(df.loc[0:3])

# #print(df.loc[:,"seri1"])

# #print(df.loc[2:5,"seri1":"seri3"])

            # 4. Uygulama 

# rastgele1 = np.random.randint(1,20,size=(4,3))
# rastgele2 = np.random.randint(20,40,size=(4,3))

# df1 = pd.DataFrame(rastgele1,columns=["x","y","z"])
# df2 = pd.DataFrame(rastgele2,columns=["x","y","z"])

# df = pd.concat([df1,df2])

# df = pd.concat([df1,df2], ignore_index=True)

# df2.columns=["x","y","a"]
# df=pd.concat([df1,df2],ignore_index=True)

# df = pd.concat([df1,df2], ignore_index=True, join="inner")


# # print(df2)