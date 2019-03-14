# f = open('newfile.txt', 'w')  writes new

f = open('newfile.txt', 'a')  #appends
lines = ['Hello', 'World', 'Welcome', 'To', 'File IO']
text = '\n'.join(lines)
f.writelines(text)
f.close()