import math

def distance(a = (0, 0), b = (0, 0)):
	return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Returns the perpendicular distance from c to line ab, 
# or inf if the point is not perpendicular to any point on the segment
def perpendicular_distance(a = (0,0), b = (0,0), c = (0,0)):
	x1, y1 = a
	x2, y2 = b
	x0, y0 = c
	# ax + by + c = 0
	if x1 == x2: # if vertical line
		a = 1
		b = 0
		c = -x1
	elif y1 == y2: # if horizontal line
		a = 0
		b = 1
		c = -y1
	else:
		a = 1 / (x2 - x1)
		b = -1 / (y2 - y1)
		c = -a * x1 - b * y1
	# Calculate point F (closest point on line to center of circle)
	xF = (b*(b*x0 - a*y0) - a*c) / (a**2 + b**2)
	yF = (a*(-b*x0 + a*y0) - b*c) / (a**2 + b**2)
	# Calculate distance from the line to the center of the circle
	d = math.sqrt((xF-x0)**2+(yF-y0)**2)
	# Return d if point is on segment, else return inf
	if min(x1,x2) <= xF <= max(x1,x2) and min(y1,y2) <= yF <= max(y1,y2):
		return d
	return float('inf')

# Returns a list of all intersection points between a line segment and circle
def line_circle_intersect(a = (0, 0), b = (0, 0), c = (0,0), r = 5):
	intersections = []
	x1, y1 = a
	x2, y2 = b
	x0, y0 = c
	# ax + by + c = 0
	if x1 == x2: # if vertical line
		a = 1
		b = 0
		c = -x1
	elif y1 == y2: # if horizontal line
		a = 0
		b = 1
		c = -y1
	else:
		a = 1 / (x2 - x1)
		b = -1 / (y2 - y1)
		c = -a * x1 - b * y1
	# Calculate point F (closest point on line to center of circle)
	xF = (b*(b*x0 - a*y0) - a*c) / (a**2 + b**2)
	yF = (a*(-b*x0 + a*y0) - b*c) / (a**2 + b**2)
	# Calculate distance from the line to the center of the circle
	d = math.sqrt((xF-x0)**2+(yF-y0)**2)
	# If line does not pass within r of the circle center, return empty list
	if d > r:
		return intersections
	# Calculate the distance s from F to the edge of the circle along line AB
	s = math.sqrt(r**2 - d**2)	
	# Calculate line segment AB length
	line_len = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	# return no intersections if line is of length 0
	if line_len == 0:
		return intersections
	# Calculate unit vector AB
	ux = (x2 - x1) / line_len
	uy = (y2 - y1) / line_len
	# Calculate extreme x and y for line segment
	min_x = min(x1,x2)
	max_x = max(x1,x2)
	min_y = min(y1,y2)
	max_y = max(y1,y2)
	# Calculate possible intersection points as s * +/- unit_vector + F 
	xi1 = xF + s * ux
	yi1 = yF + s * uy
	xi2 = xF - s * ux
	yi2 = yF - s * uy
	# Test if possible intersection points are within the bounds of the line segment
	if  min_x <= xi1 <= max_x and min_y <= yi1 <= max_y:
		intersections.append((xi1, yi1))
	if  min_x <= xi2 <= max_x and min_y <= yi2 <= max_y:
		intersections.append((xi2, yi2))
	return intersections

