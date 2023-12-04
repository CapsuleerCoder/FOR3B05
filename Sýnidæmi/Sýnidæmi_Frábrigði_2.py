def flatarmál_ferhyrnings(l, b):
    f = 0
    try:
        f = l*b
    except TypeError:
        print("Færibreyta/ur eru ekki af réttri tegund!")
    return f

lengd = int(input("Sláðu inn lengd ferhyrningsins"))
breidd = int(input("Sláðu inn breidd ferhyrningsins"))
# byrjum á því að reikna flatarmál ferhyrningsins
flatarmál = flatarmál_ferhyrnings(lengd, breidd)
print("Flatarmálið er: ", flatarmál)

# löngu seinna í stóru forriti ...
flatarmál_2 = flatarmál_ferhyrnings("rangur texti á röngum tíma í vitlausu húsi", "á móti sól")




