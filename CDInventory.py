#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# MBailey, 02-18-2020 Created File and Converted Lists to Dictionaries
# MBailey, 02-19-2020 Added Deletion and Loading Data Options
# MBailey, 02-23-2020 Added some comments
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts - COMPLETE
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file name
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':    
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data - COMPLETE
        print('Loading data from file...\n')
        objFile = open(strFileName, 'r')
        for row in objFile:
                lstRow = row.strip().split(' | ')
                dicRow = {'ID': lstRow[0], 'title': lstRow[1], 'artist':lstRow[1]}
                lstTbl.append(dicRow)
        objFile.close()
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        dicRow = {'ID': strID, 'title': strTitle, 'artist': strArtist}
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID | CD Title | Artist')
        for row in lstTbl:
            print(*row.values(), sep = ' | ')   #Updated to only print each dictionary value, asterisk unpacks each item from list of values 
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry - COMPLETE
        deleteChoice = None
        while deleteChoice == None:
            deleteChoice = input('Would you like to delete based on ID or CD title? Enter ID or CD: ').lower()
            if deleteChoice == 'id':
                idChoice = input('Enter the ID of the CD you would like to delete: ')
                idFound = False      #using a flag to mark whether or not ID was found
                for i in range(len(lstTbl)):    #this works better than "for row" loop, since it is required to go through each row in order
                    if lstTbl[i]['ID'] == idChoice:
                        lstTbl.remove(lstTbl[i])
                        print('CD #', idChoice, ' has been deleted.')
                        idFound = True
                        break
                if idFound == False:
                    print('CD with ID #', idChoice, 'was not found.')
            elif deleteChoice == 'cd':
                cdChoice = input('Enter the Title of the CD you would like to delete: ')
                cdFound = False     #using a flag to mark whether or not CD was found
                for i in range(len(lstTbl)):    
                    if lstTbl[i]['title'].lower() == cdChoice.lower():
                        lstTbl.remove(lstTbl[i])
                        print(cdChoice, ' has been deleted.')
                        cdFound = True
                        break
                if cdFound == False:
                        print(cdChoice, ' was not found.')
            else:
                print('Invalid input. Please enter \'ID\' or \'CD\'.')
                deleteChoice = None
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row.values():   #Updated to only loop through items in the dictionary's values
                strRow += str(item) + ' | '   #str function not really needed since input() automatically creates string objects
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        print("Data saved to file.")
    else:
        print('Please choose either l, a, i, d, s or x!')

