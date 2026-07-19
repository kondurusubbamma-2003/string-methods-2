#1.Implement a Python function clean_string that takes a string as input, removes leading and trailing whitespaces, and converts it to lowercase.
def clean_string(text):
    print(text.strip().lower())
clean_string("PYTHON programming ")
#2.Write a Python function extract_substring that takes two parameters: a string and a starting index. This function should return the substring from the starting index to the end of the string.
def extract_substring(text,start):
    return text[start:]
result=extract_substring("programming",3)
print(result)
#3.Create a function replace_vowels that replaces all vowels in a given string with '*'.
def replace_vowels(text):
    text=text.replace("a","*")
    text=text.replace("e","*")
    text=text.replace("i","*")
    text=text.replace("o","*")
    text=text.replace("u","*")
    return text
result=replace_vowels("python programming")
print(result)
#4.Use Python's built-in string method to split a given string into a list of words, assuming words are separated by spaces.
text="pytho is very easy"
s=text.split()
print(s)
#5.Demonstrate the use of the join() method to concatenate elements of a list into a single string, with each element separated by a comma.
text=["akki","subbu","raji"]
s=",".join(text)
print(s)