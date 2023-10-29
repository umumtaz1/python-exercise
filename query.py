from movies import Movies

movies = Movies('./movies.txt')

x = ""

while (not (x=="q")):
    print("q: quit")
    x=input()