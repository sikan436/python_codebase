import argparse

# Define the parser
parser = argparse.ArgumentParser(description='Short sample app')

# Declare an argument (`--algo`), saying that the 
# corresponding value should be stored in the `algo` 
# field, and using a default value if the argument 
# isn't given
parser.add_argument('--algo', action="store", dest='algo', default='bye')
parser.add_argument('--load', action="store", dest='load', default='bye')

# Now, parse the command line arguments and store the 
# values in the `args` variable
args = parser.parse_args()

print (args.algo)
print (args.load)


