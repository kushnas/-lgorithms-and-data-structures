def is_valid_parentheses(s: str) -> bool:
    # Создаем стек для хранения открывающих скобок
    stack = []
    
    # Словарь для соответствия открывающих и закрывающих скобок
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        # Если символ - это закрывающая скобка
        if char in mapping:
            # Извлекаем верхний элемент стека, если стек не пуст
            top_element = stack.pop() if stack else '#'
            print(top_element)
            print(stack.pop() if stack else '#')
            print(top_element)
            # Проверяем, соответствует ли открывающая скобка закрывающей
            if mapping[char] != top_element:
                return False
        else:
            # Если символ - это открывающая скобка, добавляем его в стек
            stack.append(char)
    
    # Если стек пуст, все скобки были правильно закрыты
    return not stack

# Примеры использования
print(is_valid_parentheses("()"))        # True
print(is_valid_parentheses("()[]{}"))    # True
print(is_valid_parentheses("(]"))        # False
print(is_valid_parentheses("([)]"))      # False
print(is_valid_parentheses("{[]}"))      # True