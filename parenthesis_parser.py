from stack import Stack

def parenthesis_match(s):
    st = Stack()

    for c in s:
        if c == '(':
            st.push(c)
        elif c == ')':
            try:
                st.pop()
            except IndexError:
                return False


    return len(st) == 0
