import random 

def rando_seq(alphabet, length):
    i = 0
    new_seq = []
    while i <= length:
        digit = random.randint(a = 0, b = (len(alphabet) - 1))
        #helps in getting a random integer 
        new_seq.append(alphabet[digit])
        #index the list, obtain the letter indicated by the random digit
        final_seq = ''.join(new_seq)
        #go from the list to a string, no spaces between characters
        i = i + 1
    return(final_seq)
