str = input("File name: ").strip()

extension = ""
if "." in str:
    extension = str[str.rindex("."):].lower()


match extension:
    case ".gif":
        print("image/gif")
    case ".jpg" | ".jpeg":
        print("image/jpeg")
    case ".txt":
        print("text/plain")
    case ".png":
        print("image/png")
    case ".pdf":
        print("application/pdf")
    case ".zip":
        print("application/zip")
    case _:
        print("application/octet-stream")