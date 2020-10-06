import argparse
import locale
import logging
import requests
import json

from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient
from aiy.voice import tts
from google.cloud import texttospeech


def get_hints(language_code):
    if language_code.startswith('ko_'):
        return ('질문하시오')
    return None

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

def google_say(text):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.types.SynthesisInput(text=text)

    voice = texttospeech.types.VoiceSelectionParams(language_code='ko-KR', ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config=texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    with open('temp.mp3', 'wb') as out:
        out.write(response.audio_content)

    mixer.init(frequency=22100)
    mixer.music.load('temp.mp3')
    mixer.music.play()
    mixer.quit()

def main():
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(description='Assistant service example.')
    parser.add_argument('--language', default='ko-KR')
    args = parser.parse_args()

    logging.info('%s... 초기화중...', args.language)
    hints = get_hints(args.language)
    client = CloudSpeechClient()
    with Board() as board:
        while True:
            logging.info('Press button to start conversation...')
            board.led.state = Led.ON
            board.button.wait_for_press()            
            logging.info('Conversation started!')

            if hints:
                logging.info('??????')
            else:
                logging.info('말씀해주세요')
            
            text = client.recognize(language_code=args.language, hint_phrases = hints)

            if text is None:
                logging.info('아무것도 못 들었어요.')
                tts.say('You said nothing.')
                continue
            
            elif '안녕' in text:
                tts.say("Bye Bye")
                break
                     
            elif 'goodbye' in text:
                tts.say("Goodbye")
                break

            logging.info("제가 제대로 들은게 맞나요? : '%s'" % text)
            

            data = {'text' : text}
            res = requests.post("http://3.34.174.254:3000/python/py", data=data)
            try:        
                say = json.loads(res.text)
                board.led.state = Led.BLINK #요청 응답이 잘 이루어졌다는 뜻
                for i in range(len(say)):
                    answer = str(say[i]['ans'])
                    logging.info(answer)
                    tts.say(answer)
                    google_say(answer + "입니다")
            except:
                logging.info("잘못된 응답입니다.")
                board.led.state = Led.BEACON_DARK
                tts.say("Its SQL error.")
            

            
            
    



if __name__ == "__main__":
    main()