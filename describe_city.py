import random
MAP_STEP = ["Citadel","Plaza","Temple","Walls","Shanty town","River","Coast"]

SMALL_NAME = ["a village","a town", "a small city"]
MEDIUM_NAME = ["a large town", "a city", "a municipal centre"]
LARGE_NAME = ["a large city", "a metropolis", "the biggest city", "one of the most important city","the hugest metropolis"]

POP_NAME = ["souls","inhabitants","people", "citizen", "folks"]

DEF_ARMY = ["troop","guards","swordsman"]
DEF_CULT = ["worship","cult","faith","belief"]

DEF_AGE = ["100 years ago","150 years ago","200 years ago","250 years ago","300 years ago","500 years ago","1000 years ago","a decade ago", "some years ago","in the past", "in the forgotten days","in the mitical days"]
DEF_ENEMIES = ["beastman","nearest kingdom", "fire nation", "goblins", "orks", "lizardman"]
DEF_ENEMIES_SEA = ["pirates","peiratēs", "marauder", "misterious sea creature", "fishman", "marauder"]
DEF_ENEMIES_SEA.extend(DEF_ENEMIES)

DEF_ADJECTIVE = ["strong ","huge ","tall ","wood ","rock ","improvised ","","","","","",""]

DEF_LORD = ["the land lord", "the aristocracy","the lord"]
DEF_CHURCH = ["the bishop", "the high priest","the clairvoyant","the holy man"]
DEF_CITIZEND = ["the citizen","poor mans","the population","some folks"]

DEF_ENV = ["natural defence","huge forest","high mountain surrounding the area","continuous fog","magical force that protect people","magical force that make it hard to reach","magical force that protect the area"]

GOD = [
	['Chauntea',' goddess of agriculture','0100000' ],
	['Eldath',' goddess of peace ','0010000'],
	['Gond',' god of craft',' ','0100000'],
	['Helm',' god of protection',' ','0101000'],
	['Kelemvor',' god of the dead',' ','0110000'],
	['Lathander',' god of birth and renewal','0110000'],
	['Malar',' god of the hunt',' ','0100000'],
	['Mielikki',' goddess of forests','0000000'],
	['Mystra',' goddess of magic','1000000'],
	['Oghma',' god of knowledge','1010000' ],
	['Talos',' god of storms','0000001'],
	['Tempus',' god of war','1001000'],
	['Tyr',' god of justice','1010000'],
	['Umberlee',' goddess of the sea','0000001'],
	['Waukeen',' goddess of trade','0100001'],
	['Waukeen',' goddess of trade','01000xx'],
	['Mask',' god of thieves','0000100'],
	['Auril', 'goddess of winter','000x000']
	]

# 385192 / 58000
FORENGIN = 6.64

RACE = ["Human","Elf","Dwarf","Tiefeling","Dragonborn","Halfling","Half Ork"]
RACE_WIGHT = [80,5,5,4,4,1,1]

def c(group):
	return random.choice(group)

def sup(code,step):
	t = True
	for i in range(0,len(code)):
		if not code[i] == '0':
			#print(str(code[i])+" "+str(step[i])+" "+str(code[i] == str(step[i]) or (code[i] == 'x' and '0' == str(step[i]))))
			if code[i] == str(step[i]) or (code[i] == 'x' and '0' == str(step[i])):
				pass
			else:
				t=False
	return t			

def iv(size):
	return random.randint(0,20)+random.randint(0,int(size/20))

def wc(group,weight):
	r = random.randint(0,100)
	acc = 0
	for i in range(0,len(weight)):
		acc+= weight[i]
		if(r<acc):			
			return group[i]
	return group[-1]

