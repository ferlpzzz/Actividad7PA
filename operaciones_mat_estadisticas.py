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

def show_statistics():
    numbers = enter_numbers("Ingrese cuantos números desea: ")
    if not numbers
        return
    add = sum(numbers)
    average = add / len(numbers)
    positives = sum(1 for num in numbers if num > 0)
    negatives = sum(1 for num in numbers if num < 0)
    zeros = sum(1 for num in numbers if num == 0)
    multiples_3 = sum(1 for num in numbers if num % 3 == 0)
    print(f"Suma total: {add:.2f}")
    print(f"Promedio: {average:.2f}")
    print(f"Positivos: {positives}")
    print(f"Negativos: {negatives}")
    print(f"Ceros: {zeros}")
    print(f"Multiplos de 3: {multiples_3}")

