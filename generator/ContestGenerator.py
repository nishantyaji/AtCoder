import copy
import os


def create_contest():
    contest = "abc370"
    problems = ["a", "b", "c", "d", "e", "f", "g"]

    os.mkdir("../contest/" + contest)
    with open("template.txt", "r") as file:
        file_content = file.read()

    filenames = list(map(lambda x: contest + "_" + x, problems))
    for fn in filenames:
        file_content_copy = copy.deepcopy(file_content)
        file_content_copy = file_content_copy.replace("zzz.zzz", fn + ".txt")
        with open("../contest/" + contest + "/" + fn + ".txt", "w") as f:
            pass
        with open("../contest/" + contest + "/" + fn + ".py", "w") as f:
            f.write(file_content_copy)


if __name__ == '__main__':
    create_contest()
