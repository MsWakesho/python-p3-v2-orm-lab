
#!/usr/bin/env python3.10

# lib/config.py

import sqlite3

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()
