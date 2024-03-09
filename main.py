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

# polling 
def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers = headers)
    # print(polling_response)
    # print(polling_response.json())
    return polling_response.json()

#will check whether the polling is complete or not
def get_transcription_result_url(audio_url):
    transcript_id = transcribe(audio_url)
    while True:
        data = poll(transcript_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']
        
audio_url = upload(filename)
data,error = get_transcription_result_url(audio_url)
print(data)

# save transcription