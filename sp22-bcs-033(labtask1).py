#String Operations:
#slicing:
string1 = "programming is fascinating"
print(string1[2:14])         # Slice from index 3 to 11
string2 = "exploring the unknown"
print(string2[5:]) 
string3 = "coding challenges"
print(string3[-10:-5])  

#concatenation:
text1 = "coding is"
text2 = "a creative process"
combined_text = text1 + " " + text2  # Add space between text1 and text2
print(combined_text)

#accessing individual characters.
sentence_x = "programming is an art"
sentence_y = "It requires creativity and logic"
# Accessing individual characters
first_char_x = sentence_x[0]
last_char_y = sentence_y[-1]
print("First character of x:", first_char_x)
print("Last character of y:", last_char_y)
#single,double,triple quotes
#no differnece between single and double quote string
quote1 = 'coding is fun'         #single quote
print(quote1)
quote2 =  "python is amazing"       
print(quote2)
quote3 = '''Learning to code  
opens new horizons
in technology.'''
print(quote3)            

#Type Casting:
#Float to int
float_number = 9.75
integer_number = int(float_number)
print("Float to int:", integer_number)
#Int to str
int_num = 28
str_num = str(int_num)
print("Integer to str:", str_num)

#Str to int
str_num = "456"
int_num=int(str_num)
print("String to int:", int_num)
#str to float
str_float = "2.718"
float_from_str = float(str_float)
print("String to float:", float_from_str)

#Formatted Strings (F-strings):
product_name ="laptop"
product_price = 1200
product_height = 1.5
formatted_description = f"The product is {product_name}. It costs {product_price} and has a height of {product_height} meters."
print(formatted_description)

#Lists:
#Lists are used to store multiple items in a single variable.

items_list1=["pen", "book", "notebook", "pencil","ruler"]
print(items_list1)
print(items_list1[2])                   
items_list1[2] = "tablet"
print(items_list1)                        
items_list1.append("calculator")
print(items_list1)                        #add item in list
items_list1.insert(1,"marker")
print(items_list1)                        #insert item at specific index

#extend
items_list2 = ["grape", "kiwi", "melon" ,"strawberry"]
items_list1.extend(items_list2)
print(items_list1)                      #add items of items_list2 in items_list1

items_list1.remove("notebook")
print(items_list1)                     #remove item from list


#sets:
set_A= {1, 2, 3, 4, 5}
set_B={3, 4, 5, 6, 7,8}
print("Set A:", set_A)
print("Set B:", set_B)
#union
union_set=set_A.union(set_B)
print("Union of Set A and Set B:", union_set)
#intersection
intersection_set=set_A.intersection(set_B)
print("Intersection of Set A and Set B:", intersection_set)
# Difference between sets
difference1= set_A.difference(set_B)
difference2= set_B.difference(set_A)
print("Difference of Set A from Set B",difference1)
print("Difference of Set B from Set A",difference2)

#tuples
#Tuple items are ordered, unchangeable, and allow duplicate values.
tuple1=("banana",)
print(type(tuple1))

#NOT a tuple
tuple1=("banana")
print(type(tuple1))

#unlike list tuples have items with different data types
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
#Tuples are preferred over lists in scenarios where immutability and integrity of data are important
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


# Dictionaries in Python
# Storing information about vegetables using dictionaries
vegetables_data = {
    'Carrot': 'Orange',
    'Broccoli': 'Green',
    'Tomato': 'Red',
    'Eggplant': 'Purple',
    'Lettuce': 'Green'
}
print("Original Vegetables Data:")               # Displaying the original data
for veggie, color in vegetables_data.items():
    print(f"{veggie}: {color}")

# Adding a new vegetable
vegetables_data['Cucumber'] = 'Green'

# Updating an existing vegetable's color
vegetables_data['Tomato'] = 'Red and Green'

# Displaying the updated data
print("\nUpdated Vegetables Data:")
for veggie, color in vegetables_data.items():
    print(f"{veggie}: {color}")

# Retrieving information about a specific vegetable
veggie_name = 'Broccoli'
broccoli_color = vegetables_data.get(veggie_name, "N/A")
print(f"\n{veggie_name}'s Color: {broccoli_color}")

#Deterministic and Non-Deterministic Loops:
'''
Deterministic Loops:
In a deterministic loop, the behavior is entirely predictable based on the initial conditions and the input parameters.
Given the same initial state and input, a deterministic loop will always produce the same result.
Examples of deterministic loops include traditional for and while loops where the loop control variable and conditions are well-defined and predictable.
'''
'''
Non-Deterministic Loops:
In a non-deterministic loop, the behavior is not entirely predictable based on the initial conditions and inputs.
The loop may produce different results for the same initial conditions and inputs, introducing an element of randomness or uncertainty.
Non-deterministic loops are often associated with probabilistic algorithms or scenarios where the order of execution is not guaranteed.
Example of a non-deterministic loop (Python while loop with a random condition)
'''


