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
    if not numbers:
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

def rectangle_area(base, height):
    return base * height

def rectangle_perimeter(base, height):
    return 2 * (base + height)

def rectangle_operations():
    while True:
        try:
            base = float(input("Ingrese la base del rectángulo: "))
            height = float(input("Ingrese la altura del rectángulo: "))
            if base <= 0 or height <= 0:
                print("Los numeros deben ser positivos.")
                continue
            break
        except ValueError:
            print('Debes ingresar numeros validos.')
    area = rectangle_area(base, height)
    perimeter = rectangle_perimeter(base, height)
    print(f'El area del rectangulo es: {area:.2f}')
    print(f"El perimetro del rectangulo es: {perimeter:.2f}")

def is_prime_number(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
        return True
def grade_analyze():
    grades = enter_numbers("Ingresa cuantas calificaciones quieres analizar: ")
    if not grades:
        return
    average = sum(grades) / len(grades)
    good_grades = sum(1 for grad in grades if grad >= 85)
    risky = sum(1 for grad in grades if grad < 60)
    print(f"El promedio es: {average:.2f}")
    print(f"Las notas buenas son: {good_grades:.2f}")
    print(f"Las notas en riesgo de desaprobar son: {risky:.2f}")

def show_low_high_freq():
    numbers = enter_numbers("Cuantos numeros enteros deseas ingresar?: ")
    if not numbers:
        print("No se ingresaron numeros validos")
        return
    numbers = [int(num) for num in numbers if num.is_integer()]
    if not numbers:
        print("No se ingresaron numeros enteros validos.")
        return
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    same = sum(1 for count in freq.values() if count > 1)
    print(f"El numero mayor es: {max(numbers)}")
    print(f"El numero menor es: {min(numbers)}")
    print(f"Numeros que se repiten son: {same}")

def calculator():
    while True:
        try:
            num_one = float(input("Ingrese el primer numero: "))
            num_two = float(input("Ingrese el segundo numero: "))
            break
        except ValueError:
            print("Debe ingresar numeros validos")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    while True:
        option = input("Seleccione una operacion (1-4): ")
        match option:
            case "1":
                print(f"{num_one} + {num_two} = {num_one + num_two}")
                break
            case "2":
                print(f"{num_one} - {num_two} = {num_one - num_two}")
                break
            case "3":
                print(f"{num_one} * {num_two} = {num_one * num_two}")
                break
            case "4":
                try:
                    print(f"{num_one} / {num_two} = {num_one / num_two:.2f}")
                except ZeroDivisionError:
                    print("No se puede dividir entre cero")
                break
            case _:
                print("Ingresaste una opción no válida, vuelve a intentarlo.")



