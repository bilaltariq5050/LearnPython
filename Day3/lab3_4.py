my_name="Ahmed Bilal Tariq"
# Pick every 3rd character:
# Index 0 → "A".
# Index 3 → "e".
# Index 6 → "B".
# Index 9 → "a".
# Index	0	1	2	3	4	5	6	7	8	9	10
# Char	A	h	m	e	d		B	i	l	a	l
# Step 3 (0:11:3): Picks "A", "e", "B", "a" → Result: "AeBa".

print(my_name[0:11])
print(my_name[0:11:3])