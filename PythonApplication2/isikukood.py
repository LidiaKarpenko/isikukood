from omamoodul import*
ikood=""
while True:
    ikood=input("sisesta isikukood: ")
    if pikkus(ikood)==False:
        print("liiga pikk või lühike isikukood")
    else:
        print("11 sümbolid ")
        s=sugu(ikood)
        if s=="viga":
            print("esimene täht ei ole õige")
        else:
            print(s)
            if sunnipaev(ikood)=="viga":
                print("2-7 tähed on valesti sisestatud")
            else:
                print(sunnipaev(ikood))