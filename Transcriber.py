from load_api_key import load_api_key
import openai

"""Transcriber can transcribe audio file in formats:  mp3, mp4, mpeg, mpga, wav, webm into a text."""

def load_and_and_transcript_audio(filename: str) -> None:
    """loads audio file, connects with whisper, 
    transcribes audio file into a text and prints it"""
    load_api_key()
    with open(filename, 'rb') as audio_file:
        transcription = openai.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format='text'
)
    print(transcription)
    # ubgrade: mmozna wybrac print, save into a file or return

    # dry i kiss
    # porady co usprawnic w kodzie, tylko porady
    # dodam streszczenie


def main():
    filename = "C:\\Users\\renio\\Documents\\Recordings\\Text to transcribe.mp3"
    load_and_and_transcript_audio(filename)

if __name__ == '__main__':
    main()











# jestem kobietą, więc jak mówię to podaję dużo informacji kontekstowych, ale dopóki nie sformułuję pytania to go nie zadałam. 

# * FUNKCJA - zapisywanie do pliku, 
# * nowa funkcja - translacja
# klasa - plik poczatkowy, plik końcowy lub druk if None, transkrypcja lub translacja
# * dzieki klasie mozliwosc poddawania wielu plików tym procedurom