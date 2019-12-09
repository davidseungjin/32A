def create_grid(locked_pos={}):  # *
	grid = [[(0,0,0) for _ in range(6)] for _ in range(13)]
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if (j, i) in locked_pos:
				c = locked_pos[(j,i)]
				grid[i][j] = c
	return grid

a = create_grid()

print(a)
