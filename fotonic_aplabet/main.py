alphabet = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "inda", "julet", "kilo", "lima", "mike", "novmber", "oscar", "papa", "qubeck", "romeo", "serria", "tango", "uniform", "victor", "wiskey", "xray", "yankie", "zulu"]


def convert_char(char):
    try:
        char = char.lower()
        index = ord(char) - 97
        return alphabet[index]

    except:
        pass
        # print("only use letters")
    # return alphabet[ord(char.lower() - 97)]


# print(convert_char("j"))

def convert_string(str):

    for c in str:
        result = convert_char(c)
        if result:
            print(convert_char(c))


# convert_string("Jordan")
# convert_string("RoB")
# convert_string("abcdefghijklmnopqrstuvwxyz")

convert_string("Jor1dan")
