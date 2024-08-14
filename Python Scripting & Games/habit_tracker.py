import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'

USERNAME = ''
TOKEN = ''

paramaters = {
    'token' : TOKEN,
    'username' : USERNAME,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes'
}


# CREATE ACCOUNT
# respone = requests.post(url=pixela_endpoint, json=paramaters)
# print(respone.text)

graph_endpoint = f'https://pixe.la/v1/users/{paramaters['username']}/graphs'

graph_config = {
    'id' : 'graph1',
    'name' : 'Cycling graph',
    'unit' : 'Km',
    'type' : 'float',
    'color' : 'momiji'
}

header = {
    'X-USER-TOKEN' : paramaters['token']
}

# CREATE GRAPH
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

date = datetime.now()

post_pixel_endpoint = f'https://pixe.la/v1/users/{paramaters["username"]}/graphs/{graph_config["id"]}'

post_config = {
    'date' : date.strftime("%Y%m%d"),
    'quantity' : str(input('How many kilometers did you cycle today? : '))
}


# POST PIXEL
response = requests.post(url=post_pixel_endpoint, json=post_config, headers=header)
print(response.text)