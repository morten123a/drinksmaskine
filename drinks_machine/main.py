from drinks_machine import DrinksMachine

def main():
    drinks_machine = DrinksMachine()
    while True:
        try:
            drinks_machine.update()
        except Exception as e:
            print(e)
            break
        except KeyboardInterrupt:
            break
    print("shutting down gracefully...")
    drinks_machine.destroy()

if __name__ == "__main__":
    main()
