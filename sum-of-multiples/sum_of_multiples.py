

def sum_of_multiples(number, factors):
    their_sum = 0
    for i in range(number):
        for fack in factors:
            if fack is not 0 and i % fack is 0:
                their_sum += i
                break
    return their_sum
