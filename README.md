# Lexycon
Algorithm to search a string in all txt files in a folder.

How to use?

For BM implementation

Place bm.py in the folder containing the text file to be searched.
Open terminal in the same folder, type

  $python bm.py

play along! 

For indexing implementation

Place the buildindex.py and querytexts.py in the same folder where alll the txt files to be searched is places

  $python3 querytexts.py

play along!

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
