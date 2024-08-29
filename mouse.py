import pyautogui
import keyboard

def move_cursor_to_center_of_second_monitor():
    screen_width, screen_height = pyautogui.size()

    # Отримання координат початку другого монітора
    second_monitor_x = screen_width
    second_monitor_y = 0

    # Отримання розмірів другого монітора
    second_monitor_width, second_monitor_height = pyautogui.size()

    # Розрахунок координат центра другого монітора
    center_x = second_monitor_x + second_monitor_width // 2
    center_y = second_monitor_y + second_monitor_height // 2

    # Переміщення курсора у центр другого монітора
    pyautogui.moveTo(center_x, center_y, duration=0.25)

if __name__ == "__main__":
    # Функція, яка буде викликана при натисканні на клавішу "F12"
    keyboard.add_hotkey('f12', move_cursor_to_center_of_second_monitor)

    # Прослуховування клавіші
    keyboard.wait('esc')  # Чекаємо, поки не буде натиснута клавіша "Esc" для завершення програми
