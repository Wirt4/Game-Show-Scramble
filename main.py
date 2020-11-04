from game import Game

ans = input("Is this double score? (y/n)").strip().upper()
doub = False
if ans =="Y":
    doub = True
infile = input("Enter the filepath for the csv to read: ")
game = Game(infile, doub)

outfile = input("Enter the name to save the new list: ")
game.make_file(outfile)
print("questions scrambled")