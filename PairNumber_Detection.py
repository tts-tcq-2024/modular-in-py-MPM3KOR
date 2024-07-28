import Color_Code_main
from Exceptions_Messages import Exception_major_index_OutOfRange , Exception_minor_index_OutOfRange

def get_pair_number_from_color(major_color, minor_color):
  try:
    major_index = Color_Code_main.MAJOR_COLORS.index(major_color)
  except ValueError:
    Exception_major_index_OutOfRange()
  
  try:
    minor_index = Color_Code_main.MINOR_COLORS.index(minor_color)
  except ValueError:
    Exception_minor_index_OutOfRange()
    
  return major_index * len(Color_Code_main.MINOR_COLORS) + minor_index + 1
