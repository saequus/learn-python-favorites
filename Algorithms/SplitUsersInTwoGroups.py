def check_on_big_num(num1, num2):
	items = [i for i in range(num1, num2)]
	v1, v2 = 0, 0
	for i in items:
		if define_ab_group2(i):
			v1 += 1
		else:
			v2 += 1
	print('A group items number: %s', v1)
	print('B group items number: %s', v2)
	print('Relation A to B: %s%s' % (round(v1 / v2 * 100, 4), '%'))


def define_ab_group1(e):
	e = str(e)
	c0, c1 = 0, 0
	for i in e:
		if int(i) % 2 == 0:
			c0 += 1
		else:
			c1 += 1
	return True if c0 >= c1 else False


def define_ab_group2(e):
	e = str(e)
	c0, c1 = 0, 0
	for i in e:
		if int(i) % 2 == 0:  # 2, 4, 6, 8
			c0 += int(i)
		else:  # 1, 3, 5, 7, 9
			c1 += int(i)
	return True if c0 >= c1 else False


# A group items number: %s 3575891
# B group items number: %s 4596109
# Relation A to B: 77.8026%


def define_ab_group(e):
	return True if sum([int(_) for _ in str(e)]) % 2 == 0 else False

# A group items number: %s 86000
# B group items number: %s 86000
# Relation A to B: 100.0%
