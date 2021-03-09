import urllib.request
import base64
from io import BytesIO

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) \
       Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

url_with_ext = None
url_without_ext = None


def get_image_download_link(img):
    """Generates a link allowing the PIL image to be downloaded
	in:  PIL image
	out: href string
	"""
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:image/jpeg;base64,{img_str}">Download result</a>'
    return href


def get_zip_download_link(zip_path):
    with open(zip_path, "rb") as f:
        bytes = f.read()
        b64 = base64.b64encode(bytes).decode()
        href = f'<a href="data:file/zip;base64,{b64}">Download File</a> (right-click and save as .zip)'
        # st.sidebar.markdown(href, unsafe_allow_html=True)
        return href


def url_with_extension(image_url, file_save_path):
    if len(image_url) >= 8:
        try:
            page = urllib.request.Request(image_url, headers=hdr)
            infile = urllib.request.urlopen(page).read()
            # Read the content as string decoded with ISO-8859-1
            # data = infile.decode('ISO-8859-1')
            image_name = image_url.split("/")[-1]
            # print(image_name)
            imagefile = open(file_save_path + image_name, "wb")
            imagefile.write(infile)
            imagefile.close()
        except Exception as e:
            print("Can't Find Url or Invalid URL")
    else:
        return print("Failed: Problem in URL")


def url_without_extension(image_url, file_save_path):
    if "." not in image_url[-6:] and len(image_url) >= 8:
        try:
            page = urllib.request.Request(image_url, headers=hdr)
            infile = urllib.request.urlopen(page).read()
            # Read the content as string decoded with ISO-8859-1
            # data = infile.decode('ISO-8859-1')
            image_name = image_url.split("/")[-1]
            # print(image_name)
            imagefile = open(file_save_path + image_name + ".jpeg", "wb")
            imagefile.write(infile)
            imagefile.close()
        except Exception as e:
            print("Can't Find Url or Invalid URL")
    else:
        return print("Failed: Problem in URL")


def with_extensions(df, file_save_path):
    links = df.values.tolist()
    for i in range(0, len(links)):
        try:
            image_url = str(links[i]).replace("['", "").replace("']", "")
            # Open the URL as Browser, not as python urllib
            page = urllib.request.Request(image_url, headers=hdr)
            infile = urllib.request.urlopen(page).read()
            # Read the content as string decoded with ISO-8859-1
            # data = infile.decode('ISO-8859-1')
            image_name = image_url.split("/")[-1]
            # print(image_name)
            imagefile = open(file_save_path + image_name, "wb")
            imagefile.write(infile)
            imagefile.close()
        except Exception as e:
            print("Error1_F: ", e)
            break
    links = None


def without_extensions(df1, file_save_path):
    links = df1.values.tolist()
    for i in range(0, len(links)):
        try:
            image_url = str(links[i]).replace("['", "").replace("']", "")
            # Open the URL as Browser, not as python urllib
            page = urllib.request.Request(image_url, headers=hdr)
            infile = urllib.request.urlopen(page).read()
            # Read the content as string decoded with ISO-8859-1
            # data = infile.decode('ISO-8859-1')
            image_name = image_url.split("/")[-1]
            # print(image_name)
            imagefile = open(file_save_path + image_name + ".jpeg", "wb")
            imagefile.write(infile)
            imagefile.close()

        except Exception as e:
            print("Error2_F: ", e)
            break
    links = None
