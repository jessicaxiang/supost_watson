import csv
import urllib

def main():

	with open('negative_2.csv', 'rb') as f:
		reader = csv.reader(f)
		ids = list(reader)
		
		for x in range(1,100):
			url = "http://supost-prod.s3.amazonaws.com/posts/" + ids[x][0][:-1] + "/post_" + ids[x][0]
			urllib.urlretrieve(url, "negative2/" + ids[x][0] + ".jpg")

main()