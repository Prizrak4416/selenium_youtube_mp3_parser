from pytube import YouTube
from pathlib import Path
from pydub import AudioSegment


""" bug pytube in extract.py
        def apply_descrambler(stream_data: Dict, key: str) -> None:
should be            
            cipher_url = [
                parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats)
            ]       
was
        cipher_url = [
                parse_qs(formats[i]["Cipher"]) for i, data in enumerate(formats)
            ]
"""


DIR = Path(__file__).resolve().parent
AUDIO_PATH = DIR.joinpath('audio')

def get_video_audio(url):
    """Get parameters video from youtube url

        Get parameters from youtube, chooses audio 128kbps

    :param str url:
        The html contents.
    :return:
        parameters video content and audio content
    """
    video = YouTube(url)
    list_video = video.streams
    audio_mas = []

    for i in list_video:
        if i.type == 'audio':
            audio_mas.append((i.abr, i))

    audio_for_download = ''

    for value, key in audio_mas:
        if value == "128kbps":
            audio_for_download = key
        elif audio_for_download == '':
            audio_for_download = key

    print('audio - ', audio_for_download)

    return audio_for_download, video.title.replace('\\', ' ').replace('/', ' ').replace('\'', ' ').replace('\"', ' ')


def download_audio(audioParam):
    """Download audio with youtube

    :param audioParam:
        audio parameters on youtube
    :return:
        return the path to the audio file
    """
    audioParam.download(filename='audio', output_path=DIR)


def create_audio(titleFile):
    """ converting audio file to mp3

    :param titleFile:
        name video on youtube
    :return: None
    """
    if Path(AUDIO_PATH.with_suffix('.mp4')).exists():
        mp4_version = AudioSegment.from_file(AUDIO_PATH.with_suffix('.mp4'), "mp4")
    else:
        mp4_version = AudioSegment.from_file(AUDIO_PATH.with_suffix('.webm'), "webm")
    mp4_version.export(DIR.joinpath(titleFile).with_suffix('.mp3'), format="mp3")


def del_file():
    """ delet audio file and video file downloaded with youtube

    :return: None
    """
    if Path(AUDIO_PATH.with_suffix('.mp4')).exists():
        path = Path(AUDIO_PATH.with_suffix('.mp4'))
        path.unlink()
    elif Path(AUDIO_PATH.with_suffix('.webm')).exists():
        path = Path(AUDIO_PATH.with_suffix('.webm'))
        path.unlink()

def make_mp3_file(url_youtube):
    """
        make mp3 file from video youtube
    :param str url_youtube:
    :return: None
    """

    audio, title = get_video_audio(url_youtube)
    if DIR.joinpath(title).with_suffix('.mp3').exists() == False:
        download_audio(audio)
        create_audio(title)
        del_file()
