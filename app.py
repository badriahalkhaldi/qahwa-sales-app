import streamlit as st
import pandas as pd

st.title("Qahwa Corner Sales Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("cafe_sales.csv")

df = load_data()

selected_branch = st.selectbox("Select Branch", df['branch'].unique())
filtered_df = df[df['branch'] == selected_branch]

total_rev = filtered_df['total_sar'].sum()
st.metric(label=f"Total Revenue ({selected_branch})", value=f"{total_rev:,.2f} SAR")

st.subheader("Revenue by Product")
product_rev = filtered_df.groupby('product')['total_sar'].sum()
st.bar_chart(product_rev)
