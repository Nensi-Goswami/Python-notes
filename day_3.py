#Listing 
courses = ["History" , "math" , "physics", "Science"]
print(courses[-1])  #last number
print(courses[0:2]) #number between starting and 2 i.e excluding 2
print(courses[2:])
courses.append("Biology")   #adding to the list
print(courses)
courses.insert(0 ,"Social Studies") #inserting name in the first position we can define specific locations
print(courses)
courses_2 = ["chemistry" , "Physical Activities"]   #each items will be extended to the list. 
courses.extend(courses_2)
print(courses)
courses.remove("math")  #if course.pop is used it will delete the last member of the list. 
print(courses)
courses.pop
print(courses)


#Sorting

courses.reverse()  
print(courses)
courses.sort()#alphabetical order sorting
print(courses)
nums = [5, 2, 33, 4] 
nums.sort()
print(nums) 
print(min(nums))#when min is used it gives minimum value, similarly for maximum use max. 
print(sum(nums))
print(courses.index("physics"))#finding location in the list. 
print( "Arts" in courses)#True or false 
courses_3 = ("Cricket" , "Football" , "Baseball" , "Hockey")
for i in courses_3:
    print(i)


#Tupels are immutable(cannot change)

#Sets  get rid of duplicates

