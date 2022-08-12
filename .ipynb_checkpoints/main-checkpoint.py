import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

st.title('Streamlit超入門')

st.write('DataFrame')

st.write('Hello, *World!* :sunglasses:')

df= pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]  
})

st.write(df)

st.write('+++++++++++++++ st.dataframe(df, width =100,height = 300) +++++++++++++++')

st.dataframe(df, width =100,height = 300)

st.write('st.write(df)との違い：サイズ指定可能')

st.write('+++++++++++++++  st.write("1 + 1 = ", 2) +++++++++++++++')

st.write('1 + 1 = ', 2)

st.write('+++++++++++++++ st.write("Below is a DataFrame:", df, "Above is a dataframe.") +++++++++++++++')

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

st.write('+++++++++++++++++++++++++++++++++++++++++++++')
df = pd.DataFrame(
     np.random.randn(300, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)
st.write('+++++++++++++++++++++++++++++++++++++++++++++')

'''
{
  "config": {
    "background": "#ffffff",
    "axis": {
      "labelColor": "#31333F",
      "titleColor": "#31333F",
      "gridColor": "rgba(49, 51, 63, 0.2)",
      "labelFont": "\"Source Sans Pro\", sans-serif",
      "titleFont": "\"Source Sans Pro\", sans-serif",
      "labelFontSize": 12,
      "titleFontSize": 12
    },
    "legend": {
      "labelColor": "#31333F",
      "titleColor": "#31333F",
      "labelFont": "\"Source Sans Pro\", sans-serif",
      "titleFont": "\"Source Sans Pro\", sans-serif",
      "labelFontSize": 12,
      "titleFontSize": 12
    },
    "title": {
      "color": "#31333F",
      "subtitleColor": "#31333F",
      "labelFont": "\"Source Sans Pro\", sans-serif",
      "titleFont": "\"Source Sans Pro\", sans-serif",
      "labelFontSize": 12,
      "titleFontSize": 12
    },
    "header": {"labelColor": "#31333F"},
    "view": {"continuousWidth": 400, "continuousHeight": 300}
  },
  "data": {"name": "2387229826064"},
  "mark": "circle",
  "encoding": {
    "color": {"field": "c", "type": "quantitative"},
    "size": {"field": "c", "type": "quantitative"},
    "tooltip": [
      {"field": "a", "type": "quantitative"},
      {"field": "b", "type": "quantitative"},
      {"field": "c", "type": "quantitative"}
    ],
    "x": {"field": "a", "type": "quantitative"},
    "y": {"field": "b", "type": "quantitative"}
  },
  "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json",
  "autosize": {"type": "fit", "contains": "padding"},
  "padding": {"bottom": 20}
}
'''

st.write('++++++++++++++++++ st.table(df) +++++++++++++++++++')

df = pd.DataFrame(
    np.random.rand(20,3),
    columns = ['a','b','c'])

st.table(df)

st.write('++++++++++++++++++ st.table(df.style.highlight_max()) +++++++++++++++++++')
st.table(df.style.highlight_max())



st.write('++++++++++++++++++ st.table(df.style.highlight_max(axis=0)) +++++++++++++++++++')

st.table(df.style.highlight_max(axis=0))

st.write('++++++++++++++++++ st.table(df.style.highlight_max(axis=1)) +++++++++++++++++++')
st.table(df.style.highlight_max(axis=1))

st.write('++++++++++++++++++ st.line_chart(df) +++++++++++++++++++')
st.line_chart(df)

st.write('++++++++++++++++++ st.area_chart(df) +++++++++++++++++++')
st.area_chart(df)

st.write('++++++++++++++++++ st.bar_chart(df) +++++++++++++++++++')
st.bar_chart(df)



st.write('++++++++++++++++++ st.pyplot(fig) +++++++++++++++++++')
arr = np.random.normal(1,1,size =100)
fig, ax = plt.subplots()
ax.hist(arr,bins=20)

st.pyplot(fig)






st.write('++++++++++++++++++ st.map(df) +++++++++++++++++++')
df = pd.DataFrame(
    np.random.rand(100,2),
    columns = ['lat','lon']
)

st.map(df)

st.write('++++++++++++++++++ st.map(df) +++++++++++++++++++')
df = pd.DataFrame(
    np.random.rand(100,2)/[50,50],
    columns = ['lat','lon']
)

st.map(df)


st.write('++++++++++++++++++ st.map(df) +++++++++++++++++++')
df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns = ['lat','lon']
)

st.map(df)

st.write('++++++++++++++++++ st.image(img) +++++++++++++++++++')

from PIL import Image

img = Image.open('sunny_hose_clean.jpg')

st.image(img)

st.write('++++++++++++++++++ st.image(img,caption = SH,use_column_width = True) +++++++++++++++++++')

st.image(img,caption = 'SH',use_column_width = True)


st.write('++++++++++++++++++ セレクトボックスによる値の動的変更 +++++++++++++++++++')

st.write('++++++++++++++++++ st.option+++++++++++++++++++')

option = st.selectbox(
    'Please mention the number you like',
    list(range(1,11))    
)

'Please mention the number you like',option,'!'
