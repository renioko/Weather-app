import os
from dotenv import load_dotenv

import openai

class Transformer:
    @staticmethod
    def load_api_key() -> str:
        """loads api key"""
        load_dotenv()
        try:
            openai.api_key = os.getenv('OPEN_API_KEY')
        except ValueError:
            print('problem with OPEN_API_KEY')
        return openai.api_key
    
    def __init__(self) -> None:
        pass

class Transcribed(Transformer):
    def __init__(self, inputfile: str) -> None:
        super().load_api_key()
        self.inputfile = inputfile

        """Transcriber can transcribe audio file in formats:  mp3, mp4, mpeg, mpga, wav, webm into a text."""
    
    def load_and_and_transcript_audio(self) -> None:
        """loads audio file, connects with whisper, 
        transcribes audio file into a text and prints it"""
        Transformer().load_api_key()

        with open(self.inputfile, 'rb') as audio_file:
            transcription = openai.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format='text'
    )
        print(transcription)
        # ubgrade: mmozna wybrac print, save into a file or return

def main():
    filename = "C:\\Users\\renio\\Documents\\Recordings\\Text to transcribe2.mp3"

    transcribed = Transcribed(filename)
    transcribed.load_and_and_transcript_audio()

if __name__ == '__main__':
    main()