# Number letters count

dict = { 0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 
        16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 100:7, 1000:8}
dict2 = { 0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 
    11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 
    19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninty', 
    100:'hundred', 1000:'thousand'}

def count(n):
    sum = 0
    for i in range(1, n + 1):
        sum += numberCount(i)
    return sum

def numberCount(n):
    if n in dict:
        return dict[n]
        # return len(dict2[n])
    else:
        p = str(n)
        if len(p) == 2:
            return numberCount(int(p[0]) * 10) + numberCount(int(p[1]))
        elif len(p) == 3:
            return numberCount(int(p[0])) + numberCount(100) + numberCount(1) + numberCount(int(p[1:]))
        elif len(p) == 4:
            return numberCount(int(p[0])) + numberCount(1000) + numberCount(int(p[1:]))

print(count(1000)) # 21124
