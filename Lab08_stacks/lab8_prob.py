from stacks import ArrayStack


def stack_sum(s):
    if len(s) == 1:
        return s.top()
    to_add = s.pop()
    prev_sum = stack_sum(s)
    s.push(to_add)
    return to_add + prev_sum


def eval_prefix(exp_str):
    op_lst = exp_str.split(" ")
    stack = ArrayStack()
    nums_enc = 0
    operators = "+-/*^"
    for i in range(len(op_lst) - 1, -1, -1):
        if op_lst[i] in operators:
            val1 = int(stack.pop())
            val2 = int(stack.pop())
            operator = op_lst[i]
            if operator == "+":
                stack.push(val1 + val2)
            elif operator == "-":
                stack.push(val1 - val2)
            elif operator == "*":
                stack.push(val1 * val2)
        else:
            stack.push(op_lst[i])
    return stack.top()


def flatten_list(lst):
    s = ArrayStack()
    final_lst = []
    for i in range(len(lst)):
        s.push(lst[i])
    while len(s) > 0:
        item = s.pop()
        if isinstance(item, list):
            for i in range(len(item)):
                s.push(item[i])
        else:
            final_lst.append(item)
    final_lst.reverse()
    return final_lst

def stack_sort(s):
    help_stack = ArrayStack()
    help_stack.push(s.pop())

    # O(N^2) Runtime
    while not s.is_empty():
        v = s.pop()
        if help_stack.is_empty():
            help_stack.push(v)
        elif v > help_stack.top():
            help_stack.push(v)
        else:
            num_back = 0
            correct_place = False
            while not correct_place and not help_stack.is_empty():
                if v < help_stack.top():
                    v2 = help_stack.pop()
                    num_back += 1
                    s.push(v2)
                else:
                    correct_place = True
            help_stack.push(v)
            for i in range(num_back):
                help_stack.push(s.pop())

    while not help_stack.is_empty():
        s.push(help_stack.pop())
    return s


# Q1 unit Test
t_stack = ArrayStack()

t_stack.push(4)
t_stack.push(1)
t_stack.push(3)
t_stack.push(5)
t_stack.push(2)

print(stack_sum(t_stack))
print(len(t_stack))
# Q2 Unit test
test_str = "- + * 16 5 * 8 4 20"
print(eval_prefix(test_str))

# Q3 Unit Test
lst = [[[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
print(flatten_list(lst))


#Q4 Optional:
stack_sort(t_stack)

while not t_stack.is_empty():
    print(t_stack.pop())