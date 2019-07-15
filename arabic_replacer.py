# coding=utf-8

# ask what file you wanna to modify. The file needs to be in the same directry.
your_file = input("what file do you want to modify? :")

#reading file and put it in "data" variable.
with open(your_file, 'r') as mytext:
  data = mytext.read()

# You can add anything to the dictionary to replace.
arabic_dict = {'٠':'0',
              '١': '1',
              '٢': '2',
              '٣': '3',
              '٤': '4',
              '٥': '5',
              '٦': '6',
              '٧': '7',
              '٨': '8',
              '٩':'9'}

#replace all the keys with value in the dictionaly.
for key in arabic_dict:
  data = data.replace(key, arabic_dict[key])

# To check the data on terminal as well.
print(data)

# out put file will be named as "after" + riginal name.
new_file = open("after_" + your_file, "w+")
new_file.write(data)
new_file.close()
