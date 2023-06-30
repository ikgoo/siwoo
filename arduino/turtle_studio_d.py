import turtle

text = "Hello, World!"
length = len(text)
substring = text[7:12]

turtle.write(text, align="center")
turtle.write("Length: " + str(length), align="center")
turtle.write("Substring: " + substring, align="center")

turtle.done()