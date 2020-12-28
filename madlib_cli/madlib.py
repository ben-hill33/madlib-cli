from greeting import print_greeting
# read a template madlib file and parse that file into usable parts



def read_template(filename='../assets/template.txt'):
  with open(filename, 'r') as reader:
    contents = reader.read()
    return contents

def user_input():
  message = 'Please enter an Adjective'
  return input(f'{message} >>')

# def parse_template():
#   contents = reader.read

# def merge():
#   pass


if __name__ == '__main__':
  greeting = print_greeting()
  print(greeting)

  show_message = user_input()
  print(show_message)

  template = read_template()
  print(template)
