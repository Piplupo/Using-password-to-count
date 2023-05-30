#!/usr/bin/env python
# coding: utf-8

# In[3]:


password = "RIGHTPASSWORD"
passer = ""
while passer != password:
    passer = input()
    if passer != password:
        print ("access denied")
print ("Welcome, counting now :)")
i = 0
while True:
    i += 3
    print(i)
    if i == 69:
        break


# In[ ]:




