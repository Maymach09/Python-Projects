line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?")

letter = position[0].lower()
number = position[1]

columns = ['a','b','c']
rows = ['1','2','3']

col_index = columns.index(letter)
row_index = rows.index(number)

map[row_index][col_index] = 'X'

print(f"{line1}\n{line2}\n{line3}")