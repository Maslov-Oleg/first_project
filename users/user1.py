import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from author import author

login = "Oleg"
password = "WATAFAKA67"

print(f"Ваш логин - {login}, ваш пароль - {password}.")
print("Вы вошли в систему!")

print("О проекте:")
author()