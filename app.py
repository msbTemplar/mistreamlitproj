import streamlit as st
from PIL import Image
import requests
import json
from streamlit_lottie import st_lottie



st.set_page_config(page_title="Valerapp", page_icon=":person_mountain_biking:", layout="wide")
email_contact = "msb.duck@gmail.com"

def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)
        

css_load("style/main.css")

def load_lottiefile(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# Cargar el archivo
lottie_animation = load_lottiefile("style/Animation - 1751134517464.json")  # ajusta la ruta

#intro

with st.container():
    st.header("hola, somos valerapp  :dolphin:")
    st.title("Creamos soluciones para acelerar tu negocio")
    st.write("Somos unos apasionados de la tecnologia y la innovacion, especializados en elsector de la digitalizacion y automatizacion de negocios")
    st.write("[Saber mas >](https://valerapp.com/)")
    
with st.container():
    st.write("--------")
    text_column, animation_column = st.columns(2)
    with text_column:
        st.header("Sobre nosotros  :family_man_man_girl_boy:")
        st.write("""Nuestro objetivo es poder aportar valor a los negocios-....................................................................................................................................................................................................................................................................................................................................................................
                ***Si esto os suena interesante para ti contactarnos a traves de este formulario*** 
        """)
        st.write("[Mas sobre nostros >](https://valerapp.com/about/)")
    with animation_column:
        st_lottie(lottie_animation,height = 400)
        
        
    
    #servicios
    
    with st.container():
        st.write("---")
        st.header("Servicios  :moon_cake:")
        st.write("##")
        image_column, text_column = st.columns ((1,2))
        with image_column:
            image = Image.open("imagenes/Mecca-Saudi-Arabia-Kaaba.jpg")
            st.image(image, caption="Mecca",use_container_width=True)
        with text_column:
            st.subheader("Diseño de aplicaciones.......11eeeee")
            st.write(
                """si en tus procesos diarios tienes que introducir informacion en diferentes fuentes de datos o bien tienes que trabajar con documentacion
                """
            )
            st.write("[Ver servicios >](https://valerapp.com/servicios/)")
            
        
        
    with st.container():
        st.write("---")
        st.header("Servicios  :moon_cake:")
        st.write("##")
        image_column, text_column = st.columns ((1,2))
        with image_column:
            image = Image.open("imagenes/Mecca-Saudi-Arabia-Kaaba.jpg")
            st.image(image, caption="Mecca",use_container_width=True)
        with text_column:
            st.subheader("Diseño de aplicaciones.......11eeeee")
            st.write(
                """si en tus procesos diarios tienes que introducir informacion en diferentes fuentes de datos o bien tienes que trabajar con documentacion
                """
            )
            st.write("[Ver servicios >](https://valerapp.com/servicios/)")
    
    with st.container():
        st.write("---")
        st.header("Contacta con nosotros ")
        st.write("####")
        contact_form = f"""
            <form action="https://formsubmit.co/{email_contact}" method="POST">
            <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder = "Tu nombre " required>
                <input type="email" name="email" placeholder = "Tu email " required>
                <textarea type="message" name="message" placeholder = "Tu mensage " required></textarea>
                <button type="submit">Enviar mensaje</button>
            </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
            
            
            