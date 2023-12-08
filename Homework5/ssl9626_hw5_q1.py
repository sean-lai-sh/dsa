from ArrayStack import *


def operation(stack, opn, key_var):
    # pop the two most recent values
    val2 = stack.pop()
    val1 = stack.pop()
    if len(key_var) > 0 and isinstance(val1, str) and not val1.isdigit():
        val1 = key_var[val1]
    if len(key_var) > 0 and isinstance(val2, str) and not val2.isdigit():
        val2 = key_var[val2]
    # A switch statement where we returna certain value
    # based on operation char
    val1 = int(val1)
    val2 = int(val2)
    # convert to int to avoid issues.
    if opn == "*":
        return val1 * val2
    elif opn == "+":
        return val1 + val2
    elif opn == "-":
        return val1 - val2
    elif opn == "/":
        return val1 / val2
    else:
        return val1**val2


curr_statement = ""
variables = {}
operators = "*-/+^**"  # Define supported operation chars
end_program = False
while end_program is False:
    curr_statement = input("--> ")
    if curr_statement == "done()":
        end_program = True
        continue
    lst_vars = curr_statement.split(" ")
    currentStack = ArrayStack()  # init Stack
    re_val = 0  # Set our sum to 0
    add_variable = False
    for i in range(len(lst_vars)):  # iterate over all operands
        if lst_vars[i] in operators:
            # do operation
            currentStack.push(operation(currentStack, lst_vars[i], variables))
        elif lst_vars[i] == "=":
            add_variable = True
        else:
            # add the value to the stack
            currentStack.push(lst_vars[i])
    if currentStack.top() in variables:
        print(variables[currentStack.top()])
    elif not add_variable:
        # Get the last value that was pushed to stack
        re_val = currentStack.pop()
        print(re_val)
    else:
        re_val = currentStack.pop()
        var_k = currentStack.pop()
        variables[var_k] = re_val
        print(var_k)
