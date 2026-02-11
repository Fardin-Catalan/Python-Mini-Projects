name=input('Enter your name:')
print('\n**Welcome to the 99 bottles of beer song classic program '+name+' !**')
for i in range(99,0,-1):
    a = "bottle" if  i==1 else "bottles"
    b = "bottle" if (i-1) == 1 else "bottles" 




    print(str(i) + " "+ a + ' of beer on the wall, ' + str(i) + " " + a + ' of beer')




    if i!=1:
      print('\nTake one and pass it around,now there are ' + str(i-1)+' '+ b +'on the table')
    else:
      print('\nTake one and pass it around,now there are no more bottles left')
  
#final message:
print("\nThanks for enjoying the 99 bottles of beer song")
