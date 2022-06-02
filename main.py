from abc import ABC

class Abstrct(ABC):
    address = ''

    def __init__(self, address):
        self.address = address

    def calculateFreqs(self):
        pass

class ListCount(Abstrct):


    def calculateFreqs(self):
        f = open(self.address)
        text = f.read()
        textList = text.replace('\n', ' ').split(" ")
        print(textList)
        list = []

        for i in textList:

            if i not in list:

                list.append(i)

        for i in range(0, len(list)):

            print('Frequency of', list[i], 'is :', text.count(list[i]))


class DissCount(Abstrct):
    def __init__(self, address):
        Abstrct.__init__(self, address)

        def calculateFreqs(self):
            freqs = open(self.address, 'r').read()

            dict = {}

            lst = freqs.split()
            for word in lst:
                dict[word] = 0

            for word in lst:
                if word[-1] == '.':
                    word = word[0:len(word) - 1]

                if word in dict:
                    dict[word] += 1

                else:
                    dict.update({word: 1})

            for keys in dict:
                print("\"", keys, "\"", end=" ")
                print(dict[keys], end=" ")
                print()

obj = ListCount("C:\\Users\\yagmu\\Documents\\strange.txt")
obj.calculateFreqs()

obj2 = DissCount("C:\\Users\\yagmu\\Documents\\strange.txt")
obj2.calculateFreqs()