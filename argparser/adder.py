import argparse

parser = argparse.ArgumentParser()

parser.add_argument("greeting", help="greeting message displays")
parser.add_argument('-n','--numbers', type=float, nargs=2, help="The number to be added")



args = parser.parse_args()

print(args)
print(args.greeting)
print(args.numbers)

if args.numbers is not None:
    print(f"Number sum is {args.numbers[0] + args.numbers[1]}")