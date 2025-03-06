def cute_converter():
    print("✨ Welcome to the Cute Unit Converter! ✨")
    print("🐻 Choose a category:")
    print("1️⃣ Temperature 🌡️\n2️⃣ Weight ⚖️\n3️⃣ Length 📏")

    choice = input("👉 Enter your choice (1/2/3): ")

    if choice == "1":
        print("\n🌡️ Temperature Conversions 🌡️")
        print("1. Celsius to Fahrenheit (°C → °F)")
        print("2. Fahrenheit to Celsius (°F → °C)")
        temp_choice = input("👉 Choose an option (1/2): ")
        temp = float(input("💫 Enter temperature value: "))

        if temp_choice == "1":
            result = (temp * 9/5) + 32
            print(f"🎉 {temp}°C is {result:.2f}°F! 🌞")
        elif temp_choice == "2":
            result = (temp - 32) * 5/9
            print(f"🎉 {temp}°F is {result:.2f}°C! ❄️")
        else:
            print("😵 Oops! Invalid choice.")

    elif choice == "2":
        print("\n⚖️ Weight Conversions ⚖️")
        print("1. Kilograms to Pounds (kg → lb)")
        print("2. Pounds to Kilograms (lb → kg)")
        weight_choice = input("👉 Choose an option (1/2): ")
        weight = float(input("💫 Enter weight value: "))

        if weight_choice == "1":
            result = weight * 2.20462
            print(f"🎉 {weight} kg is {result:.2f} lb! 🏋️‍♂️")
        elif weight_choice == "2":
            result = weight * 0.453592
            print(f"🎉 {weight} lb is {result:.2f} kg! 🐘")
        else:
            print("😵 Oops! Invalid choice.")

    elif choice == "3":
        print("\n📏 Length Conversions 📏")
        print("1. Meters to Feet (m → ft)")
        print("2. Feet to Meters (ft → m)")
        length_choice = input("👉 Choose an option (1/2): ")
        length = float(input("💫 Enter length value: "))

        if length_choice == "1":
            result = length * 3.28084
            print(f"🎉 {length} m is {result:.2f} ft! 🚀")
        elif length_choice == "2":
            result = length * 0.3048
            print(f"🎉 {length} ft is {result:.2f} m! 🌍")
        else:
            print("😵 Oops! Invalid choice.")

    else:
        print("😵 Oops! Invalid category. Try again! 💖")

# Run the cute converter
cute_converter()
