# Lexycon
Lexycon is a command-line tool that will revolutionise the way you search. Made with Python 3.5, Lexycon will search for a
pattern and show you where the search pattern exists, along with extended line context - neighbouring words around the match.

## How do I use Lexycon?

### Single File search:

To search a file, place it in the same directory as pygrep.py, browse there and run,
Note - This will search a query only in 'filename.txt'.
```
python3 pygrep.py filename.txt
```
### Multi File search:

Te search multiple files at once, keep the buildindex.py and querytext.py in same folder as all the text files. then run
```
python3 querytext.py
```
Enter your desired query and get which all files have that and at which location.

### Boyer Moore Implementation:

Boyer Moore's searching algorithm is implemented in bm.py. It is a bit slower but it works.

## To Dos
- [x] Implement Cosine-inverse Ranking system
- [ ] Make code compatibl to capital letters
- [ ] Make a GUI using Tkniter
