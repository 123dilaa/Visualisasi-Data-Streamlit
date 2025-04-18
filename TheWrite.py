# import streamlit as st
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(
#     np.random.randn(30, 10),
#     columns=('col_no %d' for i in range (10)))
# # Defining multiple arguments in  write function
# st.write('Here is our Data', df, 'Data is in dataFrame.\n', '\nWrite is super function')

# #Importing Necessary Libraries
# import altair as alt

# # Defining random values for Chart
# df = pd.DataFrame(
#     np.random.randn(10, 2),
#     columns=['a', 'b'])

# # Defining Chart
# chart = alt.Chart(df).mark_bar().encode(
#     x='a', y='b', tooltip=['a', 'b']
# )

# #Defining Chart in Write() functiom
# st.write(chart)

# # MAGIC
# st.Write('Magic')
# #Math Calculations with no functional defind
# 'Adding 5 & 4 =',5+4

# #Displaying Variable 'a' and its value
# a = 5
# 'a', a

# #Markdown with Magic

# """
# # Magic Feature
# Markdown working without defining its functional explicitly.   
# """

# # DataFrame Using magic
# import pandas as pd
# df = pd.DataFrame({'col' : [1,2]})
# 'dataframe', df

# # Magic Working on Charts
# import matplotlib.pyplot as plt
# s = np.random.logistic(10, 5, size=5)
# chart, ax = plt.subplots()
# ax.hist(s, bins=15)

# #magic chart
# "chart", chart

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

# DataFrame awal
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=[f'col_no_{i}' for i in range(10)]
)
st.write('Here is our Data', df, 'Data is in dataFrame.\n', '\nWrite is super function')

# Altair Chart
df_chart = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b']
)
chart = alt.Chart(df_chart).mark_bar().encode(
    x='a', y='b', tooltip=['a', 'b']
)
st.write(chart)

# MAGIC
st.write('Magic')

# Math calculation
st.write('Adding 5 & 4 =', 5 + 4)

# Display variable
a = 5
st.write('a', a)

# Markdown with magic
"""
# Magic Feature
Markdown working without defining its functional explicitly.   
"""

# DataFrame using magic
df_simple = pd.DataFrame({'col': [1, 2]})
df_simple

# Matplotlib chart
s = np.random.logistic(10, 5, size=5)
chart_plot, ax = plt.subplots()
ax.hist(s, bins=15)
chart_plot
