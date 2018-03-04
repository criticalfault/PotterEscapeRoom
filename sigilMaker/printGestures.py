from PIL import Image, ImageFont, ImageDraw, ImageEnhance






def drawSigil(num, movements):
	source_img = Image.new('RGB', (300,300))
	draw = ImageDraw.Draw(source_img)
	movements = 'down right down up left'
	moveArray = movements.split(" ")

	x=150
	y=150

	directions = [(x, y)]

	for item in moveArray:
		if item == "down":
			y += 50
		if item == "up":
			y -= 50
		if item =="right":
			x += 50
		if item == "left":
			x-= 50
		directions.append((x,y))

	draw.line(directions, fill=None, width=2)
	source_img.save('sigil-'+num+'.jpg')