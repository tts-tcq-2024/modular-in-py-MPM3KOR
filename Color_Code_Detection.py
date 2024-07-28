from Color_Code_main import *

def get_color_from_pair_number(pair_number):
  zero_based_pair_number = pair_number - 1
  
  major_index = zero_based_pair_number // len(MINOR_COLORS)
  if major_index >= len(MAJOR_COLORS):
    Exception_major_index_OutOfRange()
  
  minor_index = zero_based_pair_number % len(MINOR_COLORS)
  if minor_index >= len(MINOR_COLORS):
    Exception_minor_index_OutOfRange()
 
  return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]
