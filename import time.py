import time

# Создаем класс таймера и секундомера
class TimerStopwatch:
    def start_timer(self, seconds):
        print(f"Таймер запущен на {seconds} секунд.")
        time.sleep(seconds)
        return "Таймер завершен!"

    def start_stopwatch(self, duration):
        print("Секундомер запущен.")
        start_time = time.time()
        time.sleep(duration)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return f"Секундомер остановлен. Прошло: {elapsed_time:.2f} секунд."

# Пример использования
timer_stopwatch = TimerStopwatch()

# Запуск таймера на 5 секунд и секундомера на 3 секунды
timer_result = timer_stopwatch.start_timer(5)
stopwatch_result = timer_stopwatch.start_stopwatch(3)

print(timer_result)
print(stopwatch_result)