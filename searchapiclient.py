import requests

url = 'http://13.232.114.25:8000/'  # Replace with your Django server URL
data = {'img_url': 'https://articlebucketgts.s3.ap-south-1.amazonaws.com/seapi/2.jpg'}
response = requests.post(url, data=data)
print(response.json())