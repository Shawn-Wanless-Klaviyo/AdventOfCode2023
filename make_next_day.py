import os
import shutil


def _next_day():
    days = []
    for entry in os.scandir("."):
        if entry.name.isnumeric() and entry.is_dir():
            days.append(int(entry.name))
    days.sort()
    return days[-1] + 1


def update_readme(day):
    with open("README.md", "a") as f:
        lines = [
            f"<h2>Day {day}</h2>\n",
            "\n",
            f"- [Prompt](https://adventofcode.com/2023/day/{day})\n",
            f"- [Solution](./{day}/solution.py)\n",
            "\n"
        ]
        f.writelines(lines)


def make_next_dir(day):
    os.mkdir(f"./{day}")
    for entry in os.scandir("./boilerplate"):
        shutil.copy(entry.path, f"./{day}")


if __name__ == '__main__':
    next_day = _next_day()
    make_next_dir(next_day)
    update_readme(next_day)
