#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import pandas as pd
import plotly.express as px  # pip install plotly-express
import streamlit as st 
import plotly.graph_objects as go
import numpy as np


st.set_page_config(page_title="COVID-19 Dashboard", page_icon=":heavy_check_mark:", layout="wide")

df = pd.read_excel(
    io="COVID-19-2020.xlsx",
    engine="openpyxl",
    sheet_name="Sheet1",
    skiprows=0,
    
    nrows=335,
    )
df_2021 = pd.read_excel(
    io="COVID-19-2021.xlsx",
    engine="openpyxl",
    sheet_name="Sheet1",
    skiprows=0,
    
    nrows=338,
    )

st.sidebar.header("Please Filter Here:")

Month1 = st.sidebar.multiselect(
    "Select the month-2020:",
    options=df["month"].unique()
    
)
Month = st.sidebar.multiselect(
    "Select the month-2021:",
    options=df_2021["month"].unique()
    
)

df_selection = df.query(
    "month == @Month1"
)
dff_selection = df_2021.query(
    "month ==@Month"
)

day1 = st.sidebar.multiselect(
    "Select the day-2020:",
    options=df["Day"].unique()
    
)
day = st.sidebar.multiselect(
    "Select the day-2021:",
    options=df_2021["Day"].unique()
    
)
df_selection = df.query(
   "Day ==@day1"
)
dff_selection = df_2021.query(
    "Day ==@day"
)
st.title(":part_alternation_mark: COVID-19 Dashboard")
st.markdown("##")


total_Confirmed = int(df_selection["Confirmed"].sum())
total_Active = int(df_selection["Active"].sum())
total_Deaths = int(df_selection["Deaths"].sum())
total_Recovered = int(df_selection["Recovered"].sum())
st.subheader(" COVID-19 cases-2020")
left_column, middle_column, right_column ,rright_column = st.columns(4)
with left_column:
    
    st.markdown("##### Confirmed:")
    st.subheader(f"{total_Confirmed:,}")
with middle_column:
    st.markdown("##### Active:")
    st.subheader(f" {total_Active:,}")
with right_column:
    st.markdown("##### Deaths:")
    st.subheader(f"{total_Deaths:,}")
with rright_column:
    st.markdown("##### Recovered:")
    st.subheader(f" {total_Recovered:,}")

st.markdown("""---""")
total_Confirmed2 = int(dff_selection["Confirmed"].sum())
total_Active2 = int(dff_selection["Active"].sum())
total_Deaths2 = int(dff_selection["Deaths"].sum())
total_Recovered2 = int(dff_selection["Recovered"].sum())
st.subheader(" COVID-19 cases-2021")
left_column, middle_column, right_column ,rright_column = st.columns(4)
with left_column:
    st.markdown("##### Confirmed:")
    st.subheader(f"{total_Confirmed2:,}")
with middle_column:
    st.markdown("##### Active:")
    st.subheader(f" {total_Active2:,}")
with right_column:
    st.markdown("##### Deaths:")
    st.subheader(f"{total_Deaths2:,}")
with rright_column:
    st.markdown("##### Recovered:")
    st.subheader(f" {total_Recovered2:,}")

st.markdown("""---""")
left_column,right_column  = st.columns(2)
with left_column:
     figg = px.bar(df, x="month", y=["Deaths","Recovered","Active","Confirmed"], title="COVID-19 cases-2020"
    ,barmode ="overlay"
     )
     figg.update_layout(
         plot_bgcolor="rgba(0,0,0,0)",
         xaxis=(dict(showgrid=False))
    )
     figg.update_yaxes(
         showticklabels=False,
         showgrid = False,
         zerolinecolor = 'rgba(0,0,0,0)'
    )
     st.plotly_chart(figg)
with right_column:
    fig = px.bar(df_2021, x="month", y=["Deaths","Recovered","Active","Confirmed"], title="COVID-19 cases- 2021"
    ,barmode ="overlay"
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
    )
    fig.update_yaxes(
        showticklabels=False,
        showgrid = False,
        zerolinecolor = 'rgba(0,0,0,0)'
    )
    st.plotly_chart(fig)





