import sys  # to get the file name from the terminal
from api_communication import * 

new_filename = input('Suggest a name for the output file: ')
filename = sys.argv[1]

audio_url = upload(filename)
save_transcript(audio_url,new_filename)