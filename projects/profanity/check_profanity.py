import urllib
def read_text():
	quotes=open("/root/Desktop/projects/profanity/movie_quotes.txt")
	contents_of_file=quotes.read()
	print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)	
def check_profanity(text_to_check):
	connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output=connection.read()
	if output=='false':
		print("No profanity,good boiii")
	else:
		print("Oh damn, these profanities")
	connection.close()	
read_text()
