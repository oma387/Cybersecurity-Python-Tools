from datetime import datetime


def local_input_capture():
    captured_keys = []

    print("=" * 50)
    print("        LOCAL KEYLOGGER SIMULATOR")
    print("=" * 50)
    print("Everything captured is typed directly into this terminal.")
    print("Type STOP to end the session.\n")

    while True:
        user_input = input("Enter text: ")

        # Stop command
        if user_input.upper() == "STOP":
            break

        # Store timestamp + input
        entry = {
            "time": datetime.now().strftime("%H:%M:%S"),
            "input": user_input
        }

        captured_keys.append(entry)

        print(
            f"[+] {entry['time']} | "
            f"Captured: {entry['input']}"
        )

    return captured_keys


def display_results(data):
    print("\n" + "=" * 50)
    print("             CAPTURE REPORT")
    print("=" * 50)

    if not data:
        print("No data was captured.")
        return

    for number, entry in enumerate(data, start=1):
        print(
            f"{number}. "
            f"[{entry['time']}] "
            f"{entry['input']}"
        )

    print(f"\nTotal entries: {len(data)}")


def save_to_file(data, filename="capture_log.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("LOCAL KEYLOGGER SIMULATOR LOG\n")
        file.write("=" * 40 + "\n")

        for entry in data:
            file.write(
                f"[{entry['time']}] {entry['input']}\n"
            )

    print(f"[+] Log saved to {filename}")


# Main program
final_data = local_input_capture()

display_results(final_data)

save_to_file(final_data)