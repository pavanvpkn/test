#assignment
#assign single value to multiple variables
a=b=c=100

print(a)
print(b)
print(c)


#assign multiple values to multiple variables

a,b,c=1,5.5,"pavan"
print(a,b,c)



#tokens
#a.keywords
#b.identifiers
# identifier is a variable name
# identify a variable--> function name,class name,module name or other object name
#
#
# myVariable
# variable_1
#variable_for_print

#variable1--> is a valid
#1variable --> is not valid
#c.literals
#variable__ name="PAVAN"   --string literal identifier

age=10

#d.operator

#+,_,/,*,


a=1
b=4

print(a+b)
print(a-b)
print(a*b)
print(a/b)




#constants
age =10  #variable

PI=3.14 #PI constant

GRAVITY=9.8













#strings:

#a='me to'

#a[1]='y' #it will show error ,because of we cant able to change.


#local scope

#def some_function(TestMode):
    #TestMode=False


#print(TestMode)
#some_function()


# for i in range(1,11):
#     test_scope='variable inside for loop'
#
# print(test_scope)
#
#
# is_python_awesome=True
#
# if is_python_awesome:
#     test_scope="python awesome"
# print(test_scope)
#
# TestMode=True
# def some_function():
#     global TestMode
#     TestMode=False
# some_function()
# print(TestMode)

# y='Abc'
# print(y[:2])
# print(y[1:])
# print(y[:-2])
# print(y[-2:])


# x = 'abc'
# x= x[::-1]
# print(x)

# y='abc'
# print(y[:-1])


y = 'abc'
print(y[0])
print(y[-len(y)])


name = 'farhad'
index = name.find('r')
print(index)

name = 'farhad'
index = name.find('a', 2)
print(index)


a=1
b=float(a)
print(b)

print(tuple([1,2,3]))
print(list((1,2,3)))



a={1,2,3,4,5}
b={3,4,6,7}
c=a.intersection(b)
print(c)


a={1,2,3,4,5}
b={3,4,6,7}
c=b.difference(a)
print(c)


a={1,2,3,4,5}
b={3,4,6,7}
c=a.union(b)
print(c)

x='no'
if x=='Yes':
    print('njb')
else:
    print('bgb')


# var_one = 123
# def func_one(var_one):
#     c_one(var_one):
#     var_one = 234
#     var_three = 'abc'
#
#
# var_two = 456
#
#
# def func_two():
#     print(var_three)
#
#
# func_one(var_one)
# func_two()
# print(dir())
# var_one = 234
#     var_three = 'abc'
# var_two = 456
# print(dir())var_one = 123
# def fun



var_one = 123
def func_one(var_one):
    var_one = 234
    var_three = 'abc'
var_two = 456
def func_two():
    var_four = 123
    print(dir())
func_two()
#
# variable1 = 1
# variable2 = "abc"
# variable3 = (1,2)
# variable4 = ['a',1]
# #Print their Ids
# print('Variable1: ', id(variable1))
# print('Variable2: ', id(variable2))
# print('Variable3: ', id(variable3))
# print('Variable4: ', id(variable4))
#
# variable5 = variable1
# variable6 = variable4
# print('Variable1: ', id(variable1))
# print('Variable4: ', id(variable4))
# print('Variable5: ', id(variable5))
# print('Variable6: ', id(variable6))
#
#
# print('Variable1: ', id(variable1))
# variable1 = 2
# print('Variable1: ', id(variable1))
#
#
#
#
# #********
#
#
# print('Variable6: ', id(variable6))
# variable6.append('new')
# print('Variable6: ', id(variable6))
#
#
#
# def update_variable(variable_to_update):
#   print(id(variable_to_update))
#
# update_variable(variable6)
# print('variable6:',id(variable6))
#
#
#
# variable6 = [’newrg']
# print(’Variable6:',id(variable6))
# def update_variable(variable_to_update):    variable_to_update.append(’inside’)
# update_variable(variable6)
# print('Variable6: ', variable6)
#
#
#
# print('Variable6: ', variable6)
# def update_variable(variable_to_update):
#     print(id(variable_to_update))
#     variable_to_update = ['inside']
# update_variable(variable6)
# print('Variable6: ', variable6)
#


#
# variable_nine = "a"
# variable_ten = "a"
# print('Variable9: ', id(variable_nine))
# print('Variable10: ', id(variable_ten))
#


variable_nine = "a"*21
variable_ten = "a"*21
print('Variable9: ', id(variable_nine))
print('Variable10: ', id(variable_ten))