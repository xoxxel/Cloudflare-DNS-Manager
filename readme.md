# 🌐 Cloudflare DNS Manager

**Version**: `v2.0.0`
**Status**: ✅ Production Ready
**Last Updated**: July 28, 2025

---

## ✨ What Is Cloudflare DNS Manager?

**Cloudflare DNS Manager** is a powerful and developer-friendly tool for managing your DNS records via the [Cloudflare API](https://api.cloudflare.com/). Whether you're running multiple subdomains, operating a staging environment, or simply need automated DNS control — this tool is for you.

### 🔧 Key Features

* 🧩 Modular Python-based architecture
* 🖥️ Interactive CLI & automated scripting
* ⚙️ Add, edit, delete, and query DNS records (A, CNAME)
* ♻️ Bulk record operations
* 📊 Statistics, monitoring, and logging
* 🔄 Cloudflare Proxy & TTL configuration
* 🧪 100% test coverage and safe for production

Perfect for:

* Developers
* System administrators
* DevOps teams
* Anyone managing subdomains or microservices

---

## 🚀 Quick Start Guide

### 1⃣ Clone the Project

```bash
git clone https://github.com/xoxxel/Cloudflare-DNS-Manager.git
cd Cloudflare-DNS-Manager
```

### 2⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3⃣ Configure Environment

Create a `.env` file in the root directory:

```env
API_TOKEN=your_cloudflare_api_token_here
ZONE_ID=your_zone_id_here
```

> ✅ TIP: Get your API Token and Zone ID from [dash.cloudflare.com](https://dash.cloudflare.com/profile/api-tokens)

### 4⃣ Run the Tool

```bash
python app.py     # Launch interactive DNS manager
```

---

## 🧩 Features Overview

### ✅ Supported Record Types

* **A Records**: Subdomain → IP
* **CNAME Records**: Subdomain → another domain

### ✏️ Actions Supported

* Create subdomains
* Edit existing records
* Enable/disable proxy
* Adjust TTL (cache time)
* Delete records (by name or ID)
* Search and list records
* Export DNS record list

### 🧪 System Test Coverage

```bash
python app.py --test   # Run test suite
# ✅ All 5/5 tests must pass
```

---

## 🖥️ CLI Usage

### Main Commands

```bash
python app.py               # Interactive menu mode
python app.py --test        # Run all tests
python app.py --examples    # View usage examples
python app.py --help        # Show help menu
```

### Common Interactive Options

1. List all DNS records
2. Search record by name
3. Filter records by type (A/CNAME)
4. Add A or CNAME records
5. Edit IP or TTL
6. Toggle CDN proxy
7. Delete records
8. Show usage stats

---

## 🧠 Example Use Cases

### 🌐 Subdomain Deployment (Microservices)

```python
from app.feature.add_record import AddRecord
add = AddRecord()
add.add_subdomain("auth", "10.0.0.1")
add.add_cname_record("api", "auth.example.com")
```

### ✨ CDN Boost

```python
from app.feature.edit_record import EditRecord
edit = EditRecord()
edit.toggle_proxy("api", True)
edit.update_record_ttl("api", 300)
```

### 📊 Query All Records

```python
from app.feature.query_record import QueryRecord
q = QueryRecord()
records = q.list_all_records()
```

### ❌ Clean Up Staging

```python
from app.feature.delete_record import DeleteRecord
delr = DeleteRecord()
delr.delete_record_by_name("staging")
```

---

## 📁 Project Structure

```
Cloudflare-DNS-Manager/
├── app.py                # 🌟 Entry launcher
├── config.py             # ⚙️ Loads API credentials
├── requirements.txt      # 📦 Dependencies
├── .env.example          # 🔐 Config template
├── app/
│   ├── main.py           # 🎮 Interactive CLI logic
│   ├── examples.py       # 📚 Usage samples
│   └── feature/          # 🧩 Core DNS operations
│       ├── add_record.py
│       ├── delete_record.py
│       ├── edit_record.py
│       ├── query_record.py
│       └── base_api.py   # 🔗 Auth + HTTP core
└── test_app.py           # ✅ 5 system-level tests
```

---

## 🔒 Security Best Practices

* ❌ Never share your `.env` file or API token
* ✅ Limit API token permissions to `Zone:DNS:Edit`
* ⌛ Set expiration dates for temporary access
* 🌐 Use IP restrictions in Cloudflare when possible

---

## 🧪 Testing & Stability

* ✅ 100% test coverage (5/5 pass)
* ⚠️ Deleting `config.py` or `.env` will break execution
* 🧪 Recommended to test in staging before production

---

## 🔮 Roadmap

### 📦 v2.1.0 (Coming Soon)

* [ ] MX record support
* [ ] TXT/SPF for email
* [ ] AAAA record (IPv6)
* [ ] Auto-sync (schedule updates)
* [ ] Web dashboard (GUI)

### 💡 v3.0.0 (Planned)

* [ ] AI-powered DNS optimization
* [ ] Multi-domain management
* [ ] Mobile app (iOS/Android)
* [ ] Analytics dashboard

---

## 🦘 Support

* 🔛 Bug reports: [GitHub Issues](https://github.com/xoxxel/Cloudflare-DNS-Manager/issues)
* 📚 Full documentation: See `readme.md`, `examples.py`
* ❓ Feature ideas? Open a PR or suggestion issue

---

## 🏁 Final Notes

* ✅ Modular, production-grade Python tool
* 📚 Fully documented with usage examples
* 🛠️ Easily extensible for more DNS operations
* 🧱 Clean separation of concerns (OOP + CLI)

> Made with ❤️ by xoxxel | Contributions welcome!
