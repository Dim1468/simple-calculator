def evaluate(expression):
    stack = []
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y}
    current_number = ''
    for char in expression:
        if char.isdigit() or char == '.':
            current_number += char
        elif char in operators:
            if current_number:
                stack.append(float(current_number))
                current_number = ''
            operator = operators[char]
            if len(stack) >= 2:
                y = stack.pop()
                x = stack.pop()
                result = operator(x, y)
                stack.append(result)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                y = stack.pop()
                x = stack.pop()
                operator = stack.pop()
                result = operator(x, y)
                stack.append(result)
            if stack and stack[-1] == '(':
                stack.pop()
        elif char == ' ':
            continue
        else:
            raise ValueError("Invalid character in expression")
    if current_number:
        stack.append(float(current_number))
    while len(stack) > 1:
        y = stack.pop()
        x = stack.pop()
        operator = stack.pop()
        result = operator(x, y)
        stack.append(result)
    return stack[0]

print("Расширенный калькулятор")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Выражение")

выбор = input("Введите выбор (1-5): ")

if выбор == '5':
    выражение = input("Введите выражение: ")
    результат = evaluate(выражение)
else:
    число1 = float(input("Введите первое число: "))
    число2 = float(input("Введите второе число: "))

    if выбор == '1':
        результат = число1 + число2
    elif выбор == '2':
        результат = число1 - число2
    elif выбор == '3':
        результат = число1 * число2
    elif выбор == '4':
        результат = число1 / число2
    else:
        результат = "Ошибка: Неверный выбор"

print("Результат:", результат)