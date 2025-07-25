def enter_numbers(message):
    while True:
        try:
            n = int(input(message))
            if n <= 0:
                print("Debe ingresar un número positivo")
                continue
            break
        except ValueError:
            print("Debe ingresar un número entero válido")
    numbers = []
    for i in range(n):
        while True:
            try:
                num = float(input(f"Ingrese el número: {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Debe ingresar un número válido")
    return numbers
