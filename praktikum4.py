# Buttons

import streamlit as st
st.title("Creating a Button")

#Defining a Button
button = st.button("Clik Here")
if button:
    st.write(" You have clicked the button")
else:
    st.write(" You have not clicked the button")


# Radio Buttons
import streamlit as st

st.title('Creating Radio Buttons')

#Defining Radio Button
gender = st.radio(
    "Select your Gender",
    ('Male', 'Female', 'Others')
)
if gender == 'Male':
    st.write('you have selected Male')
elif gender == 'Female':
    st.write('you have selected Female')
else:
    st.write('you have selected Others')


#Check Boxes
import streamlit as st
st.title('Creating Check Boxes')
st.write('Selected your hobies:')

#defining Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

#Drop-Downs
import streamlit as st
st.title('Creating Dropdown')

#Creating Dropdown
hobby = st.selectbox('Choose your hobby: ', 
                    ('Books', 'Movies', 'Sports'))


#Multiselects
import streamlit as st
st.title('Creating Multiselect')

#Defining Multi_Select with Pre_Selection
hobbies = st.multiselect(
    'what are your hobbies',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
    ['Reading', 'Playing']
    )


# Download Buttons
import streamlit as st
st.title('Creating Download Buttons')

# Creating Download Button
down_btn = st.download_button(
    label="Download Image", 
    data=open('Foto/capybara.jpg', 'rb'),
    file_name="capybara.jpg",
    mime="image/jpg"
)

#Progres Bars
import streamlit as st
import time
st.title("Progress Bar")

#Defining Progress Bar
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complete')

# Spinners
import streamlit as st
import time
st.title('Spinner')

#defining Spinner
with st.spinner('Loading...'):
    time.sleep(5)
st.write("Hello Data Scientist")