# Dictionaries

band = {
    "vocals": "Plant",
    "guitar": "Page"
}
band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))
print(type(band2))
print(len(band2))

# Access items
print(band["vocals"])
print(band.get("guitar"))


# list all keys

print(band.keys())

# List all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# if key exist
print("guitar" in band)
print("cowbell" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())
print(band)


band2 = dict(vocals="Plant", guitar="Page")
print(band2)

band2 = band.copy()
band2["drums"] = "Rusty"
print(band)
print(band2)

# Or use the dict() constructor funtion
band3 = dict(band)
print("Good copy!")
print(band3)

# Nested dictionaries
print("****************************")
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])

# Sets
print("***********************************")
nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

nums = {1, 2, 2, 3}
print(nums)

nums = {1, True, 2, False, 3, 4, 0}
print(nums)

print(2 in nums)

# Add a new element to a set
nums.add(8)
print(nums)

morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# Merge
one = {1, 2, 3}
two = {5, 6, 7}
mynewset = one.union(two)
print(mynewset)

one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)


print("")
print("************END********************")
print("")
