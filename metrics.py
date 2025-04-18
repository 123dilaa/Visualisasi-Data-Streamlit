# #Metrics dalam Streamlit adalah elemen yang digunakan untuk menampilkan informasi kunci 
# atau indikator penting dalam format yang sederhana dan informatif. Streamlit menyediakan 
# fungsi st.metric untuk menunjukkan data berupa nilai utama, beserta perubahan nilai yang 
# relevan. Biasanya digunakan untuk menampilkan metrik seperti pertumbuhan, performa, 
# atau statistik penting dalam aplikasi.

import streamlit as st
# Defining Metrics
st.metric(label='Temprature', value='31 °C', delta='-1.2 °C')


#Defining columns
c1, c2, c3 = st.columns(3)
#Defining Metrics
c1.metric("Rainfall", "100 cm", "10 cm")
c2. metric(label="Population", value="123 Billions", delta="1 billions", delta_color="inverse")
c3.metric(label="Customers", value=None, delta=0, delta_color="off")
st.metric(label="speed", value=None, delta=0)
st.metric("Tress", "91456", "-1132649")
