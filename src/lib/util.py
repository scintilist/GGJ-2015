import math
from collections import namedtuple

import pyglet

# Animation/images

def get_pixel_alpha(img, x, y):
	rawimage = img.get_image_data()
	format = 'RGBA'
	pitch = rawimage.width * len(format) # string length per image row
	pixels = rawimage.get_data(format, pitch)
	rows = len(pixels) // pitch # number of image columns
	columns = pitch // len(format)
	y = constrain(y, 0, rows-1)
	x = constrain(x, 0, columns-1)
	return pixels[y * pitch + x * len(format) + 3]
					

def make_animation(fn_base, frame_count = 0, num_digits = 2, center = False, center_x = False, loop = True, duration = 1):
	frame_list = get_frame_list(fn_base, frame_count, num_digits, center, center_x)
	return pyglet.image.Animation.from_image_sequence(frame_list, duration, loop = True)

def center_image(image):
    '''Sets an image's anchor point to its center'''
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

def get_frame_list(fn_base, frame_count = 0, num_digits = 2, center = False, center_x = False):
	fn, ext = fn_base.split('.')
	frame_list = []
	i = 0
	try:
		while True:
			name = '{}{:0{}}.{}'.format(fn, i, num_digits, ext)
			img = pyglet.resource.image(name)
			if(center):
				center_image(img)
			if(center_x):
				img.anchor_x = img.width/2
			frame_list.append(img)
			i += 1
	except:
		pass
	return frame_list

# Geometry

def constrain(v, mn, mx):
	return max(mn, min(mx, v))

Point = namedtuple('Point', ['x', 'y'])

