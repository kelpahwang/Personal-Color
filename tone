def warm(skin_ton):
	warm_std = []
	cool_std = []

	warm_ton = 0
	cool_ton = 0

	for i in range(3):
		warm_ton = abs(skin_ton[i] - warm_std[i])
		cool_ton = abs(skin_ton[i] - cool_std[i])

	if (warm_ton <= cool_ton):
		return 'warm'
	else:
		return 'cool'

