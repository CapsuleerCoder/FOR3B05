
with open("Synidaemi24.txt", "r") as skrá1, open("Fornöfn.txt", "w") as skrá2:
    for line in skrá1:    
        snyrt_lina = line.split()
        if len(snyrt_lina) > 0:
            fornafn = snyrt_lina[0]
            skrá2.write(fornafn+"\n")
    


