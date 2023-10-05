def bottle_song(num):
	for i in range(num,-1,-1):
		if i >1:
			print(f"{i} bottles of beer on the wall, {i} bottles of beer. Take one down and pass it around, {i-1} bottles of beer on the wall.")
		elif i==1:
			print("1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.")
		else:
			print("No more bottles of beer on the wall, no more bottles of beer.No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")

bottle_song(66)
