import sqlite3
base_name = "Players.db"
success = print("Success")

def create_table():
    conn = sqlite3.connect(base_name)

    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS Players (
              name TEXT,
              level TEXT,
              team_points INT,
              quiz_points INT,
              act_points INT,
              improv_points INT
        )
        """)
    conn.commit()
    conn.close()
    success
def fetch_players():
    conn = sqlite3.connect(base_name)
    c = conn.cursor()

    c.execute("SELECT name, level, team_points, quiz_points, act_points, improv_points FROM Players")
    players = c.fetchall()
    conn.close()
    success
    return players

def insert_players(name, level, team_points, quiz_points, act_points, improv_points):
    conn = sqlite3.connect(base_name)
    c = conn.cursor()
    c.execute("INSERT INTO Players (name, level, team_points, quiz_points, act_points, improv_points) VALUES (?,?,?,?,?,?)",
              (name, level, team_points, quiz_points, act_points, improv_points))
    conn.commit()
    conn.close()
    success
def delete_players(name):
    conn = sqlite3.connect(base_name)
    c = conn.cursor()
    c.execute("DELETE FROM Players WHERE name = ?", (name,))

    conn.commit()
    conn.close()
def update_players(new_name, new_level, new_team_points, new_quiz_points, new_act_points, new_improv_points):
    conn = sqlite3.connect(base_name)
    c = conn.cursor()

    c.execute("UPDATE Players SET level = ?, team_points = ?, quiz_points = ?, act_points = ?, improv_points = ? WHERE name = ?",
              (new_level, new_team_points, new_quiz_points, new_act_points, new_improv_points, new_name))
    conn.commit()
    conn.close()
    success
def name_exists(name):
    conn = sqlite3.connect(base_name)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM Players WHERE name = ?", (name,))
    result = c.fetchone()
    conn.close()
    return result[0] > 0
def find_player(points):
    conn = sqlite3.connect(base_name)
    c = conn.cursor()
    c.execute("SELECT * FROM Players WHERE team_points = ? OR quiz_points = ? OR act_points = ? OR improv_points = ?",
              (points, points, points, points))
    player = c.fetchone()
    if player:
        return player
    else:
        print(f"No player was found with {points}")

