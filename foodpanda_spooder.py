from bs4 import BeautifulSoup
import pandas as pd
import re
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(
    r"C:\Users\Brendan\Desktop\Python\chromedriver.exe", chrome_options=options)

driver.get("https://www.foodpanda.sg/city/singapore")
pageSource = driver.page_source
b_soup = BeautifulSoup(pageSource, 'html.parser')
names = []
ratings = []
ratings_count = []
delivery_fee = []
minimum_order = []
vendor_char = []


# In[6]:


for a in b_soup.findAll('a', attrs={'class': 'hreview-aggregate url'}):
    name = a.find('span', attrs={'class': 'name fn'})
    names.append(name.text)
    rating = a.find('span', attrs={'class': 'rating'})
    if rating:
        ratings.append(rating.text)
        rating_count = a.find('span', attrs={'class': 'count'})
        ratings_count.append(rating_count.text)
    else:
        ratings.append(None)
        ratings_count.append(None)
    min_order = a.find('ul', attrs={'class': 'extra-info mov-df-extra-info'})
    ls = min_order.text.split('\n')
    ls_ = [s for s in ls if s]
    minimum_order.append(ls_[0])
    delivery_fee.append(ls_[1])
    vendor_characteristics = a.find(
        'li', attrs={'class': 'vendor-characteristic'})
    vendor_char.append(vendor_characteristics.text)


# #### creating a data frame

# In[7]:


restaurants_df = pd.DataFrame()
restaurants_df["name"] = pd.Series(names)
restaurants_df["rating"] = pd.Series(ratings)
restaurants_df["rating_count"] = pd.Series(ratings_count)
restaurants_df["delivery_fee"] = pd.Series(delivery_fee)
restaurants_df["min_order"] = pd.Series(minimum_order)
restaurants_df["vendor_char"] = pd.Series(vendor_char)


# In[8]:


restaurants_df


# ### Data Cleaning

# In[9]:


restaurants_df['rating_count'] = restaurants_df['rating_count'].apply(
    lambda x: x if (x is None) else re.findall(r'\d+', x)[0])


# In[10]:


restaurants_df['vendor_char'] = restaurants_df['vendor_char'].apply(
    lambda x: x.split('\n'))
restaurants_df['vendor_char']


# In[11]:


restaurants_df['vendor_char'] = restaurants_df['vendor_char'].apply(lambda x: [
                                                                    s for s in x if s])
restaurants_df['vendor_char']


# In[12]:


restaurants_df['delivery_option'] = restaurants_df['vendor_char'].apply(
    lambda x: ''.join([s for s in x if "delivery" in s]))
restaurants_df['delivery_option']


# In[13]:


restaurants_df['food'] = restaurants_df['vendor_char'].apply(
    lambda x: [s for s in x if "delivery" not in s])
restaurants_df['food']


# In[14]:


# we don't need to keep this column now
restaurants_df.drop('vendor_char', axis=1, inplace=True)


# In[15]:


restaurants_df['rating'] = restaurants_df['rating'].apply(
    lambda x: x if x is None else x.split('/')[0])


# In[16]:


restaurants_df.rename(columns={'rating': 'rating(out of 5)'}, inplace=True)


# In[17]:


restaurants_df


# In[18]:


restaurants_df.describe(include='all')


# In[19]:


restaurants_df.dtypes


# #### changing the data type of columns with numerical data

# In[20]:


restaurants_df['rating(out of 5)'] = restaurants_df['rating(out of 5)'].astype(
    'float')


# In[21]:


restaurants_df['rating_count'] = restaurants_df['rating_count'].astype('float')


# In[22]:


restaurants_df.dtypes


# In[23]:


# now that we have float data type, the output of describe() is below
restaurants_df.describe(include='all')


# ### Saving Data Frame as CSV File

# In[24]:


restaurants_df.to_csv('food_panda_lhr_data.csv', sep="\t")


# ### Analyzing Data

# In[25]:


restaurants_df['rating(out of 5)'].hist()


# We see that less than 10 restaurants has rating=5

# #### list of unique items in 'food' column

# In[26]:


set([item for list in restaurants_df['food'].values for item in list])


# #### restaurants which serve certain type of food

# In[29]:


food_type = ['Pakistani']
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(restaurants_df[pd.DataFrame(
        restaurants_df.food.tolist()).isin(food_type).any(1)]['name'])


# #### minimum and maximum value of rating for each type of delivery option

# In[30]:


restaurants_df.groupby('delivery_option')['rating(out of 5)'].agg(
    [('Min', 'min'), ('Max', 'max')])


# #### word cloud to view items that are available in most of the restaurants

# In[36]:


list_of_food = restaurants_df['food'].values
flat_list = [item for sublist in list_of_food for item in sublist]
