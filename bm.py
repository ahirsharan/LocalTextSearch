import os
# Boyer Moore String Search implementation in Python
# Ameer Ayoub <ameer.ayoub@gmail.com>

# Generate the Bad Character Skip List
def generateBadCharShift(term):
    skipList = {}
    for i in range(0, len(term) - 1):
        skipList[term[i]] = len(term) - i - 1
    return skipList


# Generate the Good Suffix Skip List
def findSuffixPosition(badchar, suffix, full_term):
    for offset in reversed(range(1, len(full_term) + 1)):
        flag = True
        for suffix_index in range(0, len(suffix)):
            term_index = offset - len(suffix) - 1 + suffix_index
            if term_index < 0 or suffix[suffix_index] == full_term[term_index]:
                pass
            else:
                flag = False
        term_index = offset - len(suffix) - 1
        if flag and (term_index <= 0 or full_term[term_index - 1] != badchar):
            return len(full_term) - offset + 1


def generateSuffixShift(key):
    skipList = {}
    buffer = ""
    for i in range(0, len(key)):
        skipList[len(buffer)] = findSuffixPosition(key[len(key) - 1 - i], buffer, key)
        buffer = key[len(key) - 1 - i] + buffer
    return skipList


# Actual Search Algorithm
def boyer_moore_search(text, pattern):
    goodSuffix = generateSuffixShift(pattern)
    badChar = generateBadCharShift(pattern)
    i = 0
    shift_positions = []
    while i < len(text) - len(pattern) + 1:
        j = len(pattern)
        while j > 0 and pattern[j - 1] == text[i + j - 1]:
            j -= 1
        if j > 0:
            i += max(badChar.get(text[i + j - 1], len(pattern)), goodSuffix[len(pattern) - j])
        else:
            shift_positions.append(i)
            i += 1
    return shift_positions


def build_lines(block):
    line_numbers = []
    line_number = 0

    for line in block:
        if line == "\n":
            line_numbers.append(line_number)
        line_number += 1
    return line_numbers


if __name__ == "__main__":

    filename = input("Enter the name of file to be searched (with extension): ")
    if os.path.isfile(filename):
        with open(filename, 'r') as myfile:
            text = myfile.read()

        pattern = input("Enter the pattern to be searched: ")

        shift_positions = boyer_moore_search(text, pattern)
        lines = build_lines(text)

        if len(shift_positions) > 0:
            print("Pattern match found", len(shift_positions), "times, at lines:")

            line_number = 1
            for i in range(len(shift_positions)):
                while line_number < len(lines) and lines[line_number] < shift_positions[i]:
                    line_number += 1
                print(line_number, end="")
                if i != len(shift_positions) - 1:
                    print(", ", end="")
                else:
                    print()
        else:
            print("Pattern not found.")

    else:
        print("File with specified name doesn't exist.")
