usernames = ['admin', 'aleja', 'billy', 'lana', 'tinder', 'petra']

if usernames:
  for username in usernames:
    if username == 'admin':
      print(f"Hello {username}, would you like to see a status report?")
    else:
      print(f"Hello {username}!")
else:
  print("we need more users!")

current_users = ['Billy', 'Aleja', 'Calvin', 'Silvana', 'Jenny', 'Aj']
new_users = ['Caro', 'Jenny', 'Aj', 'Janet', 'Natalie']

for new_user in new_users:
  if new_user in current_users:
    print(f"sorry {new_user}, you need a different name")
  else:
    print("username is available!")