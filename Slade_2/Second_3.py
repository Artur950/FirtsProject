def list_generator():
    balances = [1, 2, 3, 4, 5]
    del_balances = {0, 4}
    New_balances = [x for i, x in enumerate(balances) if i not in del_balances]
    print(New_balances)


list_generator()
