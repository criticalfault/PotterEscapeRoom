from PIL import Image, ImageDraw
import random
gestures = list()
directions = ['up ','right ','down ','left ']

def makeGesture():
	
	gesture = list()
	gesture.append(random.choice(directions))
	i=1
	while i < 7:
		i += 1
		temp = random.choice(directions)
		if(temp == gesture[-1] 
			or temp == "up " and gesture[-1] == "down " 
			or temp == "down " and gesture[-1] == "up "
			or temp == "right " and gesture[-1] == "left "
			or temp == "left " and gesture[-1] == "right "):
			i -= 1
			continue
		else:
			gesture.append(temp)
	if gesture in gestures:
		return
	else:
		gestures.append(gesture)



def drawSigil(num, movements):
	source_img = Image.new('RGB', (400,400),'#FFFFFF')
	draw = ImageDraw.Draw(source_img)

	x=200
	y=200

	directions = [(x, y)]

	for item in movements:
		if item == "down ":
			y += 50
		if item == "up ":
			y -= 50
		if item =="right ":
			x += 50
		if item == "left ":
			x-= 50
		directions.append((x,y))

	draw.line(directions[0:2], "#0000ff", width=5)
	draw.line(directions[1:3], "#00ff00", width=5)
	draw.line(directions[2:4], "#ff0000", width=5)
	draw.line(directions[3:5], "#000055", width=5)
	draw.line(directions[4:6], "#005500", width=5)
	source_img.save('./sigils/sigil-%i.jpg' % num)



while len(gestures) < 150:
	makeGesture()
	

thefile = open('gestures.txt', 'w')
i=0		
for item in gestures:
  	i+=1
  	for g in item:
  		thefile.write("%s" % (g))
  	thefile.write("\n")
i=0
for item in gestures:
	i+=1
	drawSigil(i,item)



