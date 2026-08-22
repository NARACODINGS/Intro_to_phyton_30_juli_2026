# Numerik
# Interger
a = 32764
print("Tipe data Interger : {0}".format(a))
# FLoat
b = 3.14
print("Tipe data Float : {0}".format(b))
# Complex
c = 5 +3j
print("Tipe data Complex : {0}".format(c))


# Squence
# List
d = [1, 2, 3, 4, 5]
print("Tipe data List : {0}".format(d))
# Tuple
e = (4, 5, 6, 7, 8)
print("Tipe data Tuple : {0}".format(e))
# Range
# Range (start, end, step)
# Range (end)
f = range(1, 10, 2)
print("Tipe data Range : {0}".format(f))

# Tipe Text
# Char / varChar
g = 'C' # tipe data Statik
print("Tipe data Char : {0}".format(g))
# String
h = "Hello Wolrd" # tipe data Dinamis
print("Tipe data String : {0}".format(h))

# Mapping
# Dictionary (Array) (dict)
profile = {"name" : "naren", "Umur" : 22}
print("Tipe data Dictionary : {0}".format(profile))

# Boolean
# bool : True (1) / False (0)
i = True
print("Tipe data Boolean : {0}".format(i))

# Set
j = {1,2,3,4,5}
print("Tipe data Set : {0}".format(j))
#FroenSet
k = frozenset({1,2,3,4,5,6,7}) # atau bisa k = forzenset(J) saja
print("Tipe data Frozenset : {0}".format(k))

# Binary
l = 0b01000010
# casting
#Cra kurang Tepat
desimal = int(l)
char = chr(desimal)
#Cara tepat
char = chr(int(l))
print("Tipe data Binary : {0}".format(l))
print("Tipe data Desimal : {0}".format(desimal))
print("Tipe data Char : {0}".format(char))