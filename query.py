from movies import Movies

movies = Movies('./movies.txt')

x = ""

while (not (x=="q")):
    print("q: quit")
    print("list: print all the movie names")
    x=input()
    if x=="list":
        for name in movies._movies:
            print(name['name'])
