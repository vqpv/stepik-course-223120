data_volume, cpu_load, memory, server_connection = input().split()

data_volume = float(data_volume)         # Объём данных (ТБ)
cpu_load = float(cpu_load)                 # Загрузка процессора (%)
memory = float(memory)                     # Доступная память (ГБ)
server_connection = server_connection == "True"  # Наличие соединения

print(data_volume <= 1.0 and cpu_load <= 70 and memory >= 16 and server_connection)
