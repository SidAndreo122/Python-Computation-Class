
filename = input("Enter filename: ")
content_ = "This is a test\n"
# outfile = None
try:
    outfile = open(filename, "w")
    try:
        outfile.write(content_)
    finally:
        outfile.close()
except FileNotFoundError as e:
    print('exception occured as', e)

print('Continue with program')
