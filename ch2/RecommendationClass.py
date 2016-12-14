import codecs
from math import sqrt
import csv

users = {}

def loadMovieData(path = ''):
	count = 0
	reader = csv.reader(open(path))
	first_line = next(reader)
	users = {}

	for ele in first_line:
		if ele != '':
			users[ele] = {}
	for line in reader:
		count = 1
		for rater in users:
			if line[count] == '':
				continue
			else:
				users[rater][line[0]] = int(line[count])
			count += 1
	print users



	







loadMovieData("/Users/yuguanxu/Desktop/courses/data_mining/ch2/Movie_Ratings.csv")



		
		