import logging
try:
    f = open("filee.txt", "r")
    print(f.read())
except FileNotFoundError as e:
    logging.warning(e)
