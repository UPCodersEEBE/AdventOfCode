class Board:
    lines: list = None
    not_checked_sum: dict = None
    has_won = False

    def __init__(self, data):
        self.lines = []
        self.not_checked_sum = {"checked": [], "amount": 0}

        total_value = 0
        for row in data:
            numbers = [int(num) for num in row.split(" ")]
            total_value += sum(numbers)
            self.lines.append(
                {
                    "numbers": numbers,
                    "guessed": 0,
                }
            )
        for i in range(5):
            numbers = [int(row.split(" ")[i]) for row in data]
            self.lines.append(
                {
                    "numbers": numbers,
                    "guessed": 0,
                }
            )
        self.not_checked_sum["amount"] = total_value
        pass

    def update(self, num):
        for line in self.lines:
            if num in line["numbers"]:
                if num not in self.not_checked_sum["checked"]:
                    self.not_checked_sum["checked"].append(num)
                    self.not_checked_sum["amount"] -= num
                line["guessed"] += 1
                if line["guessed"] == 5:
                    self.has_won = True
                return f"result: {self.not_checked_sum['amount'] * num}"
        pass


boards = []
with open("input.dat") as f:
    numbers_selected = [int(num) for num in f.readline().split(",")]

    data = [line.replace("\n", "").strip().replace("  ", " ") for line in f.readlines()]

    for i in range(len(data) // 6):
        boards.append(Board(data[i * 6 + 1 : (i + 1) * 6]))


for num in numbers_selected:
    for board in boards:
        res = board.update(num)
        if board.has_won:
            if len(boards) == 1:
                print(res)
                exit()
            else:
                boards.pop(boards.index(board))
