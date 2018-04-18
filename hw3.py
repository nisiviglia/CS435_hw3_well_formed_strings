from stack import Stack

def wellFormed(input_data):

    s = Stack()
    leftside = ['(', '{', '[', '<']
    rightside = [')', '}', ']', '>']

    for ch in input_data.replace(" ", ""):
        if ch in leftside:
            s.push(ch)

        else:
            if s.empty() == True or ch not in rightside:
                return False

            pop_char = s.pop()

            if leftside.index(pop_char) != rightside.index(ch):
                return False

    return s.empty()

#Main program below here
input_data = input("Enter data: ")

print(wellFormed(input_data))
