import logging
from pynput import mouse, keyboard
from datetime import datetime

# Налаштування Логера
# Створюється log_file.txt.
# format='...' додає дату та час автоматично до кожного запису.
# datefmt визначає формат дати.
# encoding='utf-8' додає кодировку UTF-8, для коректного відображення українських символів.
logging.basicConfig(
    filename=("activity_log.txt"),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)

print("Логер запущено. Усі дії записуються у файл 'activity_log.txt'.")
print("Щоб зупинити програму, натисніть ESC.")


# Функції для Клавіатури

def on_press(key):
    try:
        # Для звичайних символів (букви, цифри)
        logging.info(f"КЛАВІАТУРА: Натиснуто клавішу '{key.char}'")
    except AttributeError:
        # Для спеціальних клавіш (Enter, Space, Shift і тд)
        logging.info(f"КЛАВІАТУРА: Натиснуто спец. клавішу {key}")

    # Умова виходу: Якщо натиснуто ESC, зупиняємо логер
    if key == keyboard.Key.esc:
        logging.info("ПРОГРАМА: Користувач ініціював зупинку (ESC)")
        return False

    return None


# Функції для мишки

def on_move(x, y):
    # Можна би було для переміщення мишки зробити так:
    # logging.info(f"МИША: Переміщення на позицію ({x}, {y})")
    pass

# Функція перевіряє чи натиснуто чи відпущено кнопку миші
def on_click(x, y, button, pressed):
    action = "Натиснуто" if pressed else "Відпущено"
    logging.info(f"МИША: {action} {button} на позиції ({x}, {y})")

# Функція перевіряє чи натиснуто чи  скрол вгору чи вниз
def on_scroll(x, y, dx, dy):
    direction = "вниз" if dy < 0 else "вгору"
    logging.info(f"МИША: Прокрутка {direction} на позиції ({x}, {y})")


# Запуск логування і прослуховування

# Запускаємо Listener для клавіатури та мишки
# Вони працюють у фоновому режимі до моменту повернення, тобто закриття програми
if __name__ == "__main__":
    # 1. Створюємо слухачів
    m_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
    k_listener = keyboard.Listener(on_press=on_press)

    # 2. Запускаємо їх
    m_listener.start()
    k_listener.start()


    k_listener.join()
    m_listener.stop()

    print("Логування завершено.")