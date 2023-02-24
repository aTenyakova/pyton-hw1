# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input("Введите число: "))
firstNumber = number % 10
secondNumber = number % 100 // 10
thirdNumber = number // 100
print(firstNumber + secondNumber + thirdNumber)