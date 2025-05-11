
<p align="center">
  <img src="https://github.com/HexTide.png" width="100" alt="Hex Logo"/>
</p>

<h1 align="center">HexStack</h1>
<p align="center"><strong>Chain HEX bots into automated flows</strong></p>
<p align="center">
Sequential Automation • Modular Execution • Zero Dashboard
</p>
<p align="center">
Created by <a href="https://github.com/HexTide">HexTide</a>
</p>

---

## 🔗 What is HexStack?

HexStack is the chaining engine for the HEX Automation Ecosystem.  
It executes multiple HEX bots in a defined sequence with no user input, API, or frontend.

---

## 🧠 Use Case

Example bot chain:

```
HexDropper → HexClick → HexTrackr
```

Each bot runs after the previous one completes. Designed for passive, scalable workflows.

---

## 🚀 Usage

```bash
python run.py
```

HexStack reads the `STACK_SEQUENCE` list from `hexstack/config.py`  
and executes each bot in order.

---

## 📁 Structure

| File | Description |
|------|-------------|
| `hexstack/stack.py` | Main engine that runs the chain |
| `hexstack/config.py` | List of bots to run |
| `run.py` | Launch entry point |
| `LICENSE.txt` | Terms of use |

---

## 🔐 License

This module is licensed and bound to HEX system modules.  
It may only be used in official HEX chains.  
See LICENSE.txt for usage rules.

<p align="center">
  <strong>© HEX Automation • All Rights Reserved</strong><br/>
  Created by <a href="https://github.com/HexTide">HexTide</a>
</p>
