def foo(inputstring, inputbit):
    if inputbit & 0b1:
        inputstring = f"{'<b>'}{inputstring}{'</b>'}"
    if inputbit & 0b10:
        inputstring = f"{'<i>'}{inputstring}{'</i>'}"
    if inputbit & 0b100:
        inputstring = f"{'<u>'}{inputstring}{'</u>'}"
    if inputbit & 0b1000:
        inputstring = f"{'<s>'}{inputstring}{'</s>'}"
    return inputstring


print(foo("test", 13))
