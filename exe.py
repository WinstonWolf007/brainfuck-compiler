all_char = "+-><[].,/\\:"
mem = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

idx = 0
idx_y = 0

loop_data = []
loop = False
while_loop = False

def more():
    if mem[idx_y][idx] < 256:
        mem[idx_y][idx] += 1
    else:
        mem[idx_y][idx] = 0

def less():
    if mem[idx_y][idx] > 0:
        mem[idx_y][idx] -= 1
    else:
        mem[idx_y][idx] = 256

def left():
    global idx
    if idx > 0:
        idx -= 1
    else:
        idx = len(mem[0])-1

def right():
    global idx
    if idx < len(mem[0])-1:
        idx += 1
    else:
        idx = 0

def up():
    global idx_y
    if idx_y > 0:
        idx_y -= 1
    else:
        idx_y = len(mem)-1

def down():
    global idx_y
    if idx_y < len(mem)-1:
        idx_y += 1
    else:
        idx_y = 0

def out():
    print(chr(mem[idx_y][idx]), end="")

def inp():
    entry = input("> ")
    if not entry:
        mem[idx_y][idx] = 0
    else:
        mem[idx_y][idx] = ord(entry)

def loop_in():
    global loop
    loop = True

def loop_out():
    global loop
    loop = False

def jumpLine():
    print("")

execute = {
    "+": more,
    "-": less,
    ">": right,
    "<": left,
    ".": out,
    ",": inp,
    "[": loop_in,
    "]": loop_out,
    "/": down,
    "\\": up,
    ":": jumpLine
}

with open("./script.bf", "r+") as file:
    for line in file:
        for char in line:
            if char in all_char:
                execute[char]()
                if loop and char != "[":
                    loop_data.append(char)
                elif len(loop_data) > 0:
                    looping = True
                    while looping:
                        for code in loop_data:
                            execute[code]()
                        if mem[idx_y][idx] == 0:
                            looping = False
                    loop_data = []

print("")

for row in mem:
    print(row)
