# tuples
my_tuple = (1, 2, 3, 4, 6)
#my_tuple[1] = 8 # gives error because tuples are immutable
print(my_tuple[:3])
print(my_tuple[1:3])

tuple2 = ("spoo", 1, 2, "keer")
tuple3 = my_tuple + tuple2
print(tuple3)

#Set Operations
fruits_sets = {"apple", "banana", "watermelon"}
fruits_friends = {"banana", "guava","apple", "mango"}
print(fruits_sets | fruits_friends)# union
print(fruits_sets & fruits_friends)# intersection
print(fruits_sets - fruits_friends)# difference which gives elements in fruits_sets but not in friends
print(fruits_friends - fruits_sets) # gives elements in fruits_friends but not in fruits_sets
print(fruits_sets ^ fruits_friends) # gives elements in either fruits_sets or fruits_friends but not in both
fruits_sets.add("mustard")
fruits_sets.remove("apple")
fruits_sets.discard("watermelon")
print(fruits_sets)

s = [1, 2, 3, 4, 5,]
s2 = set(s)
s3 = tuple(s)
print(s2, s3)
