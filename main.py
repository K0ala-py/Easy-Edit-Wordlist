def commands():
  print('COMMANDS: ')
  print('''
  ---> [-e <char or word>] = inserts character at the end of each word
  ---> [-s <char or word>] = inserts character at the beginning of each word
  ---> [-m <char or word>] = inserts character in the center of each word
  ---> [-r <char_old = char_new>] = replicates the old character with a new one in each word
  ---> [-n <range>] = range of numbers after each word
  ---> [-ns <range>] = range of numbers at the beginning of each word

  ---> [-q] QUIT
  ''')


def main(one):  

  if one:
    commands()
  print('')
  command = input('COMMAND ----> ')

  file = open(f'{name}','r')
  wordlist = []
  
  # -e COMMAND
  if command == '-e':

    char = input('INSERT ----> ')
    for word in file:
      wordlist.append(word.replace('\n',char+'\n'))
        
    file = open(f'{name}','w')
    for word in wordlist:
      file.write(str(word))
    file.close()

  # -s COMMAND
  if command == '-s':

    char = input('INSERT ----> ')
    for word in file:
      wordlist.append(word.replace(word,char+word))
        
    file = open(f'{name}','w')
    for word in wordlist:
      file.write(str(word))
    file.close()


  # -m COMMAND
  if command == '-m':
      
    char = input('INSERT ----> ')
    for word in file:
      lunghezza = len(word)    
      number = int(lunghezza/2)
      wordlist.append(word[:number] + char + word[number:])
      
    file = open(f'{name}','w')
    for word in wordlist:
      file.write(str(word))
    file.close()

  # -r COMMAND
  if command == '-r':
      
    old = input('INSERT OLD ----> ')
    new = input('INSERT NEW ----> ')
      
    for word in file:
      wordlist.append(word.replace(old,new))

    file = open(f'{name}','w')
    for word in wordlist:
      file.write(str(word))
    file.close()


  # -n COMMAND
  if command == '-n':

    a = int(input('FROM ----> '))
    b = int(input('TO  ----> '))

    for word in file:
      for i in range(a,b):
        wordlist.append(word.replace('\n',str(i)+'\n'))

    file = open(f'{name}','w')
    for word in wordlist:
      file.write(str(word))
    file.close()


  # -ns COMMAND
  if command == '-ns':
    
    a = int(input('FROM ----> '))
    b = int(input('TO  ----> '))

    for word in file:
      for i in range(a,b):
        wordlist.append(word.replace(word,str(i)+word))

    file = open(f'{name}','w')
    for word in wordlist:
      file.write(str(word))
    file.close()

  # -q COMMAND
  if command == '-q':
    quit()
  one = False

name = input('File wordlist: ')
c = 0
while True:    
  if c == 0:
    main(one=True)
  c += 1
  if c != 0:
    main(one=False)
