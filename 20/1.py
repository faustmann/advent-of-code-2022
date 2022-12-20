with open("20_1.txt") as fp:
    enc_file = list(
        map(lambda val_str: [int(val_str), False], fp.read().splitlines()))

for idx in range(len(enc_file)):
    while not enc_file[idx][1]:
        cur_elem = enc_file[idx]
        new_idx = (idx+cur_elem[0])
        new_idx += new_idx // len(enc_file)
        new_idx = new_idx % (len(enc_file))
        del enc_file[idx]
        enc_file.insert(new_idx, cur_elem)
        cur_elem[1] = True

dec_file = [val_elem[0] for val_elem in enc_file]

zero_idx = dec_file.index(0)
groove_coord = [(zero_idx+i) % len(dec_file) for i in [1000, 2000, 3000]]

print(f'fin {sum([dec_file[i] for i in groove_coord])}')
