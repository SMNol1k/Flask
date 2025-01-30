import requests

# response = requests.post(
#     'http://127.0.0.1:5000/api',
#     json={'id':'5', 'title': 'Test Ad', 'content': 'This is a test advertisement.', 'owner': 'user2'},
# )
# print(response.status_code)
# print(response.json())

response = requests.delete(
    "http://127.0.0.1:5000/api/5",
)
print(response.status_code)
print(response.text)

# response = requests.get(
#     "http://127.0.0.1:5000/api/5",
# )
# print(response.status_code)
# print(response.text)