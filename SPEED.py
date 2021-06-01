def driver_speed(speed):
    i=75
    point=0
    while i<=speed:
        if speed>70:
            point=point+1
            i=i+5
        print("point",point)
    if speed<70:
        print("okay")
    if point>12:
        print("licenese suspended")
speed=int(input("enter your speed"))
driver_speed(speed)