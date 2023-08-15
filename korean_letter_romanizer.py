
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

VOWEL_ALPHABET_LIST={
    'ㅏ':'a',
    'ㅓ':'ŏ',
    'ㅗ':'o',
    'ㅜ':'u',
    'ㅡ':'ŭ',
    'ㅣ':'i',
    'ㅐ':'ae',
    'ㅔ':'e',
    'ㅚ':'oi',
    'ㅟ':'wi',

    'ㅑ':'ya',
    'ㅕ':'yŏ',
    'ㅛ':'yo',
    'ㅠ':'yu',
    'ㅒ':'yae',
    'ㅖ':'ye',
    'ㅘ':'wa',
    'ㅝ':'wŏ',
    'ㅙ':'wae',
    'ㅞ':'we',
    'ㅢ':'ŭi',
}
CONSONANT_ALPHABET_LIST={
    '':[''],
    'ㄱ':['k'], 'ㅋ':['kh'], 'ㄲ':['kk'],
    'ㄷ':['t'], 'ㅌ':['th'], 'ㄸ':['tt'],
    'ㅂ':['p'], 'ㅍ':['ph'], 'ㅃ':['pp'],

    'ㅈ':['j'], 'ㅊ':['ch'], 'ㅉ':['jj'],
    'ㅅ':['s'], 'ㅆ':['ss'], 'ㅎ':['h'],
    'ㅁ':['m'], 'ㄴ':['n'], 'ㅇ':['','ng'], 'ㄹ':['r','l'], #l
}






