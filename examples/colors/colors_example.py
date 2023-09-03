from xsera import Colors
from random import choice
from time import sleep
c = Colors()


#debug color (if colors not visibledet)
c.debug_color()

#show all colors
#c.show_all()

#get all colors and styles code
#c.get_all()

#hex exmp
print(c.hex("#58d68a", "Hello"))
print(c.hex("#58d68a") + "Hello Friend" + c.color("color_end"))

print("\n\n")


#code exmp
print(c.color("red", "Hello"))
print(c.color("green") + "Hello Friend" + c.color("color_end"))
txt = c.color("red") + c.color("b_green") + "Hello Friend" + c.color("color_end")
print(txt)

#manual color challenge
print(c.blue+"Hello!!!"+c.color_end)


#blink exmp
c.sleeping_blink(text=txt, repetitions=7, wait=0.7)


sleep(3)


#random color
colors = c.get_all()
for i in range(999999):
	color = choice(colors)
	print(c.color(color, f"Hello, {color}"))
	sleep(0.2)
