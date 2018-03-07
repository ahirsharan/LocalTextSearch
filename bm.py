import os
# Boyer Moore String Search implementation in Python
# Ameer Ayoub <ameer.ayoub@gmail.com>

# Generate the Bad Character Skip List
def generateBadCharShift(term):
    skipList = {}
    for i in range(0, len(term)-1):
        skipList[term[i]] = len(term)-i-1
    return skipList

# Generate the Good Suffix Skip List
def findSuffixPosition(badchar, suffix, full_term):
    for offset in range(1, len(full_term)+1)[::-1]:
        flag = True
        for suffix_index in range(0, len(suffix)):
            term_index = offset-len(suffix)-1+suffix_index
            if term_index < 0 or suffix[suffix_index] == full_term[term_index]:
                pass
            else:
                flag = False
        term_index = offset-len(suffix)-1
        if flag and (term_index <= 0 or full_term[term_index-1] != badchar):
            return len(full_term)-offset+1

def generateSuffixShift(key):
    skipList = {}
    buffer = ""
    for i in range(0, len(key)):
        skipList[len(buffer)] = findSuffixPosition(key[len(key)-1-i], buffer, key)
        buffer = key[len(key)-1-i] + buffer
    return skipList
    
# Actual Search Algorithm
def BMSearch(haystack, needle):
    goodSuffix = generateSuffixShift(needle)
    badChar = generateBadCharShift(needle)
    i = 0
    a = []
    while i < len(haystack)-len(needle)+1:
        j = len(needle)
        while j > 0 and needle[j-1] == haystack[i+j-1]:
            j -= 1
        if j > 0:
            badCharShift = badChar.get(haystack[i+j-1], len(needle))
            goodSuffixShift = goodSuffix[len(needle)-j]
            if badCharShift > goodSuffixShift:
                i += badCharShift
            else:
                i += goodSuffixShift
        else:
            a.append(i)
            i += 1
    return a

def Build(haystack):
    b = []
    c=1
    for line in block:
        if line == "\n":
            b.append(c-1)
        c += 1
    return b

if __name__ == "__main__":
    
    name = raw_input("\nEnter the name of file to be searched(with extension): ")

    if os.path.isfile(name):
        with open(name, 'r') as myfile:
            block=myfile.read()
        #print(block)
        # len = len(block)
        pat = raw_input("\nEnter the Pattern to be searched: ")

        b = BMSearch(block,pat)
        a = Build(block)
        #print(b)
        #print(a)
        print("\nPattern match found %d times. \n" % len(b) )
        c = 0
        f=0
        for i in xrange(len(b)):
            if(f == 0):
                print("Pattern found in lines numbered: ")
                f=1
            while ((c < len(a)) and (a[c] < b[i])):
                c += 1
            print(c+1),
            if(i != len(b)-1):
                print(","),

    else:
        print("File with specified name doesn't exist")