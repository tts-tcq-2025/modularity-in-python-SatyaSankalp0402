from Color_Constants import MAJOR_COLORS
from Color_Constants import MINOR_COLORS

def color_pair_to_string(major_color, minor_color):
  return f'{major_color} {minor_color}'

def color_coding_manual(major_colors,minor_colors):
  pair_number=1
  for major_color in major_colors:
    for minor_color in minor_colors:
      color_combination = color_pair_to_string(major_color,minor_color)
      print("{:<20} | {:<10}".format(color_combination, pair_number))
      pair_number +=1
