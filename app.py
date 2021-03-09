import streamlit as st
import os
from PIL import Image
import pandas as pd
import func_file
#from class_Excel_File_Upload import FileUpload
from zipfile import ZipFile

file_save_path = "./pics/"
img1 = "./pics_4_code/img1.jpg"
img2 = "./pics_4_code/img2.jpg"
zip_path = './zip/Images.zip'
zip_folder = "./zip/"


# @st.cache(allow_output_mutation=True)
# def get_state():ython
#     return []


def upload_file_with_extension():
    df = None
    upload_file = st.file_uploader("Upload Excel File", type=["xlsx"], key="a") # key=a is to seperate the identity of
                                                                                # same widget
    if upload_file is not None:
            st.info('File Uploaded and Executing')
            df = pd.read_excel(upload_file, index_col=None)
    return df


def upload_file_without_extension():
    df = None
    upload_file = st.file_uploader("Upload Excel File", type=["xlsx"], key="b") # key=b is to seperate the identity of
                                                                                # same widget
    if upload_file is not None:
            st.info('File Uploaded')
            df = pd.read_excel(upload_file, index_col=None)
    return df


def main():

    #global df
    st.title("Bulk Image Downloader")

    acitvity = ['Multiple Image URLs with Image Extensions', 'Multiple Image URLs without Image Extensions',\
                                    'Single Image URL with Image Extension', 'Single Image URL without Image Extension',
                                                                                                            "About"]

    choice = st.sidebar.selectbox('Chose An Activity', acitvity)

    if choice == 'Multiple Image URLs with Image Extensions':
        st.subheader("Multiple Image URLs with Image Extensions")
        st.text("")
        st.write("Supported Image Formats: JPEG/JPG, PNG")
        st.text("Upload Excel file with file extension .xlsx in the following format")
        st.image(img1, use_column_width=True)

        # Delete Files in ./pics/ Directory
        for root, dirs, files in os.walk(file_save_path):
            for filename in files:
                del_files = file_save_path + filename
                os.remove(del_files)

        # Delete Files in ./zip/ Directory
        for root, dirs, files in os.walk(zip_folder):
            for filename in files:
                del_zip = zip_folder + filename
                os.remove(del_zip)

        df = upload_file_with_extension()
        try:
            st.dataframe(df.head(5))
        except Exception as e:
            print("Error: In DataFrame", e)

        # fileUpload = FileUpload()
        # df = fileUpload.run()

        try:
            with st.spinner("Please Wait....."):
                func_file.with_extensions(df, file_save_path)
                # Zip and download
                zipObj = ZipFile(zip_path, 'w')
                if zipObj is not None:
                    # Add multiple files to the zip
                    for root, dirs, files in os.walk(file_save_path):
                        for filename in files:
                            img = file_save_path + filename
                            zipObj.write(img)
                    zipObj.close()
                    st.markdown(func_file.get_zip_download_link(zip_path), unsafe_allow_html=True)
                    st.markdown("Right Click and Save As .zip")
                # End Zip and download
            st.write("Process Completed, Hit Refresh Button  or 'F5' to Clear Uploaded File")
        except Exception as e:
            print("Error1: ", e)

    elif choice == 'Multiple Image URLs without Image Extensions':
        st.subheader("Multiple Image URLs without Image Extensions")
        st.text("")
        st.write("Supported Image Formats: JPEG/JPG, PNG")
        st.text("Upload Excel file with file extension .xlsx in the following format")
        st.image(img2, use_column_width=True)
        # df = None
        # Delete Files in ./pics/ Directory
        for root, dirs, files in os.walk(file_save_path):
            for filename in files:
                del_files = file_save_path + filename
                os.remove(del_files)

        # Delete Files in ./zip/ Directory
        for root, dirs, files in os.walk(zip_folder):
            for filename in files:
                del_zip = zip_folder + filename
                os.remove(del_zip)

        df1 = upload_file_without_extension()
        try:
            st.dataframe(df1.head(5))
        except Exception as e:
            print("Error: In DataFrame", e)
        # fileUpload1 = FileUpload()
        # df1 = fileUpload1.run()

        try:
            with st.spinner("Please Wait....."):
                func_file.without_extensions(df1, file_save_path)
                # Zip and download
                zipObj = ZipFile(zip_path, 'w')
                if zipObj is not None:
                    # Add multiple files to the zip
                    for root, dirs, files in os.walk(file_save_path):
                        for filename in files:
                            img = file_save_path + filename
                            zipObj.write(img)
                    zipObj.close()
                    st.markdown(func_file.get_zip_download_link(zip_path), unsafe_allow_html=True)
                    st.markdown("Right Click and Save As .zip")
                # End Zip and download
            st.write("Process Complete, Hit Refresh Button  or 'F5' to Clear Uploaded File")
        except Exception as e:
            print("Error2:", e)

    elif choice == 'Single Image URL with Image Extension':
        st.subheader("Single Image URL with Image Extension")
        st.text("")
        st.write("Supported Image Formats: JPEG/JPG, PNG")

        image_url = st.text_input("Enter URL")

        # Delete Files in ./pics/ Directory
        for root, dirs, files in os.walk(file_save_path):
            for filename in files:
                img = file_save_path + filename
                os.remove(img)

        # Delete Files in ./zip/ Directory
        for root, dirs, files in os.walk(zip_folder):
            for filename in files:
                del_zip = zip_folder + filename
                os.remove(del_zip)

        if image_url[-4:] == ".jpg" or image_url[-5:] == ".jpeg" \
                or image_url[-4:] == ".bmp" or image_url[-4:] == ".png":
            try:
                func_file.url_with_extension(image_url, file_save_path)
                st.write("Success")
                for root, dirs, files in os.walk(file_save_path):
                    for filename in files:
                        img = file_save_path + filename
                        st.image(img, use_column_width=True)
                        #functions.get_image_download_link(file_save_path + filename)
                        img = Image.open(img)
                        st.markdown(func_file.get_image_download_link(img), unsafe_allow_html=True)
                        st.markdown("Right Click and Save Link As")
            except Exception as e:
                st.write("Operation Failed")
        else:
            st.write("Enter Valid URL")

    elif choice == 'Single Image URL without Image Extension':
        st.subheader("Single Image URL without Image Extension")
        st.text("")
        st.write("Supported Image Formats: JPEG/JPG, PNG")

        image_url = st.text_input("Enter Image URL without Image Extension")

        #Delete Files in ./pics/ Directory
        for root, dirs, files in os.walk(file_save_path):
            for filename in files:
                img = file_save_path + filename
                os.remove(img)

        # Delete Files in ./zip/ Directory
        for root, dirs, files in os.walk(zip_folder):
            for filename in files:
                del_zip = zip_folder + filename
                os.remove(del_zip)

        if "." not in image_url[-6:] and len(image_url) >= 8:
            try:
                func_file.url_without_extension(image_url, file_save_path)
                #st.write("Party Time")
                for root, dirs, files in os.walk(file_save_path):
                    for filename in files:
                        img = file_save_path + filename
                        st.image(img, use_column_width=True)
                        img = Image.open(img)
                        st.markdown(func_file.get_image_download_link(img), unsafe_allow_html=True)
                        st.markdown("Right Click and Save Link As")
            except Exception as e:
                st.write("Operation Failed")
        else:
            st.write("Enter Valid URL")

    elif choice == 'About':
        #st.subheader("Bulk Image Downloader")
        st.text("")
        st.info("By: Mazhar")
        st.info("mazqoty.01@gmail.com")


if __name__ == '__main__':
    main()

