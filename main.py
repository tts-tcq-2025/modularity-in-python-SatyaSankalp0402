from testColorCoder import test_number_to_pair
from testColorCoder import test_pair_to_number
from WiringManualGeneration import print_color_coding_manual
from ColorConstants import MAJOR_COLORS, MINOR_COLORS
if __name__ == '__main__':
  test_number_to_pair(4, 'White', 'Brown')
  test_number_to_pair(5, 'White', 'Slate')
  test_pair_to_number('Black', 'Orange', 12)
  test_pair_to_number('Violet', 'Slate', 25)
  test_pair_to_number('Red', 'Orange', 7)
  print('Done :)')
  print_color_coding_manual(MAJOR_COLORS,MINOR_COLORS)
