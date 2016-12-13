from math import sqrt

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

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



#print manhattan(users["Hailey"], users["Veronica"])

def computeNearestNeighbor(username, users):
  # creates a sorted list of users based on their distance to username
  distance_dic = []
  for user in users:
    if user != username:
      #distance = manhattan(users[username], users[user])
      distance = minkowski(users[username], users[user], 2)
      distance_dic.append((distance, user))
  #sort based on distance  -- closest first
  distance_dic.sort()
  return distance_dic

def recommend(username, users):
  # Given list of recommendations 
  nearest = computeNearestNeighbor(username, users)[0][1]
  recommendations = []
  # now find bands neighbor rated that user did not 
  neighborRatings = users[nearest]
  userRatings = users[username]

  for band in neighborRatings:
    if band not in userRatings:
      recommendations.append((band, neighborRatings[band]))
  # sort 
  return sorted(recommendations,
                key = lambda bandTuple: bandTuple[1],
                reverse = True)


print recommend("Hailey",users)






