################################################
#             Stephen Bridgett                 #
#              Searching Lists                 #
################################################

def search_sorted_list(sorted_list, item):                            #Algorithm works as follows:
    first = 0                                                         #It returns the index of the current element. If the desired element being searched for is not present it will return '-1'
    last = len(sorted_list)-1                                         #Then is goes and searches through the left half of the array
    index = -1                                                        #Then it does the same for the right half of the array
    while (first <= last) and (index == -1):                          #There can be only one iteration at a time and the pool of matches gets divided by 2 within every iteration. 
        mid = (first+last)//2                                         #This makes my time complexity for the binary search O(log n).
        if sorted_list[mid] == item:                                
            index = mid
        else:
            if item<sorted_list[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

print("---------------- #1 ------------------")
sortedList = [0, 1, 4, 6, 7, 11, 14, 17, 19, 21, 25, 27, 28, 29]  
print(search_sorted_list(sortedList, 4))                               #
print(search_sorted_list(sortedList, 6))                               #
print(search_sorted_list(sortedList, 12))                              #
print(search_sorted_list(sortedList, 15))                              #testing the search_sorted_list method
print(search_sorted_list(sortedList, 20))                              #
print(search_sorted_list(sortedList, 24))                              #
print(search_sorted_list(sortedList, 29))                              #
print()



class HashList:                                                        #creates the hashlist class
    def __init__(self):                                                #initializes needed attributes
        self.size = 19                                                 #hashlist size is 19
        self.slot = [None] * self.size                                 #initialize self.slot

    def HashList(self, length):                                        #function that creates a hashlist
        length = self.size                                             #length initialized as the size of hash
        mylist = HashList(length)
        
    def hashFunction(self, item):                                      #function that determines which slot to place the item in
        hash = 0                                                       
        for pos in range(item):                                        #In order to find the position in the table,
            hash += item                                         
        return hash % self.size                                        #use the position given from the modulous of the item divided by the size of the list

    def rehash(self,item):                                             #rehash function made for put function
        return (item+1)%self.size                                      #returns the modulous of the (item+1) divided by hashlist size

    def put(self, item):                                               #put function that places items in the hashlist
        itemHash = self.hashFunction(item)                             #itemHash calls back to the original hashFunction

        if self.slot[itemHash] == None:                                #if the slot is empty,
            self.slot[itemHash] = item                                  #place that item in that slot
        else:                                                          #Or if the current slot is not empty,
            newSlot = self.rehash(item)                                 #newSlot initialized as the rehash function
            while self.slot[newSlot] != None:                           #while the slot is not empty,
                newSlot = self.rehash(item)                              #run through the hashFunction, but adding one beforehand this time(rehash)
            if self.slot[newSlot] == None:                              #If the next slot is empty,
                self.slot[newSlot] = item                                #place that item in the next slot
            else:                                                       #if there are no more empty spots,
                print("Error. This list is already full.")               #print an error

    def contains(self, item):                                          #contains function that sees if an item is in the list
         found = False                                                 #found is initiallized as false
         itemHash = self.hashFunction(item)                            #itemHash calls back to the original hashFunction
         if self.slot[itemHash] == item:                               #if the slots contains the item,                                
             found = True                                               #found is set to true
         if self.slot[itemHash] != item:                               #if the slots do not contain the item,
             found = False                                              #found is set to false
         return found                                                  #return the verdict

    def items():                                                       #function that prints the list
        return mylist
        
print("---------------- #2 ------------------")                        #
mylist = HashList()                                                    #
print(mylist.hashFunction(20))                                         #
mylist.put(41)                                                         #
mylist.put(67)                                                         #
mylist.put(2)                                                          #
mylist.put(32)                                                         #places new numbers into list and then checks if
mylist.put(53)                                                         #  certain numbers are now included or not
mylist.put(123)                                                        #
mylist.put(43)                                                         #
print(mylist.contains(41))                                             #
print(mylist.contains(32))                                             #
print(mylist.contains(34))                                             #
print()                                                                #


############################################################################################                
#When it comes to running times when using the hash list methods, the best-case scenario   #
#would be when there are no collisions occurring and would lead to a constant running time.#
#In the worst case scenario, many collisions would occur which would make the running time #
#linear compared to the collsions that are occuring.                                       #
############################################################################################



############################################################################################                
#In order to turn our hash list into a dictionary, we would have to go back and modify the #
#hash list to give a corresponding item to each of the integers being added. Most of the   # 
#functions would need to have two inputs, instead of just one. Implemented below is a      #
#proper working hash list that has been turned into a dictionary.                           #
############################################################################################

class HashTable:                                                            #This class creates and outputs HashTable based on the data input
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size
        #Sets Every Cell Equal to None

    def getHash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
    #Calculates index for key and returns the index

    def add(self, key, value):
        key_hash = self.getHash(key)
        #Index value it is placed in
        key_value =[key, value]
        #constructing a key and a list from the value that was passed in

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
                self.map[key_hash].append(key_value)
                return True

    def get(self, key):
        key_hash = self.getHash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
            return None

    def delete(self, key):
        key_hash = self.getHash(self)

        if self.map[key_hash] is None:
            return False
        for i in range (0, len(self.map[key_hash])):
            #need index in order to remove something in the list in python
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print()
        print('---Age---')
        for item in self.map:
            if item is not None:
                print(str(item))
                
print("---------------- #3 ------------------")                     #Adds name and age data into the HashTable
h = HashTable()                                                     # as well as retrieves data specific to one person
h.add('Jane', '23')
h.add('Alex', '50')
h.add('Joe', '5')
h.add('Sally', '16')
h.add('Mason', '14')
h.add('Meg', '74')
h.add('Siri', '37')
h.add('Jason', '18')
h.add('Mia', '89')
h.add('Sara', '20')
h.print()
h.delete('Jane')                                                    #HELP - Is this call to action doing anything??
h.print()
print('Meg: ' + h.get('Meg'))
print()


                

def sort_list(MyList):                                                #function that sorts a list
    for slot in range(len(MyList)-1,0,-1):                            #for a slot in the list,
        posOfMax = 0                                                   #initialize the highest number to be in the first slot
        for location in range(1,slot+1):                               #for loop that keeps the highest number at the end of the list and works down until the whole list is done
            if MyList[location] > MyList[posOfMax]:                      
                posOfMax = location

        sort = MyList[slot]
        MyList[slot] = MyList[posOfMax]
        MyList[posOfMax] = sort

print("---------------- #4 ------------------")        
MyList = [23, 3, 54, 12, 34, 25, 56, 80, 68, 37, 76, 16, 21, 42, 39]  #creates a list with 15 items
sort_list(MyList)                                                     #calls the function to sort the list
print(MyList)                                                         #prints the new sorted list

################### Sources #########################
#                 youtube.com                       #
#              stackoverflow.com                    #
#Problem Solving with Algorithms and Data Structures#
#####################################################













