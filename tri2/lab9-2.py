# ----------------------
# Made by Brady Hodge
# Status: Done
# Date Started: 5/4/22
# ----------------------

def countChar(mystr):
    numb_of_e = mystr.count('e') + mystr.count('E')
    numb_of_char = len(mystr)
    percent_of_e = round(((numb_of_e / numb_of_char) * 100), 1)
    print("The text contains {} alphabetic characters, of wich {} ({}%) are 'e'.".format(numb_of_char, numb_of_e,
                                                                                         percent_of_e))


txt = """The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as 
it continues. The 20 meter pacer test will begin in 30 seconds. Line up at the start. The running speed starts 
slowly, but gets faster each minute after you hear this signal. [beep] A single lap should be completed each time you 
hear this sound. [ding] Remember to run in a straight line, and run as long as possible. The second time you fail to 
complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, 
start. """

countChar(txt)
 
 