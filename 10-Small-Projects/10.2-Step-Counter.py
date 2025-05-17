print("🏃 STEP COUNTER 🏃")
daily_goal = input("❓ What is your daily step goal? ❓")
current_steps = input("🌟 How many steps you have taken today? 🌟")

remaining = int(daily_goal) - int(current_steps)

if remaining > 0:
    print(f"👉 You have {remaining} steps remaining today!")
else:
    print("🎉 Congratulations! You have met your goal!")