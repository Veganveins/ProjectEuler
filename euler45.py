def triangle_nums(n):
	t_nums = []
	for i in range(1,n+1):
		t_nums.append(i*(i+1)/2)
	return t_nums


def pentagon_nums(n):
	p_nums = []
	for i in range(1,n+1):
		p_nums.append(i*(3*i-1)/2)
	return p_nums

def hexagon_nums(n):
	h_nums = []
	for i in range(1,n+1):
		h_nums.append(i*(2*i-1))
	return h_nums

def find_intersection(n):
	h_nums = hexagon_nums(n)
	p_nums = pentagon_nums(n)
	t_nums = triangle_nums(n)

	intersect = set(t_nums).intersection(p_nums, h_nums)

	return intersect

print(find_intersection(300000))