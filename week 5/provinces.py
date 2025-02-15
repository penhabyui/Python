def main():
    text_list = read_list("provinces.txt")
    print(text_list)

    if len(text_list) > 1:
        text_list.pop(0)    
        text_list.pop()
    
    count = text_list.count("Alberta")
    print(f"Alberta occurs {count} times in the modified list")

def read_list(filename):
    text_list = []

    with open(filename, "rt") as text_file:
        for line in text_file:
            text_list.append(line.strip())

        for i in range(len(text_list)):
            if text_list[i] =="AB":
                text_list[i] = "Alberta"

    return text_list 

if __name__ == "__main__":
    main()
