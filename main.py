import time
import random
is_doing_shit = True
variables = []
fns = []
arrays = []
commands = ['print:do_print','var:make_variable','concat:concat','fn:make_function','run:run_f','read:read_f','array:array_make']
def read_array(wholething):
  global arrays
  index = ''
  name = ''
  anum = 0
  before = True
  for char in wholething:
    if char == '|':
      before = False
    elif before:
      name += char
    elif not before:
      index += char
  index = eval_key(index)
  name = eval_key(index)
  for arr in arrays:
    if arr[0].split(":")[0] == name:
      break
    anum += 1
  if name == '':
    return arrays[anum]
  return arrays[anum][int(index)]
    
def array_make(name,*items):
  global arrays
  temp = [name]
  for item in items:
    temp.append(item)  
  num = 0
  for arr in arrays:
    if arr.split(':')[0] == name:
      arrays[num] == temp
      return True
    num += 1
  arrays.append(temp)
      
def read_f(name):
    with open(name + '.txt') as file:
      lines = file.readlines()
      print('start of: ' + name + '---------')
      for line in lines:
        if not line.startswith('//') or not line.startswith('>') or not line.startwith('>>'):
          rd_line(line.rstrip())
      print('end of: '+ name + '-----------')
    print('reading failure')
def run_f(name):
  global fns
  for fn in fns:
    if fn.split(':')[0] == name:
      if '&' in fn.split(':')[1]:
        content = fn.split(':')[1].split('&')
        for cmd in content:
          rd_line(cmd.lstrip())
      else:
        content = fn.split(':')[1]
        rd_line(content)
def make_function(name,*args):
  global fns
  toapp = ''
  for arg in args:
    toapp += arg + ' '
  num = 0
  for fn in fns:
    if fn.split(':')[0] == name:
      fns[num] = name + ':' + toapp.rstrip()
      return True
    num += 1
  fns.append(name + ':' + toapp.rstrip())
def manipulate(equation):
  actual_stuf = equation[1:len(equation)-1].split('_')
  sort_num = 0
  result = None
  actual_stuf[1] = eval_key(actual_stuf[1])
  if actual_stuf[1] == '*':
    result = int(eval_key(actual_stuf[0])) * int(eval_key(actual_stuf[2]))
  if actual_stuf[1] == '/':
    result = int(eval_key(actual_stuf[0])) / int(eval_key(actual_stuf[2]))
  if actual_stuf[1] == '+':
    result = int(eval_key(actual_stuf[0])) + int(eval_key(actual_stuf[2]))
  if actual_stuf[1] == '-':
    result = int(eval_key(actual_stuf[0])) - int(eval_key(actual_stuf[2]))
  if len(actual_stuf) > 3:
    remaning = actual_stuf[3:]
    sort_num = 0
    while sort_num < len(remaning):
      if sort_num % 2 == 0:
        if eval_key(remaning[sort_num]) == '*':
          result = result * int(eval_key(remaning[sort_num+1]))
        elif eval_key(remaning[sort_num]) == '/':
          result = result / int(eval_key(remaning[sort_num+1]))
        elif eval_key(remaning[sort_num]) == '+':
          result = result + int(eval_key(remaning[sort_num+1]))
        elif eval_key(remaning[sort_num]) == '-':
          result = result - int(eval_key(remaning[sort_num+1]))
      sort_num += 1
  return result  #(1[0]+[1]1[2]2[3]-3[4])
def concat(*args):
    toconc = args[1:]
    tostore = ''
    for string in toconc:
        tostore += string
    make_variable(args[0],tostore)
def get_variable(name):
  global variables
  for vari in variables:
    if vari.split(":")[0] == name:
      return vari.split(":")[1]
  return False
def eval_key(keyword):
  if keyword.startswith('*'):
    return keyword[1:]
  if keyword.startswith('^'):
    return read_array(keyword[1:])
  if keyword.startswith('('):
    return manipulate(keyword)
  if keyword.startswith('$'):
    return get_variable(keyword[1:])
  return keyword
def make_variable(name,*values):
  global variables
  toapp = ''
  for value in values:
    toapp += value + ' '
  for existing in variables:
    if existing.split(":")[0] == name:
      existing = (name + ":" + toapp)
      return True
  variables.append(name + ':' + toapp)
def do_print(*args):
    toprin = ''
    for string in args:
        toprin += string + ' '
    print(toprin)
    return True
def rd_line(line):
  global commands
  args = None
  tosend = ''
  parse = line.split(' ')
  for cmd in commands:
    if eval_key(parse[0]) == cmd.split(':')[0]:
      cmd_do = cmd.split(':')[1]
      args = parse[1:]
      for arg in args:
        tosend += '"' + str(eval_key(arg)) + '"' + ',' 
      eval(cmd_do + '(' + tosend + ')')
      return True
  print("failed")
while is_doing_shit:
  rd_line(input("cmd? "))