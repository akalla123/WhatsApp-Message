
# coding: utf-8

# In[88]:


from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
  
# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome('C:\\Users\\Ayush\\Desktop\\extra\\BIA 660\\Project\\chromedriver_win32\\chromedriver.exe') 
  
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 
  
# Replace 'Friend's Name' with the name of your friend  
# or the name of a group  
target = 'Target Contact/Group'
time.sleep(10)
# Replace the below string with your own message 
driver.find_element_by_css_selector("[title^='New chat']").click()
time.sleep(1)
a = driver.find_element_by_css_selector("[title^='Search contacts']")
a.send_keys(target)
time.sleep(2)
t = driver.find_element_by_class_name('_2EXPL')
t.find_element_by_css_selector("[title^='Target Contact/Group']").click()
time.sleep(2)
b = driver.find_element_by_class_name("_2S1VP")
b.send_keys("Hi")
time.sleep(1)
b.send_keys(Keys.ENTER)


# In[76]:


numbers = numbers.split(",")


# In[87]:


print((numbers[22]).replace(" ", ""))

