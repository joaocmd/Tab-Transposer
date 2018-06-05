#João Carlos Morgado David.
#Information on the github page: https://github.com/joaocmd/Tab-Transposer

import re

def check_strs_in_line(line, strs):
     """string x list of strings -> bool. Returns whether any of the strings in strs is part
     of the string line."""

     for str in strs:
          if str in line:
               return True

     return False

def replace_numbers_in_line(line, transpose_value):
     """string x int -> string. Returns a new string where the numbers found in line
     are replaced by themselves - transpose_value."""

     # Sorting so that we start replacing the lower numbers so that there are
     # no conflicts
     numbers = sorted(set(int(i) for i in re.findall(r"\d+", line)))
     for n in numbers:
          new_number = n-transpose_value
          new_number_str = str(n-transpose_value)
          if n >= 10 and new_number < 10:
               #Add a dash to compensate the lost character
               new_number_str = "-" + new_number_str

          line = line.replace(str(n), new_number_str)

     return line

def add_strings(l, msg):
     """ list x string ->. Prints msg and appends each input line to l until it finds an emtpy
     line."""

     print(msg)
     while True:
          s = input();
          if s == "":
               break

          l.append(s)

def main():
     """->. This is where the main program runs."""

     file_name = input("File name (without \".txt\"): ") 
     tranpose_value = int(input("How many frets to transpose: "))
     right_instrument = False

     valid_strs = []
     print("Press just enter to finish (with no trailing whitespace).\n")
     add_strings(valid_strs, "Green light strings (e.g: Guitar 1): ")
     if (len(valid_strs) == 0):
          #Start replacing from the beginning.
          right_instrument = True

     invalid_strs = [] 
     add_strings(invalid_strs, "Red light strings (e.g: Guitar): ")

     f = open(file_name + ".txt", "r")
     lines = f.readlines()
     f.close()

     new_file = open(file_name + "_new.txt", "w")
     for line in lines:
          if check_strs_in_line(line, valid_strs):
               right_instrument = True
               new_file.write(line)
          elif check_strs_in_line(line, invalid_strs):
               right_instrument = False
               new_file.write(line)
          elif right_instrument:
               new_file.write(replace_numbers_in_line(line, tranpose_value))
          else:
               new_file.write(line)

     new_file.close()

main()
