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
	top1 = y1
	bottom1 = y1+h1

	left2 = x2
	right2 = x2+w2
	top2 = y2
	bottom2 = y2+h2

	return !(left2 > right1 or
		 right2 < left1 or
		 top2 > bottom1 or
		 bottom2 < top1)
