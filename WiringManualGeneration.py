from ColorConstants import MAJOR_COLORS
from ColorConstants import MINOR_COLORS

def color_pair_to_string(major_color, minor_color):
  return f'{major_color} {minor_color}'

def color_coding_manual(major_colors,minor_colors):
  manual_lines=[]
  pair_number=1
  for major_color in major_colors:
    for minor_color in minor_colors:
      color_combination = color_pair_to_string(major_color,minor_color)
      manual_lines.append(f"{color_combination:<20} | {pair_number:<5}")
      pair_number +=1
  return "\n".join(manual_lines)

def print_color_coding_manual(major_color,minor_color):
  manual_text = color_coding_manual(major_color, minor_color)
  print("Color Coding Reference Manual\n" + "=" * 35)
  print(manual_text)
