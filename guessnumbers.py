import random

class Solution:
    def guessnumbers(self):
        numbers = [x for x in range(10)]
        target = random.sample(numbers, 4)
        flag = True

        while flag:
            acount = 0
            bcount = 0
            inputnumber = input("Input your 4 numbers:")
            listinputnumber = list(inputnumber)
            for x in range(len(listinputnumber)):
                listinputnumber[x] = int(listinputnumber[x])
            # print(listinputnumber)
            for x in range(4):
                if listinputnumber[x] == target[x]:
                    acount += 1
            for x in listinputnumber:
                if x in target:
                    bcount += 1
            bcount -= acount
            if acount == 4:
                flag = False
            print(acount,"A",bcount,"B")


test=Solution()
test.guessnumbers()
