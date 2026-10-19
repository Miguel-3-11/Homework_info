n = int(input())
counts = {}

for i in range(n):
    movie = input()
    counts[movie] = counts.get(movie, 0) + 1

sorted_movies = sorted(counts.items(), key = lambda x: x[1], reverse = True)

for movie, count in sorted_movies:
    print(movie, count)