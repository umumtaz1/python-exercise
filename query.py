from movies import Movies

movies = Movies('./movies.txt')

x = ""

while (not (x=="q")):
    print("q: quit")
    print("list: print all the movie names")
    print("sn: search movie names")
    print("sc: search casts")
    x=input()
    if x=="list":
        for name in movies._movies:
            print(name['name'])
    if x=="sn":
        print("enter a word to search:")
        y = input()
        for name in movies._movies:
            if (y.lower() in name['name'].lower()):
                print(name['name'])
    if x=="sc":
        print("enter a word to search:")
        z = input()
        for name in movies._movies:
            for i in range(len(name['cast'])):
                if (z.lower() in name['cast'][i].lower()):
                    print(name['name'])
                    print (name['cast'][i])
                    

    
                
