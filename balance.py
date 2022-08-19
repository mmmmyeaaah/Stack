from lifo import Stack

def balance(text: str) -> bool:
    stack = Stack()
    open_ = ('(', '[', '{')
    close_ = (')', ']', '}')

    for bracket in text:
        if bracket in open_:
            stack.push(bracket)

        elif bracket in close_:
            if stack.isEmpty():
                return "Несбалансированно"

            else:
                if open_.index(stack.peek()) == close_.index(bracket):
                    stack.pop()

                else:
                    return "Несбалансированно"    

    if stack.isEmpty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"    