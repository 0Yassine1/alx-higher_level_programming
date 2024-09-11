#!/usr/bin/python3
# Print the ASCII alphabet in lowercase, excluding 'q' and 'e'

print("{}".format("".join(chr(i) for i in range(97, 123)
      if i != 101 and i != 113)), end="")