def _dist(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	return math.sqrt(dx*dx + dy*dy)

def dist(p1, p2):
	return _dist(p1.x, p1.y, p2.x, p2.y)

def _ang_rad(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	return math.atan2(dy, dx)

def ang_rad(p1, p2):
	return _ang_rad(p1.x, p1.y, p2.x, p2.y)

def _ang_deg(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	return math.atan2(dy, dx) * 180.0/math.pi

def ang_deg(p1, p2):
	return _ang_deg(p1.x, p1.y, p2.x, p2.y)

def _point_in_rect(x, y, rx, ry, rw, rh):
	x_col = (x >= rx and x <= (rx+rw))
	y_col = (y >= ry and y <= (ry+rh))
	return x_col and y_col

def point_in_rect(point, corner, w, h):
	return _point_in_rect(point.x, point.y, corner.x, corner.y, w, h)

def _rect_collide(x1, y1, w1, h1, x2, y2, w2, h2):
	left1 = x1
	right1 = x1+w1
	top1 = y1+h1
	bottom1 = y1

	left2 = x2
	right2 = x2+w2
	top2 = y2+h2
	bottom2 = y2

	return not (left2 > right1 or
		 right2 < left1 or
		 top2 > bottom1 or
		 bottom2 < top1)

def rect_collide(corner1, w1, h1, corner2, w2, h2):
	return _rect_collide(corner1.x, corner1.y, w1, h1, corner2.x, corner2.y, w2, h2)

def rockstar():
	print(r'''cccllllllooo0OkkkkkkkkkkkkkOOOOOOO00000KKKXXNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNXX
ccllllllloo0KK0OOOkOOOOOOOOOOOOOOO000000KKKXXNNWWMMMMMMMMMMMMMMMMMMMMMMMWWNXXKK00
llllllloooxWNNXXK0OOOOOOOOOOOOOOOO0000000KKKKXXXNNWWWMMMWWNNXMMMMMNNXXKKK000OOOOO
clllllllllkNWWNNXK00000OOOOOOOOOOOOO00000000000KKKKKKKK00OOOOXNNNK00OOOkkkkkkkkkx
ccccccllllxWWNWWNXK0000OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkkkkkkkkkkkkOkkkkkkxxxxxxxxx
cccccllllloNWWNNNNXKK0OOOOOOOOOOOOOOOOOkkkkkkkkkkkkkkkkkkkkkxxxxxxxxxxxxxxxxxdddd
cccccllllllXWWWWNXXXK0OOOOOkOkkkkkkkkkkkkkkkkkkkxkxxxxxxxxxxxxxxxxxxxxxdddddddddd
cccccclllll0WWWWWNXKKK0Okkkkkkkkkkkkkkkkkkxxxxxxxxxxxxxxxxxxxxxxxxddddddddddddddd
cccccclllllkWWWWWNXXK00OOkxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdd
ccccccllllldWWWWWNNXK0OOOkxxxxddooooddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxddddddd
ccccccclllloXWWWWNNXKK0Okkxl:'.......;;clxkkkkkkkxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxd
ccccccclllll0WWWWNNXXK0Okl...     ........lxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ccccccclllllxWWWWWNNXKK0x.           .... .'lxkkkkkkkkkxxxxxxxxxxxxxxkkkkkkxxxxxx
cccccccclllloWWWWWNNXKK0d.         .. .... ..:dkkkkkkkkkkkkkkkkkkkkkkkkkkkxxkkkkk
cccccccccllllXWWWWNNXXK0l........      .   ...'okkkkkkkkkOOOkkkkkdxxkkkkkxddkkkkk
cccccccccccllOWWWWNNXXK0l ...```........     ...okkxxdkOOOOOOOOOkxdxkkkkkkxdkkkkk
:ccccccccccccxWWWWWNNXK0x......''.....','...   .;kkkxdxOOOOOOOOOkkdkOOOOOOkxddddo
cccccccccc;;xkWWWWWNNXXK0o.....','.....,;'..   .cOOOkkxkkkxxxddxkOoxOOOOOOOkxxxdd
:cccccc::;,.ldXWWWWNNXXK0Oo'...,,,,'',,;;;,'.  .oOOOOOkxxddddxkOOOxkOOOOOOOOOOOkx
:::::::;;;,.;lKWNWWNNXXK0Ok''..``````,,;;;;..  .l00000000OOkdOO00000OOOOOOOOOOkkk
::::::;;;;,.'ckWWNNNNXXKK0O;'.....```',;;;;.    c000000000OOdO00000000OOOOOOOOOkk
::::;;;;;;;..loNWNWNNXXXK00Od'.......',,;;,.   .dO0000000000dO000000OOOOOOOOOOOkk
::::;;;;;'......;XNNNNXXKK0OOd'.....'',,,,,,'::c:clldk000000xO000000OOOOOOOOOOOOO
::::;;;;,      ..;NNXXXXKK00Odc'....```'',,:;```'',,;o000000kx0000000OOOOOOOOOOOO
:::;;;;;,.  . ....NNXXXXOxo:'..........'',;,,.```,,::clodkO0Ox00000000OOOOOOOOOOO
::::::::;......''.KN0xl;,'............'',,';,......'',;:;:cdOxO000000000OOOOOOOOO
:::::::::.. ......xl,''.........''...','',;,`````````.,:;';:ldO0000000OOOOOOOOO00
:::::;,',. ... .'..'.'............``````,```',,,,,;;;,;::,',;:lkO0O0OOOOOOOOOO00O
:::::;'.... ........`````````..'.....';,''.'......',;;::cl;,,,;ldkOOOOOOOOOOO00Ok
ccccccc,```..........``````'...'.....';,'...',,'',,,,;;;:clc,',;:oxOOOOOOOOOO0Okk
::::::;......''... ...............................'',,;:c:cclc;,,cldkOOOOOOOOOOkk
::::::,........ .....                         ....```,;;;::::lll::lldkOOOOOOOOOxx
::;::;'......''. .... ...                         ...',;;:::cccllolcloxOOOOOOOkkd
;::;;;'..................                       .......'',;;::cccclooooxkOOOOOOkx
;::;::;,'.....'..........       .               ......... ..,;::cccccloddxkOOOkkx
::::::::;'....'......    . ..                      ........';',;::ccccccclloxkkkk
::::::::``````'......                              ........cxd:,;;::::cccccccokkk
:::::c:``````''.......   .....                     .......'okkxl,,;;:::::c:cccxkk
::::::,.``````'....ox..  ........     .            ......',xkkkxd;,,;;::::::ccldo
::::::'.``````....,OK;.   .............          .....''.';ooooooo:,,,;;:::::::lo
::::::,..```'....,cxKk..........   .......       ....'..',:looooooolc;,;;::::::lo
::::cc:........';ccdKKl........     ......       ....```,,:looooooooooolc:::;:ldd
::::ccc;'...',:ccccl0Kx........      ....      ......'';;::cdddddddddddddddddddoo
::::ccccc:ccccllcccckKd.......     ......     .......,;;;:::odddddxdddxxxddddxxxx
:::::cccccllllllllllx0c.. ...............   ........';;;;:::lxddddxxxxxxddxxxxxdd
::::ccccllloodxoolllo0c.. ...............  ..........,;;;;::cddxxxxdddxkkkxxdxxkk
::::cclllxkxkOOdoolllOo...............................,;;;::oxxxxxxkkkxxxxdxkkkkO
::::::ddodk00K0OdolllkO'.............................',;;;:cdxxxkkkkkxxxkkkkkkkxx
;:llcccloxkOkkkdoolllx0l...        . ................',,;;::dkkkkkkkkkkkkkkkxxkkO
;;,';cdoodlodkdooooooo0O;......        ..............',,;;::dkxxxxkkkkOOkkkkkkkkk
,,..,,;,,,;okOxodoooooO0c..........................'',,,;;;:ldxxkkkkxxxxkkkOOOOkk
'....```;:cxOOxoooooooxk'........................'',,,,,,,::ldxxxxxxdxkkOkkkkkxxk
'..';;::cccdOOxloooolloo'.....................```'',,,,,,;,.:lxxxxxxxkxxkkkkxxxkx
....,;:::ccdOOxclllllloo......................```',,,,,,,,'';,xdxkkkkkxxxdddxxxkk''')
