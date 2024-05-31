import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64

def get_image_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
    
def color_line():
    st.markdown(
        """
        <hr style="border: none; height: 2px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet); margin-top: 0;">
        """,
        unsafe_allow_html=True,
    )

# Cargar la imagen de perfil
image_path = "circular_image_sin_bg.png"
image_base64 = get_image_as_base64(image_path)

# Crear la barra de navegación lateral
with st.sidebar:
    # Mostrar la imagen de perfil centrada
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; margin-bottom: 20px;">
            <img src="data:image/jpeg;base64,{image_base64}" width="450">
        </div>
        """,
        unsafe_allow_html=True,
    )
    selected = option_menu(
        menu_title="Navegación",  # required
        options=["Introducción", "Habilidades", "Proyectos", "Investigaciones y Publicaciones", "Logros", "Servicios", "Contacto", "¡Ponte en Contacto!"],  # required
        icons=["house", "book", "code", "file-earmark-text", "trophy", "briefcase", "envelope", "phone"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
    )


# Sección Introducción
if selected == "Introducción":
    st.title("Introducción")
    color_line()
    st.write("""
    ¡Bienvenidos a mi aplicación! Aquí encontrarás información sobre mí, mis proyectos, y cómo puedes contactarme.
    """)

# Sección Habilidades
elif selected == "Habilidades":
    st.title("Habilidades")
    st.write("""
    - Programación en Python
    - Desarrollo web con Django y Flask
    - Análisis de datos con Pandas y NumPy
    - Machine Learning con scikit-learn
    - Visualización de datos con Matplotlib y Seaborn
    """)

# Sección Proyectos
elif selected == "Proyectos":
    st.title("Proyectos")
    st.write("### Proyecto 1: [Nombre del Proyecto 1]")
    st.write("Descripción breve del proyecto 1.")
    st.write("Enlace: [GitHub/Website](https://github.com/tu_usuario/proyecto1)")
    st.write("### Proyecto 2: [Nombre del Proyecto 2]")
    st.write("Descripción breve del proyecto 2.")
    st.write("Enlace: [GitHub/Website](https://github.com/tu_usuario/proyecto2)")

# Sección Investigaciones y Publicaciones
elif selected == "Investigaciones y Publicaciones":
    st.title("Investigaciones y Publicaciones")
    st.write("""
    - Publicación 1: Título de la publicación
    - Publicación 2: Título de la publicación
    - Publicación 3: Título de la publicación
    """)

# Sección Logros
elif selected == "Logros":
    st.title("Logros")
    st.write("""
    - Logro 1: Descripción del logro
    - Logro 2: Descripción del logro
    - Logro 3: Descripción del logro
    """)

# Sección Servicios
elif selected == "Servicios":
    st.title("Servicios")
    st.write("""
    - Servicio 1: Descripción del servicio
    - Servicio 2: Descripción del servicio
    - Servicio 3: Descripción del servicio
    """)

# Sección Contacto
elif selected == "Contacto":
    st.title("Contacto")
    st.write("Si quieres ponerte en contacto conmigo, puedes encontrarme en:")
    st.write("[LinkedIn](https://www.linkedin.com/in/tu_perfil)")
    st.write("[Twitter](https://twitter.com/tu_usuario)")
    st.write("[Email](mailto:tu_correo@example.com)")

# Sección ¡Ponte en Contacto!
elif selected == "¡Ponte en Contacto!":
    st.title("¡Ponte en Contacto!")
    st.write("Me encantaría saber de ti. ¡No dudes en enviarme un mensaje!")