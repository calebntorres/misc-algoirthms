def process_id(og_string):

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
  process_id = [string for string in num_substring_list if len(string) == 4]
          
  return process_id
    
    

def process_name(_id, _string):
    id = _id[0]
    str = ""
    substring = str.join(id)   
    #print(substring)

    if substring in _string:
        #new_string = _string[1:-1]
        process_name = _string.partition("/")
    
    for part in process_name:
        print(part)

        
    



if __name__ == "__main__":
  string = '//location01/1234_Process_Name_DB1/abc820fddfd'
  list_of_num_strings = process_id(string)
  process_name(list_of_num_strings, string)
