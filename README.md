# Warframe Syndicate Market CLI tool

A simple Python CLI tool to fetch and display **online buy orders** from [Warframe Market](https://warframe.market) for syndicate-specific **Weapons** and **Mods** across all platforms (PC, Xbox, Switch, PS4).

---

## Features

- See **online buy orders** from **any** platform
- Customizable **weapon** and **mod** lists


## Requirements

- Python 3.8 or later
- [`pywmapi`](https://pypi.org/project/pywmapi)

Install dependencies with:

```bash
pip install -r requirements.txt
```

## How to Use
```bash
python main.py
```

You'll be prompted to choose a syndicate and whether you want to see Mods or Weapons

## File Format

Each .txt file inside Weapons/ or Mods/ should list Warframe Market item names line-by-line, like:

Example `Mods/ArbitersOfHexis.txt`:

```
Power Drift
Steel Charge
Brief Respite
```

## Customization
- Simply add or remove items by editing the .txt files

## License
MIT License. Feel free to fork, improve, and share.