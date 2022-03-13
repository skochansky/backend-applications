import logging
text = input("Podaj text, ktory chcesz zapisac o pliku")
try:
    f = open("file_save.txt", "w")
    f.write(text)
except FileExistsError as e:
    logging.warning(e)
