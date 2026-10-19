french = set(input().split())
swimmers = set(input().split())
pianists = set(input().split())

ans = (swimmers & pianists) - french

print(" ".join(sorted(ans, reverse = True)))