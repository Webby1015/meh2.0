import urllib.request
import requests
import os
from Square_image import make_square

#### cat image
if not os.path.exists('images\Cat_image'):
    os.makedirs('images\Cat_image')

url = 'https://cataas.com/cat'
filename = "cat.jpg"
#           saving image
urllib.request.urlretrieve(url, os.path.join('images\Cat_image', filename))
#           Making Square
image_path = 'images\Cat_image\cat.jpg'
square_image = make_square(image_path)
square_image.save('images\Cat_image\cat.jpg')


#### dog image
if not os.path.exists('images\Dog_image'):
    os.makedirs('images\Dog_image')
    
url = 'https://dog.ceo/api/breeds/image/random'

response = requests.get(url)
imge_object = response.json()

url = imge_object['message']
filename = "dog.jpg"
#           saving image
urllib.request.urlretrieve(url, os.path.join('images\Dog_image', filename))
#           Making Square
image_path = 'images\Dog_image\dog.jpg'
square_image = make_square(image_path)
square_image.save('images\Dog_image\dog.jpg')


#### Anime images
if not os.path.exists('images\Anime_girl_image'):
    os.makedirs('images\Anime_girl_image')
url = "https://random-anime-img.p.rapidapi.com/anime"

headers = {
	"X-RapidAPI-Key": "bb438b10afmshd734efc47e0394dp11e7a8jsn641bc21f219f",
	"X-RapidAPI-Host": "random-anime-img.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
url = response.json()['url']
filename = "AnimeGirl.jpg"
#           saving image
urllib.request.urlretrieve(url, os.path.join('images\Anime_girl_image', filename))
#           Making Square
image_path = 'images\Anime_girl_image\AnimeGirl.jpg'
square_image = make_square(image_path)
square_image.save('images\Anime_girl_image\AnimeGirl.jpg')