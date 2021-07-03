import numpy as np

def preprocessingArr(arr):
  array_temp = arr.copy()
  array = [int(x) for x in array_temp]
  array.sort()
  raw_len = len(array) 
  idx = 1
  while idx < raw_len:
    if array[idx - 1] == array[idx]:
      del array[idx - 1]
      raw_len -= 1
    idx += 1
  return array

# nothing = 0, pair = 1, two pair = 2, triple = 3, four = 4, full = 5
def isNumSame(array):
  flag = 0
  is_pair = False
  is_triple = False
  temp = -1
  temp_arr = []
  for i in range(5):
    temp_arr.append(array[i]%13)
  for i in range(5):
    for j in range(i + 1, 5):
      if temp_arr[i] == temp_arr[j]:
        for k in range(j + 1, 5):
          if temp_arr[j] == temp_arr[k]:
            for l in range(k + 1, 5):
              if temp_arr[k] == temp_arr[l]:
                # fourcard
                return 4
            is_triple = True
            flag = 3
            temp = temp_arr[i]
        if temp == -1:
          # one pair
          flag = 1
          is_pair = True
          temp = temp_arr[j]

        elif is_triple and temp == temp_arr[i]:
          temp = temp_arr[j]
          if is_pair:
            # full house
            return 5

        else:
          if is_triple:
            # full house
            return 5
          # two pair
          return 2
  return flag

# nothing = 0, straight = 1, back straight = 2, mountain = 3
def isSeries(array):
  temp_arr = []
  for i in range(5):
    temp_arr.append(array[i]%13)
  
  temp_arr.sort()
  if temp_arr[0] == 0:
    if temp_arr[1] == 1:
      for i in range(2, 5):
        if temp_arr[i-1] != temp_arr[i] - 1:
          return 0
      return 3

    elif temp_arr[1] == 9:
      for i in range(2, 5):
        if temp_arr[i-1] != temp_arr[i] - 1:
            return 0
      return 2
    return 0

  else: 
    for i in range(1, 5):
      if temp_arr[i-1] != temp_arr[i] - 1:
        return 0
    return 1

# nothing = 0, flush = 1
def isFlush(array):
  for i in range(4):
    if int(array[i]/13) != int(array[i+1]/13): 
      return 0
  return 1

def pokerClassification(array):
  labels = ["Nothing", "OnePair", "TwoPair", "Triple", "Straight",
            "Backstraight", "Mountain", "Flush", "FullHouse", "FourCard", 
            "StraightFlush", "BackstraightFlush", "RoyalStraightFlush"]
  result = 0
  
  # nothing = 0, pair = 1, two pair = 2, triple = 3, four = 4, full = 5
  is_num_same = isNumSame(array)
 
  # one pair
  if is_num_same == 1:
    return labels[1]
  # two pair
  elif is_num_same == 2:
    return labels[2]
  # triple
  elif is_num_same == 3:
    return labels[3]
  # four card
  elif is_num_same == 4:
    return labels[9]
  # full house
  elif is_num_same == 5:
    return labels[8]
  
  # nothing = 0, straight = 1, back straight = 2, mountain = 3
  is_series = isSeries(array)
  # straight
  if is_series == 1:
    result = 4
  # backstraight
  elif is_series == 2:
    result = 5
  # mountain
  elif is_series == 3:
    result = 6

  # nothing = 0, flush = 1
  is_flush = isFlush(array)

  if is_flush:
    # straight flush
    if is_series == 1:
      return labels[10]
    # back straight flush
    elif is_series == 2:
      return labels[11]
    # royal straight flush
    elif is_series == 3:
      return labels[12]
    # flush
    else:
      return labels[7]

  return labels[result]
