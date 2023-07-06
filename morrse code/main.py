alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", " n", "o", "p", "q", "r", " s", "t", "u", "v", "w", "x", "z"]

morsse_code =["·−", "−···", "−·−·", "−··", "·", "··−·", "−−·", "····", "··", "·−−−", "−·−", "·−··", "−−", "−·", "−−−", "·−−·", "−−·−", "·−·", "···", "−", "··−", "···−", "·−−", "−··−", "−·−−", "−−··" ]


def convert_string(str):
    result = []

    for char in str:
        #result.append(ascii(char) - 97)

        i  = ord(char) - 97
        result.append(morsse_code[i])

    return result



print(convert_string("jordan"))
