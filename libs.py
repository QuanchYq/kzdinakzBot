import sqlite3

usersnamedb = sqlite3.connect('usersname.db')
usersname = usersnamedb.cursor()

usersdb = sqlite3.connect('users.db')
users = usersdb.cursor()


users.execute('''CREATE TABLE IF NOT EXISTS usersname (
                    id INTEGER PRIMARY KEY,
                    is_allowed INTEGER DEFAULT 0,
                    username TEXT
                )''')
usersdb.commit()

def grant_admin_access(user_id: int):
    users.execute('INSERT INTO users  WHERE id=?', (user_id,))
    usersdb.commit()

def isAdmin(user_id: int) -> bool:
    users.execute('SELECT is_allowed FROM users WHERE id=?', (user_id,))
    result = users.fetchone()
    if result is None:
        return False
    else:
        return bool(result[0])
def isAdminUsername(username: str) -> bool:
    users.execute('SELECT is_allowed FROM usersname WHERE username=?', (username,))
    result = users.fetchone()
    if result is None:
        return False
    else:
        return bool(result[0])


async def add_user(user_id: int):
    users.execute('INSERT INTO users (id, is_allowed) VALUES (?, 1)', (user_id,))
    usersdb.commit()
async def add_user_username(username: str):
    users.execute('INSERT INTO usersname (username, is_allowed) VALUES (?, 1)', (username,))
    usersdb.commit()

    


