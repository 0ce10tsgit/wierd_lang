print('package time D:')
import time
import random
isrunning = True
hasPrompted = False
wantsElse = False
variables = []
file = 'main'
recur = []
arrays = []
do_debug_out = False
jokes = ['Why was the cow afraid? He was a cow-herd.','What dog keeps the best time? A watch dog.','What did one plate say to the other? Lunch is on me.','How do you make a good egg roll? You push it down a hill.','What do you call a fake noodle? An im-pasta.']
print("made by 0ce10t")
print('github.com/0ce10tsgit/wierd_lang')
print("type : '>help' for help")
print("input command")
def arr_eval(content):
  global arrays
  try:
    spaced_content = content.split(' ')
    action = eval_var(spaced_content[1])
    name = eval_var(spaced_content[2])
    val = eval_var(spaced_content[3])
  except:
    print("all args not met")
  num = 0
  while num<len(arrays):
    if name == arrays[num][0]:
      break
    else:
      num += 1
  if action == "app" or action == 'append':
    arrays[num].append(val)
  elif action == 'rep' or action == 'replace':
    arrays[num][eval_var(spaced_content[4])] = val
#mod_arr append/replace nase val index 
def arr_check(name):
  global arrays
  items = len(arrays)
  num = 0
  while num<items:
    if arrays[num][0] == name:
      arr = [True,num]
      return arr
    else:
      num += 1
  arr = [False,'dummy']
  return arr
def array_get(name,index):
  global arrays
  items = len(arrays)
  num = 0
  while num<items:
    if arrays[num][0] == name:
      return arrays[num][index]
    else:
      num += 1
  print('failed to find an array with that name')
  return False
def array_m(content):
  global arrays
  #array seal []
  spaced_content = content.split(" ")
  name = eval_var(spaced_content[1]) 
  items = len(spaced_content)-2
  items_to_add = spaced_content[2:]
  num = 0
  arr = [] 
  arr.append(name)
  while num < items:
    arr.append(eval_var(items_to_add[num]))
    num += 1
  cek = arr_check(name)
  if cek[0]:
     arrays[cek[1]] = arr
     print('replaced value')
  else:
    arrays.append(arr)
def output_method(tprint):
  global do_debug_out
  if do_debug_out:
    print(tprint)
def eval_var(name):
  global varaibles
  try:
    tor = int(name)
    return tor 
  except:
    if name[0] == '*':
      return name[1:]
    if name[0] == '@':
      return len(eval_var(name[1:]))
    if name[0] == '^':
      return array_get((name[2:]),int(name[1]))
    if name[0] == '%':
      first = getv_int(getv_int(name[1:])[1])
      if first[0] == 1:
        return first[1]
      else:
        return name
    if name[0] == '$':
      res = getv_int(name[1:])
      if res[0] == 1:
          return res[1]
      else:
        return name
    else:
      return name
def inpu(content):
  #input var prompt
  spaced_content = content.split(' ')
  varx = eval_var(spaced_content[1])
  prompt = spaced_content[2]
  tostore = input(str(eval_var(prompt)) + ': ')
  var('var ' + varx + ' ' + tostore) 
def prin(content):
  spaced_content = content.split(' ')
  #print seals are very $OP
  toprint = ''
  if len(spaced_content)-1 > 1:
    num = 0
    while num < len(spaced_content)-1:
      toprint += str(eval_var(spaced_content[num+1])) + ' '
      num += 1
    print(toprint)
  else:
    toprint = spaced_content[1]
    print(eval_var(toprint))

def whil(content):
  spaced_content = content.split(' ')
  try:
    type_check = spaced_content[1]
    arg1 = spaced_content[2]
    arg2 = spaced_content[3]
    recur = spaced_content[4]
    slep = spaced_content[5]
  except:
    print("did not find all required args")
    return 'done'
  while (if_statment_r('if ' + type_check + ' ' + arg1 + ' ' + arg2)):
    eval_command('>recur_r' + ' ' + recur) 
    time.sleep(int(slep))
def run_f(lines):
  del lines[0:4]
  num = 0
  print('start of program----------')
  while (num < len(lines)):
    if not lines[num].startswith('//'):
      eval_command('>' + lines[num].rstrip())
    num += 1
  print('end of program------------')
def read():
  global file
  try:
    with open(file + '.weird') as f:
      lines = f.readlines()
  except:
      print('failed to find file, check its a .weird file')
      return 's'
  try:
    lines[0:]
  except:
    print('failed to read file: check format')
  print('opening file: ' + lines[1] + '...')
  print('file description: ' + lines[2])
  print('file cmd length: ' + str(len(lines)-4))
  cont = input('run script? ')
  if cont == 'yes' or cont == 'Yes' or cont == 'y' or cont == 'Y':
    print('running')
    run_f(lines)
  else:
     print('ending script')
  
def if_statment_r(content):
  #if = var1 var2 recur
  spaced_content = content.split(' ')
  check_type = spaced_content[1]
  var1 = int(eval_var(spaced_content[2]))
  var2 = int(eval_var(spaced_content[3]))
  result = False
  if check_type == '=':
    if var1 == var2:
      result = True
  elif check_type == '!=':
    if var1 != var2:
      result = True
  elif check_type == 'g':
    if var1 > var2:
      result = True
  elif check_type == 'l':
    if var1 < var2:
      result = True
  elif check_type == 'g=':
    if var1 >= var2:
      result = True
  elif check_type == 'l=':
    if var1 <= var2:
      result = True
  if result:
    return True
  else:
    return False      
def if_statment(content):
  #if = var1 var2 recur
  spaced_content = content.split(' ')
  check_type = spaced_content[1]
  var1 = eval_var(spaced_content[2])
  var2 = eval_var(spaced_content[3])
  recur_state = spaced_content[4]
  result = False
  if check_type == '=':
    if var1 == var2:
      result = True
  elif check_type == '!=':
    if var1 != var2:
      result = True
  elif check_type == 'g':
    if var1 > var2:
      result = True
  elif check_type == 'l':
    if var1 < var2:
      result = True
  elif check_type == 'g=':
    if var1 >= var2:
      result = True
  elif check_type == 'l=':
    if var1 <= var2:
      result = True
  if result:
    output_method('If statement returned True: running recur')
    eval_command('>recur_r '+ recur_state)
  else:
    output_method("returned False")
def concation(content):
  #conc var hai hai hai 
  spaced_content = content.split(' ')
  len_ = len(spaced_content)-2
  var_ = eval_var(spaced_content[1])
  num = 0
  toconc = ''
  while num < len_:
    print(spaced_content[num+2])
    toconc += str(eval_var(spaced_content[num+2]))
    num += 1
  var('var ' + str(var_) + ' ' + toconc)
  output_method("concated")

def recursion(content):
  global recursion
  hasSpace = True
  try:
    command = eval_var(content.split(":")[1])
  except:
    print("failed to find command be sure there is a : after the function name and there is a space between it and first keyword")
    return "finch"
  try:
    command.split(' ')
  except:
    hasSpace = False
  if hasSpace:
    command = eval_var(command.lstrip(' '))
  new = eval_var(content.split(' ')[1].lstrip(";"))
  recur.append(new + str(command))
  new = content.split(' ')[1]
  output_method("recursion command " + str(new) + " stored as " + str(command))  
def getv_int(name):
  global variables
  num = 0
  while(num<len(variables)):
    if name == eval_var(variables[num].split(':')[0]):
      arr = [1,eval_var(variables[num].split(':')[1])]
      return arr
    else:
      num += 1
  arr = [0,0]
  return arr
