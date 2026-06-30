import os
import boto3
import numpy as np

ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET = os.getenv("AWS_SECRET")
AWS_REGION = "eu-north-1"

if not ACCESS_KEY or not AWS_SECRET:
    raise ValueError(
        "missing AWS credentials, make sure to add them to your environment variables!"
    )

client = boto3.client(
    'polly',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET,
    region_name=AWS_REGION
)

def speak(text, voice="Brian"):
    response = client.synthesize_speech(VoiceId=voice,
                    Text=text,
                    OutputFormat='pcm',
                    Engine='standard',
                    SampleRate='16000')
    
    audio_data = response["AudioStream"].read()

    samples = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0

    sd.play(
        samples,
        samplerate=16000,
        blocking=True
    )

if __name__ == "__main__"
    speak("Hello world") #test with brian voice
    speak("Hello world", voice="Kevin") #test with another voice
