#Vote For Better Nation
from cs1graphics import *
from time import sleep

paper=Canvas(1400,1400,'skyBlue','project',autoRefresh=True)

def Sc(self,factor):
    if not isinstance(factor,(int,float)):
	      raise TypeError('scaling factor must be a positive number')
    p=self._localToGlobal(self._reference)
    tra=_Transformation((1.,0.,0.,1.)+p.get())
    s=_Transformation((factor,0.,0.,factor,0.,0.))
    self._transform=tra*(s*(tra.inv()*self_trasform))
    self._update({'transformation':self_transform})

room=Rectangle(200,400,Point(1230,540))
room.setFillColor('brown')
room.setBorderColor('black')
roof=Polygon(Point(1080,270),Point(1170,270),Point(1260,368),Point(1000,368))
roof.move(100,0)
roof.setFillColor('darkgray')
roof.setDepth(20)
room.setDepth(30)
door=Rectangle(20,70,Point(1230,570))
door.setFillColor('black')
door.setDepth(50)
paper.add(room)
paper.add(roof)
ce=Text('Complain Room')
ce.moveTo(1190,240)
ce.setFontSize(40)
ce.setDepth(50)
paper.add(ce)

stickman=Layer()
head=Circle(27,Point(130,110))
head.setFillColor('black')
stickman.add(head)
body=Rectangle(5,100,Point(130,170))
body.setFillColor('black')
body.setDepth(50)
stickman.add(body)
hand1=Path(Point(133,175),Point(150,175),Point(160,175))
hand1.setBorderWidth(7)
hand1.rotate(10)
stickman.add(hand1)
hand2=Path(Point(130,175),Point(114,175),Point(97,175))
hand2.setBorderWidth(7)
hand2.rotate(-10)
stickman.add(hand2)
leg1=Path(Point(130,220),Point(150,230),Point(170,235))
leg1.setBorderWidth(7)
leg1.rotate(24)
stickman.add(leg1)
leg2=Path(Point(130,220),Point(110,230),Point(90,235))
leg2.setBorderWidth(7)
leg2.rotate(-24)
stickman.add(leg2)

paper.add(stickman)

for i in range(1,40):
   timeDelay=0.5
   stickman.move(20,0)
   sleep(timeDelay)
for i in range(1,17):
   timeDelay=0.5
   stickman.move(0,24)
   sleep(timeDelay)
for i in range(1,9):
   timeDelay=0.5
   stickman.move(20,0)
   sleep(timeDelay)
dialouge=Text('Why these doors are closed?')
dialouge.moveTo(900,500)
paper.add(dialouge)
timeDelay=1
sleep(timeDelay)
paper.remove(dialouge)
   
stickman2=stickman.clone()
stickman2.move(-650,68) 
stickman2.sc(1)
stickman2.setDepth(40)
paper.add(stickman2)
for i in range(1,45):
   timeDelay=0.5
   stickman2.move(20,0)
   sleep(timeDelay)   
paper.remove(stickman2)

dia=Text('????')
dia.moveTo(980,500)
paper.add(dia)
timeDelay=2
sleep(timeDelay)
paper.remove(dia)

stickman3=stickman.clone()
stickman3.move(-650,68) 
stickman3.sc(1.1)
stickman3.setDepth(40)
paper.add(stickman3)
for i in range(1,43):
   timeDelay=0.5
   stickman3.move(20,0)
   sleep(timeDelay)   


dia=Text('Whats wrong with this door..If all can go then why dont me!!')
dia.moveTo(850,500)
paper.add(dia)
timeDelay=3
sleep(timeDelay)
paper.remove(dia)

di=Text('Ahmm..Let me ask someone')
di.moveTo(900,500)
paper.add(di)
timeDelay=2
sleep(timeDelay)
paper.remove(di)

for i in range(1,18):
   timeDelay=0.5
   stickman3.move(-20,0)
   sleep(timeDelay)


