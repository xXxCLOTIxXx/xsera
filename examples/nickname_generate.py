from xsera import generate_nikcnameV2, generate_nikcnameV1
from xsera import Colors

c = Colors()
c.debug_color()

print(c.color("blue", "generate #1 (generate_nikcnameV1)"))
print(c.color("magenta"))
for i in range(15):
	print(generate_nikcnameV1())
print(c.color("blue", "generate #2 (generate_nikcnameV2)"))
print(c.color("magenta"))
for i in range(15):
	print(generate_nikcnameV2())

print(c.color("color_end"))