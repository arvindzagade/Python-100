#

def format_name(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()

  #print(f"{formated_f_name},{formated_l_name}")
  return f"{formated_f_name},{formated_l_name}"
formated_string = format_name("anGeLA","YU")
print(formated_string)