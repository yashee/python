#!/usr/bin/env python
# coding: utf-8

# In[5]:


import rasterio
import numpy as np
import matplotlib.pyplot as plt


# In[6]:


dataset = rasterio.open(r'E:\USGS\LC08_L1TP_012031_20190417_20190423_01_T1.tar\LC08_L1TP_012031_20190417_20190423_01_T1\LC08_L1TP_012031_20190417_20190423_01_T1_B6.TIF')


# In[7]:


dataset.crs


# In[8]:


dataset.transform


# In[9]:


dataset.height


# In[10]:


dataset.width


# In[11]:


dataset.count


# In[12]:


dataset.driver


# In[13]:


dataset.meta


# In[14]:


from rasterio.plot import show


# In[15]:


show((dataset,1))


# In[16]:


show((dataset,1), cmap='Greens')


# In[17]:


B4=rasterio.open(r'E:\USGS\LC08_L1TP_012031_20190417_20190423_01_T1.tar\LC08_L1TP_012031_20190417_20190423_01_T1\LC08_L1TP_012031_20190417_20190423_01_T1_B4.TIF')


# In[18]:


B3=rasterio.open(r'E:\USGS\LC08_L1TP_012031_20190417_20190423_01_T1.tar\LC08_L1TP_012031_20190417_20190423_01_T1\LC08_L1TP_012031_20190417_20190423_01_T1_B3.TIF')


# In[19]:


B2=rasterio.open(r'E:\USGS\LC08_L1TP_012031_20190417_20190423_01_T1.tar\LC08_L1TP_012031_20190417_20190423_01_T1\LC08_L1TP_012031_20190417_20190423_01_T1_B2.TIF')


# In[20]:


B5=rasterio.open(r'E:\USGS\LC08_L1TP_012031_20190417_20190423_01_T1.tar\LC08_L1TP_012031_20190417_20190423_01_T1\LC08_L1TP_012031_20190417_20190423_01_T1_B5.TIF')


# In[21]:


B8=rasterio.open(r'E:\USGS\LC08_L1TP_012031_20190417_20190423_01_T1.tar\LC08_L1TP_012031_20190417_20190423_01_T1\LC08_L1TP_012031_20190417_20190423_01_T1_B8.TIF')


# In[22]:


Red=B4.read(1)


# In[23]:


Green=B3.read(1)


# In[24]:


Blue=B2.read(1)


# In[25]:


NIR=B5.read(1)


# In[26]:


Pan=B8.read(1)


# In[27]:


def normalize (array):
    array_min, array_max = array.min(), array.max()
    return((array - array_min)/(array_max-array_min))


# In[28]:


Redn=normalize(Red)


# In[29]:


Greenn=normalize(Green)


# In[30]:


Bluen=normalize(Blue)


# In[31]:


NIRn=normalize(NIR)


# In[32]:


Pann=normalize(Pan)


# In[33]:


print("Normalized bands")


# In[34]:


print(Redn.min(),'-', Redn.max(),'mean:',Redn.mean())
print(Greenn.min(),'-', Greenn.max(),'mean:',Greenn.mean())
print(Bluen.min(),'-', Bluen.max(),'mean:',Bluen.mean())
print(NIRn.min(),'-', NIRn.max(),'mean:',NIRn.mean())
print(Pann.min(),'-', Pann.max(),'mean:',Pann.mean())


# In[35]:


rgb = np.dstack((Redn, Greenn, Bluen))


# In[36]:


plt.imshow(rgb)


# In[37]:


nrg=np.dstack((NIRn, Redn, Greenn))
plt.imshow(nrg)


# In[63]:


falsecolor=rasterio.open('E:/USGS/falsecolor.tiff','w',
                         driver='Gtiff', 
                         width=B5.width, 
                         height=B5.height, 
                         count=3,
                         crs=B5.crs,
                        transform=B5.transform,
                        dtype='uint16')
falsecolor.write(B2.read(1),3)
falsecolor.write(B3.read(1),2)
falsecolor.write(B4.read(1),1)
falsecolor.close()


# In[ ]:




