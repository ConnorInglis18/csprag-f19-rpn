#!/usr/bin/env python3

def calculate(arg):
  stack = list()
  for token in arg.split():
    if token == '+':
      arg2 = stack.pop()
      arg1 = stack.pop()
      result = arg1 + arg2
      stack.append(result)
    elif token == '-':
      arg2 = stack.pop()
      arg1 = stack.pop()
      result = arg1 - arg2
      stack.append(result)
    else:
      stack.append(int(token))
  if len(stack) != 1:
    raise TypeError('malformed input')
  return stack.pop()

def main():
  while True:
    result = calculate(input("rpn calc> "))
    print(result)

if __name__ == '__main__': #aka dunder main (double _ main)
  main()