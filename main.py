import os
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

last_output = ""

def generate_bash_script():
    global last_output
    task = input("\nDescribe the Bash script you want: ")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a Linux shell expert. Return only the script code."},
            {"role": "user", "content": task}
        ]
    )
    last_output = response.choices[0].message.content
    print("\n=== Bash Script Output ===\n")
    print(last_output)

def explain_concept():
    global last_output
    topic = input("\nWhat concept do you want explained? ")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Linux tutor who explains clearly and simply."},
            {"role": "user", "content": topic}
        ]
    )
    last_output = response.choices[0].message.content
    print("\n=== Explanation ===\n")
    print(last_output)

def breakdown_script():
    global last_output
    print("\nPaste the Bash script you want explained. Type ':end' on a new line when finished:")
    lines = []
    while True:
        line = input()
        if line.strip() == ":end":
            break
        lines.append(line)
    script = "\n".join(lines)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a Bash expert who breaks down scripts line by line with clear explanations."},
            {"role": "user", "content": script}
        ]
    )
    last_output = response.choices[0].message.content
    print("\n=== Script Breakdown ===\n")
    print(last_output)

def save_output():
    global last_output
    if not last_output:
        print("\nNo output to save yet.")
        return
    filename = input("\nEnter filename to save (default: output_<timestamp>.txt): ")
    if not filename:
        filename = f"output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write(last_output)
    print(f"\nSaved to {filename}")

def main():
    while True:
        print("\n=== AI Scripting Lab ===")
        print("1. Generate a Bash script")
        print("2. Explain a Linux/DevOps concept")
        print("3. Break down a script line by line")
        print("4. Save last output to file")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            generate_bash_script()
        elif choice == "2":
            explain_concept()
        elif choice == "3":
            breakdown_script()
        elif choice == "4":
            save_output()
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
