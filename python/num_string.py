# finds digit subtring of certain lenth and returns partitioned array of 
#characters in that substring
def digit_subtring(og_string, subtring_length):

  integer_list = []
  string = iter(og_string)
  char = next(string)

  for char in string:
      if char.isdigit == False:
        char = next(string)

      else: 
        num_substring = []
        while char.isdigit():
          num_substring.append(char)
          char = next(string)
        integer_list.append(num_substring)

  num_substring_list = [x for x in integer_list if x != []]   
  substring_list = [string for string in num_substring_list if len(string) == subtring_length]
          
  return substring_list
    
    
# turns array of digits in substring to string and prints
def to_string(list):
    substring = list[0]
    str = ""
    digit_substring = str.join(substring)   
    print(digit_substring)

# testing
if __name__ == "__main__":
  string = 'abcd12th456y4589_'
  substring_array = digit_subtring(string, 4)
  to_string(substring_array)