This work has been sponsored by [Sythe Labs](https://sythelabs.com).

# smtp-enum
A straightforward smtp enumeration script

## Usage
```
 Usage: main.py [OPTIONS] TARGET WORDLIST

╭─ Arguments ─────────────────────────────────────────────────────────────────────────────╮
│ *    target        TEXT  [default: None] [required]                                     │
│ *    wordlist      TEXT  [default: None] [required]                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────╮
│ --sleep-every               INTEGER  [default: 10]                                      │
│ --install-completion                 Install completion for the current shell.          │
│ --show-completion                    Show completion for the current shell, to copy it  │
│                                      or customize the installation.                     │
│ --help                               Show this message and exit.                        │
╰─────────────────────────────────────────────────────────────────────────────────────────╯
```

## Example
```bash
./smtp-enum 192.168.1.1 ~/Desktop/Kali/Tools/statistically-likely-usernames/jsmith.txt

# or

uv run smtp-enum 192.168.1.1 ~/Desktop/Kali/Tools/statistically-likely-usernames/jsmith.txt
```
