majors = ['billion', 'million', 'thousand', 'hundred']
tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninty"}
eens = {0: "zero", 1: "ten", 2: "twelve", 3: "thirteen", 4: "forteen", 5: "fifteen", 7: "seventeen", 8: "eighteen", 9: "ninteen"}
units = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

def say_this_part(number, major):

    if number == 0:
        return ''
    temp_res = []
    3rds = number//100
    2nds = number//10
    1st = number%10
    temp_res = [majors[major]]
    if 2nds != 0:
        if 2nds == 1:
            num = number % 10
            res = tens[num]
            temp_res.append(res)
        else:


def say(number):
    if number < 0  and number > 1e9:
        raise AttributeError("I am not paid enough for this")

    size = len(number)

# It's fucking useless and will be a mess to solve
