# 007-TheBond 🕵️‍♂️

<div align="center">

![007-TheBond](https://img.shields.io/badge/007--TheBond-v3.0-blue?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Available-blue?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

**A powerful Python-based OSINT (Open Source Intelligence) tool for gathering information across multiple platforms and services.**

*007-TheBond helps security researchers, investigators, and ethical hackers collect publicly available information from various sources including social media profiles, phone numbers, IP addresses, and more.*

[🐳 Docker Hub](https://hub.docker.com/r/deadshot0x7/007-thebond) • [💬 Discord](https://discord.gg/WAhQ8EcV4C) • [☕ Support](https://www.buymeacoffee.com/Deadshot0x7) • [🐛 Issues](https://github.com/Deadshot0x7/007-TheBond/issues)

</div>

---

## 🔍 Features

| Feature | Description | Status |
|---------|-------------|--------|
| 📸 **Instagram OSINT** | Gather information from Instagram profiles | ✅ Working |
| 📞 **Phone Number OSINT** | Extract details using phone numbers | ✅ Working |
| 👤 **Username Search** | Find username presence across social media platforms | ✅ Working |
| 🌐 **Web Search** | Perform comprehensive web searches | ✅ Working |
| 🌍 **IP Lookup** | Retrieve detailed IP address information | ✅ Working |
| 📧 **Email Lookup** | Check email breaches using Have I Been Pwned API | ✅ Working |
| 🔄 **Cross-Platform** | Works on multiple operating systems | ✅ Working |

---

## 🚀 Installation & Usage

### 🐳 **Method 1: Docker (Recommended)**

**Why Docker?** Docker ensures consistent performance across all platforms and eliminates dependency issues.

```bash
# Pull the latest image
docker pull deadshot0x7/007-thebond:latest

# Run the tool interactively
docker run -it deadshot0x7/007-thebond:latest

# Run with volume mounting to save results
docker run -it -v $(pwd)/results:/app/results deadshot0x7/007-thebond:latest
```

**Docker Compose (Optional):**
```yaml
version: '3.8'
services:
  osint-tool:
    image: deadshot0x7/007-thebond:latest
    stdin_open: true
    tty: true
    volumes:
      - ./results:/app/results
      - ./config:/app/config
```

### 🛠️ **Method 2: Local Installation**

**Quick Setup Scripts:**

#### For Linux/macOS:
```bash
git clone https://github.com/Deadshot0x7/007-TheBond.git
cd 007-TheBond
bash run_007-TheBond.sh
```

#### For Windows:
```bash
git clone https://github.com/Deadshot0x7/007-TheBond.git
cd 007-TheBond
run_007-TheBond.bat
```

### 🔧 **Method 3: Manual Installation**

```bash
# 1. Clone the repository
git clone https://github.com/Deadshot0x7/007-TheBond.git
cd 007-TheBond

# 2. Create and activate virtual environment
# Linux/macOS:
python3 -m venv venv
source venv/bin/activate

# Windows:
python -m venv venv
venv\Scripts\activate

# 3. Install requirements
pip install -r requirements.txt
# OR using uv (faster)
uv pip install -r requirements.txt

# 4. Run the script
cd scripts
python 007-TheBond.py
```

---

## 🖥️ **Platform Compatibility**

### ✅ **Fully Tested & Working**
| Platform | Status | Installation Method | Notes |
|----------|--------|-------------------|-------|
| 🐧 **Kali Linux** | ✅ **Perfect** | Native / Docker | Recommended for security research |
| 🦜 **Parrot Security OS** | ✅ **Perfect** | Native / Docker | Excellent performance |
| 🔥 **Garuda Linux** | ✅ **Perfect** | Native / Docker | All features working |
| 🏹 **Arch Linux** | ✅ **Perfect** | Native / Docker | Latest packages support |
| 🐳 **Docker** | ✅ **Perfect** | Docker | **Universal compatibility** |
| 📱 **Termux (Android)** | ⚠️ **Partial** | Native | Instagram OSINT not working |

### ⚠️ **Limited Support**
| Platform | Status | Recommended Solution | Issues |
|----------|--------|---------------------|--------|
| 🪟 **Windows 10/11** | ⚠️ **Partial** | **Use Docker** | Dependency conflicts |
| 🍎 **macOS** | ⚠️ **Partial** | **Use Docker** | Library compatibility issues |
| 🐧 **Ubuntu/Debian** | ⚠️ **Mixed** | **Use Docker** | Version-dependent issues |
| 📱 **iOS** | ❌ **Not Supported** | **Use Docker on Mac** | Not compatible |

### 🚫 **Non-Working Distros/Platforms**
> **❌ These platforms are known to have critical issues:**

| Platform | Issue | Recommended Alternative |
|----------|-------|------------------------|
| **CentOS/RHEL 7** | Python version too old | Use Docker or upgrade to RHEL 8+ |
| **Windows 7/8** | Python 3.10+ not available | Use Docker Desktop or upgrade OS |
| **Alpine Linux** | Missing dependencies | Use Docker with Ubuntu base |
| **Raspberry Pi OS (32-bit)** | Architecture limitations | Use 64-bit OS or Docker |
| **OpenSUSE Leap <15.3** | Package conflicts | Use Docker or upgrade |
| **Amazon Linux 1** | EOL, missing packages | Use Amazon Linux 2 + Docker |
| **Any Distro without Python 3.10+** | Python compatibility | **Use Docker (Universal Solution)** |

---

## 📋 **Prerequisites**

### For Native Installation:
- **Python**: 3.10 or higher
- **Git**: Latest version
- **Internet Connection**: Required for OSINT operations
- **pip/uv**: Package manager

### For Docker Installation:
- **Docker**: 20.10+ 
- **Docker Compose**: 2.0+ (optional)
- **4GB RAM**: Minimum recommended
- **Internet Connection**: Required

---

## 🛡️ **Ethical Usage & Legal Disclaimer**

> **⚠️ CRITICAL: This tool is designed for legitimate security research and educational purposes only.**

### ✅ **Authorized Uses:**
- Educational and learning purposes
- Authorized penetration testing
- Security research with proper permissions
- OSINT investigations within legal boundaries
- Cybersecurity awareness training

### ❌ **Prohibited Uses:**
- Harassment, stalking, or intimidation
- Unauthorized surveillance
- Privacy violations
- Illegal data collection
- Corporate espionage
- Any activity violating local/international laws

### 📋 **Legal Requirements:**
- **Always obtain explicit permission** before investigating individuals
- **Respect privacy laws** in your jurisdiction (GDPR, CCPA, etc.)
- **Use responsibly** and within legal frameworks
- **Document your authorization** for security assessments

**Disclaimer**: The developer (@Deadshot0x7) assumes no responsibility for misuse of this tool. Users are solely responsible for ensuring legal and ethical compliance.

---

## 🔧 **Configuration**

### Environment Variables:
```bash
# Optional configurations
export OSINT_OUTPUT_DIR="/path/to/results"
export OSINT_CONFIG_FILE="/path/to/config.json"
export PYTHONPATH="${PYTHONPATH}:/path/to/007-TheBond"
```

### API Keys (Optional):
Some features may require API keys. Create a `.env` file:
```env
HAVEIBEENPWNED_API_KEY=your_api_key_here
SHODAN_API_KEY=your_shodan_key
```

---

## 🐳 **Docker Advantages**

**Why we recommend Docker:**

| Advantage | Description |
|-----------|-------------|
| 🔄 **Universal Compatibility** | Works on any system with Docker |
| 📦 **No Dependency Issues** | All requirements pre-installed |
| 🛡️ **Isolated Environment** | Doesn't affect your system |
| ⚡ **Quick Setup** | One command to run |
| 🔄 **Consistent Results** | Same environment everywhere |
| 🧹 **Easy Cleanup** | Remove container when done |

---

## 📊 **Usage Statistics**

```bash
# Run with Docker
docker run -it deadshot0x7/007-thebond:latest

# Example session:
┌─────────────────────────────────────────┐
│         007-TheBond v3.0                │
│     OSINT Intelligence Toolkit         │
└─────────────────────────────────────────┘

[1] Instagram OSINT
[2] Phone Number OSINT  
[3] Username Search
[4] Web Search
[5] IP Lookup
[6] Email Lookup
[0] Exit

Select option: _
```

---

## 🤝 **Contributing**

We welcome contributions! Here's how:

### 🍴 **Quick Contribution:**
```bash
# 1. Fork the repository
# 2. Create feature branch
git checkout -b feature/AmazingFeature

# 3. Make changes and commit
git commit -m 'Add some AmazingFeature'

# 4. Push and create PR
git push origin feature/AmazingFeature
```

### 📋 **Contribution Guidelines:**
- Follow Python PEP 8 standards
- Add docstrings for new functions
- Test on multiple platforms
- Update README for new features
- Maintain ethical usage standards

---

## 🔍 **Troubleshooting**

### Common Issues:

**Issue: "Module not found"**
```bash
# Solution: Use Docker
docker run -it deadshot0x7/007-thebond:latest
```

**Issue: "Permission denied"**
```bash
# Linux/macOS: Fix permissions
chmod +x run_007-TheBond.sh
# Or use Docker (recommended)
```

**Issue: "Python version incompatible"**
```bash
# Solution: Use Docker for consistent Python 3.10
docker run -it deadshot0x7/007-thebond:latest
```

---

## 📞 **Support & Community**

<div align="center">

### 💬 **Join Our Community - We're Waiting for You!**

**🚀 Ready to level up your OSINT skills?** Join our **vibrant Discord community** where security researchers, ethical hackers, and OSINT enthusiasts gather to share knowledge, get instant help, and collaborate on investigations!

**🎯 What you'll get:**
- ⚡ **Instant support** from experienced researchers
- 🧠 **Pro tips & tricks** for advanced OSINT techniques  
- 🔥 **Exclusive updates** about new features & tools
- 🤝 **Network with experts** in cybersecurity field
- 📚 **Learning resources** and guided tutorials
- 🎉 **Fun community events** and challenges

**Don't investigate alone - join the pack!** 🐺

[![Discord](https://img.shields.io/discord/YOUR_DISCORD_ID?color=7289da&label=Join%20Discord%20Community&logo=discord&logoColor=white&style=for-the-badge)](https://discord.gg/WAhQ8EcV4C)

### ☕ **Fuel the Development:**

**Love 007-TheBond?** Help us keep building amazing OSINT tools! Your support means everything to our small but passionate development team. Every contribution helps us add new features, fix bugs faster, and keep the tool free for everyone! 🙏

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black)](https://www.buymeacoffee.com/Deadshot0x7)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-FF5E5B?style=for-the-badge&logo=ko-fi&logoColor=white)](http://www.ko-fi.com/deadshot0x7)
[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/Deadshot0x7?locale.x=en_GB)

**UPI**: `sviquarahmed@okaxis`

</div>



---

## 📜 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🏆 **Acknowledgments**

- Security research community
- Open source contributors
- Ethical hackers worldwide
- All users providing feedback

---

<div align="center">

**Made with ❤️ for the cybersecurity community by [Deadshot0x7](https://github.com/Deadshot0x7)**

⭐ **Star this repository if it helped you!**

</div>
