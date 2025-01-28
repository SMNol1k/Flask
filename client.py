import requests

response = requests.post(
    'http://127.0.0.1:5000/api',
    json={'title': 'Объявление', 'content': 'Ваше новое объявление'},
)
print(response.status_code)
print(response.text)


# response = requests.delete(
#     "http://127.0.0.1:5000/api/1/",
# )
# print(response.status_code)
# print(response.text)
#
# response = requests.get(
#     "http://127.0.0.1:5000/api/1",
# )
# print(response.status_code)
# print(response.text)