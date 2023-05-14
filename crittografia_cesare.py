import string

letter_low = []
letter_up = []
numbers = []

def set():
    for x in range(len(string.ascii_lowercase) or len(string.ascii_uppercase)):
        letter_low.append(string.ascii_lowercase[x])
        letter_up.append(string.ascii_uppercase[x])
    for x in range(0, 10):
        numbers.append(str(x))
set()

jump = 2
var = str(input('inserisci una parola d\'ordine: '))
length = len(var)
cont = 0
cod = str()

def loc(letter):
    done = False
    i = 0
    if letter >= 'a' and letter <= 'z':
        while not done:
            if letter == letter_low[i]:
                done = True
                return i
            else:
                i+=1
    elif letter >= 'A' and letter <= 'Z':
        while not done:
            if letter == letter_up[i]:
                done = True
                return i
            else:
                i+=1
    elif letter >= '0' and letter <= '9':
        return letter

while cont < length:
    if var[cont] >= 'a' and var[cont] <= 'z':
        tmp = loc(var[cont])
        if tmp+jump == len(letter_low) - 1 or tmp == len(letter_low)  - 1:
            cod += letter_low[(tmp+jump - len(letter_low) - 1) + jump - 1]
        elif tmp+jump > len(letter_low) - 1:
            cod += letter_low[(tmp+jump - len(letter_low))]
        else:
            cod += letter_low[tmp+jump]
    elif var[cont] >= 'A' and var[cont] <= 'Z':
        tmp = loc(var[cont])
        if tmp+jump == len(letter_up) - 1 or tmp == len(letter_up)  - 1:
            cod += letter_up[(tmp+jump - len(letter_up) - 1) + jump - 1]
        elif tmp+jump > len(letter_up) - 1:
            cod += letter_up[(tmp+jump - len(letter_up))]
        else:
            cod += letter_up[tmp+jump]
    elif var[cont] >= '0' and var[cont] <= '9':
        tmp = loc(var[cont])
        if int(tmp)+jump == len(numbers) - 1 or int(tmp) == len(numbers)  - 1:
            cod += numbers[(int(tmp)+jump - len(numbers) - 1) + jump - 1]
        elif int(tmp)+jump > len(numbers) - 1:
            cod += numbers[(int(tmp)+jump - len(numbers))]
        else:
            cod += numbers[int(tmp)+jump]
    cont+=1

print('parola decifrata: ' + var)
print('parola cifrata: ' + cod)