a=Text('Heyy')
a.moveTo(950,480)
paper.add(a)
timeDelay=3
sleep(timeDelay)
paper.remove(a)
b=Text('Hello')
b.moveTo(890,550)
paper.add(b)
timeDelay=3
sleep(timeDelay)
paper.remove(b)
c=Text('Can you please help me to get a answer of a question?')
c.moveTo(890,480)
paper.add(c)
timeDelay=3
sleep(timeDelay)
paper.remove(c)
d=Text('Yeah..Sure. Say what is the problem?')
d.moveTo(820,550)
paper.add(d)
timeDelay=3
sleep(timeDelay)
paper.remove(d)
e=Text('I am trying to enter in a room to register a complain')
e.moveTo(890,480)
paper.add(e)
timeDelay=3
sleep(timeDelay)
paper.remove(e)
f=Text('But it seems that doors are closed for me only')
f.moveTo(880,480)
paper.add(f)
timeDelay=3
sleep(timeDelay)
paper.remove(f)
g=Text('I just cant find the reason..Please help me')
g.moveTo(880,480)
paper.add(g)
timeDelay=3
sleep(timeDelay)
paper.remove(g)
h=Text('Ohh...Can I ask you 1 question?')
h.moveTo(830,550)
paper.add(h)
timeDelay=3
sleep(timeDelay)
paper.remove(h)
i=Text('Yeah..Sure')
i.moveTo(960,480)
paper.add(i)
timeDelay=3
sleep(timeDelay)
paper.remove(i)
j=Text('Have you ever voted for our better nation?')
j.moveTo(780,550)
paper.add(j)
timeDelay=3
sleep(timeDelay)
paper.remove(j)
k=Text('Vote!!! No..But how is it related to this?')
k.moveTo(900,480)
paper.add(k)
timeDelay=3
sleep(timeDelay)
paper.remove(k)
l=Text('I dnt think 1 vote make any difference to the nation')
l.moveTo(890,480)
paper.add(l)
timeDelay=3
sleep(timeDelay)
paper.remove(l)
m=Text('So,why should I waste my time?')
m.moveTo(910,480)
paper.add(m)
timeDelay=3
sleep(timeDelay)
paper.remove(m)
n=Text('Thats what makes the difference')
n.moveTo(800,550)
paper.add(n)
timeDelay=3
sleep(timeDelay)
paper.remove(n)
q=Text('As a responsible citizen of the nation,')
q.moveTo(780,550)
paper.add(q)
timeDelay=3
sleep(timeDelay)
paper.remove(q)
r=Text('One must go for voting')
r.moveTo(800,550)
paper.add(r)
timeDelay=3
sleep(timeDelay)
paper.remove(r)
w=Text('And if you dont want to go for it,')
w.moveTo(800,550)
paper.add(w)
timeDelay=3
sleep(timeDelay)
paper.remove(w)
x=Text('Then you dont have any right to complain to the government')
x.moveTo(750,550)
paper.add(x)
timeDelay=3
sleep(timeDelay)
paper.remove(x)
y=Text('As when you had a chance to change the government,')
y.moveTo(750,550)
paper.add(y)
timeDelay=3
sleep(timeDelay)
paper.remove(y)
z=Text('You have not used your power of vote..')
z.moveTo(790,550)
paper.add(z)
timeDelay=3
sleep(timeDelay)
paper.remove(z)
p=Text('oh..You have really opened up my eyes')
p.moveTo(900,480)
paper.add(p)
timeDelay=3
sleep(timeDelay)
paper.remove(p)
o=Text('Nowonwards I too will go for vote to make my nation better')
o.moveTo(850,480)
paper.add(o)
timeDelay=3
sleep(timeDelay)
paper.remove(o)

paper.remove(room)
paper.remove(roof)
paper.remove(stickman3)
flag=Rectangle(400,80,Point(690,200))
flag.setFillColor('orange')
flag1=Rectangle(400,80,Point(690,280))
flag1.setFillColor('white')
flag2=Rectangle(400,80,Point(690,360))
flag2.setFillColor('green')
chakra=Circle(38,Point(690,280))
chakra.setFillColor('skyblue')
paper.add(flag)
paper.add(flag1)
paper.add(flag2)
paper.add(chakra)
slogan=Text('Vote for better india')
slogan.moveTo(700,500)
slogan.setFontSize(70)
paper.add(slogan)

for i in range(1,12):
    stickman.move(0,-20)
    stickman.rotate(4)
    timeDelay=0.5
    sleep(timeDelay)
    stickman.rotate(-4)
    timeDelay=0.5
    sleep(timeDelay)
for i in range(1,5):
    stickman.move(-20,0)
    stickman.rotate(4)
    timeDelay=0.5
    sleep(timeDelay)
    stickman.rotate(-4)
    timeDelay=0.5
    sleep(timeDelay)










   
   



#dialouge=Text('What is this?')
#dialouge.move(250,400)
#paper.add(dialouge)
#paper.add(Image)
#paper.refresh()


