#ARMANDO MARQUEZ OCHOA 
#212664761
#DATA ANALITICS 2023

# In[3]:


import pandas as pd
import numpy as np

#creando un array
data= np.array([[1,4], [2,5], [3,6]])

#creando un dataframe
df= pd.DataFrame(data, index = ['row1', 'row2', 'row3'],
                columns = ['col1', 'col2'])
#mostrar el dataframe
df


# In[4]:


#creando un array en forma de lista
data = [[1,4],[2,5],[3,6]]

#creando un dataframe
df = pd.DataFrame(data, index =['row1','row2','row3'],
                 columns=['col1','col2'])
#mostrando el dataframe
df


# In[6]:


#leyendo el archivo csv
df_exams = pd.read_csv('C:/analitica/StudentsPerformance.csv')

#mostrando el dataframe
df_exams


# In[9]:


import pandas as pd
#leyendo el archivo CSV
df_exams = pd.read_csv('C:/analitica/StudentsPerformance.csv')

#mostrar primeras 5 filas del dataframe
df_exams.head()


# In[10]:


#mostrar ultimas 5 filas del dataframe
df_exams.tail()


# In[11]:


#mostrar ultimas n filas del dataframe
df_exams.tail(10)


# In[12]:


#accediendo al atributo shape
df_exams.shape


# In[13]:


#mostrar "n" filas
pd.set_option('display.max_rows',1000)
df_exams


# In[ ]:




