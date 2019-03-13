import math
# File for Trainig
allWordsT = {}  ##our lists of words we collected from the texts files.
allWordsAfterT = {}
fileUrlT = "/Users/mohammedchowdhury/Desktop/example.txt"
bigramT = {}
finalT = ""
unkWordT = []
totalBeforeUnkT = 0
totalAfterUnkT = 0

# File for brown test
allWordsBT = {}
allWordsAfterBT = {}
fileUrlBT = "/Users/mohammedchowdhury/Desktop/exampleBT.txt"
bigramBT = {}
finalBT = ""
unkWordBT = []
totalBeforeUnkBT = 0
totalAfterUnkBT = 0

# file from learner test
allWordsLT = {}
allWordsAfterLT = {}
fileUrlLT = "/Users/mohammedchowdhury/Desktop/exampleLT.txt"
bigramLT = {}
finalLT = ""
unkWordLT = []
totalBeforeUnkLT = 0
totalAfterUnkLT = 0

##processing brown training File
def AddWordsT(word):
    key = allWordsT.get(word)
    if key == None:
        allWordsT.setdefault(word, 1)
    else:
        key = allWordsT.get(word)
        key = key + 1
        allWordsT[word] = key

def FindOneWordT():  ##used once
    global totalBeforeUnkT
    for i in allWordsT.keys():
        value = allWordsT.get(i)
        totalBeforeUnkT = value + totalBeforeUnkT
        if value == 1:
            unkWordT.append(i)
    for i in range(len(unkWordT)):
        allWordsT.pop(unkWordT.__getitem__(i))
        # print(unkWordT.__getitem__(i))
    replaceOneWordT()

def replaceOneWordT():  # replace all words that shows us once with <unk> , pad all the sentenses with <s> </s> , and lowercase.
    file = open(fileUrlT, "r")
    global finalT
    for line in file:
        temp = line.split()  # splitting each words in the sentence as a array
        oneLine = "<s> "
        a = 0
        counter = len(temp)

        while a < counter:
            temp2 = (temp.__getitem__(a)).lower()
            if (unkWordT.__contains__(temp2)):
                oneLine = oneLine + " <unk>"
            else:
                oneLine = oneLine + " " + (temp2)
            if a == counter - 1:
                oneLine = oneLine + " </s>"
            a = a + 1

        # print(oneLine)## this is where i need to write each line back to a file.
        finalT = finalT + oneLine + "\n"
    file.close()
    file = file = open(fileUrlT, "w")
    file.write(finalT)
    afterPreprocessingT()

def readFromFileT():  # reading from file and adding to the hashtable.
    file = open(fileUrlT, "r")
    for word in file:  # word is each line in the file
        individualWords = word.split()
        for i in individualWords:
            AddWordsT(i.lower())
    file.close()
    FindOneWordT()

def afterPreprocessingT():
    words = finalT.split()
    for i in words:
        AddWordsAfterT(i)

def AddWordsAfterT(word):
    global totalAfterUnkT
    totalAfterUnkT = totalAfterUnkT + 1
    key = allWordsAfterT.get(word)
    if key == None:
        allWordsAfterT.setdefault(word, 1)
    else:
        key = allWordsAfterT.get(word)
        key = key + 1
        allWordsAfterT[word] = key

# processing brown testing file
def AddWordsBT(word):
    key = allWordsBT.get(word)
    if key == None:
        allWordsBT.setdefault(word, 1)
    else:
        key = allWordsBT.get(word)
        key = key + 1
        allWordsBT[word] = key

def FindOneWordBT():  ##used once
    global totalBeforeUnkBT
    for i in allWordsBT.keys():
        value = allWordsBT.get(i)
        totalBeforeUnkBT = value + totalBeforeUnkBT
        if value == 1:
            unkWordBT.append(i)
    for i in range(len(unkWordBT)):
        allWordsBT.pop(unkWordBT.__getitem__(i))
    # print(unkWordBT.__getitem__(i))
    replaceOneWordBT()

def replaceOneWordBT():  # replace all words that shows us once with <unk> , pad all the sentenses with <s> </s> , and lowercase.
    file = open(fileUrlBT, "r")
    global finalBT
    for line in file:
        temp = line.split()  # splitting each words in the sentence as a array
        oneLine = "<s> "
        a = 0
        counter = len(temp)
        while a < counter:
            temp2 = (temp.__getitem__(a)).lower()
            if (unkWordBT.__contains__(temp2)):
                oneLine = oneLine + " <unk>"
            else:
                oneLine = oneLine + " " + (temp2)
            if a == counter - 1:
                oneLine = oneLine + " </s>"
            a = a + 1

        # print(oneLine)## this is where i need to write each line back to a file.
        finalBT = finalBT + oneLine + "\n"
    file.close()
    file = file = open(fileUrlBT, "w")
    file.write(finalBT)
    afterPreprocessingBT()

def readFromFileBT():  # reading from file and adding to the hashtable.
    file = open(fileUrlBT, "r")
    for word in file:  # word is each line in the file
        individualWords = word.split()
        for i in individualWords:
            AddWordsBT(i.lower())
    file.close()
    FindOneWordBT()

def afterPreprocessingBT():
    words = finalBT.split()
    for i in words:
        AddWordsAfterBT(i)

def AddWordsAfterBT(word):
    global totalAfterUnkBT
    totalAfterUnkBT = totalAfterUnkBT + 1
    key = allWordsAfterBT.get(word)
    if key == None:
        allWordsAfterBT.setdefault(word, 1)
    else:
        key = allWordsAfterBT.get(word)
        key = key + 1
        allWordsAfterBT[word] = key

##processing Learner test
def AddWordsLT(word):
    key = allWordsLT.get(word)
    if key == None:
        allWordsLT.setdefault(word, 1)
    else:
        key = allWordsLT.get(word)
        key = key + 1
        allWordsLT[word] = key

def FindOneWordLT():  ##used once
    global totalBeforeUnkLT
    for i in allWordsLT.keys():
        value = allWordsLT.get(i)
        totalBeforeUnkLT = value + totalBeforeUnkLT
        if value == 1:
            unkWordLT.append(i)
    for i in range(len(unkWordLT)):
        allWordsLT.pop(unkWordLT.__getitem__(i))
    # print(unkWordLT.__getitem__(i))
    replaceOneWordLT()

def replaceOneWordLT():  # replace all words that shows us once with <unk> , pad all the sentenses with <s> </s> , and lowercase.
    file = open(fileUrlLT, "r")
    global finalLT
    for line in file:
        temp = line.split()  # splitting each words in the sentence as a array
        oneLine = "<s> "
        a = 0
        counter = len(temp)
        while a < counter:
            temp2 = (temp.__getitem__(a)).lower()
            if (unkWordLT.__contains__(temp2)):
                oneLine = oneLine + " <unk>"
            else:
                oneLine = oneLine + " " + (temp2)
            if a == counter - 1:
                oneLine = oneLine + " </s>"
            a = a + 1

        # print(oneLine)## this is where i need to write each line back to a file.
        finalLT = finalLT + oneLine + "\n"
    file.close()
    file = file = open(fileUrlLT, "w")
    file.write(finalLT)
    afterPreprocessingLT()

def readFromFileLT():  # reading from file and adding to the hashtable.
    file = open(fileUrlLT, "r")
    for word in file:  # word is each line in the file
        individualWords = word.split()
        for i in individualWords:
            AddWordsLT(i.lower())
    file.close()
    FindOneWordLT()

def afterPreprocessingLT():
    words = finalLT.split()
    for i in words:
        AddWordsAfterLT(i)

def AddWordsAfterLT(word):
    global totalAfterUnkLT
    totalAfterUnkLT = totalAfterUnkLT + 1
    key = allWordsAfterLT.get(word)
    if key == None:
        allWordsAfterLT.setdefault(word, 1)
    else:
        key = allWordsAfterLT.get(word)
        key = key + 1
        allWordsAfterLT[word] = key

def question1():
    print("1. How many word types (unique words) are there in the training corpus?")
    print("There are "+str(len(allWordsAfterT))+ " unique words in the corpus.")

def question2():
    print(" ")
    print("2. How many word tokens are there in the training corpus?")
    print("There are "+str(totalAfterUnkT)+" word tokens in the corpus.")

def question3():

    print(" ")
    print("3. What percentage of word tokens and word types in each of the test corpora dod not occur in the training? ")
    print(" ")

    temT = dict(allWordsT)
    tempBT = dict(allWordsBT)
    tempLT = dict(allWordsLT)

    #print(unkWordBT)
    for i in unkWordT:
        temT.setdefault(i,1)

    for i in unkWordBT:
        tempBT.setdefault(i,1)

    for i in unkWordLT:
        tempLT.setdefault(i,1)

    BrownWordToken = 0
    BrownWordType = 0;
    for i in tempBT:
        if temT.get(i)==None:
            BrownWordToken = BrownWordToken+tempBT.get(i)
            BrownWordType = BrownWordType+1
    percentage  = BrownWordType/len(tempBT)*100

    print("Percentage of Token that did not occur in Training corpora form Brown-Test is "+str((BrownWordToken/totalBeforeUnkBT*100))+"%")
    print("Percentage of Word Types that did not occur in Training from Brown-Test is "+str(percentage)+"%")
    print(" ")

    LearnWordToken = 0
    LearnWordType = 0;
    for i in tempLT:
        if temT.get(i) == None:
            LearnWordToken = LearnWordToken + tempLT.get(i)
            LearnWordType = LearnWordType + 1
    percentage = LearnWordType / len(tempLT) * 100
    print("Percentage of Token that did not occur in Training corpora form Learner-Test is " + str(
        (LearnWordToken / totalBeforeUnkLT * 100)) + "%")
    print("Percentage of Word Types that did not occur in Training from Learner-Test is " + str(percentage) + "%")
    print(" ")


##processing brown training File
def AddWordsBigram(word,dictionary):
    key = dictionary.get(word)
    if key == None:
        dictionary.setdefault(word, 1)
    else:
        key = dictionary.get(word)
        key = key + 1
        dictionary[word] = key


def bigram(finalWOrd,dictionary):
    word = finalWOrd.split()
    for i in range(len(word)):
        # if word.__getitem__(i)!="<s>" and word.__getitem__(i-1)!="<s>":
        #     temp = word.__getitem__(i-1)+","+word.__getitem__(i)
        #     AddWordsBigram(temp,dictionary)
        if word.__getitem__(i) != "<s>" and word.__getitem__(i) != "</s>" and word.__getitem__(
                i - 1) != "<s>" and word.__getitem__(i - 1) != "</s>":
            temp = word.__getitem__(i - 1) + "," + word.__getitem__(i)
            AddWordsBigram(temp, dictionary)


def question4():
    print("4. What percentage of Bigrams in each of the test corpora that did not occur in training? ")
    bigram(finalT,bigramT)
    bigram(finalBT,bigramBT)
    bigram(finalLT,bigramLT)

    BrownWordToken = 0
    BrownWordType = 0

    totalBT = 0

    for i in bigramBT:
        totalBT = totalBT+ bigramBT.get(i)   ##total words in the bigram
        if bigramT.get(i) == None:
            BrownWordToken = BrownWordToken + bigramBT.get(i)
            BrownWordType = BrownWordType + 1

    percentage = BrownWordType / len(bigramBT) * 100

    print("Percentage of Token that did not occur in Training corpora Bigram form Brown-Test is " + str(
        (BrownWordToken / totalBT * 100)) + "%")
    print("Percentage of Word Types that did not occur in Training corpora for Bigram in Brown-Test is " + str(percentage) + "%")
    print(" ")


    LearnWordToken = 0
    LearnWordType = 0
    totalLT = 0

    for i in bigramLT:
        totalLT = totalLT + bigramLT.get(i)  ##total words in the bigram
        if bigramT.get(i) == None:
            LearnWordToken = LearnWordToken + bigramLT.get(i)
            LearnWordType = LearnWordType + 1

    percentage = LearnWordType / len(bigramLT) * 100

    print("Percentage of Token that did not occur in Training corpora Bigram form Learner-Test is " + str(
        (LearnWordToken / totalLT * 100)) + "%")
    print("Percentage of Word Types that did not occur in Training corpora for Bigram in Learner-Test is " + str(
        percentage) + "%")
    print(" ")


def Unigram(sent):
    total = 1
    sent = sent.split()
    temp =0
    for i in sent:
        if allWordsAfterT.get(i)==None:
            temp = allWordsAfterT.get("<unk>")/totalAfterUnkT
            total = total*temp
        else:
            temp = (allWordsAfterT.get(i)/totalAfterUnkT)
            total = total*temp
            temp = 0
    return total


def BiGram(sent):
    total = 1
    sent = sent.split()
    temp = 0

    first = sent.__getitem__(0)

    if allWordsAfterT.get(first) == None:
        total = allWordsAfterT.get("<unk>")/totalBeforeUnkT

    else:
        total = allWordsAfterT.get(first) / totalBeforeUnkT

    for i in range(len(sent)-1):
        t1 = sent.__getitem__(i)
        t2 = sent.__getitem__(i+1)

        if allWordsAfterT.get(t1) == None:
            t1 = "<unk>"

        if allWordsAfterT.get(t2) == None:
            t2 = "<unk>"

        together = str(t1)+","+str(t2)

        if bigramT.get(together)!=None:
            num = bigramT.get(together)
            total = total * (num/totalAfterUnkT)

        if bigramT.get(together)==None:
            total  = total*0
            return 0
    return total

