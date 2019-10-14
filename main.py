MAX_VAL = 10


def main():
    op_combinations = get_combinations("1", 2)
    for comb in op_combinations:
        if eval(comb) == 100:
            print(comb)


def get_combinations(parent_name, val):
    if val >= MAX_VAL:
        return [parent_name]
    else:
        name_son1 = parent_name + "+" + str(val)
        comb_1 = get_combinations(name_son1, val + 1)

        name_son2 = parent_name + "-" + str(val)
        comb_2 = get_combinations(name_son2, val + 1)

        name_son3 = parent_name + "" + str(val)
        comb_3 = get_combinations(name_son3, val + 1)

        return comb_1 + comb_2 + comb_3


if __name__ =="__main__":
    main()
