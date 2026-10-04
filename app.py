import streamlit as st
import sqlite3
import pandas as pd


DB_NAME = "MobileDetails.db"


conn = sqlite3.connect(DB_NAME)
query = "SELECT * FROM Mobiledata"
data = pd.read_sql_query(query, conn)
conn.close()


st.title("Technolife Mobile Products")

for index, row in data.iterrows():
    col1, col2 = st.columns(2)
    with col1:
        # Product Image
        st.image(row["image"], width=250)
        st.subheader(row["title"])
        st.write("حافظه داخلی:", row["storage"])
        st.write("رم:", row["ram"])
        st.write("رنگ:", row["color"])
        st.write("امتیاز کاربران:", row["rating"])

    with col2:
        st.write("توضیحات:")
        st.write(row["description"])
        st.link_button("مشاهده محصول",row["link"])

    st.divider()