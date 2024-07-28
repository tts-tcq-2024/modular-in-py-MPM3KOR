from Color_Code_main import *
from Exceptions_Messages import *

def get_pair_number_from_color(major_color, minor_color):
  try:
    major_index = MAJOR_COLORS.index(major_color)
  except ValueError:
    Exception_major_index_OutOfRange()
  
  try:
    minor_index = MINOR_COLORS.index(minor_color)
  except ValueError:
    Exception_minor_index_OutOfRange()
    
  return major_index * len(MINOR_COLORS) + minor_index + 1
