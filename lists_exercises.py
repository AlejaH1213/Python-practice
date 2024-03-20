# creating a list
guests = ['Jenny', 'Aj', 'Janet', 'Phil', 'Caro', 'Phillip', 'Casey', 'Gaby']
# printing invitations
print(f"{guests[0]}, I would love to have you at my party")
print(f"{guests[1]}, I would love to have you at my party")
print(f"{guests[2]}, I would love to have you at my party")
print(f"{guests[3]}, I would love to have you at my party")
print(f"{guests[4]}, I would love to have you at my party")
print(f"{guests[5]}, I would love to have you at my party")
print(f"{guests[6]}, I would love to have you at my party")
print(f"{guests[7]}, I would love to have you at my party")
# pretending someone cant make it
print(f"it looks like {guests[7]} cant make it to the party!")
# replacing gaby with andrea
guests[7] = 'Andrea'
# printing a new invitation
print(f"{guests[7]}, I would love to have you at my party")
# i found a bigger table so more people can come!
print("Guys dont worry I found a bigger table")
# adding three guests more in different positions, using insert for specific indexes
guests.insert(0, 'Alex')
guests.insert(4, 'Illary')
# using append to add to the end of the list
guests.append('Ari')
print(f"{guests[0]}, I would love to have you at my party")
print(f"{guests[1]}, I would love to have you at my party")
print(f"{guests[2]}, I would love to have you at my party")
print(f"{guests[3]}, I would love to have you at my party")
print(f"{guests[4]}, I would love to have you at my party")
print(f"{guests[5]}, I would love to have you at my party")
print(f"{guests[6]}, I would love to have you at my party")
print(f"{guests[7]}, I would love to have you at my party")
print(f"{guests[8]}, I would love to have you at my party")
print(f"{guests[9]}, I would love to have you at my party")
print(f"{guests[10]}, I would love to have you at my party")
#sorry guys i can only have two people now
print('sorry guys only two guests now!')
# removing using the pop method
first_elimination = guests.pop(0)
print(f"sorry! {first_elimination}")
second_elimination = guests.pop(3)
print(f"sorry! {second_elimination}")
third_elimination = guests.pop(4)
print(f"sorry! {third_elimination}")
fourth_elimination = guests.pop(5)
print(f"sorry! {fourth_elimination}")
fifth_elimination = guests.pop(6)
print(f"sorry! {fifth_elimination}")
sixth_elimination = guests.pop(2)
print(f"sorry! {sixth_elimination}")
seventh_elimination = guests.pop(3)
print(f"sorry! {seventh_elimination}")
eight_elimination = guests.pop(2)
print(f"sorry! {eight_elimination}")
nine_elimination = guests.pop(2)
print(f"sorry! {nine_elimination}")
# removing using del 
del guests[0]
del guests[0]
print(guests)
#==============================================================================================


#==============================================================================================
places_to_visit = ['Bali', 'Italy', 'France', 'Argentina', 'Bahamas']
#printing the list
print(places_to_visit)
# printing the list sorted
print(sorted(places_to_visit))
print(places_to_visit)
# printing the list in reverse aphabetical order using reverse
print(sorted(places_to_visit, reverse=True))
print(places_to_visit)
# reversing the order permanently with reverse
places_to_visit.reverse()
print(places_to_visit)
# reversing the order again
places_to_visit.reverse()
print(places_to_visit)
# changing the order wit sort
places_to_visit.sort()
print(places_to_visit)
# changing the order to reverse aphabeticall 
places_to_visit.sort(reverse= True)
print(places_to_visit)
# checking the len of a list
print(len(places_to_visit))
#==============================================================================================


#==============================================================================================
slice_practice = ['lana', 'petra', 'tinder', 'mouse', 'chili', 'pandora']
# to slice the first three items in the list
print('the first three items in the list are:', slice_practice[:3])
# to slice the two items in the middle
print('two items from the middle', slice_practice[2:4])
# the slice the last three items in the list
print('the last three items are', slice_practice[-3:])
#to make a copy of a list 
practice_copy = slice_practice[:]
#adding something to the original list
slice_practice.append('Tico')
#adding something to the copy list
practice_copy.append('bucky')
#prove that i have different lists
print('my pets names are:')
for pet in slice_practice:
  print(pet)
print('\nthe copy list has these pets')
for copy in practice_copy:
  print(copy)

