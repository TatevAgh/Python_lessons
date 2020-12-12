#zugaher cragravorum , multiprocessing, multitrading
#process - task manager ) sepaakan cpu memory amen inche sepakanna
#tred-

import multiprocessing


# def act(text):
#     while True:
#         print(text)
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=act, args=('hello',))
#     p2 = multiprocessing.Process(target=act, args=('barev',))
#     p1.start()
#     p2.start()

#
# def even_numbers(numbers):
#     print('even numbers: ', list(filter(lambda num: num % 2 == 0, numbers)))
#
# def mult_3(numbers):
#     print('multipied by 3: ',list(map(lambda num: num * 3, numbers)))
#
#
# if __name__ == '__main__':
#     numbers = [6, 8, 4, 2, 12, 45]
#     p1 = multiprocessing.Process(target=even_numbers, args=(numbers,))
#     p2 = multiprocessing.Process(target=mult_3, args=(numbers,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print('Processes are finished *******')

# def act(numbers):
#     numbers[0] = 55
#     print(list(numbers))
#
# if __name__ == '__main__':
#     numbers = multiprocessing.Array('i', [2, 7, 4, 8])
#     print(list(numbers))
#     p1 = multiprocessing.Process(target=act, args=(numbers,))
#     p1.start()
#     p1.join()
#     print(list(numbers))

def put_numbers(queue):
    for i in range(10):
        queue.put(i)

def print_numbers(queue):
    while not(queue.empty()):
        print(queue.get())

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=put_numbers, args=(queue,))
    p2 = multiprocessing.Process(target=print_numbers, args=(queue,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

