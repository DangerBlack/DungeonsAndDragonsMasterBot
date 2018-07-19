import random


f = open('assets/city/cityname.txt', 'r')
CITY_NAMES = f.read()
f.close()
CITY_NAMES = CITY_NAMES.split(",")

MEDIUM_PEOPLE = 38850
SMALL_PEOPLE = MEDIUM_PEOPLE/4
LARGE_PEOPLE = MEDIUM_PEOPLE*3

PEOPLE = [SMALL_PEOPLE,MEDIUM_PEOPLE,LARGE_PEOPLE]

#8: 9700
#18: 38850
#42: 116500

#y = 2915 x - 13620

#City Info
#http://www222.pair.com/sjohn/blueroom/demog.htm
# (PLACE, SV, IMPORTANT)
OTHER_PLACE = (
        ('BAKERY',800,1),
        ('BARBER_SHOP',350,0),
        ('BATHER',1900,0),
        ('BREWERY',1400,1),
        ('BLEACHER_SHOP',2100,0),
        ('BOOKBINDERS_SHOP',3000,0),
        ('BOOK_SHOP',6300,1),
        ('BUCKLE_MAKER_SHOP',1400,0),
        ('BUTCHER_SHOP',1200,1),
        ('CARPENTERY',550,0),
        ('CHANDLERS',700,0),
        ('CHICKEN_SHOP',1000,1),
        ('COOPERS',700,0),
        ('COPYIST',2000,1),
        ('CUTLER',2300,0),
        ('DOCTOR',1700,1),
        ('FISHMONGER',1200,1),
        ('FURRIERS',250,0),
        ('GLOVEMAKER_SHOP',2400,0),
        ('HARNESS_MAKERS',2000,0),
        ('HAY_MERCHANT',2300,0),
        ('HEADGEAR',950,0),
        ('ILLUMINATOR',3900,0),
        ('INN',2000,1),
        ('JEWELER',400,1),
        ('LOCKSMITH',1900,0),
        ('MAGIC_SHOPS',2800,1),
        ('MAIDSERVANTS',250,0),
        ('MASONS',500,0),
        ('MERCERS',700,0),
        ('OLD-CLOTHES',400,0),
        ('PAINTERS',1500,0),
        ('PASTRYCOOKS',500,0),
        ('PLASTERER',1400,0),
        ('PURSE_SHOP',1100,0),
        ('ROOFER',1800,0),
        ('ROPEMAKER',1900,0),
        ('RUGMAKER',2000,0),
        ('SADDLERY',1000,1),
        ('SCABBARDMAKERS',850,0),
        ('SCULPTOR',2000,1),
        ('SHOEMAKERS',150,0),
        ('SMITHY',1500,1),
        ('SPICE_SHOP',1400,1),
        ('TAILOR_SHOP',250,1),
        ('TANNER_SHOP',2000,1),
        ('TAVERN',400,1),
        ('WATERCARRIERS',850,0),
        ('WEAVERS',600,0),
        ('WINE-SELLERS',900,0),
        ('WOODCARVER_SHOP',2400,0),
        ('WOODSELLERS',2400,0),
    )

OP_NAME = 0
OP_SV = 1
OP_IMPORTANT = 2

def addSpace(name,LONGWORD):
    space = len(LONGWORD)- len(name)
    return name.replace('_',' ').lower()+(" "*space)

#City Name
#https://www.namegenerator.biz/application/p.php?type=1&id=place_names&spaceflag=false

def getCityDetail(size):
    if size>4:
        people = int(2915* size - 13620)
        people+= random.randint(-1000,1000)
    else:
        people= random.randint(100,2000)
    out = "<b>Name:</b> "+random.choice(CITY_NAMES)+"\n"
    out+= "<b>People:</b> "+str(people)+"\n"
    out+="<b>Buildings:</b>\n<pre>\n"
    i = 1
    for other in OTHER_PLACE:
        if other[OP_IMPORTANT]>0:
            out+= addSpace(other[OP_NAME],"CHICKEN_BUTCHER")+" | "+addSpace(str(int(people/other[OP_SV])),"000")
            if i%2 == 0:
                out+=" |\n"
            else:
                out+= " | "
            i+=1
    out+="</pre>"
    return out
