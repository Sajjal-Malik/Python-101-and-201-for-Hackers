from ctypes import *

print("--- C types Booleans ---")
b0 = c_bool(0)           # Create C boolean with value 0 (false)
b1 = c_bool(1)           # Create C boolean with value 1 (true)

print(b0)                # Print the c_bool object itself
print(b1)                # Print the c_bool object itself
print(type(b0))          # Show the type is c_bool, not Python bool
print(type(b1))          # Show the type is c_bool, not Python bool
print(b0.value)          # Access the actual boolean value (False)
print(b1.value)          # Access the actual boolean value (True)
print()

print("--- C types Integers ---")
ui0 = c_uint(-1)         # Create unsigned int, -1 wraps to max value
print(ui0)               # Print the c_uint object
print(type(ui0))         # Show type is c_uint
print(ui0.value)         # Show the actual value (4294967295 for 32-bit)
print()

print("--- C types Pointers ---")
c0 = c_char_p(b"test")   # Create pointer to immutable string
print(c0)                # Print the pointer object
print(type(c0))          # Show type is c_char_p
print(c0.value)          # Get the string value
# Changing the Value will store at different location
c0 = c_char_p(b"new_test")  # Create new pointer to new string
print(c0)                # New pointer object
print(type(c0))          # Same type
print(c0.value)          # New string value

# Creating empty pointer Variable for 'char' values with Buffer size of 5
p0 = create_string_buffer(5)  # Create mutable buffer of 5 bytes
print(p0)                # Print buffer object
print(p0.raw)            # Show raw bytes in buffer (null initialized)
print(p0.value)          # Show as null-terminated string

p0.value = b"newww"      # Assign new value to buffer
print(p0)                # Buffer object remains same
print(p0.raw)            # Raw bytes now contain "newww\0"
print(p0.value)          # String value "newww"

print("----Working with POINTER functions----")
i = c_int(42)            # Create C integer
pi = pointer(i)          # Create pointer to the integer
print(i)                 # Print the integer object
print(pi)                # Print the pointer object
print(pi.contents)       # Dereference pointer to get value

print(p0.value)          # Current string value
print(p0)                # Buffer object
print(hex(addressof(p0)))  # Get memory address of buffer

pt = byref(p0)           # Create lightweight reference/pointer
print(pt)                # Print the reference


class Person(Structure):  # Define C structure equivalent
    _fields_ = [("name", c_char_p),  # Structure field: string pointer
                ("age", c_int)]      # Structure field: integer


john = Person(b"John", 24)  # Create Person instance
print(john.name)         # Access name field
print(john.age)          # Access age field

anna = Person(b"Anna", 20)  # Create another Person instance
print(anna.name)         # Access name field
print(anna.age)          # Access age field

person_array_t = Person * 3  # Create array type of 3 Person structs
person_array = person_array_t()  # Instantiate the array

person_array[0] = Person(b"John", 34)  # Assign to first element
person_array[1] = Person(b"Nina", 23)  # Assign to second element
person_array[2] = Person(b"Jack", 40)  # Assign to third element
for person in person_array:    # Iterate through array
    print(person.name, "=>", person.age)  # Access each person's fields
