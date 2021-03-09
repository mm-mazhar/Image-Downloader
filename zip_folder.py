from zipfile import ZipFile
import os
#import base64
#import streamlit as st

file_save_path = "./pics/"
zip_path = './zip/Images.zip'

# create a ZipFile object
zipObj = ZipFile(zip_path, 'w')
# Add multiple files to the zip
for root, dirs, files in os.walk(file_save_path):
    for filename in files:
        img = file_save_path + filename
        zipObj.write(img)

zipObj.close()

# with open(zip_path, "rb") as f:
#     bytes = f.read()
#     b64 = base64.b64encode(bytes).decode()
#     href = f'<a href="data:file/zip;base64,{b64}">Download File</a> (right-click and save as .zip)'
#     st.sidebar.markdown(href, unsafe_allow_html=True)