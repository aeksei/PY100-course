pages = int(input())
lines = int(input())
chars = int(input())

total_chars = pages * lines * chars
total_bytes = total_chars * 1

disk_size = 1.44 * 1024 * 1024  # размер в байтах

print(disk_size // total_bytes)