# Line segment intersection
def intersect(a = (0, 0), b = (0, 0), c = (0, 0), d = (0, 0)):
	# Given 2 line segments defined by endpoints, returns the coordinates of the intersection, 
	# or false if they do not intersect
	x1, y1 = a
	x2, y2 = b
	x3, y3 = c
	x4, y4 = d
	if min(max(x1,x2), max(x3,x4)) < max(min(x1, x2), min(x3, x4)):
		return False # There is no mutual x coordinate
	if x1 == x2: # If L1 vertical
		if x3 == x4:
			return False # Both vertical
		Xa = x1
		a2 = (y3 - y4) / (x3 - x4)
		b2 = y3 - a2 * x3
		Ya = a2 * Xa + b2
		if min(y1, y2) <= Ya <= max(y1, y2):
			return (Xa, Ya)
		else:
			return False # Intersection not in L1 y span
	if x3 == x4: # If L2 vertical
		Xa = x3
		a1 = (y1 - y2) / (x1 - x2)
		b1 = y1 - a1 * x1
		Ya = a1 * Xa + b1
		if min(y3, y4) <= Ya <= max(y3, y4):
			return (Xa, Ya)
		else:
			return False # Intersection not in L2 y span
	a1 = (y1 - y2) / (x1 - x2)
	b1 = y1 - a1 * x1
	a2 = (y3 - y4) / (x3 - x4)
	b2 = y3 - a2 * x3
	if a1 == a2:
		return False # Parallel
	Xa = (b2 - b1) / (a1 - a2)
	if max(min(x1, x2), min(x3, x4)) <= Xa <= min(max(x1,x2), max(x3,x4)):
		Ya = a1 * Xa + b1
		return (Xa, Ya)
	else:
		return False # Intersection is out of bound

def point_in_poly(a = (0,0), poly = [(0,0),(0,0),(0,0)]):
	x, y = a
	n = len(poly)
	inside = False
	p1x,p1y = poly[0]
	for i in range(n+1):
		p2x,p2y = poly[i % n]
		if y > min(p1y,p2y):
			if y <= max(p1y,p2y):
				if x <= max(p1x,p2x):
					if p1y != p2y:
						xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
					if p1x == p2x or x <= xinters:
						inside = not inside
		p1x,p1y = p2x,p2y
	return inside

def tri_poly(polygon):
	# Polygon triangulation
	# Input is a simple polygon defined as a list of points
	# Output is a list where every set of 3 points forms a triangle
	# Implementation is ear clipping
	poly = polygon[:]
	triangles = []
	while len(poly) > 3: # While ears remain
		l = len(poly)
		for i, p in enumerate(poly):
			p_prev = poly[(i-1)%l]
			p_next = poly[(i+1)%l]
			midpoint = ((p_prev[0]+p_next[0])/2, (p_prev[1]+p_next[1])/2)
			if point_in_poly(midpoint, poly): # if midpoint is in the polygon
				# Check that there are no intersections
				intersection = False
				for i in range(i+2, l+i-2):
					a = poly[i%l]
					b = poly[(i+1)%l]
					if intersect(a, b, p_prev, p_next):
						intersection = True
						break
				if intersection:
					continue
				triangles.extend([p_prev, p, p_next])
				poly.remove(p)
				break
	triangles.extend(poly)
	return triangles
	
def remove_duplicate_vertices(poly):
	# Remove duplicate vertices
	poly_2 = []
	for i in range(len(poly)):
		if poly[i] != poly[(i+1)%len(poly)]:
			poly_2.append(poly[i])
	return poly_2
	
def poly_split(poly):
	# Split polygon into non-intersecting polygons
	poly = remove_duplicate_vertices(poly)
	poly_list = []
	_split(poly, poly_list)
	return poly_list
	
def _split(poly, poly_list):
	# Perform recursive splitting of polygon until no self-intersections remain
	l = len(poly)
	split_found = False
	for i in range(l):
		if split_found:
			break
		a = i
		b = (i+1)%l
		for j in range(i+2, i-1+l):
			c = j%l
			d = (j+1)%l
			i_point = intersect(poly[a], poly[b], poly[c], poly[d])
			if i_point:
				split_found = True
				if d != 0:
					_split(poly[:b] + [i_point] + poly[d:], poly_list)
					_split(poly[b:d] + [i_point], poly_list)
				else:
					_split(poly[:b] + [i_point], poly_list)
					_split(poly[b:] + [i_point], poly_list)
				break
	if not split_found:
		poly_list.append(poly) #polygon cannot be split, add to list