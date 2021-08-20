import requests


# url = 'http://127.0.0.1:5000/register'
# param = {
#     'username':'liokkk',
#     'password':'123456',
#     'sex':1,
#     'telephone':'8989898989',
#     'address':'bj'
# }
# res = requests.post(url,param)
# print(res.text)

url = 'http://127.0.0.1:5000/login'
param = {
    'username':'liokkk',
    'password':'123456'
}
res = requests.post(url,param)
print(res.text)