# Lexycon
Lexycon is a command-line tool that will revolutionise the way you search.

How do I use Lexycon?

Give "!q" (without quotes) as query for stopping the script

For an Boyer-Moore Search Implementation

Place bm.py in the folder containing the text file to be searched.
Open terminal in the same folder, type

  $python bm.py

For a Word-indexing Implementation

Place the buildindex.py and querytexts.py in the same folder as all the text files to be searched.

  $python3 querytexts.py


Sample output by indexing all files in Corpus:

TIME TO INDEX = 
0:00:03.045874

ENTER THE SEARCH QUERY: ronaldo


COMPLETE PATTERN FOUND IN : 

test.txt
res.txt

SEPERATE WORDS FOUND IN:

WORD IS:
----------
ronaldo
----------

FILE NAME:

res.txt

LOCATION IN THE FILE: 

[937]

FILE NAME:

test.txt

LOCATION IN THE FILE: 

[1, 56, 116, 184, 280]


ENTER THE SEARCH QUERY:
