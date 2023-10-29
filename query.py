from movies import Movies

movies = Movies('./movies.txt')

x = ""

while (not (x=="q")):
    print("q: quit")
    print("list: print all the movie names")
    print("sn: search movie names")
    x=input()
    if x=="list":
        for name in movies._movies:
            print(name['name'])
    if x=="sn":
        print("enter a word to search:")
        y = input()
        for name in movies._movies:
            if (y in name['name'].lower()):
                print(name['name'])
                