def addOneBigram(sent):
    total = 1
    sent = sent.split()
    temp = 0
    first = sent.__getitem__(0)

    if allWordsAfterT.get(first) == None:
        total = ((allWordsAfterT.get("<unk>")+1)/totalBeforeUnkT)
    else:
        total = (allWordsAfterT.get(first)+1)/ totalBeforeUnkT

    for i in range(len(sent)-1):
        t1 = sent.__getitem__(i)
        t2 = sent.__getitem__(i+1)

        if allWordsAfterT.get(t1) == None:
            t1 = "<unk>"

        if allWordsAfterT.get(t2) == None:
            t2 = "<unk>"
        together = str(t1)+","+str(t2)

        if bigramT.get(together)!=None:
            num = bigramT.get(together)
            total = total * ((num+1)/(totalAfterUnkT+len(bigramT)))

        if bigramT.get(together)==None:
            total = total * ((1)/(totalAfterUnkT+len(bigramT)))
    return total

def question5():
    print("5.")
    sentence1 = "He was laughed off the screen ."
    sentence2 = "There was no compulsion behind them ."
    sentence3 = "I look forward to hearing your reply ."

    temp =  allWordsAfterT.pop("<s>")
    global totalAfterUnkT
    totalAfterUnkT = totalAfterUnkT - temp

    sentence1 = sentence1.lower()
    sentence2 = sentence2.lower()
    sentence3 = sentence3.lower()

    s1Uni = Unigram(sentence1)
    s2Uni = Unigram(sentence2)
    s3Uni = Unigram(sentence3)

    if s1Uni != 0:
        s1Bi = math.log2(s1Uni)
    if s2Uni != 0:
        s1Bi = math.log2(s2Uni)
    if s3Uni != 0:
        s1Bi = math.log2(s3Uni)

    print("The log probabilities of unigram ( He was laughed off the screen .) is "+str(s1Uni))
    print("The log probabilities of unigram ( There was no compulsion behind them .) is " + str(s2Uni))
    print("The log probabilities of unigram ( I look forward to hearing your reply .) is " + str(s3Uni))
    print(" ")


    s1Bi = BiGram(sentence1)
    s2Bi = BiGram(sentence2)
    s3Bi = BiGram(sentence3)

    if s1Bi != 0:
        s1Bi = math.log2(s1Bi)
    if s2Bi != 0:
        s2Bi = math.log2(s2Bi)
    if s3Bi != 0:
        s3Bi = math.log2(s3Bi)

    print("The log probabilities of bigram ( He was laughed off the screen .) is " + str(s1Bi))
    print("The log probabilities of bigram ( There was no compulsion behind them .) is " + str(s2Bi))
    print("The log probabilities of bigram ( I look forward to hearing your reply .) is " + str(s3Bi))
    print(" ")

    s1AOne = addOneBigram(sentence1)
    s2AOne = addOneBigram(sentence2)
    s3AOne = addOneBigram(sentence3)


    if s1AOne != 0:
        s1AOne = math.log2(s1AOne)
    if s2AOne != 0:
        s2AOne = math.log2(s2AOne)
    if s3AOne != 0:
        s3AOne = math.log2(s3AOne)

    print("The log probabilities of Add-One Smoothing bigram ( He was laughed off the screen .) is " + str(s1AOne))
    print("The log probabilities of Add-One Smoothing bigram ( There was no compulsion behind them .) is " + str(s2AOne))
    print("The log probabilities of Add-One Smoothing bigram ( I look forward to hearing your reply .) is " + str(s3AOne))
    print(" ")
    print(" ")

    print("6. Compute the perplexities of each of the sentences above under each of the models")

    lenS1 = len(sentence1.split())
    lenS2 = len(sentence2.split())
    lenS3 = len(sentence3.split())

    uniS1p = (1 / lenS1) * s1Uni
    uniS2p = (1 / lenS2) * s2Uni
    uniS3p = (1 / lenS3) * s3Uni

    uniS1p = math.pow(2,-uniS1p)
    uniS2p = math.pow(2,-uniS2p)
    uniS3p = math.pow(2,-uniS3p)

    print("Under Unigram ( He was laughed off the screen .) perplexities is  "+ str(uniS1p))
    print("Under Unigram ( There was no compulsion behind them .) perplexities is  " + str(uniS2p))
    print("Under Unigram ( I look forward to hearing your reply .) perplexities is  " + str(uniS3p))
    print(" ")
    print(" ")

    biS1p = (1 / lenS1) * s1Bi
    biS2p = (1 / lenS2) * s2Bi
    biS3p = (1 / lenS3) * s3Bi

    biS1p = math.pow(2, -biS1p)
    biS2p = math.pow(2, -biS2p)
    biS3p = math.pow(2, -biS3p)

    print("Under bigram ( He was laughed off the screen .) perplexities is  " + str(biS1p))
    print("Under bigram ( There was no compulsion behind them .) perplexities is  " + str(biS2p))
    print("Under bigram ( I look forward to hearing your reply .) perplexities is  " + str(biS3p))
    print(" ")
    print(" ")

    AOS1p = (1 / lenS1) * s1AOne
    AOS2p = (1 / lenS2) * s2AOne
    AOS3p = (1 / lenS3) * s3AOne

    AOS1p = math.pow(2, -AOS1p)
    AOS2p = math.pow(2, -AOS2p)
    AOS3p = math.pow(2, -AOS3p)

    print("Under Add-One Smoothing bigram ( He was laughed off the screen .) perplexities is  " + str(AOS1p))
    print("Under Add-One Smoothing bigram ( There was no compulsion behind them .) perplexities is  " + str(AOS2p))
    print("Under Add-One Smoothing bigram ( I look forward to hearing your reply .) perplexities is  " + str(AOS3p))
    print(" ")



