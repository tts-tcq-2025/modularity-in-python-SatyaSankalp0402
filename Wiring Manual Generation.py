def color_pair_to_string(major_color, minor_color):
  return f'{major_color} {minor_color}'

def color_coding_manual(major_colors,minor_colors):
  pair_number=1
  for major_color in major_colors:
    for minor_color in minor_colors:
      color_combination = color_pair_to_string(major_color,minor_color)
      print_color_coding_manual(color_combination)
      pair_number +=1
