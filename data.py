# loading the data into file
data_dir = 'Black_Mirror_3x04_-_San_Junipero.txt'

with open(data_dir) as f:
    data = f.read()
    
data = data[81:].lower()

# seperate the punchuations from the words
punch = ['.', '[', ']', '(', ')', ';', ':', "'", '/', '"', ',', '?', '*', '!', '-', '$', '%', '&', '\n']

for i in punch:    
    data = data.replace(i, ' ' + i + ' ')
    
data = data.replace('\n', '<NEWLINE>')
