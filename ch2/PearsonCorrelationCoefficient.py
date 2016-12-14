import codecs
from math import sqrt
import csv

users = {}

def loadMovieData(path = ''):
  count = 0
  reader = csv.reader(open(path))
  first_line = next(reader)

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

def manhattan (rating1, rating2):
  ''' Computes the Mahatten distance 
      Both rating1 and rating2 are dictionaries of every user's rating'''
  distance = 0;
  for key in rating1:
    if key in rating2:
      distance += abs(rating1[key]-rating2[key])
  return distance

def minkowski(rating1, rating2, r):
  # calculate minkowski distance
  distance = 0
  for key in rating1:
    if key in rating2:
      distance += pow(abs(rating1[key] - rating2[key]), r)
  return pow(distance, 1/r)

def pearson(rating1, rating2):
  productSum = 0
  xSum = 0
  ySum = 0
  xPow = 0
  yPow = 0
  count = 0

  for key in rating1:
    if key in rating2:
      count += 1
      productSum += rating1[key] * rating2[key]
      xSum += rating1[key]
      ySum += rating2[key]
      xPow += pow(rating1[key], 2)
      yPow += pow(rating2[key], 2)


  denominator = sqrt(xPow - (xSum**2) / count) * sqrt(yPow - (ySum**2) / count)
  if denominator == 0:
    return 0
  else:
    return (productSum - xSum * ySum/count) / denominator

def computeNearestNeighbor(username, users):
  # creates a sorted list of users based on their distance to username
  distance_dic = []
  for user in users:
    if user != username:
      #distance = manhattan(users[username], users[user])
      #distance = minkowski(users[username], users[user], 2)
      distance = pearson(users[username], users[user])
      distance_dic.append((distance, user))
  #sort based on distance  -- closest first
  distance_dic.sort(reverse = True)
  return distance_dic

def recommend(username, users):
  # Given list of recommendations 
  distance_dic = computeNearestNeighbor(username, users)
  distance_dic_length = distance_dic.__len__()

  count = 0
  while count < distance_dic_length:
    nearest = computeNearestNeighbor(username, users)[count][1]
    count += 1
    recommendations = []
    # now find bands neighbor rated that user did not 
    neighborRatings = users[nearest]
    userRatings = users[username]

    for movie in neighborRatings:
      if movie not in userRatings:
        recommendations.append((movie, neighborRatings[movie]))

    if recommendations != []:
      break
  # sort
  print "The recommendation is "
  return sorted(recommendations,
                key = lambda bandTuple: bandTuple[1],
                reverse = True)


loadMovieData("/Users/yuguanxu/Desktop/courses/data_mining/ch2/Movie_Ratings.csv")
print recommend("vanessa",users)










