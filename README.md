# selenium_youtube_mp3_parser

#### Programm for download list muzik files from youtube and convert to mp3

start file **selen_youtube.py** </br>
**URL_LIST_YOUTUBE** - playlist with youtube files. </br>
exemple: URL_LIST_YOUTUBE = "https://www.youtube.com/watch?v=h8gE1WF7mBE&list=PL4C2OaC1jQqR3ICDBf4j1dH1Fk4uIo-Lx&index=101"
</br>
### For work need webdriver.Chrome()
download webdriver for Chrome https://chromedriver.chromium.org/downloads




#### bug pytube in extract.py

```
       def apply_descrambler(stream_data: Dict, key: str) -> None:
should be            
            cipher_url = [
                parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats)
            ]       
was
        cipher_url = [
                parse_qs(formats[i]["Cipher"]) for i, data in enumerate(formats)
            ]
```
