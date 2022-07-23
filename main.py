import requests
import random
import time
import json

print("Введите Discord-token")
while True:
    TOKEN = str(input())
    r = requests.get(f"https://discord.com/api/v9/users/@me?token={TOKEN}")
    if "message" in r.json().keys():
        if r.json()["message"] == "401: Unauthorized":
            print("Неверный Discord-token, введите токен аккаунта:")
            continue
    elif "id" in r.json().keys():
        print("Получен действующий токен, запуск поиска Врат Штейна...")
        break
    else:
        print("Неверный Discord-token, введите токен аккаунта:")
        continue

attractors = ["α", "β", "γ", "δ", "ω", "???"]

steins_gate = 1.048596
counter = 0

start = time.perf_counter()


def steins_gate():
    end_time = start - time.perf_counter() // 3600
    if (end_time % 10 == 0) or (5 <= end_time % 10 <= 9):
        hours = "часов"
    elif end_time % 10 == 1:
        hours = "час"
    elif 2 <= end_time % 10 <= 4:
        hours = "часа"

    if (counter % 10 == 0) or (5 <= counter % 10 <= 9):
        counter = str(counter) + "попыток"
    elif counter % 10 == 1:
        counter = str(counter) + "попытку"
    elif 2 <= counter % 10 <= 4:
        counter = str(counter) + "попытки"
    status = f"1.048596.. спустя {counter} и {end_time} {hours}"
    status_data = json.dumps(
        {"custom_status": {"text": status}})
    requests.patch("https://discordapp.com/api/v6/users/@me/settings", headers={
        "Authorization": TOKEN, "Content-Type": "application/json"}, data=status_data)


print("Поиск Врат Штейна начат!")
while True:
    convergence = round(random.uniform(-1.999999, 3.999999), 6)
    print(convergence)
    if convergence != 1.048596:
        if (convergence != 1.048595) or (convergence != 1.048597):
            if 0 <= convergence < 1:
                attractor = attractors[0]
            elif 1 <= convergence < 2:
                attractor = attractors[1]
            elif 2 <= convergence < 3:
                attractor = attractors[2]
            elif 3 <= convergence < 4:
                attractor = attractors[3]
            elif -1 <= convergence < 0:
                attractor = attractors[4]
            elif -2 <= convergence < -1:
                attractor = attractors[5]
            status = f"{str(convergence) + attractor} - текущая дивергенция мировой линии"
            status_data = json.dumps(
                {"custom_status": {"text": status}})
            requests.patch("https://discordapp.com/api/v6/users/@me/settings", headers={
                           "Authorization": TOKEN, "Content-Type": "application/json"}, data=status_data)
        else:
            status = f"Конец. {convergence} - Можно сказать последнее предупреждение от Бога тем, кто ещё противится."
            status_data = json.dumps(
                {"custom_status": {"text": status}})
            requests.patch("https://discordapp.com/api/v6/users/@me/settings", headers={
                           "Authorization": TOKEN, "Content-Type": "application/json"}, data=status_data)
            print("Поиск Врат Штейна невозможно продолжить, ...")
            break
    else:
        steins_gate()
        print("Поиск Врат Штейна завершен.")
        break
    counter += 1
    time.sleep(5)

input("Нажмите любую клавишу для выхода из программы...")
