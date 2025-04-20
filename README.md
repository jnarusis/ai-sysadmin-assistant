# AI Sysadmin Assistant

A command-line learning tool that uses GPT to generate, explain, and break down Bash scripts and Linux/DevOps concepts—built for hands-on learning and skill-building.

## 🚀 What It Does

This assistant helps you:

- 🛠️ Generate Bash scripts from natural language prompts
- 🧠 Learn and review Linux/DevOps concepts
- 📖 Break down scripts line-by-line for better understanding
- 💾 Save outputs as files for your own script library or documentation

Powered by the OpenAI API and written in Python.

## 🎯 Why I Built This

I'm building a strong foundation in systems administration and automation with a long-term goal of moving deeply into AI and prompt engineering. This project helps me:

- Practice Python, Bash, and prompt design
- Learn by building something useful
- Capture scripts and explanations I can refer to later
- Keep expanding my own toolkit as I grow

## 🛠️ How to Use It

1. **Clone the repo**:
   ```bash
   git clone git@github.com:jnarusis/ai-sysadmin-assistant.git
   cd ai-sysadmin-assistant
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install openai python-dotenv
   ```

4. **Set up your `.env` file** with your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-api-key
   ```

5. **Run the tool**:
   ```bash
   python3 main.py
   ```

## 💡 Example Prompts

- `Write a Bash script to archive logs older than 7 days in /var/log`
- `Explain how systemd services work`
- `Break down this script line by line:` (then paste a script)

## 🧱 Folder Structure

```
ai-sysadmin-assistant/
├── main.py           # Core script
├── .env              # (not tracked)
├── .gitignore
├── venv/             # (not tracked)
└── README.md
```

## 🔮 Future Plans

- Add PowerShell scripting support
- Organize output into folders (`scripts/`, `explanations/`, etc.)
- Add logging or history tracking
- Possibly build a web UI in Streamlit or Flask later

## 📘 License

MIT License. Use, adapt, or contribute freely.

