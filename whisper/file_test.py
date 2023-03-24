import requests


# Call the other API endpoint and pass the file
url = "http://localhost:5000/whisper"
# headers = {'Authorization': 'Bearer YOUR_TOKEN'}
files = {'file': open(f"./whisper/harvard.wav", 'rb')}
response = requests.post(url, files=files)

if response.status_code == 200:

    print(response.json())
else:
    print(response.status_code)
    print(response.text)