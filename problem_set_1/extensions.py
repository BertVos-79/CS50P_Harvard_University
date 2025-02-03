def main():
    filename = input("Write your filename here. Use the format 'filename.filetype':\n").strip().lower()
    media_converter(filename)

def media_converter(filename):
    filename_list = filename.split(".")
    match filename_list[-1]:
        case "gif"|"jpeg"|"png":
            print(f"image/{filename_list[-1]}")
        case "jpg":
            print("image/jpeg")
        case "pdf"|"zip":
            print(f"application/{filename_list[-1]}")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")


main()

