# from h11 import Response
# import requests
# from requests.exceptions import HTTPError
# from load_api_key import load_api_key


# filename_ = "C:\\Users\\renio\\Documents\\Recordings\\Text to transcribe.mp3"

# api_key = load_api_key()

# url = 'https://api.openai.com/v1/audio/transcriptions'
# headers = {
#     "Authorization": f"Bearer {api_key}", 
#     # "Content-Type": "multipart/form-data" -> bedzie ustawiony automatycznie dla requests
# }
# data = {
#     # 'file': stream,   -> plik musi byc podany osobno
#     'model': 'whisper-1',
#     'response_format': 'text',
#     }


# def post_audio_and_get_trqnscription(filename_: str, url: str, headers: dict, data:dict) -> Response:
#     with open(filename_, 'rb') as stream:
#         files = {
#             'file': stream
#         }
#         try:
#             response = requests.post(url, headers=headers, files=files, data=data) # argumenty muszą byc nazwane
#             response.raise_for_status()  
#         except HTTPError as http_err:
#             print(f'Http error: {http_err}')
#         except Exception as e:
#             print(f'Other exception: {e}')
#         else:
#             print('Succes!')

#         return response

# if __name__ == '__main__':
#     response = post_audio_and_get_trqnscription(filename_, url, headers, data)
#     print(response)
#     print(response.content)

#  =====================
import sys
from h11 import Response
from load_api_key import load_api_key
from requests.exceptions import HTTPError
import requests

"""Transcriber can transcribe audio file in formats:  mp3, mp4, mpeg, mpga, wav, webm into a text. Then it can print the text or save it into a file."""

class Transcription:
    # @staticmethod ??
    api_key = load_api_key()

    def __init__(self, inputfile: str, outputfile:str, operation: str) -> None:
        self.inputfile = inputfile
        self.outputfile = outputfile
        self.operation = operation

    def save_response_into_file(self, response: Response, outputfile: str) -> None:
        with open(outputfile, 'wb') as writer:
            writer.write(response.content)
        print(f'transcription have been saved into: {outputfile}')

    def post_audio_and_get_trqnscription(self) -> None:
        
        file = self.inputfile
        operation = self.operation
        outputfile = self.outputfile

        url = 'https://api.openai.com/v1/audio/transcriptions'
        # csv 
        headers = {
        "Authorization": f"Bearer {self.api_key}"
        }
        if operation == 'transcription':
            data = {
        'model': 'whisper-1',
        'response_format': 'text',
        }
        else:
            print('wrong operation')
            sys.exit(1)

        with open(file, 'rb') as stream:
            files = {
                'file': stream
            }
            try:
                response = requests.post(url, headers=headers, files=files, data=data) 
                response.raise_for_status()  
            except HTTPError as http_err:
                print(f'Http error: {http_err}')
            except Exception as e:
                print(f'Other exception: {e}')
            else:
                print('Succes!')

        if outputfile:
            self.save_response_into_file(response, outputfile)
        else:
            print(response.content)
            

if __name__ == '__main__':
    file = r"C:\Users\renio\Documents\Recordings\Text to transcribe.mp3"
    outputfile = r"C:\Users\renio\Documents\Python\Projects\Text_transcribed.txt"

    t = Transcription(file, outputfile=outputfile, operation='transcription')

    t.post_audio_and_get_trqnscription()




