import csv
import urllib

def main():

	with open('../bikes_subcat_4.csv', 'rb') as f:
		reader = csv.reader(f)
		ids = list(reader)
		
		for x in range(1,100):
			# url = "http://supost-prod.s3.amazonaws.com/posts/" + ids[x][0][:-1] + "/post_" + ids[x][0]
			url = ids[x][0]
			urllib.urlretrieve(url, "../bikes/" + ids[x][1] + ".jpg")

main()