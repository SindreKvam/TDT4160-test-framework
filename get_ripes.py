import requests
import platform
import os

LINUX_APP = "https://github.com/mortbopet/Ripes/releases/download/v2.2.6/Ripes-v2.2.6-linux-x86_64.AppImage"
WINDOWS_APP = "https://github.com/mortbopet/Ripes/releases/download/v2.2.6/Ripes-v2.2.6-win-x86_64.zip"
OSX_APP = "https://github.com/mortbopet/Ripes/releases/download/v2.2.6/Ripes-v2.2.6-mac-x86_64.zip"



if __name__ == "__main__":
    operative_system = platform.system()

    print(f"Starting ripes download for {operative_system}")

    if operative_system == "Windows":
        r = requests.get(WINDOWS_APP, allow_redirects=True)

    elif operative_system == "Darwin":
        r = requests.get(OSX_APP, allow_redirects=True)

    elif operative_system == "Linux":
        r = requests.get(LINUX_APP, allow_redirects=True)
    
    else:
        print("Unknown OS")
        exit()
    
    with open("Ripes.zip","wb") as f:
        f.write(r.content)


    