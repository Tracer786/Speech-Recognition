import requests   # requests library is required to talk to the Assembly AI's API.
from api_secrets import API_KEY_ASSEMBLYAI
import sys  # to get the file name from the terminal
upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'
headers = {'authorization': API_KEY_ASSEMBLYAI} 
filename = sys.argv[1]

# upload
def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data   
    upload_response = requests.post(upload_endpoint,
                                headers=headers,
                                data=read_file(filename))
    # we are doing a post request while uploading the file to Assembly AI.
    # print(response.json())  # after uploading the file we need to check what kind of response we are getting
    audio_url = upload_response.json()['upload_url']
    return audio_url

# transcribe
def transcribe(audio_url):
    transcript_request = { "audio_url": audio_url}
    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    # print(response.json())
    job_id = transcript_response.json()['id']
    return job_id

audio_url = upload(filename)
job_id = transcribe(audio_url)
print(job_id)

# pooling 

# save transcription