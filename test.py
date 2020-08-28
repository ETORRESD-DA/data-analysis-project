from pandas import DataFrame
import matplotlib
import matplotlib.pyplot as plt
   
Data = {'Country': ['USA','Canada','Germany','UK','France'],
        'GDP_Per_Capita': [45000,42000,52000,49000,47000]
       }
print(Data) 
df = DataFrame(Data,columns=['Country','GDP_Per_Capita'])
print(df)
df.plot(x ='Country', y='GDP_Per_Capita', kind = 'bar')
plt.show()