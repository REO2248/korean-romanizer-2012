
def korean_letter_to_codepoint(korean_letter):
    codepoint = ord(korean_letter) - 0xAC00
    if codepoint < 0 or codepoint > 11172:
        return None
    else:
        return codepoint

def decompose_korean_letter(korean_letter):
    codepoint = korean_letter_to_codepoint(korean_letter)
    if codepoint is None:
        return None, None, None
    else:
        jaum = codepoint // (21 * 28)
        moum = (codepoint - jaum * 21 * 28) // 28
        patchim = codepoint - jaum * 21 * 28 - moum * 28
        return jaum, moum, patchim

def compose_korean_letter(jaum:int, moum:int, patchim:int):
    codepoint = jaum * 21 * 28 + moum * 28 + patchim + 0xAC00
    return chr(codepoint)

def is_korean_letter(korean_letter):
    codepoint = korean_letter_to_codepoint(korean_letter)
    if codepoint is None:
        return False
    else:
        return True

jaum_list = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ',
    'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
    'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ',
    'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

moum_list = [
    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ',
    'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
    'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ',
    'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ',
    'ㅣ'
]

patchim_list = [
    '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ',
    'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ',
    'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ',
    'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ',
    'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ',
    'ㅌ', 'ㅍ', 'ㅎ'
]

if __name__ == '__main__':
    while True:
        string = input('문자를 입력하시오: ')
        output = ''
        for char in string:
            if is_korean_letter(char):
                jaum, moum, patchim = decompose_korean_letter(char)
                output += jaum_list[jaum] + moum_list[moum] + patchim_list[patchim]
            else:
                output += char
        print(output)