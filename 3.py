from urllib.request import urlopen
from PIL import Image

with urlopen('https://img.freepik.com/free-photo/close-up-on-kitten-surrounded-by-flowers_23-2150782329.jpg?size=626&ext=jpg&ga=GA1.1.1413502914.1713744000&semt=ais', 'rb') as f:
    Image.open(f).show()