m = input()
e = input()
m = int(m)
e = int(e)
if m>90 and e>90:
    print("可拿獎品")
elif m<60 and e<60:
    print("要處罰")
elif m<60 or e<60:
    print("再加油")
