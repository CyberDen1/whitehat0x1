def modify_every_tenth_byte(input_file, output_log_file):
    try:
        with open(input_file, 'rb') as f:
            all_bytes = list(f.read())

        changed_bytes = []

        start_index = 1
        step = 1
        max_iterations = 30

        for iteration in range(max_iterations):
            i = start_index + iteration * step

            if i >= len(all_bytes):
                break

            original_value = all_bytes[i]
            changed_bytes.append((i, original_value))
            all_bytes[i] = 0x03

        with open(input_file, 'wb') as f:
            f.write(bytes(all_bytes))

        with open(output_log_file, 'w', encoding='utf-8') as log:
            log_entries = []
            for index, byte_value in changed_bytes:
                hex_str = f"{byte_value:02X}"
                entry = f"d[{index}] = 0x{hex_str}"
                log_entries.append(entry)
            log.write("; ".join(log_entries) + ";")

        print(f"Успешно изменено {len(changed_bytes)} байт в файле {input_file}")
        print(f"Информация о заменённых байтах записана в {output_log_file}")

    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден")
    except PermissionError:
        print(f"Ошибка: нет прав для доступа к файлу {input_file}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    modify_every_tenth_byte('cs.bin', 'log.txt')
