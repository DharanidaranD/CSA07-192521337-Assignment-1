def mod2_div(dividend, divisor):
    rem = list(dividend)
    for i in range(len(dividend)-len(divisor)+1):
        if rem[i] == "1":
            for j in range(len(divisor)):
                rem[i+j] = str(int(rem[i+j]) ^ int(divisor[j]))
    return "".join(rem[-(len(divisor)-1):])

def encode(data, gen):
    return data + mod2_div(data + "0"*(len(gen)-1), gen)

def check(frame, gen):
    return set(mod2_div(frame, gen)) == {"0"}

GEN="1011"
frame=encode("1101011011",GEN)
print("transmitted:",frame)
print("no error :",check(frame,GEN))
bad=frame[:4]+("1" if frame[4]=="0" else "0")+frame[5:]
print("1-bit error:",check(bad,GEN))
burst=frame[:2]+"".join("1" if b=="0" else "0" for b in frame[2:5])+frame[5:]
print("3-bit burst:",check(burst,GEN))
# Search a short nonzero undetected error pattern
for n in range(1,13):
    for x in range(1,2**n):
        e=f"{x:0{n}b}"
        if set(mod2_div(e,GEN))=={"0"}:
            print("undetected error pattern:",e)
            raise SystemExit
