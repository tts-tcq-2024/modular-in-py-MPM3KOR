import Color_Code_main
from Exceptions_Messages import Exception_major_index_OutOfRange , Exception_minor_index_OutOfRange

def get_color_from_pair_number(pair_number):
  zero_based_pair_number = pair_number - 1
  
  major_index = zero_based_pair_number // len(Color_Code_main.MINOR_COLORS)
  if major_index >= len(Color_Code_main.MAJOR_COLORS):
    Exception_major_index_OutOfRange()
  
  minor_index = zero_based_pair_number % len(Color_Code_main.MINOR_COLORS)
  if minor_index >= len(Color_Code_main.MINOR_COLORS):
    Exception_minor_index_OutOfRange()
 
  return Color_Code_main.MAJOR_COLORS[major_index], Color_Code_main.MINOR_COLORS[minor_index]
