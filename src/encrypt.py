from hashlib import md5


with open("wordlist/wordlist.txt", "r") as wl:
	
	with open("wordlist/wordlist_md5.txt", "w") as wl_md5:
			
		line = wl.readline().strip()
		
		while line:
			
			digest = md5(line).hexdigest()
				
			wl_md5.write("{} {}\n".format(digest, line))
			
			line = wl.readline().strip()
