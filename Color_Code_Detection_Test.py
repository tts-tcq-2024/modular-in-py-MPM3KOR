import Color_Code_Detection

def test_number_to_pair(pair_number,expected_major_color, expected_minor_color):
  
  major_color, minor_color = Color_Code_Detection.get_color_from_pair_number(pair_number)
  
  assert(major_color == expected_major_color)
  assert(minor_color == expected_minor_color)
  
