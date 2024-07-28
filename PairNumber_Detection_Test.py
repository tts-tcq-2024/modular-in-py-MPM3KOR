import PairNumber_Detection

def test_pair_to_number(major_color, minor_color, expected_pair_number):
  pair_number = PairNumber_Detection.get_pair_number_from_color(major_color, minor_color)
  
  assert(pair_number == expected_pair_number)
