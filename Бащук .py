while True:
    inp = input("Введіть перше число (або 'exit' для виходу): ")
    if inp.lower() == 'exit':
        break
    a = float(inp)
    b = float(input("Введіть друге число: "))
    
    print(f"Сума: {a + b}")
    print(f"Добуток: {a * b}")
    if b != 0:
        print(f"Ділення: {a / b}")
    else:
        print("Ділення на нуль неможливе!")