def describe(name, population, size, step):
	IV = {
			"sword":iv(size),
			"shield":iv(size),
			"leather armor":iv(size),
			"iron armor":iv(size),
			"food":iv(size),
			"magic artifact":iv(size),
			"potion":iv(size),
			"jewelry":iv(size),
			"wine":iv(size),
			"beer":iv(size),
			"clothes":iv(size),
			"marble statue":iv(size)			
		}
	d = ""+name+" "
	cn = ""
	if(size < 12):
		cn = c(SMALL_NAME)
		d+= "is "+cn
	if(size >= 12 and size <= 24):
		cn = c(MEDIUM_NAME)
		d+= "is "+cn
	if(size > 24):
		cn = c(LARGE_NAME)
		d+= "is "+cn
	d+=" with a population of "+str(population)+" "+c(POP_NAME)+".\n"
	
	if(step[0]==1 and size>12):
		d+="In the city there are around "+str(int(population/100*random.randint(1,3)))+" "+c(DEF_ARMY)+".\n"
	
	TRACE = RACE.copy()
	mainRace = wc(TRACE,RACE_WIGHT)
	d+=name+" is mainly populated by "+mainRace+" around "+str(population-int(population/FORENGIN))+" "+c(POP_NAME)+",\n"
	
	fore = int(population/FORENGIN)
	numOfForegein = random.randint(1,3)
	TRACE.pop(TRACE.index(mainRace))
	
	d+="foregein are"
	if(numOfForegein>1):
		d+=" split in "+str(numOfForegein)+": "
	else:
		d+=" a solid group of "
		
	for i in range(0,numOfForegein):
		lastRace = c(TRACE)
		TRACE.pop(TRACE.index(lastRace))
		d+=lastRace+" "+str(int(fore/2))+", "
		fore = fore/2
	d+="and some other minorities not listed.\n"
	
	GOD_PICK = []
	for g in GOD:
		if(sup(g[2],step)):
			GOD_PICK.append(g[0]+","+g[1])
	
	idx = random.randint(0,len(GOD_PICK)-1)
	
	d+="The most important "+c(DEF_CULT)+" in the area is "+GOD_PICK.pop(idx)+"\n"
	if(len(GOD_PICK)>0):
		d+="but other faith are:\n"
		GOD_PICK = random.sample(GOD_PICK,min(3,len(GOD_PICK)))
		for g in GOD_PICK:
			d+="- "+g+"\n"
	
	#check wall
	if(step[3]==1):	
		d+=c(DEF_AGE).capitalize()+", after the terrible attack by the "
		if(step[6]==1):
			d+=c(DEF_ENEMIES_SEA)+", "
		else:
			d+=c(DEF_ENEMIES)+", "
		if(step[0]==1):
			if(step[2]==1):
				DEF_CHURCH.extend(DEF_LORD)
				d+=c(DEF_CHURCH)
			else:
				d+=c(DEF_LORD)
		else:
			if(step[2]==1):
				DEF_CHURCH.extend(DEF_CITIZEND)
				d+=c(DEF_CHURCH)
			else:
				d+=c(DEF_CITIZEND)
		d+= " decide to build a "+c(DEF_ADJECTIVE)+"wall."
	else:
		if(size>12 and (step[0]==1 or step[2]==1)):
			d+=cn.capitalize()+" like this does not need a wall due to the "+c(DEF_ENV)
		else:
			if(size<12 and random.randint(0,3)==0):
				d+="Continuous attack by "
				if(step[6]==1):
					d+=c(DEF_ENEMIES_SEA)+", "
				else:
					d+=c(DEF_ENEMIES)+", "
				d+="make hard for the "+c(POP_NAME)+" to grow in number"
	d+="\n"
	if(step[1]==1):
		q="In the market you can find:\n"
		for v in IV:
			if(IV[v]>=20):
				q+="The best "+v+" in the whole kingdom.\n"
			else:
				if(IV[v]>18):
					q+="Very good "+v+".\n"
				else:
					if(IV[v]>15):
						q+="They also sell "+v+"\n"
		if(not q=="In the market you can find:\n"):
			d+=q
	else:
		q="In town you can find:\n"
		for v in IV:
			if(IV[v]>=20):
				q+="The best "+v+" in the whole kingdom.\n"
		if(not q=="In town you can find:\n"):
			d+=q
		
	return d


#for i in range(0,1000):
#	out = describe("Carcosa",random.randint(1000,50109),random.randint(4,40),[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)])
#	print(out)
