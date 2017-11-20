import os




#parameters
CLIENT = 'cliente1'
APP = 'app1'

dirs_to_create = ['dirb','wordlists-custom','nikto','dnsmap'] #en wordlist-custom se tiraria html2dict file*.html 
for dir in dirs_to_create:
	os.makedirs(CLIENT+'/'+APP+'/'+dir)

