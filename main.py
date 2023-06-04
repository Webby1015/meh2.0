import urllib.request
import requests
import os
from Square_image import make_square

#### cat image
if not os.path.exists('Cat_image'):
    os.makedirs('Cat_image')

url = 'https://cataas.com/cat'
filename = "cat.jpg"
#           saving image
urllib.request.urlretrieve(url, os.path.join('Cat_image', filename))
#           Making Square
image_path = 'Cat_image\cat.jpg'
square_image = make_square(image_path)
square_image.save('Cat_image\cat.jpg')


#### dog image
if not os.path.exists('Dog_image'):
    os.makedirs('Dog_image')
    
url = 'https://dog.ceo/api/breeds/image/random'

response = requests.get(url)
imge_object = response.json()

url = imge_object['message']
filename = "dog.jpg"
#           saving image
urllib.request.urlretrieve(url, os.path.join('Dog_image', filename))
#           Making Square
image_path = 'Dog_image\dog.jpg'
square_image = make_square(image_path)
square_image.save('Dog_image\dog.jpg')

#### Anime images

url = "https://random-anime-img.p.rapidapi.com/anime"

headers = {
	"X-RapidAPI-Key": "bb438b10afmshd734efc47e0394dp11e7a8jsn641bc21f219f",
	"X-RapidAPI-Host": "random-anime-img.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

url = response.json()['url']
print(url)