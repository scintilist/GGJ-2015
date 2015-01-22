import math

def dist(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	return math.sqrt(dx*dx + dy*dy)

def ang_rad(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	return math.atan2(dy, dx)

def ang_deg(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	return math.atan2(dy, dx) * 180.0/math.pi

def point_in_rect(x, y, rx, ry, rw, rh):
	x_col = (x >= rx and x <= (rx+rw))
	y_col = (y >= ry and y <= (ry+rh))
	return x_col and y_col

def rect_collide(x1, y1, w1, h1, x2, y2, w2, h2):
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

def rockstar():
	print r'''cccllllllooo0OkkkkkkkkkkkkkOOOOOOO00000KKKXXNNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNXX
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
....,;:::ccdOOxclllllloo......................```',,,,,,,,'';,xdxkkkkkxxxdddxxxkk'''
