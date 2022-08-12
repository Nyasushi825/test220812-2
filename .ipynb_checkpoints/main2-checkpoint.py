import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
from PIL import Image

import time

st.title('Streamlit超入門')

st.write('Interactive Widgets')
st.sidebar.write('Interactive Widgets')

st.write('+++++++++++++++ 1. Side-Bar+++++++++++++++')
text = st.sidebar.text_input("What's your favorite?")
condition = st.sidebar.slider("How about your condiiton?")
conditions = st.sidebar.slider("How about your condiiton?",0,10,5)
# 左端、右端、初期値

"what's your favorite : ", text
"How about your condiiton?" , condition
"How about your condiiton?" , conditions

st.write('+++++++++++++++ 2. 2-Columns Layout+++++++++++++++')

st.write('+++++++++++++++ left_column, right_column = st.columns(2) +++++++++++++++')
st.write('+++++++++++++++ button = left_column.button('      ') +++++++++++++++')
st.write('+++++++++++++++ if button: right_column.write('      ') +++++++++++++++')


left_column, right_column = st.columns(2)
button = left_column.button('Show this text in the right column')
if button:
    right_column.write('Here is right column')
# Please replace st.beta_columns with st.columns.

st.write('+++++++++++++++ 3. Expander+++++++++++++++')
st.write('+++++++++++++++ expander1 = st.expander("Question1") +++++++++++++++')
st.write('+++++++++++++++ expander1.write(["Answer to Question1","Answer to Question1","Answer to Question1"]) +++++++++++++++')
    
expander1 = st.expander('Question1')
expander1.write(['Answer to Question1','Answer to Question1','Answer to Question1'])

expander2 = st.expander('Quesion2')
expander2.write('Answer to Quesion2')

expander3 = st.expander('Question3')
expander3.write('Answer to Question3')
# Please replace st.beta_expander with st.expander.


st.write('+++++++++++++++    Progress Bar   +++++++++++++++')


st.write('Progress Bar')
'Start!'

latest_iteration = st.empty()
bar= st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.05)
'Done!'

expander1 = st.expander('Question1')
expander1.write(['Answer to Question1','Answer to Question1','Answer to Question1'])

expander2 = st.expander('Quesion2')
expander2.write('Answer to Quesion2')

expander3 = st.expander('Question3')
expander3.write('Answer to Question3')
