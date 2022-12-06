with open("1.txt") as fp:
    message = fp.read()

pkg_start_idx = next(idx for idx in range(4, len(message))
                     if len(set(message[idx-4:idx])) == 4)

msg_start_idx = next(idx for idx in range(14, len(message))
                     if len(set(message[idx-14:idx])) == 14)

print(f'fst result {pkg_start_idx}')
print(f'snd result {msg_start_idx}')
