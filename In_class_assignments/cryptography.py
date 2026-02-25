import hashlib
h = hashlib.new('md5', b'cab').hexdigest()
print(f'initial hash is {h}')

og_hash = 'd077f244def8a70e5ea758bd8352fcd8'
for letter in 'abcdefghijklmnopqrstuvwxyz':
    best_guess = 'ca' + letter
    h = hashlib.new('md5', best_guess.encode('UTF8')).hexdigest()
    if (h == og_hash):
        print(best_guess, h)
    

letters = 'ca'
for letter1 in letters:
    for letter2 in letters:
        xx = letter1 + letter2
        print(xx)
