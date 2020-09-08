from samwise import pb  # Print with Break
import os

# String Formatting

names = ["Sam", "Tom", "Dick", "Harry", "Jeff", "Wilbur"]
pb()

for name in names:
    print("1 Hello there, " + name + "!")
    print(" ".join(["2", "Hello there,", name + "!"]))
    print("<------------------>")

# Function join()
# joins all the items in a list and separates them with a ", "
# creating single string of all the items in the list
pb("", "(names) List into 1 string: ")
print(", ".join(names))

location_of_files = "/Users/samwiseaaron/PycharmProjects/pythonDeveloper"
file_name = "example.txt"

full_file_path = location_of_files + "/" + file_name

pb(full_file_path)

with open(os.path.join(location_of_files, file_name)) as f:
    f_read = f.read()  # Returns the entire file, each line separated by \n (new line)
    f_items = f_read.split("\n")  # Creates and fills a list object with item determined by separator
    pb(f_read, "Entire File Data")
    print("<--- List created by file using split() function --->")
    print(f_items)

pb("", "Formatting")

who = "Gary"
how_many = 12

# Format desired: "Gary bought 12 apples today!"

print("1:", who, "bought", str(how_many), "apples today!")
print('2: {} bought {} apples today!'.format(who, how_many))
print('3: {0} bought {1} apples today!'.format(who, how_many))
print('4: {1} bought {0} apples today!'.format(who, how_many))
print(f'5: {who} bought {how_many} apples today!')
