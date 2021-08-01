with open('text.txt', 'w', encoding='utf-8' ) as newfile:
   contents = newfile.write("Python is the best programming language for me.\n")
   contents = newfile.write("Python For Professional.\n")

print(contents)


# simple writing and save program.

expression = True

while expression:

   try:
      user_input = input("Type somethings: ")
      if user_input == 'quit':
         expression = False
         print('program finished!')
         break
   
   
      with open('text.txt', 'at', encoding='utf-8') as textFile:
         newContent = textFile.write(f"{user_input}\n")
         #newContent = textFile.read()

         print(newContent)

   except KeyboardInterrupt:
      print('error')

      
