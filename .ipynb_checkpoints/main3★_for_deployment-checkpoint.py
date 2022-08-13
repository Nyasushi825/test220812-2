import streamlit as st
import time

st.title('Streamlit Trial')

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
