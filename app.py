import requests
import os

FEDAUTH = os.getenv('FEDAUTH')
    
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json;odata=verbose",
    "Content-Type": "application/json;odata=verbose"
})
session.cookies.set('FedAuth', FEDAUTH)
# session.cookies.set('rtFa', 'your_rtfa_cookie_value')

# File URL
file_url = "https://whiskerlabs.sharepoint.com/sites/DataProvidedbyTing/_layouts/15/download.aspx?UniqueId=02f86b37-2f24-4267-9cf2-88fc6750b269\u0026Translate=false\u0026tempauth=v1.eyJzaXRlaWQiOiJjMWEyOGM2MS1jOGYwLTQ5MzAtODNhMC00ZWIwYzA1Njc0OTUiLCJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvd2hpc2tlcmxhYnMuc2hhcmVwb2ludC5jb21ANDU1MGFmMjAtNDZjOS00NjQwLThjNGUtZDhjNDdhNmJlYzc1IiwiZXhwIjoiMTczNjU1NzE3NCJ9.CiMKCXNoYXJpbmdpZBIWOXhFU1gvaVdaMGV0QXVkWGtGSnU3dwoKCgRzbmlkEgI5ORILCOjig9mt5Ng9EAUaDjk4LjIwMy4xOTEuMjUxIhRtaWNyb3NvZnQuc2hhcmVwb2ludCosNUFMRXdqZThOT0dRREN4UEhwYWxFZW5JOEk2Yi94aFIzYkU4enRUc04vVT0wkwE4AUIQoXYucmEAAHB9GEzkvj6N7EoQaGFzaGVkcHJvb2Z0b2tlbmIEdHJ1ZXI5MGguZnxtZW1iZXJzaGlwfHVybiUzYXNwbyUzYWd1ZXN0I2thaS50ZW9oQGRhbGxhc25ld3MuY29tegEwwgE5MCMuZnxtZW1iZXJzaGlwfHVybiUzYXNwbyUzYWd1ZXN0I2thaS50ZW9oQGRhbGxhc25ld3MuY29tyAEB.3AttPcGnUc-TSyClg9oTfv0DWnNSmPoa-oEJwszl2TA"

# Download the file
response = session.get(file_url)
if response.status_code == 200:
    with open("Storm_Individual_Power_Outages.csv", "wb") as file:
        file.write(response.content)
    print("File downloaded successfully.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
