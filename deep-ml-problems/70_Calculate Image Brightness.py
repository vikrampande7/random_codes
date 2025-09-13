def calculate_brightness(img):
	# Write your code here
    if not img:
        return -1
    if len(img) == 2:
        if len(img[0]) != len(img[1]):
            return -1
    total = 0
    for i in img:
        for v in i:
            if v < 0 or v > 255:
                return -1
            else:
                total += v
    return total / (len(img) * len(img[0]))