def question7():
    print("7. Compute the perplexities of the entire test corpora.")

    BrownTest = finalBT.split() ##chnange the link to the correct string later

    BTUni =0
    BTBi = 0
    BTAOBi = 0

    sent = ""
    for i in BrownTest:
        if i!="<s>" and i!="</s>":
            sent =sent+" "+i

        if(i=="</s>"):

            BTUni = BTUni+Unigram(sent)
            BTBi = BTBi+BiGram(sent)
            BTAOBi = BTAOBi + addOneBigram(sent)

            sent = ""

    BTUni = (1/totalAfterUnkBT)*BTUni
    BTUni = math.pow(2,-BTUni)

    BTBi = (1 / totalAfterUnkBT) * BTBi
    BTBi = math.pow(2, -BTBi)

    BTAOBi = (1 / totalAfterUnkBT) * BTAOBi
    BTAOBi = math.pow(2, -BTAOBi)


    print("The perplexities of the Entire Test Copra for Brown Test for Unigram is "+str(BTUni))
    print("The perplexities of the Entire Test Copra for Brown Test for Bigram is "+str(BTBi))
    print("The perplexities of the Entire Test Copra for Brown Test for Add-One Smoothing Bigram is "+str(BTAOBi))
    print(" ")
    print(" ")

    LearnTest = finalLT.split()  ##chnange the link to the correct string later

    LTUni = 0
    LTBi = 0
    LTAOBi = 0

    sent = ""
    for i in LearnTest:
        if i != "<s>" and i != "</s>":
            sent = sent + " " + i

        if (i == "</s>"):
            LTUni = LTUni + Unigram(sent)
            LTBi = LTBi + BiGram(sent)
            LTAOBi = LTAOBi + addOneBigram(sent)

            sent = ""

    LTUni = (1 / totalAfterUnkLT) * LTUni
    LTUni = math.pow(2, -LTUni)

    LTBi = (1 / totalAfterUnkLT) * LTBi
    LTBi = math.pow(2, -LTBi)

    LTAOBi = (1 / totalAfterUnkLT) * LTAOBi
    LTAOBi = math.pow(2, -LTAOBi)

    print("The perplexities of the Entire Test Copra for Learner Test for Unigram is " + str(LTUni))
    print("The perplexities of the Entire Test Copra for Learner Test for Bigram is " + str(LTBi))
    print("The perplexities of the Entire Test Copra for Learner Test for Add-One Smoothing Bigram is " + str(LTAOBi))



def main():
    readFromFileT()
    readFromFileBT()
    readFromFileLT()



    question1()
    question2()
    question3()
    question4()
    question5() ##Question 6 is includes in the same method
    question7()







main()


