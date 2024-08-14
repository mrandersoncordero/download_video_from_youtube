import streamlit as st
import PyPDF2 # importa la biblioteca para trabajar con archivos PDF

# VARIABLES
output_pdf = 'documents/pdf_final.pdf' # define el nombre del archivo de salida donde se guardara el PDF final combinado

# FUNCTIONS

def unir_pdfs(output_path, documents):
    # Crea u nobjeto PDfMerger de PyPDF2 para combinar archivos PDF
    pdf_final = PyPDF2.PdfMerger()

    for document in documents:
        pdf_final.append(document) # Agrega cada documento PDF a la fusion
    pdf_final.write(output_path) # guarda el PDF combinado en la ruta de salida


# --- FRONT ---

st.image('./assets/combine-pdf.png')
st.header('Unir PDF')
st.subheader('Adjuntar pdfs para unir')

pdf_adjuntos = st.file_uploader(label='', accept_multiple_files=True)

unir = st.button(label='Unir PDFs') # Crea un boton llamado 'Unir PDFs'

if unir:
    if len(pdf_adjuntos) <= 1:
        st.warning('Debes adjuntar mas de un PDF')
    else:
        unir_pdfs(output_pdf, pdf_adjuntos)
        st.success('Desde aqui puede descargar el PDF final.')
        with open(output_pdf, 'rb') as file:
            pdf_data = file.read()
        st.download_button(label='Descargar PDF final', data=pdf_data, file_name='pdf_final.pdf')
