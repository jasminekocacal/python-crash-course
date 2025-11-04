def main():
    first_name = "ada"
    last_name = "lovelace"
    full_name = f"{first_name} {last_name}"
    print(full_name)
    print(f"Hello {first_name} {last_name}!")
    print(f"Hello {full_name.title()}!")

    message = f"Hello there, {full_name.upper()}"
    print(message)

    
if __name__ == '__main__':
    main()