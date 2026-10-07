id1 = {
  "one": 1,
  "two": 2,
  "three": 3
}

id2 = {
  "four": 4,
  "five": 5
}

print(id1)

id1.update(id2)

print(id1)

print(f"the total ids sum is : {id1["one"] + id1["two"] + id1['three']}")