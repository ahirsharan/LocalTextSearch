import sys, re


# Returns the first index after a newline character in the file. Used to count the lines in the text.
def newlines_index(text):
    newlines_list = [0]
    index = 1

    for char in text:
        if char == '\n':
            newlines_list.append(index)

        index += 1

    return newlines_list


# Modified binary search that returns the first index in position_list <= position, and 'None' if no such index exists.
def first_index(position, position_list):
    if position_list[0] > position:
        # all position
        return None

    low = 0
    high = len(position_list)

    while low < high - 1:
        mid = (high + low) // 2

        if position_list[mid] > position:
            high = mid - 1
        else:
            low = mid

    if position_list[low] <= position:
        return low
    else:
        return None

# Currently, sys.argv[1] is the filename with extension. Later, sys.argv[1] will be the pattern itself.
pattern = input("Enter pattern to match: ")

for file in sys.argv[1:]:
    with open(file, 'r', encoding="utf8") as f:
        text = f.read()

        # check the file text
        # print(text)

        # get indexes of first characters after newlines.
        lines_index = newlines_index(text)

        # ignore cases when searching
        # check if there is a match first
        if re.search(pattern, text, re.IGNORECASE):
            # match found.
            for match_object in re.finditer(pattern, text, re.IGNORECASE):
                print("Match at line", 1 + first_index(match_object.start(), lines_index), end="    ")

                # find the words before and after the match - parameter '3' can be changed below
                context_startindex = match_object.start()
                context_endindex = match_object.end()

                spacecount = 0
                while spacecount < 3 and context_startindex >= 0:
                    if text[context_startindex] == "\n":
                        # stop at newline!
                        break

                    if text[context_startindex].isspace():
                        spacecount += 1

                    context_startindex -= 1

                context_startindex += 1

                spacecount = 0
                while spacecount < 3 and context_endindex < len(text):
                    if text[context_endindex] == "\n":
                        # stop at newline!
                        break

                    if text[context_endindex].isspace():
                        spacecount += 1

                    context_endindex += 1

                # print matched text with context
                if context_startindex == 0:
                    print(text[0: context_endindex] + "...")
                elif context_endindex == len(text):
                    print("..." + text[context_startindex: len(text)] + ".")
                else:
                    print("..." + text[context_startindex: context_endindex] + "...")

        else:
            # no match.
            print("No match for pattern \"" + pattern + "\" in file", file)
