import requests
import time 
import webbrowser

def dogimage(count):
    for i in range(count):
        try:
            url = "https://dog.ceo/api/breeds/image/random"
            response = requests.get(url)
            response.raise_for_status()  # This will raise an error for non-2xx responses
            x = response.json()
            images = requests.get(x["message"])
            with open(f"dogimages/{i}.jpg",'wb',) as f:
                f.write(images.content)
                print(f"{i}.jpg generated succesfully")


            time.sleep(1)
        except Exception as E:
            print(f"Error Occurred: {E}")

dogimage(10)
