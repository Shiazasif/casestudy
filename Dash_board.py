from enum import unique
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import pearsonr
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Dashboard",
    page_icon=(":bar_chart:"),
    layout="wide")

st.title("Case Study - 1 Car:bar_chart:")
st.markdown("---")

df=pd.read_excel('cars.xlsx')

@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="cars.xlsx",
        engine="openpyxl",
        sheet_name="cars",
        skiprows=0,
        usecols="A:I",
        nrows=500,
    )

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
country = st.sidebar.multiselect(
    "Select the Origin:",
    options=df["Origin"].unique(),
    default=df["Origin"].unique()
)

st.sidebar.header("Please Filter Here:")
Cars = st.sidebar.multiselect(
    "Select the Car:",
    options=df["Car"].unique(),
    default=df["Car"].unique()
)

df_selection = df.query(
    "Origin == @country & Car ==@Cars"
)

#Chart
st.subheader("Correlation Chart")
fig=plt.figure(figsize=(10,4))
plot = sns.heatmap(df_selection.corr().round(2), annot=True)
plot.set_title(country)
st.markdown("---")

st.pyplot(fig)

#Table
st.subheader("Correlation Matrix Table")
matrix=df_selection.corr()
st.dataframe(matrix)
st.markdown("---")

# ---Use Local Css File to design form---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

local_css("style/style.css")