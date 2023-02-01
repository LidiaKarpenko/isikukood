def pikkus(ikood: str)->bool:
    """funktsioon tagastab True, kui pikkus on 11 sümbolid
    :param str ikood: inimeste isikukood 
    :rtype: bool
    """ 
    if len(ikood)==11:
        flag=True
    else:
        flag=False
    return flag

def sugu(ikood: str)->str: 
    """kui esimene täht on [1, 2, 3, 4, 5, 6], siis määrame sugu
    :param str ikood: isikukood
    :rtype: str
    """
    ikood_list=list(map(int,ikood))
    if ikood_list[0] in [1,3,5]:
        s="mees"
    elif ikood_list[0] in [2,4,6]:
        s="naine"
    else:
        s="viga"
    return s 
def sunnipaev(ikood: str):
    ikood_list=list(map(int,ikood))

    y=int(str(ikood_list[1])+str(ikood_list[2]))
    m=int(str(ikood_list[3])+str(ikood_list[4]))
    d=int(str(ikood_list[5])+str(ikood_list[6]))

    if int(m)>0 and int(m)<13 and int(d)>0 and int(d)<32:
        if ikood_list[0] in [1,2]:
            yy="18"
        elif ikood_list[0] in [3,4]:
             yy="19"
        else:
            yy="20"
        spaev=d+"."+m+"."+y
    else:
         spaev="viga"
    return spaev

def sunnikoht(ikood: str)->str:
    ikood_list=list(ikood)
    tahed_8910=ikood[7]+ikood_list[8]+ikood_list[9]
    t=int[tahed_8910]
    if t<t<10:
        haigla="Kuresaare haigla"
    elif 11<t<19:
        haigla="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21<t<220:
        haigla=" Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif 221<t<270:
        haigla=" Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif 271<t<370:
        haigla="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif 371<t<420:
        haigla="Narva Haigla"
    elif 421<t<470:
        haigla="Pärnu Haigla"
    elif 471<t<490:
        haigla="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif 491<t<520:
        haigla="Järvamaa Haigla (Paide)"
    elif 521<t<570:
        haigla="Rakvere, Tapa haigla"
    elif 571<t<600:
        haigla="Valga Haigla"
    elif 601<t<650:
        haigla="Viljandi Haigla"
    elif 651<t<700:
        haigla="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    else:
        haigla="välismaal"
    return haigla

def lause()->str:
    print(f"see on {sugu(ikood)} ta on sündinud {sunnipaev(ikood)}, tema sünnikoht on  {sunnikoht(ikood)}")
