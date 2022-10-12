import math
import random
import numpy
from functools import reduce
# Just chill out... numbers are so amazing :3

b9f01d = [587711563, 224603878, 497453806, 558515321, 360895440, 694133730, 880163174, 502476712, 27894617,\
          349742425, 218461964, 77547489, 479255570, 214990255, 11711038, 915066632, 661402741, 683540022,\
          160718576, 858358791, 847169962, 824725408, 527328856, 325398751, 795928249, 369494389, 67114247,\
          280065685, 361585124, 34743939, 518827345, 487473738, 89172574, 890993683, 29069136, 381055162,\
          563087002, 57331874, 873196282, 696842019, 969525043, 778779181, 132348955, 631832488, 283734321,\
          664626131];

c9df35 = [971111, 974873, 983849, 29827349, 29943041, 29946029, 29951489, 29960897,\
          3708797237, 4294966001, 5061728993, 6650672641, 6999999989, 7337737777, 9999999929,\
          107928278317, 111160669681, 129866728583, 139149151157, 166400805323, 220123456789, 298999999999,\
          555555555551, 777775777777, 999998999999, 1000000000063, 1000000002217, 1000123457689, 1110110110111,\
          1110111110111, 1111111999999, 1468986414689, 1537267083749, 1886881868881, 2748779069441, 7177111117717,\
          10987654321001, 18691113008663, 23513892331597, 27985032798461, 41434547495153, 45678910111213,\
          55555544444441, 62481801147341, 67280421310721, 69747782858687]

a81cd9 = [9813865, 4667691, 3061276, 1005502, 3576737, 4881808, 6348404, 6930555, 7890343, 2812752, 1635304,\
          5012354, 6666641, 3067781, 6821781, 316344, 3249129, 293733, 9039804, 9791230, 5353417, 6297469,\
          7895004, 3122305, 8555752, 7051796, 8415800, 4943348, 781453, 7343563, 7951783, 7858816, 3717923,\
          2930667, 7175950, 9550604, 2680141, 2969967, 2303341, 9722032, 5787769, 2467961, 9791163, 7846587,\
          3644396, 6030320]

ac71d0 = [70891103, 81889332, 80675618, 2087914430, 2634987608, 2245952175, 3863742081, 3205815979,\
          218819036983, 244813062057, 323950655552, 751526008433, 902999998581, 484290693282, 1129999991977,\
          7231194647239, 7892407547351, 8571204086478, 9183843976362, 21465703886667, 25314197530735,\
          20929999999930, 41666666666325, 91777541777686, 76999922999923, 129000000008127, 74000000164058,\
          141017407534149, 92139139139213, 88808888808880, 92222295999917, 126332831663254, 195232919636123,\
          286806044069912, 236394999971926, 1119629334363852, 1439382716051131, 1719582396796996, 2022194740517342,\
          3749994394993774, 3646240179573464, 4065422999897957, 7999998399999504, 5873289307850054, 9688380668743824,\
          11857123085976790]

# oh, this makes me feel like a highschool student :v

def method3(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n // 3 + (n % 6 == 2), dtype=numpy.bool)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]

#https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def _0xb10f92(v0, v1): #Loga v0 base v1
    return math.log(v0, v1)

def _0x8cd91f(v0, v1, v2, v3): #Loga v0 base v1 * Loga v2 base v3
    return _0xb10f92(v0, v1)*_0xb10f92(v2, v3)

def _0x3b9f12(v0, v1, v2): #Loga v0 base v1 ) * v2
    return _0xb10f92(v0, v1)*v2

def _0x5d4141(v0, v1, v2): #Loga v1 base (v0 ^ v2)
    return 1/_0x3b9f12(v0, v1, v2)

def _0x015f99(v0, v1):
    #print("Doing long shit")
    v2 = random.randint(1, 10000000) #Slow shit down - Doesnt matter
    return math.e**( (_0x8cd91f(v2, 3, v0, v2) ) / ( _0x5d4141(3, math.e, v1) ) ) # Loga base e cua v0^v1

def _0x1337fc(v0, v1): #
    return round(_0x015f99(v0, v1))  #Lam tron loga base e cua v0^v1

def _0xd11111(v0, v1): # Tinh so nho nhat de v1*v3 > v0
    v2 = 0
    v3 = math.ceil(v0 / v1)
    #while (v2 < v0):
        ##print("d11 is looping")
     #   v2 = v2 + v1
      #  v3 = v3 + 1
    return v3

def _0xd22222(v0, v1):
    v2 = v0 / v1
    #i = 1
    #while (v2 <= v0):
        ##print("d22 Looping")
        #v2 = v2 + v1*i
        #i += 5
    #while (v2 > v0):
    #v2 = v2 -v1
    return v2 % 1

# hmm.. so weird, I'll be back with my coffee

def _0x4b891c(d020c1):
    v0 = 0
    v1 = len(d020c1)
    for i in range(v0, v1):
        d020c1.pop(0)
        d020c1.append(0)

def _0x3b091c(v0): #Tim so i trong khoang 2-v0 chia het cho v0
    v1 = 2
    v2 = v0
    #print(v0)
    a = sorted(factors(v0))
    #print(a)
    return a[1]

def _0xbe4515(d2060, v0, v1):
    v2 = 0
    v3 = v1 
    for i in range(v2, v3):
        if (d2060[i] == v0):
            return i 
    return -1

def _0xc00ffee(v0):
    v1 = 0
    while (v0 != 1):
        #print("Spend time on v2")
        v2 = _0x3b091c(int(v0))
        #print("Spend time on v0")
        v0 = _0xd11111(v0, v2)
        #print("Spend time on v3")
        v3 = _0xbe4515(b9f01d, v2, v1)
        if (v3 == -1):
            b9f01d[v1] = v2
            a81cd9[v1] += 1
            v1 += 1
        else:
            a81cd9[v3] += 1
    return v1 

def _0xbae103(v0, v1):
    for i in range(v1):
        if (b9f01d[i] == v0):
            b9f01d[i] = 1
            a81cd9[i] = 1

def _0x5be091(v0):
    v1 = 1
    for i in range(v0):
        v1 *= _0x1337fc(b9f01d[i], a81cd9[i])
    return v1 

def _0xdeadbeef():
    v0 = len(c9df35)
    for i in range(v0):
        ##print(i)
        #print("Meanless shit 1")
        _0x4b891c(b9f01d) #Replace everything with 0
        #print("Meanless shit 2")
        _0x4b891c(a81cd9) #Replace everythin with 0
        #print("What the f")
        v1 = _0xc00ffee(ac71d0[i])
        #print("This shouldnt be long anymore")
        _0xbae103(c9df35[i], v1)
        #print("Almost there")
        v2 = _0x5be091(v1)
        v2 -= i
        print(chr(v2), flush=True, end = '')

# let's go

if __name__ == "__main__":
    _0xdeadbeef()