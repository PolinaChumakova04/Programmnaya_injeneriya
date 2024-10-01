def main(*args):
    total = sum(args)
    count = len(args)

result = total / count

return result
print(main(1, 2, 3, 4, 5, 6, 7, 8, 9))

print(main(3, 7, 1))