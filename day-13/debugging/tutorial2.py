import pdb

a = "aaa"
b = "bbb"
c = "ccc"


def final(var1, var2, var3):
    # if you want the function content
    # to be traced, you need to set the trace
    # within the function
    pdb.set_trace()
    return var1 + var2 + var3


print(final(a, b, c))
