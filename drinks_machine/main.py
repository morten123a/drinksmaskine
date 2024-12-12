from drinks_machine import DrinksMachine
import traceback

def main():
    drinks_machine = DrinksMachine()
    while True:
        try:
            drinks_machine.update()
        except Exception:
            traceback.print_exc()
            break
        except KeyboardInterrupt:
            break
    print("shutting down gracefully...")
    drinks_machine.destroy()

if __name__ == "__main__":
    main()
