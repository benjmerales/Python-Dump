x = 2
y = 2
n = 2


#print([i,j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n ))

#list1 = [i for i in range(6)]
list2 = [ [i,j] for i in range(x+1) for j in range(y+1) if( (i+j) != n )] 
print(list2)
