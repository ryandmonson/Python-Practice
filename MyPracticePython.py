
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

#Complete the function that takes two integers(a, b, where a < b) and return
#an array of all integers between the input parameters, including them.



# Convert and return USD to Yuan

def usdcny(usd):
    yuan = 6.75 * usd
    print ('{:0.2f} Chinese Yuan'.format(round(yuan,2)))
    return yuan
usdcny(1)


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

print((lovefunc(1,2)))

# Create a function that accepts 2 string arguments and returns 
# an integer of the count of occurrences the 2nd argument is found in the first one.

def string_char (string,char):
    count = 0
    for i in string:
        if i == char:
            count += 1
    return count
print(string_char(" ", "l"))


#Given 2 strings, a and b, return a string of the form short+long+short, 
#with the shorter string on the outside and the longer string on the inside. 
#The strings will not be the same length, but they may be empty ( zero length ).

def shortlong (a,b):
    if (len(a) > len(b)):
        return (b + a + b)
    return (a + b + a)
print(shortlong("1", "22"))
#You will be given an array a and a value x.
#All you need to do is check whether the provided array 
#contains the value.Array can contain numbers or strings. 
#X can be either.Return true if the array contains the value, 
#false if not.

def Check (a,x):
    if x in a:
        return True;
    else:
        return False;
print(Check([66,111],67))
