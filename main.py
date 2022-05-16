
#Aufgabe 1
def transform_to_row(infile, outfile='placeholder'):
    with open(infile, 'r') as txt:
        mfile = txt.readline()
        contents = mfile.split(',')
        for word in contents:
            print(word, end='\n')

    with open(outfile, 'w+') as writer:
        for word in contents:
            writer.write(word + '\n')


#Aufgabe 2
def add_greeting(infile, outfile='placeholder'):
    with open(infile, 'r') as txt:
        mfile = txt.readlines()
        for line in mfile[:-1]:
            print('Hello ' + line)

    with open(outfile, 'w+') as writer:
        for line in mfile[:-1]:
            writer.write('Hello ' + line)


#Aufgabe 3
def strip_greeting(infile, outfile='placeholder'):
    with open(infile, 'r') as txt:
        mfile = txt.readlines()
        for line in mfile:
            print(line[6:])

    with open(outfile, 'w+') as writer:
        for line in mfile:
            writer.write(line[6:])


#Aufgabe 4
def combine_files(file1, file2, outfile='placeholder'):
    with open(file1, 'r') as f1:
        mfile1 = f1.readlines()

    with open(file2, 'r') as f2:
        mfile2 = f2.readlines()

    print(len(mfile2))

    with open(outfile, 'w+') as writer:

        line_count = 0

        while line_count <= len(mfile2):

            for line in mfile1:
                print(line + mfile2[line_count])
                writer.write(line.rstrip('\n') + ' ' + mfile2[line_count])
                line_count += 1


#calling each function
transform_to_row("text.txt", 'rowtext.txt')
add_greeting('rowtext.txt', 'greeting.txt')
strip_greeting('greeting.txt', 'no_greets.txt')
combine_files('rowtext.txt', 'greeting.txt', 'combined.txt')
