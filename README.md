# korean-romanizer-2012
The Rules of Latin Alphabetic Transcription of Korean Language 로 조선글을 라틴문자로 변환하겠습니다. 

## korean_letter_separator.py
```python
from korean_letter_romanizer import romanize
romanize(string, sign:bool=True, is_oe:bool=False)
```
- string: 조선어 문자렬
- sign: 부호를 붙이기
- is_oe : ㅚ를 oe로 적기