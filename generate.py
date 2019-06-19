from hid_code import azerty_hid_codes
import json


# if __name__ == '__main__':
#
#     result = {}
#
#     for char in azerty_hid_codes:
#         print(char, azerty_hid_codes[char])
#         code = azerty_hid_codes[char]
#         if code[0] not in result:
#             result[code[0]] = []
#         result[code[0]].append([code[1], char])
#
#     print(result)
#
#     with open('key_code.json', 'w') as f:
#         f.write(json.dumps(result))


# if __name__ == '__main__':
#
#     result = {}
#
#     for char in azerty_hid_codes:
#         result[azerty_hid_codes[char]] = char
#
#     with open('key_code2.json', 'w') as f:
#         f.write(json.dumps(result))


if __name__ == '__main__':
    result = {}
    f = open('linux_scancodes.csv')
    _ = f.readline()
    while True:
        line = f.readline()
        if line == '':
            break
        data = line.split(',')
        result[int(data[0])] = data[1][:-1]

    print(result)

    with open('key_code2.json', 'w') as f:
        f.write(json.dumps(result))

