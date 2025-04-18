#Dataframes dalam Streamlit adalah struktur data dua dimensi yang terdiri dari baris dan 
# kolom, yang biasanya digunakan untuk analisis data dan machine learning. Di Streamlit, 
# dataframes dapat ditampilkan dalam format tabel interaktif menggunakan fungsi 
# st.dataframe.

import streamlit as st
import pandas as pd
import numpy as np

st.write("DataFrame")

# defining random values in a dataframe usinf pandas anf numpy
df= pd.DataFrame(
    np.random.randn(30,10),
    columns=( 'col_no %d' % i for i in range(10)))
st.dataframe(df)

# Defening random values in a dataframe using pandas and numpy
df= pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10)))
#highligting minimun value objects
st.dataframe(df.style.highlight_min(axis=0))


#Table
st.write("Table")
#defening random values in a dataframe using pandas and numpy
df= pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10)))
#defening data in table
st.table(df)