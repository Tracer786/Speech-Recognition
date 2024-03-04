import requests
# requests library is required to talk to the Assembly AI's API.

from api_secrets import API_KEY_ASSEMBLYAI


def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data
            
            
headers = {'authorization': API_KEY_ASSEMBLYAI} 
response = requests.post('https://api.assemblyai.com/v2/upload',
                             headers=headers,
                             data=read_file(filename))


# upload

# transcribe

# pooling 

# save transcription