groceries = ['bananas','strawberries','apples','bread']
addition = raw_input('type what to add to list: ')
found=True
groceries.append(addition)
print '\n\t',groceries,'\n\t'

substract = raw_input('type what you want out From the list above: ')
for c in groceries:
    if substract==c:
        groceries.remove(substract)
        print '\n\t',groceries,'\n\t'
       
search = raw_input('type what to search from store in list: ')
aisle = map(chr, range(97, 123))
for c in search:
    for i in aisle:
        if c==i:
            print 'go to aisle: ',i
            break
    break



itemPlist= {'Apple':'SPIC_APPLE','Bananas':'SPIC_BANANAS','Bread':'SPIC_BREAD',
            'Carrots':'SPIC_CARROTS','Champagne':'SPIC_CHAMPAGNE',
            'Strawberries':'SPIC_STRAWBERRIES'}

decide=raw_input('\n\n Is it winter? [1/0] ')
season = int(decide)
if season==1:
    itemPlist['Strawberries']='WPIC_STRAWBERRIES'
    print itemPlist
elif season==0:
    print itemPlist

occupation = input('\n\n are you a soccer player? [1/0] ')
if occupation==1:
    itemPlist['Chicken']= 'SPIC_CHICKEN'
    print itemPlist


print ('\n\t\tItems always in stock are as below:\n')

always_in_stock = itemPlist.keys()

neverChange = tuple(always_in_stock)
print neverChange

print ('\n\t\tthe combinations of two tuples:\n' )
firstlist=('gari','beans')
print 'first list is as : ',firstlist
secondlist=('orange',)
print '\n second list is as: ',secondlist
fullList= firstlist + secondlist[:]
print '\n Full list is as: ', fullList






