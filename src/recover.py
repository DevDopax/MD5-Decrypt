# Loading encrypted wordlist

wordlist = {}

with open("wordlist/wordlist_md5.txt", "r") as wl:
    line = wl.readline().strip()
    
    while line:    
    
        md5_hash, text = line.split(" ")
    
        wordlist[md5_hash] = text
    
        line = wl.readline().strip()

# Searching password in wordlist

with open("data/leak.txt", "r") as leaks:

    line = leaks.readline()

    while line:
        
        # split line in email and password
        email, password = line.strip().split(":")
        
        # trying to retrieve password
        try:
            print "{}:{}".format(email, wordlist[password]) # hash found
        except:
            pass # hash not found
        
        line = leaks.readline() # next line
