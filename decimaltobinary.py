toc = input('Convert to binary: ')
toc_int = int(toc)
hoch = -1

def change_string_character(index, new, string):
    tmp_list = list(string)
    tmp_list[index] = new
    new_str = "".join(tmp_list)
    return new_str

while True:
    hoch += 1
    if toc_int == 2**hoch:
        print('In binary', toc, 'is' ,  '1' + hoch*'0')
        break
    elif toc_int > 2**hoch and toc_int < 2**(hoch+1):
        remaining = toc_int - 2**hoch
        in_bin = '1' + hoch*'0'
        hoch_no_2 = hoch
        str_index = 0
        while True:
            hoch_no_2 -= 1
            str_index += 1
            if remaining == 0:
                break
            elif remaining >= 2**hoch_no_2:
                remaining = remaining - 2**hoch_no_2
                in_bin = change_string_character(str_index, '1', in_bin)
        print(in_bin)
        break