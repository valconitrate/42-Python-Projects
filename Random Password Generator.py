import random as rd

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

length = int(input('how many characters do you want? '))
let = int(input('how many letters do you want? '))
num = int(input('how many numbers do you want? '))
sym = int(input('how many symbols do you want? '))

randomizer = [letters, numbers, symbols]
newPassword = []
for i in range(0, length):
    if (let != 0 and num != 0 and sym !=0) or len(newPassword) != length:
        if let == 0:
            randomizer.remove(letters)
            let -=1
        if num == 0:
            randomizer.remove(numbers)
            num -=1
        if sym == 0:
            randomizer.remove(symbols)
            sym -=1

        val = rd.choice(rd.choice(randomizer))

        if val in letters:
            let -= 1
        elif val in numbers:
            num -= 1
        elif val in symbols:
            sym -= 1
        else:
            print('exception?')
        newPassword.append(val)

print(''.join(newPassword))