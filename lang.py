import time
import random
import json
is_doing_shit = True
variables = []
fns = []
arrays = []
before_listeners = []
after_listeners = []
store_exceptions = ['make_function','while_state','for_state']
def output_method(content):
  print(content)
def input_method(prompt):
  return input(prompt)
commands = ['print:do_print','var:make_variable','concat:concat','fn:make_function','run:run_f','read:read_f','array:array_make','if:if_state','while:while_state','input:input_state','insert:insert','append:app','randint:rand','sleep:slep','for:for_state']
def until_state(*kazoo):
  #until after func :
  pass
  if kazoo[0] == 'after':
    pass
def for_state(*idk):
  #for item in array
  item_name = eval_key(idk[0])
  w_array = eval_key(idk[2])
  code = ''
  for seal in idk[3:]:
    code += seal + ' '
  global arrays
  num = 0
  for arr in arrays:
    if arr[0] == w_array:
      break
    else:
      num += 1
  for thingy in arrays[num-1][1:]:
    make_variable(item_name,thingy)
    rd_line(code)
def slep(whenindoubtseal):
  time.sleep(int(whenindoubtseal))
def rand(*shit):
  make_variable(shit[0],str(random.randint(int(shit[1]),int(shit[2]))))
def app(*iaintgonnaliveforever):
  global arrays
  for arr in arrays:
    if arr[0] == iaintgonnaliveforever[0]:
      toapp = ''
      for item in iaintgonnaliveforever[1:]:
        toapp += item + ' '
      arr.append(toapp)
def insert(*s):
  #insert seal 2 @
  global arrays
  for arr in arrays:
    if arr[0] == s[0]:
      arr[int(s[1])] = s[2]
      return None
  output_method('failed')
def input_state(*itsmylife):
  variable = itsmylife[0]
  toask = '' 
  for words in itsmylife[1:]:
    toask += words + ' '
  sel = input_method(toask)
  make_variable(variable,sel)
def cond(var1,var2,condition):
  result = False
  if condition == '<':
    if var1 < var2:
      result = True
  elif condition == '>':
    if var1 > var2:
      result = True
  elif condition == '==':
    if var1 == var2:
      result = True
  elif condition == '!=':
    if var1 != var2:
      result = True
  elif condition == '<=':
    if var1 <= var2:
      result = True
  elif condition == '>=':
    if var1 >= var2:
      result = True
  return result
def while_state(*endme):
  condition = endme[1]
  var1 = endme[0]
  var2 = endme[2]
  torun = ''
  for code in endme[3:]:
    torun += code + ' '
  try:
    var1 = int(var1)
  except:
    pass
  try:
    var2 = int(var2)
  except:
    pass
  while cond(eval_key(str(var1)),eval_key(str(var2)),condition):
    rd_line(torun)
def if_state(*shit):
  #if seal < panda run seal
  var1 = shit[0]
  var2 = shit[2]
  torun = ''
  condition = shit[1]
  left = shit[3:]
  for command in left:
    torun += command + ' '
  torun = torun.rstrip() 
  try:
    var1 = int(var1)
  except:
    pass
  try:
    var2 = int(var2)
  except:
    pass
  if cond(var1,var2,condition):
    rd_line(torun) 
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
  name = eval_key(name)
  acnum = None
  for arr in arrays:
    if arr[0] == name:
      acnum = anum
    anum += 1
  if index == '':
    return arrays[acnum][1:]
  return arrays[acnum][int(index)]
def array_make(name,*items):
  global arrays
  temp = [name]
  for item in items:
    temp.append(item)  
  num = 0
  for arr in arrays:
    if arr[0].split(':')[0] == name:
      arrays[num] = temp
      return True
    num += 1
  arrays.append(temp)    
def read_f(name):
    with open('projects/' + name + '.txt') as file:
      lines = file.readlines()
      output_method('start of: ' + name + '---------')
      for line in lines:
        if not line.startswith('//') or not line.startswith('>') or not line.startwith('>>'):
          rd_line(line.rstrip())
      output_method('end of: '+ name + '-----------')
    output_method('reading failure')
def run_f(name):
  global fns
  for fn in fns:
    if fn.split(':')[0] == name:
      if '&' in fn.split(':')[1]:
        content = fn.split(':')[1].split('&')
        for cmd in content:
          rd_line(cmd.lstrip().rstrip())
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
  #actual_stuf = equation[1:len(equation)-1].split('_')
  if settings['do_break_math']:
      actual_stuf = equation[1:len(equation)-1].split('_')
  else:
    actual_stuf = []
    single_out = equation[1:len(equation)-1]
    isoperand = False
    temp = ''
    for char in single_out:
        if char == '+' or char == '-' or char == '*' or char == '/':
            actual_stuf.append(temp)
            temp = ''
            isoperand = True
            actual_stuf.append(char)
        else:
            isoperand = False
            if not isoperand:
                temp += char
    actual_stuf.append(temp)
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
      if string == 'HOLD':
        tostore += ' '
      else:
        tostore += string
    make_variable(args[0],tostore)
def get_variable(name):
  global variables
  for vari in variables:
    if vari.split(":")[0] == name:
      return vari.split(":")[1]
  return False
def eval_key(keyword):
  if keyword == '':
    return keyword
  global variables
  if keyword.startswith('*'):
    return keyword[1:]
  if keyword.startswith('_'):
    return ' '
  if keyword.startswith('^'):
    return read_array(keyword[1:])
  if keyword.startswith('('):
    return manipulate(keyword)
  if keyword.startswith('$'):
    if get_variable(keyword[1:]) != False:
      return get_variable(keyword[1:])
  return keyword
def make_variable(name,*values):
  global variables
  toapp = ''
  for value in values:
    toapp += (value) + ' '
  num = 0
  for existing in variables:
    if existing.split(":")[0] == name:
      variables[num] = (name + ":" + toapp.rstrip())
      return True
    num += 1
  variables.append(name + ':' + toapp.rstrip())
def do_print(*args):
    toprin = ''
    for string in args:
        toprin += string + ' '
    output_method(toprin)
    return True
def rd_line(line):
  global commands
  global store_exceptions
  args = None
  tosend = ''
  do_eval = True
  parse = line.split(' ')
  for cmd in commands:
    if eval_key(parse[0]) == cmd.split(':')[0]:
      cmd_do = cmd.split(':')[1]
      args = parse[1:]
      for exception in store_exceptions:
        if cmd_do == exception:
          do_eval = False
      for arg in args:
        if arg != '':
          if do_eval:
            tosend += '"' + str(eval_key(arg)) + '"' + ',' 
          else:
            tosend += '"' + str(arg) + '"' + ','
      eval(cmd_do + '(' + tosend + ')')
      return True
  output_method("failed")
#stuf = ['Important messages about lang:','required: time module','incomplete: random ints not added yet but module is imported anywat for future use','incomplete: math function does not currently support equation in equation']
def start():
  global is_doing_shit
  while is_doing_shit:
    rd_line(input_method("cmd? "))
settings = None
with open('lang_config.json') as config:
    settings = json.load(config)
if settings['auto_start']:
    if settings['allow_failure']:
        start()
    else:
        try:
            start()
        except:
            output_method('the program failed')