def manipulate(content):
    spaced_content = content.split(' ')
    try: 
      add1 = eval_var(spaced_content[2])
      add2 = eval_var(spaced_content[3])
      spaced_content[4]
    except:
      print("failed to find all args")
    add1 = int(add1)
    add2 = int(add2)
    if spaced_content[1] == '*':
        result = add1 * add2
    elif spaced_content[1] == '/':
        result = add1/add2
    elif spaced_content[1] == '+':
        result = add1+add2
    elif spaced_content[1] == '-':
        result = add1-add2
    var(('var ' + eval_var(spaced_content[4]) + " " + str(result)))
def getv(content):
  global variables
  temp = False
  new = content.split(' ')
  try: 
    new[1]
  except:
    print("no args added, please specify the variable name and value")
    return "finch"
  if '0123456789' in new[1]:
    needed = variables[int(new[1])]
    print(needed)
  else:
    num = 0
    while(num<len(variables)):
      if eval_var(new[1]) == variables[num].split(":")[0]:
        print(variables[num].split(":")[1])
        temp = True
        break
      else:
        num += 1
    if (len(variables) == 0):
      print("you havent inputted any variables yet")
      temp = True
    if (not temp):
      print("No variables Identified with name: " + str(new[1]))
def var(content):
  global variables
  new = content.split(' ')
  num = 0 
  while num<len(variables):
    if new[1] == variables[num].split(':')[0]:
      variables[num] = new[1] + ':' + new[2]
      output_method("replaced variable " + new[1] + " with new value " + new[2])
      return "complete"
    else:
      num += 1
  variables.append(new[1]+":"+new[2])
  output_method("variable;" + new[1] + " stored at index:" + str((len(variables)-1)))
def help():
  print("Help Menurandint => gives random value between 0 and 1000000, >var navalue => will store given value with name, >getv name => will return the result of a variable with the name specified, >help => this menu, >joke => a very shitty joke, >mani type[+,-,*,/] target1 target2 result_name, does a action on two variables or ints and puts them in the variable which is result_name")
  print("other random commands: panda, seal, no u , test ,Missle")
def recur_r(content):
  global recur
  spaced_content = content.split(' ')
  num = 0
  while num<len(recur):
    if eval_var(spaced_content[1]) == recur[num].split(':')[0]:
      if '&' in recur[num].split(':')[1]:
        spaced_2 = recur[num].split(':')[1].split('&')
        c1 = spaced_2[0] #.split(' ')[0]
        if c1.count(" ") >= 2:
          try:
            c1 = c1.lstrip(' ')
            c1 = c1.rstrip(' ')
          except:
            ahhh = 'kill me'
        else:
          c1 = spaced_2[0].split(' ')[0]
        c2 = spaced_2[1] #.split(' ')[1]
        if c2.count(" ") >= 2:
          try:
            c2 = c2.lstrip(' ')
            c2 = c2.rstrip(' ')
          except:
            ahhhhh = 'pain'
        else:
          c2 = spaced_2[1].split(' ')[1]
        output_method("running first command")
        eval_command('>' + c1)
        output_method('running second command')
        eval_command('>' + c2)
        return "done"
      else:
        output_method("running recursive command")
        try:
          eval_command('>'+str(recur[num].split(':')[1]))
        except:
          print('failed make sure the return variable is registerd right')
        return "complete"
    else:
      num += 1
  print("failed to find recursive commandd")
def eval_command(command):
  global variables
  global wantsElse
  global jokes
  global file
  global isrunning
  global recur
  exit = False
  content = command.split('>')[1]
  spaces = 0
  for i in range(0, len(content)):
    if content[i] == " ":
      spaces += 1
  if content == 'read':
    read()
    return 'done'
  if content == 'vcount':
    print(len(variables))
    return "done"
  if content == 'rcount':
    print(len(recur))
    return "done"
  if content == 'hold':
    return ':)'
  if content == 'randint':
    print(random.randint(0,1000000))
    return "finsihed"
  if content == 'help':
    help()
    return "finsihed"
  if content == 'joke':
    print(jokes[random.randint(0,len(jokes)-1)])
    return "finsihed"
  if content == 'panda' or content == 'seal':
    print(":D")
    return "happi"
  if content == 'no u':
    print("no u")
    return "finsished"
  if content == 'test':
    print('this is indeed working')
    return 'S'
  if content == 'Missle':
    print("The missile knows where it is at all times. It knows this because it knows where it isn't, by subtracting where it is, from where it isn't, or where it isn't, from where it is, whichever is greater, it obtains a difference, or deviation. The guidance sub-system uses deviations to generate corrective commands to drive the missile from a position where it is, to a position where it isn't, and arriving at a position where it wasn't, it now is. Consequently, the position where it is, is now the position that it wasn't, and it follows that the position where it was, is now the position that it isn't. In the event of the position that it is in is not the position that it wasn't, the system has required a variation. The variation being the difference between where the missile is, and where it wasn't. If variation is considered to be a significant factor, it too, may be corrected by the GEA. However, the missile must also know where it was. The missile guidance computance scenario works as follows: Because a variation has modified some of the information the missile has obtained, it is not sure just where it is, however it is sure where it isn't, within reason, and it knows where it was. It now subracts where it should be, from where it wasn't, or vice versa. By differentiating this from the algebraic sum og where it shouldn't be, and where it was. It is able to obtain a deviation, and a variation, which is called 'air")
    return 's'
  if content == 'terminate':
    print("termating prompter")
    isrunning = False
    print('ending function')
    return "done"
  try:
    spaced_content = content.split(' ')
    spaced_content[1]
  except:
    exit = True
    if content == 'print':
      print('missing string')
    if content == 'while':
      print("missing args")
    if content == 'if':
      print('variables and recur not provided')
    if (content == 'recur_r'):
      print("no function name detected")
    if(content == 'recur'):
      print("no name and/or command included use >help for help")
    if(content == 'var'):
      print("no args added, please specify the variable name and value")
    if content == 'input':
      print('missing args')
    elif(content == 'getv'):
      print("No variable name provided")
    elif(content == 'mani'):
      print("incomplete command: " + content + " ,required Argument/s is missing insure spaces are there or check >help")
    elif(content == 'file'):
      print("file not provided")
    elif content == 'conc':
      print('args and result variable not provided')
    elif(spaces == 0):
      print("command'" + content + "' not recoginised")
    else:
      print("incomplete command: " + content)
  if (not exit):
    if spaced_content[0] == 'var':
      var(content)
    elif spaced_content[0] == 'getv':
      getv(content)
    elif spaced_content[0] == 'mani':
        manipulate(content)
    elif spaced_content[0] == 'recur':
      recursion(content)
    elif spaced_content[0] == 'if':
      if_statment(content)
    elif spaced_content[0] == 'recur_r':
        recur_r(content)
    elif spaced_content[0] == 'print':
        prin(content)
    elif spaced_content[0] == 'input':
        inpu(content)
    elif spaced_content[0] == 'mod_arr':
        arr_eval(content)
    elif spaced_content[0] == 'array':
      array_m(content)
    elif spaced_content[0] == 'file':
      print("switched from file: " + file + " to " + spaced_content[1])
      file = spaced_content[1]
    elif spaced_content[0] == 'conc':
      concation(content)
    elif spaced_content[0] == 'while':
      whil(content)
    else:
      print("incomplete command: " + content + " ,required Argument/s is missing insure spaces are there or check >help")
def prompt(prompt):
  command = input(prompt)
  return command
while isrunning:
  time.sleep(0.5)
  if not hasPrompted:
    command = prompt(file + "{")
    if (command.startswith(">")):
      eval_command(command)
    else:
      if wantsElse:
        print("stuff")
      else: print("Invalid  Syntax: > not found")