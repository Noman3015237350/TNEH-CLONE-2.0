#TNEH CLONE 2.0 - Facebook Account Checker Tool

#📌 Overview

TNEH CLONE 2.0 is an advanced Facebook account checker tool developed by NOMAN HACKER. This tool provides multiple methods for checking Facebook accounts with various features and customization options.

#✨ Features

· Multiple Cloning Methods (8 different methods)
· File-Based Cloning - Check accounts from file
· Random Country Cloning - Generate random numbers for 9 countries
· Old Account Cloning - Check old Facebook accounts
· Proxy Support - Auto-download proxy list
· User-Agent Rotation - Random Android user agents
· Cookies Extraction - Save session cookies
· Voice Notifications - Espeak integration
· Colorful Interface - ANSI colored output
· Multi-threading - Fast checking with concurrent threads

#🌍 Supported Countries for Random Cloning

1. 🇧🇩 Bangladesh
2. 🇲🇾 Malaysia
3. 🇮🇳 India
4. 🇳🇵 Nepal
5. 🇵🇰 Pakistan
6. 🇦🇫 Afghanistan
7. 🇳🇬 Nigeria
8. 🇺🇸 USA
9. 🇮🇩 Indonesia

#📋 Prerequisites

Termux Installation

```bash
pkg update && pkg upgrade
pkg install python
pkg install git
pkg install espeak
```

Python Dependencies

```bash
pip install requests bs4 rich urllib3 httplib2 arrow mechanize
```

#🚀 Installation

Method 1: Clone from GitHub

```bash
git clone https://github.com/Noman3015237350/TNEH-CLONE-2.0.git
cd TNEH-CLONE-2.0
python add.py
```

Method 2: Manual Installation

```bash
# Create directory
mkdir TNEH-CLONE
cd TNEH-CLONE

# Download the tool
wget https://raw.githubusercontent.com/Noman3015237350/TNEH-CLONE-2.0/main/add.py

# Run the tool
python add.py
```

#📁 File Structure

```
TNEH-CLONE-2.0/
├── add.py                    # Main tool file
├── socksku.txt              # Proxy list file
├── TNEH-FILE-M1-OK.txt     # File method 1 OK results
├── TNEH-FILE-M1-CP.txt     # File method 1 CP results
├── TNEH-RNDM-OK.txt        # Random method OK results
├── TNEH-RNDM-CP.txt        # Random method CP results
├── TNEH-OLD-OK.txt         # Old method OK results
└── README.md               # This file
```

#🎯 Usage Guide

Step 1: Start the Tool

```bash
python add.py
```

Step 2: Choose Option

```
[1] START FILE CLONING
[2] START RANDOM ALL COUNTRY CLONING
[3] START OLD CLONING
[0] EXIT ALL CLONING
```

Option 1: File Cloning

1. Enter file path (e.g., /sdcard/uid.txt)
2. Choose password option (Auto Pass 1/2 or Custom)
3. Select method (M1 to M8)
4. Choose whether to show CP UID
5. Choose whether to show cookies

File Format: email|password or uid|name

Option 2: Random Cloning

1. Select country
2. Enter SIM code
3. Set limit
4. Choose method
5. Start cloning

Option 3: Old Cloning

1. Set limit
2. Start checking old accounts

#🔧 Configuration

Supported Methods

· M1: Standard login method
· M2: Alternative login method
· M3-M8: Various API methods

Password Options

1. Auto Pass 1: Recommended password combinations
2. Auto Pass 2: Alternative password combinations
3. Custom Pass: Manual password entry

#📊 Results Files

The tool saves results in /sdcard/ directory:

· TNEH-FILE-M*-OK.txt - File method OK accounts
· TNEH-FILE-M*-CP.txt - File method CP accounts
· TNEH-RNDM-OK.txt - Random method OK accounts
· TNEH-RNDM-CP.txt - Random method CP accounts
· TNEH-OLD-OK.txt - Old method OK accounts

#⚠️ Disclaimer

Educational Purpose Only!

· This tool is for educational purposes only
· Use only on accounts you own or have permission to test
· The developer is not responsible for any misuse
· Unauthorized access to accounts is illegal

#🔗 Connect with Developer

· Telegram: @Noman301523
· GitHub: Noman3015237350
· Team: TNEH TEAM

#📝 License

This project is for educational purposes only. Use responsibly.

#🆘 Support

For issues and support:

1. Check prerequisites are installed
2. Ensure internet connection
3. Verify file permissions
4. Contact via Telegram for help

#🎨 Features in Detail

Proxy System

· Auto-downloads proxy list
· Socks4 proxy support
· Proxy rotation

User-Agent Generation

· Random Android devices
· Multiple brands (Samsung, Xiaomi, Tecno, etc.)
· Realistic device parameters

Account Analysis

· UID to year estimation
· Account age detection
· Status classification (OK/CP/2FA)

#🚫 Terms of Use

By using this tool, you agree to:

1. Use only for legal purposes
2. Not engage in unauthorized access
3. Take full responsibility for your actions
4. Respect others' privacy

#🔄 Updates

Check GitHub for latest updates and improvements:

```
https://github.com/Noman3015237350/TNEH-CLONE-2.0
```

---

Made with ❤️ by NOMAN HACKER
