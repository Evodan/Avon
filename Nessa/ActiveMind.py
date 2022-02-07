import csv

from Nessa import mind_console

Fragments = []
Frag_Anylzed = []
Cue_words = ["You"]
counter = 0


def AddToAMem(self, data):
    Fragments.append(data)
    Frag_Anylzed.append(False)
    self.counter = +1


def AutoMemory():
    """ Stacks up immediate memory """
    load = ""
    for thought in Fragments:
        load = load + thought + "\n"
    return load


def Comprhend(self):
    thought_idx = 0
    for thought in Fragments:
        print('Processed: {0}'.format(str(thought_idx) + ' ' + thought))
        thought_idx = thought_idx + 1

       # if self.Frag_Anylzed[thought_idx] == 'NotScanned':
      #      KeywordCheck(thought, thought_idx)

        """ Send the message somewhere to start chain """


""" HAS THE INDEX ALREADY PASSED"""


def KeywordCheck(data, idx):  # TODO Eventually create keywords on it's own

    # index of delimiter
    delm_Spot = data.index(':')

    # Read everything before that point
    Keyword = data[0:delm_Spot]
    Phrase = [delm_Spot + 1, len(data)-1]
    # See if it's a keyword
    for words in Cue_words:
        if words == Keyword:
            mind_console.Check_Keywods(Keyword, Phrase, idx)
            Frag_Anylzed[idx] = 'Processing'


def wordAssoiation(idx):
    words = mind_console.Check_Keywods()

    for word in words:
        #Check Positive Words
        #Check Negetive Words
        #Check Subject
        #Check Modifier
        #Check Target
        filename = 'positive_words.as'

        with open(filename, 'r') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                print(row)

