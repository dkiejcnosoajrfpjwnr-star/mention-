import sqlite3

class BotDatabase:
    def __init__(self, db_file='database.db'):
        """Initialize database connection"""
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        """Create necessary tables if they don't exist"""
        # Users table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Chat users table (many-to-many relationship)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_users (
                chat_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                PRIMARY KEY (chat_id, user_id),
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        ''')
        
        self.conn.commit()

    def add_user(self, user_id, username):
        """Add or update a user"""
        try:
            self.cursor.execute(
                'INSERT OR REPLACE INTO users (user_id, username) VALUES (?, ?)',
                (user_id, username)
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def add_user_to_chat(self, chat_id, user_id):
        """Add user to a chat"""
        try:
            self.cursor.execute(
                'INSERT OR IGNORE INTO chat_users (chat_id, user_id) VALUES (?, ?)',
                (chat_id, user_id)
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def delete_user_from_chat(self, chat_id, user_id):
        """Remove user from a chat"""
        try:
            self.cursor.execute(
                'DELETE FROM chat_users WHERE chat_id = ? AND user_id = ?',
                (chat_id, user_id)
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def get_users_from_chat(self, chat_id):
        """Get all users in a chat"""
        try:
            self.cursor.execute('''
                SELECT u.user_id, u.username 
                FROM users u
                INNER JOIN chat_users cu ON u.user_id = cu.user_id
                WHERE cu.chat_id = ?
            ''', (chat_id,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []

    def count_users(self):
        """Count total users"""
        try:
            self.cursor.execute('SELECT COUNT(*) FROM users')
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return (0,)

    def count_chats(self):
        """Count total chats (unique chat_ids)"""
        try:
            self.cursor.execute('SELECT COUNT(DISTINCT chat_id) FROM chat_users')
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return (0,)

    def count_groups(self):
        """Count total groups (same as chats in this context)"""
        return self.count_chats()

    def close(self):
        """Close database connection"""
        self.conn.close()
