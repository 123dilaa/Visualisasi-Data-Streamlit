# Data and Media Elements 
# Data and Media Elements dalam Streamlit adalah elemen yang dirancang untuk menampilkan data 
# dan media secara interaktif dan user-friendly di dalam aplikasi.
# Images
import streamlit as st
st.write("Image")

st.write('Displaying as Images')
st.write('Let`s him cooked')

# Displaying Image by specifying path
st.image('Foto/capybara.jpg')
# Image Courtesy by unplash
st.write('Image Courtesy: unplash.com')

#image Courtesy
st.write('Displaying Multipple Images')
#Lissting out animal images
animal_images = [
    'Foto/fox.jpg',
    'Foto/dolphin.jpg',
    'Foto/bb2.jpg',
]

#Displaying Multiple Images with 150
st.image(animal_images, width=150)

#image Courtesy
st.write('Image Courtesy: Unplash')

st.write(" Background Image")
import base64
#functional to set image as background
def add_local_backgound_image_(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.write("Image Courtsdy: unplash")
    st.markdown(
    f""" 
    <style>
    .stApp {{
    background-image: url(data:files/{'jpg'};base64,{encoded_string.decode()});
    background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

st.write("Background Image")
#Calling Image In Functional
add_local_backgound_image_('Foto/fox.jpg')
