import figure

# ➕ Basic Arithmetic Operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "🚫 Error: Division by zero is not allowed."
    return a / b

# 🧠 Dictionary for Operation Mapping
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# 🧮 Main Calculation Function
def calculate(a, operation, b):
    if operation in operations:
        result = operations[operation](a, b)
        print(f"🧾 {a} {operation} {b} = {result}")
        return result
    else:
        print("❌ Invalid operation. Please choose from ➕ ➖ ✖️ ➗")
        return None

# 🚀 Application Start
print(figure.logo)
goal = True

while goal:
    # 🔢 Get the first number
    a = float(input("🟢 What's The First Number❓: "))

    while True:
        # ⚙️ Display available operations
        print("\n⚙️ Available Operations:\n➕  \n➖  \n✖️  \n➗  ")
        operation = input("👉 Pick An Operation: ")
        b = float(input("🔵 What's The Second Number❓: "))

        result = calculate(a, operation, b)

        # 🔁 Continue or restart or exit
        choice = input(
            f"\n🔄 Type 'y' to continue with the result ({result}),\n"
            "🆕 Type 'n' to start a new calculation,\n"
            "🚪 Or type 'exit' to quit: "
        ).lower()

        if choice == 'y':
            a = result
        elif choice == 'n':
            print("\n🔁 Starting New Calculation...\n")
            print(figure.logo)
            break
        elif choice == 'exit':
            print("👋 Goodbye!")
            goal = False
            break
