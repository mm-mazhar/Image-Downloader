#-----Imports-----#
import func_file


path_without_extension = "C:/LENOVO/MAZ/Coding/Python/Projects/PyCharmProjects/image_downloader" \
                         "/csv_excel_files/urls_without_extension.xlsx"
path_with_extension = "C:/LENOVO/MAZ/Coding/Python/Projects/PyCharmProjects/image_downloader/csv_excel_files/" \
                        "urls_with_extension.xlsx"

#-----If Links have no file extension, Downloading Images from Excel File-----#

url_with_ext = input("Enter Image URL with extension: ")
func_file.url_with_extension(url_with_ext)

url_without_ext = input("Enter image URL which doesn't have file extension: ")
func_file.url_without_extension(url_without_ext)

func_file.with_extensions(path_with_extension)
func_file.without_extensions(path_without_extension)



