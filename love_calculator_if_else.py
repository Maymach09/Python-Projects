print("The Love Calculator is calculating your score...")
name1 = input() # What is the first name?
name2 = input() # What is the second name?

name = name1.lower() + name2.lower()
true = 'true'
love = 'love'
true_count = 0
love_count = 0

if true[0] in name:
  true_count += (name.count(true[0]))
if true[1] in name:
  true_count += (name.count(true[1]))
if true[2] in name:
  true_count += (name.count(true[2]))
if true[3] in name:
  true_count += (name.count(true[3]))

if love[0] in name:
  love_count += (name.count(love[0]))
if love[1] in name:
  love_count += (name.count(love[1]))
if love[2] in name:
  love_count += (name.count(love[2]))
if love[3] in name:
  love_count += (name.count(love[3]))  

total = true_count*10 + love_count

if total < 10 or total > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")