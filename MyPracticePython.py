
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

# Convert and return USD to Yuan

def usdcny(usd):
    yuan = 6.75 * usd
    return '{:0.2f} Chinese Yuan'.format(round(yuan,2))
