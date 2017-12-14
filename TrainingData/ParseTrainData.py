import ast

f = open('T1','r')

line_parsed = None

clicked = None
for line in f.readlines():
	if '{' in line:
		line_parsed = ast.literal_eval(line)
	if 'clicked' in line:
		clicked = line_parsed['value']['clickedId']
		clicked = clicked.split('_')
	elif 'value' in line:
		print line_parsed['value']['x'], line_parsed['value']['y'], line_parsed['value']['z'],
		if clicked:
			print clicked[0], clicked[1]
			clicked = None
		else:
			print None, None
