formatters = [
    "plain", "bold", "italic", "header", "link",
    "inline-code", "ordered-list", "unordered-list",
    "new-line"
]

markdown = ""


def show_help():
    print("Available formatters: " + " ".join(formatters))
    print("Special commands: !help !done")


while True:
    formatter = input("Choose a formatter: ")

    if formatter == "!help":
        show_help()
        continue

    if formatter == "!done":
        with open("output.md", "w", encoding="utf-8") as file:
            file.write(markdown)
        break

    if formatter not in formatters:
        print("Unknown formatting type or command")
        continue

    if formatter == "plain":
        text = input("Text: ")
        markdown += text

    elif formatter == "bold":
        text = input("Text: ")
        markdown += f"**{text}**"

    elif formatter == "italic":
        text = input("Text: ")
        markdown += f"*{text}*"

    elif formatter == "inline-code":
        text = input("Text: ")
        markdown += f"`{text}`"

    elif formatter == "header":
        level = int(input("Level: "))

        if level < 1 or level > 6:
            print("The level should be within the range of 1 to 6")
            continue

        text = input("Text: ")
        markdown += "\n" + "#" * level + " " + text + "\n"

    elif formatter == "link":
        label = input("Label: ")
        url = input("URL: ")
        markdown += f"[{label}]({url})"

    elif formatter == "new-line":
        markdown += "\n"

    elif formatter == "unordered-list":
        rows = int(input("Number of rows: "))

        while rows <= 0:
            print("The number of rows should be greater than zero")
            rows = int(input("Number of rows: "))

        for i in range(1, rows + 1):
            text = input(f"Row #{i}: ")
            markdown += f"\n* {text}"

    elif formatter == "ordered-list":
        rows = int(input("Number of rows: "))

        while rows <= 0:
            print("The number of rows should be greater than zero")
            rows = int(input("Number of rows: "))

        for i in range(1, rows + 1):
            text = input(f"Row #{i}: ")
            markdown += f"\n{i}. {text}"

    print(markdown)

