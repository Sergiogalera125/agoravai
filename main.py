import pandas as pd
# import plotly.express as px
import streamlit as st

# emojis: https://www.vwefx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard",
                   page_icon="bar_chart:",
                   layout="wide")


df = pd.read_excel(
    io='supermarket_sales.xlsx',
    engine='openpyxl',
    sheet_name='Sales',
    skiprows=1,
    usecols='B:R',
    nrows=1000,
)

st.dataframe(df)