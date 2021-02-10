import random
import itertools

#
# ########################################################################3 first part
# def guessRandomly():
#     predicted_number = random.choice([0, 1])
#     return predicted_number
#
# correct = 0
# wrong = 0
# while True:
#     user_number = int(input("input 0 or 1 \n"))
#     if user_number != 1 and user_number != 0:
#         continue
#     protected_number = guessRandomly()
#     print('users number: ', user_number),
#     print('protected number: ', protected_number)
#
#     if user_number == protected_number:
#         correct += 1
#         print("machine predicted correctly")
#     else:
#         wrong += 1
#         print("machine predicted wrong")
#     print("wrong is =", wrong, "\ncorrect is = ", correct, '\n')

combinations = [combination for combination in itertools.product([0, 1], repeat=3)]

history = dict.fromkeys(combinations, 0)

prev_num = 0
print(history)

def guessRandomly():
    predicted_number = random.choice([0, 1])
    return predicted_number


def guessShennon(prev_1, prev_2, attempt, user_number):
    predicted_num = 0

    if attempt < 4:
        protected_number = guessRandomly()
    else:
        if history[(prev_1, prev_2, 0)] > history[(prev_1, prev_2, 1)]:
            predicted_num = 0
        else:
            predicted_num = 1

    """Save histroy"""
    history[(prev_1, prev_2, user_number)] += 1
    # print(prev_num)
    return predicted_num
    # prev_num = user_number


#
correct = 0
wrong = 0
prev1 = 0
prev2 = 0
attempt = 0


while True:
    user_number = int(input("input 0 or 1 \n"))
    if user_number != 1 and user_number != 0:
        continue
    protected_number = guessShennon(prev1, prev2, user_number, attempt)
    print('users number: ', user_number),
    print('protected number: ', protected_number)
    print(history)

    if user_number == protected_number:
        correct += 1
        print("machine predicted correctly")
    else:
        wrong += 1
        print("machine predicted wrong")
        prev1 = prev2
        prev2 = user_number
    print("wrong is =", wrong, "\n correct is = ", correct, '\n')

# shennoni algorithm
# chingachung sarqel 1 2 3 ,


