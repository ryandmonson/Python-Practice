
#  This 1) orders an array alphabetically (accounting for capital 1st letters,
#  2) takes the 1st element of the array and return that element with  *** between
#  each character

my_array = ['fLEroLQX', 'BXFJ', 'gYO', 'UmWmcNo', 'biRF', 'xkxi', 'SoZuG', 'oaEomiNS']

def two_sort(my_array):
   sorted_array = sorted(my_array)
   sorted_array_string= ""
   for i in range(0,len(sorted_array[0])-1):
        sorted_array_string += sorted_array[0][i] + '***'
   return (sorted_array_string + sorted_array[0][len(sorted_array[0])-1])
print(two_sort(my_array))


#take a value and returns a list of its multiples up to another value. 
#If limit is a multiple of integer, it should be included as well. 
#There will only ever be positive integers passed into the function,
#not consisting of 0. The limit will always be higher than the base.
#if the parameters passed are (2, 6), the function should return [2, 4, 6] 
#as 2, 4, and 6 are the multiples of 2 up to 6.
#    If you can, try writing it in only one line of code.

def multiples (multiple, limit):
    myList = []
    for i in range(1,(limit-multiple)):
        if(i*multiple <= limit):
            myList.append(i*multiple)

    print(myList)
multiples (2,6)


# Convert and return USD to Yuan

def usdcny(usd):
    yuan = 6.75 * usd
    return '{:0.2f} Chinese Yuan'.format(round(yuan,2))


#Timmy & Sarah think they are in love, but around where they live, 
#they will only know once they pick a flower each. If one of the flowers 
#has an even number of petals and the other has an odd number of petals 
#it means they are in love.

#Write a function that will take the number of petals of each flower and 
#return true if they are in love and false if they aren't.

def lovefunc(flower1, flower2):
    if (flower1%2 !=0 and flower2%2 == 0 or flower1%2==0 and flower2%2 !=0):
        return True
    else:
        return False

print (lovefunc(1,2))
