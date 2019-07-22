import random
import urllib.request

def download(URL):
    name = random.randrange(1, 2001)
    fullName = str(name) + ".jpg"
    urllib.request.urlretrieve(URL, fullName)

image_address = "http://imgnews.naver.net/image/5372/2019/07/21/0000026522_001_20190721112037616.jpg"

download(image_address)