def romanize(string, sign:bool=True, is_oe:bool=False, hyphen:bool=False):
    vowel_alphabet=VOWEL_ALPHABET_LIST.copy()
    consonant_alphabet=CONSONANT_ALPHABET_LIST.copy()
    if not sign:
        for key in vowel_alphabet:
            vowel_alphabet[key] = vowel_alphabet[key].replace('ŏ', 'o')
            vowel_alphabet[key] = vowel_alphabet[key].replace('ŭ', 'u')
    if is_oe:
        vowel_alphabet['ㅚ'] = 'oe'
    output_list = []
    output_list.append([None, None, None, None])
    for char in string:
        if is_korean_letter(char):
            jaum, moum, patchim = decompose_korean_letter(char)
            output_list.append([
                jaum_list[jaum],
                moum_list[moum],
                patchim_list[patchim],
                None
            ])
        else:
            output_list.append([None, None, None, char])
    output_list.append([None, None, None, None])

    #for char_list in output_list:
    #    print(char_list)

    for i in range(1, len(output_list)-1):
        #련음화
        if output_list[i][2] == 'ㄹ' and output_list[i+1][0] == 'ㄴ':
            output_list[i][2] = 'ㄹ'
            output_list[i+1][0] = 'ㄴ'
        if output_list[i][2] == 'ㄴ' and output_list[i+1][0] == 'ㄹ':
            output_list[i][2] = 'ㄹ'
            output_list[i+1][0] = 'ㄴ'

        #받침이 다음 글자 초성으로
        if output_list[i+1][0] == 'ㅇ':
            if output_list[i][2] == 'ㄱ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㄱ'
            if output_list[i][2] == 'ㄴ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㄴ'
            if output_list[i][2] == 'ㄷ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㄷ'
            if output_list[i][2] == 'ㄹ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㄹ'
            if output_list[i][2] == 'ㅁ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅁ'
            if output_list[i][2] == 'ㅂ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅂ'
            if output_list[i][2] == 'ㅅ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅅ'
            if output_list[i][2] == 'ㅈ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅈ'
            if output_list[i][2] == 'ㅊ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅊ'
            if output_list[i][2] == 'ㅋ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅋ'
            if output_list[i][2] == 'ㅌ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅌ'
            if output_list[i][2] == 'ㅍ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅍ'
            if output_list[i][2] == 'ㄲ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㄲ'
            if output_list[i][2] == 'ㅆ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅆ'

            if output_list[i][2] == 'ㄳ':
                output_list[i][2] = 'ㄱ'
                output_list[i+1][0] = 'ㅅ'
            elif output_list[i][2] == 'ㄵ':
                output_list[i][2] = 'ㄴ'
                output_list[i+1][0] = 'ㅈ'
            elif output_list[i][2] == 'ㄶ':
                output_list[i][2] = 'ㄴ'
                output_list[i+1][0] = 'ㅎ'
            elif output_list[i][2] == 'ㄺ':
                output_list[i][2] = 'ㄹ'
                output_list[i+1][0] = 'ㄱ'
            elif output_list[i][2] == 'ㄻ':
                output_list[i][2] = 'ㄹ'
                output_list[i+1][0] = 'ㅁ'
            elif output_list[i][2] == 'ㄼ':
                output_list[i][2] = 'ㄹ'
                output_list[i+1][0] = 'ㅂ'
            elif output_list[i][2] == 'ㄽ':
                output_list[i][2] = 'ㄹ'
                output_list[i+1][0] = 'ㅅ'
            elif output_list[i][2] == 'ㄾ':
                output_list[i][2] = 'ㄹ'
                output_list[i+1][0] = 'ㅌ'
            elif output_list[i][2] == 'ㄿ':
                output_list[i][2] = 'ㄹ'
                output_list[i+1][0] = 'ㅍ'
            elif output_list[i][2] == 'ㅀ':
                output_list[i][2] = 'ㄹ'
                output_list[i+1][0] = 'ㅎ'
            elif output_list[i][2] == 'ㅄ':
                output_list[i][2] = 'ㅂ'
                output_list[i+1][0] = 'ㅅ'
            elif output_list[i][2] == 'ㅎ':
                output_list[i][2] = ''
        
        #받침이 다음 글자 초성으로 (ㅎ)
        if output_list[i+1][0] == 'ㅎ':
            if output_list[i][2] == 'ㄱ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅋ'
            if output_list[i][2] == 'ㄷ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅌ'
            if output_list[i][2] == 'ㅂ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅍ'
            if output_list[i][2] == 'ㅅ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅌ'
            if output_list[i][2] == 'ㅈ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅊ'
            if output_list[i][2] == 'ㅊ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅊ'
            if output_list[i][2] == 'ㅋ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅋ'
            if output_list[i][2] == 'ㅌ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅌ'
            if output_list[i][2] == 'ㅍ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅍ'
            if output_list[i][2] == 'ㄲ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅋ'
            if output_list[i][2] == 'ㅆ':
                output_list[i][2] = ''
                output_list[i+1][0] = 'ㅌ'

            if output_list[i][2] == 'ㄳ':
                output_list[i][2] = 'ㄱ'
                output_list[i+1][0] = 'ㅅ'
            elif output_list[i][2] == 'ㄵ':
                output_list[i][2] = 'ㄴ'
                output_list[i+1][0] = 'ㅊ'
            elif output_list[i][2] == 'ㄶ':
                output_list[i][2] = 'ㄴ'
                output_list[i+1][0] = 'ㅎ'
            elif output_list[i][2] == 'ㄺ':
                output_list[i][2] = 'ㄹ'
                output_list[i+1][0] = 'ㅋ'
            elif output_list[i][2] == 'ㄻ':
                output_list[i][2] = 'ㄹ'
                output_list[i+1][0] = 'ㅁ'
            elif output_list[i][2] == 'ㄼ':
                output_list[i][2] = 'ㄹ'
                output_list[i+1][0] = 'ㅍ'
            elif output_list[i][2] == 'ㄽ':
                output_list[i][2] = 'ㄹ'
                output_list[i+1][0] = 'ㅅ'
            elif output_list[i][2] == 'ㄾ':
                output_list[i][2] = 'ㄹ'
                output_list[i+1][0] = 'ㅌ'
            elif output_list[i][2] == 'ㄿ':
                output_list[i][2] = 'ㄹ'
                output_list[i+1][0] = 'ㅍ'
            elif output_list[i][2] == 'ㅀ':
                output_list[i][2] = 'ㄹ'
                output_list[i+1][0] = 'ㅎ'
            elif output_list[i][2] == 'ㅄ':
                output_list[i][2] = 'ㅂ'
                output_list[i+1][0] = 'ㅅ'
            elif output_list[i][2] == 'ㅎ':
                output_list[i][2] = ''
        

        #비음화
        if (output_list[i+1][0] == 'ㄴ'
            or output_list[i+1][0] == 'ㄹ'
            or output_list[i+1][0] == 'ㅁ'
            ):
            if (output_list[i][2] == 'ㄱ'
                or output_list[i][2] == 'ㅋ'
                or output_list[i][2] == 'ㄲ'
                ):
                output_list[i][2] = 'ㅇ'
            if (output_list[i][2] == 'ㅂ'
                or output_list[i][2] == 'ㅍ'
                ):
                output_list[i][2] = 'ㅁ'
            if (output_list[i][2] == 'ㄷ'
                or output_list[i][2] == 'ㅌ'
                or output_list[i][2] == 'ㅈ'
                or output_list[i][2] == 'ㅊ'
                or output_list[i][2] == 'ㅅ'
                or output_list[i][2] == 'ㅆ'
                ):
                output_list[i][2] = 'ㄴ'

    
    #for i in range(1, len(output_list)-1):
    #    print(output_list[i])

    for i in range(1, len(output_list)-1):
        kyogumhwa = False
        if output_list[i-1][2] == 'ㄶ':
            output_list[i-1][2] = 'ㄴ'
            kyogumhwa = True
        if output_list[i-1][2] == 'ㅀ':
            output_list[i-1][2] = 'ㄹ'
            kyogumhwa = True
        if output_list[i-1][2] == 'ㅎ':
            output_list[i-1][2] = ''
            kyogumhwa = True
        if kyogumhwa == True:
            if output_list[i][0] == 'ㄱ':
                output_list[i][0] = 'ㅋ'
            if output_list[i][0] == 'ㄷ':
                output_list[i][0] = 'ㅌ'
            if output_list[i][0] == 'ㅂ':
                output_list[i][0] = 'ㅍ'
            if output_list[i][0] == 'ㅈ':
                output_list[i][0] = 'ㅊ'


    for i in range(1, len(output_list)-1):
        ##2받침 처리
        if output_list[i][2] == 'ㄳ':
            output_list[i][2] = 'ㄱ'
        if output_list[i][2] == 'ㄵ':
            output_list[i][2] = 'ㄴ'
        if output_list[i][2] == 'ㄶ':
            output_list[i][2] = 'ㄴ'
        if output_list[i][2] == 'ㄺ':
            output_list[i][2] = 'ㄱ'
        if output_list[i][2] == 'ㄻ':
            output_list[i][2] = 'ㅁ'
        if output_list[i][2] == 'ㄼ':
            output_list[i][2] = 'ㄹ'
        if output_list[i][2] == 'ㄽ':
            output_list[i][2] = 'ㄹ'
        if output_list[i][2] == 'ㄾ':
            output_list[i][2] = 'ㄹ'
        if output_list[i][2] == 'ㄿ':
            output_list[i][2] = 'ㅍ'
        if output_list[i][2] == 'ㅀ':
            output_list[i][2] = 'ㄹ'
        if output_list[i][2] == 'ㅄ':
            output_list[i][2] = 'ㅂ'
        if output_list[i][2] == 'ㅋ':
            output_list[i][2] = 'ㄱ'
        if output_list[i][2] == 'ㅈ':
            output_list[i][2] = 'ㄷ'
        if output_list[i][2] == 'ㅊ':
            output_list[i][2] = 'ㄷ'
        if output_list[i][2] == 'ㅋ':
            output_list[i][2] = 'ㄱ'
        if output_list[i][2] == 'ㅌ':
            output_list[i][2] = 'ㄷ'
        if output_list[i][2] == 'ㅍ':
            output_list[i][2] = 'ㅂ'
        if output_list[i][2] == 'ㄲ':
            output_list[i][2] = 'ㄱ'
        if output_list[i][2] == 'ㅆ':
            output_list[i][2] = 'ㅅ'




    output_string = ''
    for i in range(1, len(output_list)-1):
        if output_list[i][0] == None:
            if output_list[i][3] in '\'\"':
                continue
            output_string += output_list[i][3]
            continue
        consonant = consonant_alphabet[output_list[i][0]][0]
        if output_list[i-1][2] in ['ㅇ', 'ㄴ', 'ㄹ', 'ㅁ', '']:
            if consonant == 'k':
                consonant = 'g'
            elif consonant == 't':
                consonant = 'd'
            elif consonant == 'p':
                consonant = 'b'
        if output_list[i-1][2] == 'ㄹ':
            if consonant == 'n':
                consonant = 'l'

        output_string += consonant
        output_string += vowel_alphabet[output_list[i][1]]

        patchim = consonant_alphabet[output_list[i][2]][-1]
        if (output_list[i][2] == 'ㅅ'
        or output_list[i][2] == 'ㅆ'):
            patchim = 't'
            if output_list[i+1][0] == 'ㅅ':
                patchim = 's'

        if output_list[i][2] == 'ㅇ':
            patchim = 'ng'
            if output_list[i+1][0] == 'ㅇ':
                if hyphen:
                    patchim = 'ng-'

        output_string += patchim
        if output_list[i][3] != None:
            output_string += output_list[i][3]

    return output_string

if __name__ == '__main__':
    while True:
        string = input('입력: ')
        print(romanize(string, is_oe=True))