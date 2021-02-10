import multiprocessing
import time

# def adding(balance, amount, lock):
#     for i in range(10000):
#         lock.acquire()
#         balance.value = balance.value + amount.value
#         lock.release()
#
# def takeing(balance, amount, lock):
#     for i in range(10000):
#         lock.acquire()
#         balance.value = balance.value - amount.value
#         lock.release()
#
# if __name__ == '__main__':
#     balance = multiprocessing.Value('i', 10000)
#     amount = multiprocessing.Value('i', 1)
#     lock = multiprocessing.Lock()
#     p1 = multiprocessing.Process(target= adding, args= (balance, amount, lock))
#     p2 = multiprocessing.Process(target= takeing, args= (balance, amount, lock))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print('this is balance:', balance.value)

def plus(i):
    return i * 3 + 5 // 2

# if __name__ == '__main__':
#     collection = range(1000000)
#     pool = multiprocessing.Pool()
#     start_time = time.time()
#     result = pool.map(plus, collection)
#     end_time = time.time()
#     duration = end_time - start_time
#     print(duration, 'duration***************')
#     # print(result, 'result********************')

collection = range(1000000)
start_time = time.time()
result = list(map(plus, collection))
end_time = time.time()
duration = end_time - start_time
print(duration, 'duration***************')
# print(result, 'result********************')

# 30 tesakan, harcere inche importe, inche mutabilitin , range incha, exseptione, multiprocessinge incha, process vore, rice procesornere,
# tesakani mej 8 harca,
# 30 xndirner poqr ,  stexcel coll, tpel iranc arajin tarere , ev ayln
# 40 classeri het kapvac, usanox class, atributnerov, gorcoxutyunner uni , 2 class lini usanox ev hamalsaranan , 2 hat xndir el processneri pahov
# pool ov shared memori
# help u dirr- ov petqa ogtvenq


# haytararel student claass ir atributnerov, (anun, tariq, mog) mi sharq gorcoxutyunnerov poxel anune,
# tariqe avelacnel 1 ov, mogi gnahatakane popoxel
# haytararel magistrant class-y ir atrivutnerov (anun, tariq, mog, tezi anvanum, ararkanneri anuner irenc jamaqanakov)
# mi sharq gorcoxutyunnerov, argumentrneri het, poxel anune, avelacnel tariqe 1 tarov, mogi gnhatakane poxel,
# pntrel ararkaneri mej konkret ararka, hashvel amenashhat jamaqanak unecox ararkan, tpel ayn ararkan vore sksvum e konkret taric,
# stexcel studentner ev magistrosner, katarel gorcoxutyunner, gtnel ayn ararkaneree voronq kan

class Student:
    def __init__(self, name, old, mog):
        self.name = name
        self.old = old
        self.mog = mog

    def change_name(self, new_name):
        self.name = new_name
        return self.name

    def increase_old(self):
        self.old += 1
        return self.old

    def change_mog(self, new_rating):
        self.mog = new_rating
        return self.mog

class Master(Student):
    def __init__(self, name, old, mog, name_essay, subjects_duration):
        Student.__init__(self, name, old, mog)
        self.name_essay = name_essay
        self.subjects_duration = subjects_duration

    def search_subject(self, subject):
        print(subject) if subject in self.subjects_duration.keys() else print('this subject doesn\'t exist')
        # filter-ov kareli e nayev
        # for sub in self.subjects_duration.keys():
        #     if subject == sub:
        #         print(subject)
        #         break:
        # else:
        #     print('this subject doesn\'t exist')

    def get_longest_sub(self):
        max = 0
        longest_sub = ''
        for subject in self.subjects_duration.keys():
            if self.subjects_duration[subject] > max:
                max = self.subjects_duration[subject]
                longest_sub = subject
        return (longest_sub, max)

    def search_first_smb(self, simbol):
        found = 0
        for subject in self.subjects_duration.keys():
            if subject[0].lower() == simbol.lower():
                print(subject, 'this subject starts from inputet char')
                found +=1
        if found == 0:
            print('there is no finded subject in you inputed char')


tatev = Master('Tatev', 24, 3, 'OOP in programming', {'Python': 26, 'Security': 24, 'Data mining': 30})
print(tatev.get_longest_sub())
tatev.search_subject('Security')
tatev.search_first_smb(input('input a one char:'))