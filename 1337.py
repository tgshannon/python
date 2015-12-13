"""1337.py
Convert message to Elite Hacker Speak"""

TEST_MESSAGE = 'test message'
TEST_SUBSTITUTIONS = [
    ['a', '4'],
    ['e', '3'],
    ['i', '1'],
    ['o', '0'],
    ['t', '7']]

# function to convert a message to hacker speak
def xlate(msg, codex):
    """convert msg str parameter to hacker string using codex list parameter"""
    for c in codex:
        old = c[0]
        new = c[1]
        msg = msg.replace(old,new)
        
    return msg

# test code
message = raw_input("Type the message to encode: ")
converted_text = xlate(message, TEST_SUBSTITUTIONS)
print(converted_text)


    
