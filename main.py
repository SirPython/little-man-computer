

class LittleManComputer():
    def __init__(self):
        self.mailboxes = [0] * 100
        self.accumulator = 0

        self.flags = {
            neg: False
        }

instruction_set = {
    "ADD": lambda arg, lmc: lmc.accumulator += lmc.mailboxes[arg],
    "SUB":
}

if __name__ == "__main__":
    lmc = LittleManComputer()

    with open(sys.argv[1]) as f:
        line = f.readline().split(" ")

        instruction_set[0](int(line[1]), lmc)

        if accumulator > 1000:
            accumulator -= 1000
            lmc.flags.neg = True
    pass