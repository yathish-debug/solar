import pandas as pd
import streamlit as st
import pickle
import matplotlib.pyplot as plt
st.set_page_config(
     page_title="Solar monitoring system",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )




import streamlit as st

def get_user_name():
    return 'hello'

# ------------------------------------------------
# Want people to see this part of the code...

def get_punctuation():
    return '!!!'

greeting = "Hi there, "
user_name = get_user_name()
punctuation = get_punctuation()

st.write(greeting, user_name, punctuation)

# ...up to here
# ------------------------------------------------

foo = 'bar'
st.write('Done!')




df = pickle.load(open('data.pkl','rb'))
st.title('Solar Data Monitering dashboard')
st.caption('Data')
st.write(df)


x = df['AMBIENT_TEMPERATURE']
y = df['DC_POWER']   
import time
fig = plt.figure(figsize=(10, 4))
plt.scatter(x, y)
    
import time

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)