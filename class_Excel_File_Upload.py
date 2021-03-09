try:
    import pandas as pd
    import streamlit as st
    #import openpyxl
    #from io import StringIO
except Exception as e:
    print(e)

STYLE = """
<style>
img {max-width: 100%}
</style>
"""


class FileUpload(object):
    def __init__(self):
        self.fileTypes = ['xlsx']

    def run(self):
        global df
        st.markdown(STYLE, unsafe_allow_html=True)
        upload_file = st.file_uploader("Upload File", type=self.fileTypes, key="1")
        show_file = st.empty()
        if upload_file is not None:
            show_file.info("File Uploaded and Executing")
            df = pd.read_excel(upload_file, index_col=None)
            st.dataframe(df.head(5))
            del upload_file
        else:
            print("File is Not Appropriate")
        return df


# if __name__ == "__main__":
#     fileUpload = FileUpload()
#     df = fileUpload.run()
#     print(type(df))


