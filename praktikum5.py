# Text Box
import streamlit as st
st.title('Text Box')
#Creating Text Box
name = st.text_input("Enter your Name")
st.write(" Your Name is ", name)

# Creating Text box with 10 as character limit 
name = st.text_input("Enter your Name", max_chars=10) 
password = st.text_input("Enter your password", type='password') 

# Text Area
import streamlit as st
#Creating Text Area
input_text = st.text_area("Enter your Review")
#Printing entered text
st.write(""" You entered: \n""",input_text)

# Number input
import streamlit as st
# Create number input
st.number_input("enter your number")

num = st.number_input('Enter your Number', 0, 10, 5, 2)
st.write("min. Value is 0, \n max. value is 10")
st.write("Default Value is 5, \n Step Size value is 2")
st.write("Total value after adding Number entered with step value is:", num)

# TIME
import streamlit as st
st.title("Time")
# Defining Time Function
st.time_input('Select Your time')

# Date
import streamlit as st
import datetime
st.title ("Date")
# Defining Date Function
st.date_input('Select Your Date')

st.date_input("Select your Date", value=datetime.date(1989, 12, 25),
            min_value=datetime.date(1980, 1, 1),
            max_value=datetime.date(2025, 12, 1))


# COLOR
import streamlit as st
st.title("select color")
# Defining Color Picker
color_code = st.color_picker("Select your color")
st.header(color_code)

# Dataset Upload
import streamlit as st
import pandas as pd

st.title("CSV Data")

data_file = st.file_uploader("Upload CSV", type=["csv"])
details = st.button("Check Details")

if details:
    if data_file is not None:
        file_details = {"file_name": data_file.name, "file_type": data_file.type, "file_size": data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")


# SUBMIT BUTTON
import streamlit as st
my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')
# Defining submit button
submit_button = my_form.form_submit_button(label='Submit')

st.write(a)



