🔐 Password Generator (Python)
A customizable and persistent password generator written in Python. The program creates secure random passwords using predefined or user-defined settings and saves these preferences for future use.

📦 Features
✅ Immediate password generation on startup using saved or default settings

🛠️ Customizable settings, including:
  - Password length
  - Use of Turkish characters (ç, ğ, ö, etc.)
  - Use of special characters
  - Option to include only specific special characters
  - Include/exclude uppercase letters
  - Include/exclude lowercase letters
  - Include/exclude digits

💾 Persistent settings using a local JSON file (settings.json)

🧠 Simple CLI interface with menu options

🚀 Getting Started
1. Clone or Download the Repository
    git clone https://github.com/mustafaduzgunn/passGenerator.git
    cd password-generator
2. Run the Program
  Make sure you have Python 3 installed.
    python passwordGenerator.py

📂 File Structure
password-generator/

├── password_generator.py   # Main program

├── settings.json           # Settings file (auto-generated on first run)

└── README.md               # Project documentation

🖥️ Usage
On program start:
A password is automatically generated using current settings.
You will then be prompted with the following menu:

[1] Generate new password
[2] Change settings
[0] Exit

⚙️ Settings Explained
Setting	Description
  - length	                    Length of the generated password
  - turkish_characters	        Whether to include Turkish letters (ç, ğ, etc.)
  - use_special_characters	    Whether to include any special characters
  - custom_special_characters	  If defined, only these characters are used as special characters
  - include_uppercase	          Whether to include A-Z
  - include_lowercase	          Whether to include a-z
  - include_digits	            Whether to include 0-9

📝 Example Output
✨ Your first password (with current settings):
🔐 m8A$w@fX2z!Lk

[1] Generate new password
[2] Change settings
[0] Exit

📌 Requirements
Python 3.6+

No external dependencies required

🛡️ Security Note
This program is intended for educational and personal use. For critical applications (e.g., secure logins or password management), consider using vetted password managers.

📄 License
This project is open-source and free to use under the MIT License.
