import streamlit as st
from PIL import Image
from rembg import remove
import io

# FUNCTIONS

def process_image(image_uploaded):
    image = Image.open(image_uploaded)
    processed_image = remove_background(image)
    return processed_image

def remove_background(image):
    image_byte = io.BytesIO()
    image.save(image_byte, format='PNG')
    image_byte.seek(0)
    processed_image_bytes = remove(image_byte.read())
    return Image.open(io.BytesIO(processed_image_bytes))

# FROM

st.image('assets/auto_remove_background.jpg')
st.header('Background Removal App')
st.subheader('Upload an Image')
uploaded_image = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])

if uploaded_image is not None:
    st.image(uploaded_image, caption='Imagen subida', use_column_width=True)
    remove_button = st.button(label='Quitar fondo')

    if remove_button:
        processed_image = process_image(uploaded_image)
        st.image(processed_image, caption='Background Removed', use_column_width=True)

        # Guardar la imagen procesada en un objeto de bytes
        image_byte_arr = io.BytesIO()
        processed_image.save(image_byte_arr, format='PNG')
        image_byte_arr.seek(0)

        # Botón para descargar la imagen procesada
        st.download_button(
            label='Download Processed Image',
            data=image_byte_arr,
            file_name='processed_image.png',
            mime='image/png'
        )
