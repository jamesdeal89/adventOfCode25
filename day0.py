# dial goes from 0-99
# input is the rotations direction and amount
# whenever it points to 0, += 1 to password
# return password

def getPassword():
    password = 0
    start = 50
    with open('input', 'r') as f:
        for line in f:
            # format is [L,R][1-99]
            direction, amount = line[0], int(line[1:])
            print(direction)
            print(amount)
            amount = amount % 100
            if direction == 'R':
                start = (start + amount) % 100
            else:
                start = (start - amount) % 100
            if start == 0:
                password += 1
            print("-----")
    print(password)

# This time, it counts every time it goes *past* or *to* zero, not just end on it.
def getPassword2():
    password = 0
    start = 50
    with open('input', 'r') as f:
        for line in f:
            # format is [L,R][1-99]
            direction, amount = line[0], int(line[1:])
            print(direction)
            print(amount)
            if direction == 'R':
                password += (start + amount) // 100
                start = (start + amount) % 100
            else:
                password += (amount - start + 99) // 100
                start = (start - amount) % 100
            print(start)
            print("-----")
    print(password)

getPassword2()
