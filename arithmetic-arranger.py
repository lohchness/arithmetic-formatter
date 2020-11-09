def arithmetic_arranger(problems, solution=False):
  arranged_problems = []
  lines = ["", "", "", ""]

  times = len(problems)
  counter = 0  # Counts how many times python went through the for loop
  # First error check
  if len(problems) > 5:
    return "Error: Too many problems."
  else:
    for x in problems:
        calcs = x.split()
        first = calcs[0].strip()
        operator = calcs[1].strip()
        second = calcs[2].strip()

        # Checking for errors
        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."
        elif not first.isdigit() or not second.isdigit():
            return "Error: Numbers must only contain digits."
        elif len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator in ['+', '-']:
          answer = eval(x) # Eval function does a calculation with a string format, and outputs with an integer. 

        # dashes = len(max(first,second))+2 # Dashes = maximum length of  each calculation, so I can use this to measure
        dashes = max(len(first), len(second)) + 2

        # Adding to lines
        # For some reason the last calculation had -1 spaces ( 1 space missing), so I tried doing (if counter = 3: -> add a space to each line) to account for the missing space, but it only triggered another error so I redid the dashes to calculate the maximum length of the numbers. Took a long time to figure out because it didn't work in the IDLE when I was testing it there
        lines[0] += str(first.rjust(dashes))
        lines[1] += str(operator) + (second.rjust(dashes-1))
        lines[2] += str("-"*dashes)
        lines[3] += str(answer).rjust(dashes)

        counter += 1

        if counter != times:
            lines[:] = [f'{line}{" "*4}' for line in lines]

        if solution:
            arranged_problems = lines[0] + "\n" + lines[1] + "\n" + lines[2] + "\n" + lines[3]
        else:
            arranged_problems = lines[0] + "\n" + lines[1] + "\n" + lines[2]

    return arranged_problems