import requests
# requests library is required to talk to the Assembly AI's API.

from api_secrets import API_KEY_ASSEMBLYAI

import sys  # to get the file name from the terminal

upload_endpoint = 'https://api.assemblyai.com/v2/upload'

filename = sys.argv[1]


def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data
            
            
headers = {'authorization': API_KEY_ASSEMBLYAI} 
response = requests.post(upload_endpoint,
                             headers=headers,
                             data=read_file(filename))

# we are doing a post request while uploading the file to Assembly AI.


print(response.json())  # after uploading the file we need to check what kind of response we are getting


# upload

# transcribe

# pooling 

# save transcription