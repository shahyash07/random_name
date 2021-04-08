
import streamlit as st
import numpy as np
import random
import pandas as pd


def run():
  
  name = ['Alex','Anton','Louise','Amandeep','Brenda','Ganesh','Dmytry','Kiren','Yuliya','Robbie','Yash', 'Hiba', 'Michael', 'Pamela'] 
  q_list = ['Who was your childhood actor/actress crush?', 'What is your favorite item you’ve bought this year?', 'What would your dream house be like?',
          'What is your favorite breakfast food?', 'which was your favorite trip', 'If you could live anywhere in the world for a year, where would it be?',
           'What is the best gift ever you ever received?']



  from PIL import Image
  image = Image.open('logo.PNG')
  image2 = Image.open('logo3.jpg')

  st.image(image,use_column_width=False)
  st.header('Institutional Research and Data Governance')
  st.subheader("Meeting Assistant tool for Host and Order selection")
  
  st.sidebar.title('IRDG Meeting Assistant')
  st.sidebar.markdown('This application is created to select the meeting order and next host in online meetings')
  st.sidebar.image(image2, width=450)
  st.sidebar.success("Created by: Yash and Robbie")
 

  # if len(name)== 0:
  #   st.success('all names have been selected')
  col1, col2, col3 = st.beta_columns(3) 
  with col3:
    if st.button("Who's the Host"):
      new_li = random.choice(name)
      name = [n for n in name if n !=new_li]
      st.success(new_li)
  with col1: 
    if st.button("Choose Order"):
      new_list = random.sample(name,len(name))
      new_list = pd.DataFrame(new_list, columns={'Order'})
      st.dataframe(new_list,width=10000, height=10000)
  with col2:
    if st.button("Question?"):
      new_qu = random.choice(q_list)
      st.success(new_qu)




      # name.remove(output)
  # name.remove(output)

if __name__ == '__main__':
    run()