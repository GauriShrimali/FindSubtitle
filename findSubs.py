# Find a subtitle file for a movie
try:
    from googlesearch import search
except ImportError:
    print("Connectivity issue!")

#searching for subtitle for a movie
path = input("PATH OF THE MOVIE: ")
if '/' not in path:
    print("Incorrect path")
else:
    name = path.split('/')[-1]
    query = "Subtitles for " + name 
    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
        print(j) 