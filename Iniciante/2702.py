ref = list(map(int,input().split()))
req = list(map(int,input().split()))
final = 0
#ref = [80, 20, 40]
#req = [45, 23, 48]
#ttl1, ttl2, ttl3 = ref1-req1, ref2-req2, ref3-req3
#print(ref, req)
for x in range(3):
    #print(x)
    #print(ref[x],req[x])
    if ref[x] > req[x]:
        pass
    else:
        final += (ref[x] - req[x]) * -1
        #print(final)
    #print(final)
    x += 1

print(final)