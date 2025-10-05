from ColorConstants import MAJOR_COLORS
from ColorConstants import MINOR_COLORS
def get_color_from_pair_number(pair_number):
  zero_based_pair_number = pair_number - 1
  major_index = zero_based_pair_number // len(MINOR_COLORS)
  if major_index >= len(MAJOR_COLORS):
    raise Exception('Major index out of range')
  minor_index = zero_based_pair_number % len(MINOR_COLORS)
  if minor_index >= len(MINOR_COLORS):
    raise Exception('Minor index out of range')
  return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]




