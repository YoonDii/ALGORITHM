def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    code_list = letter.split()
    # print(code_list)['....', '.', '.-..', '.-..', '---']
    
    decode_list = [morse[code] for code in code_list]
    # print(decode_list)['h', 'e', 'l', 'l', 'o']
    
    answer = "".join(decode_list)

    return answer