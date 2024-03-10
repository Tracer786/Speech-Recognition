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