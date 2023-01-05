import re


def arithmetic_arranger(problems, show = False):
  if len(problems) > 5: return 'Error: Too many problems.'
  arranged_problems = ''
  topVals = ''
  bottomVals = ''
  sumLine = ''
  answerVals = ''
  i = 1
  for problem in problems:
    # validate input operator
    if re.search('[*/]', problem): return "Error: Operator must be '+' or '-'."
    # validate input characters (only + or -)
    if re.search('[a-zA-Z]', problem):
      return 'Error: Numbers must only contain digits.'
    # get values and operator
    vals = problem.split()
    # validate for missing whitespace.
    # ALTERNATIVELY, if no whitespace, split on + or -...
    if len(vals) == 1:
      return 'Error: No whitespace in the problem string...'
    # validate length of input values (not more than 4 characters)
    if len(vals[0]) > 4 or len(vals[2]) > 4:
      return 'Error: Numbers cannot be more than four digits.'

    # compare length of values
    topLonger = len(vals[0]) > len(vals[2])
    bottomLonger = len(vals[2]) > len(vals[0])
    # determine if this is the last problem in the set
    last = i == len(problems)

    # format return strings
    if topLonger or bottomLonger:
      diff = abs(len(vals[0]) - len(vals[2]))
      topVals = topVals + '  ' + (' '* diff if bottomLonger else '') + vals[0] + ('' if last else '    ')
      bottomVals = bottomVals + vals[1] + ' ' + (' ' * diff if topLonger else '') + vals[2] + ('' if last else '    ')
    else:
      topVals = topVals + '  ' + vals[0] + ('' if last else '    ')
      bottomVals = bottomVals + vals[1] + ' ' + vals[2] + ('' if last else '    ')
    sumLine = sumLine + '--' + '-'*abs(max(len(vals[0]),len(vals[2]))) + ('' if last else '    ')

    # evaluate the result(s)
    answer = eval(problem)
    # format answer string
    answerDiff = (2 + max(len(vals[0]),len(vals[2]))) - len(str(answer))
    answerVals = answerVals + ' ' * answerDiff + str(answer) + ('' if last else '    ')
    i += 1
    
  arranged_problems = topVals + '\n' + bottomVals + '\n' + sumLine + (('\n'+answerVals) if show else '')
  return arranged_problems

