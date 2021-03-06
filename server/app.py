import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, UJSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import sqlite3

class Score(BaseModel):
    name: str
    highscore : int

def getConn () -> sqlite3.Connection:
    return sqlite3.connect('leaderboard.db')
def databaseSetup ():
    sql_leaderboard = """
        CREATE TABLE IF NOT EXISTS leaderboard (
            name VARCHAR(100) NOT NULL,
            score TINYINT(255) NOT NULL,
            time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
    """
    conn = getConn()
    conn.execute(sql_leaderboard)
    conn.commit()
    conn.close()
databaseSetup()

app = FastAPI()
app_dir = os.environ.get("CLIENT_DIR", str(Path(__file__).parent / "../client/public"))

origins = [
    "http://localhost:5000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/leaderboard', response_class=UJSONResponse)
def getLeaderboard ():
    cur = getConn().cursor()
    cur.execute ("SELECT * FROM leaderboard ORDER BY score DESC;")
    curList = cur.fetchmany(5)
    leaderboardList = []
    for item in curList:
        leaderboardItem = {"name": item[0], "score": int(item[1]), "time": item[2]}
        leaderboardList.append(leaderboardItem)
    return leaderboardList

@app.post('/highscore')
def addLeaderboard (score: Score):
    cur = getConn()
    cur.execute("INSERT INTO leaderboard (name, score) VALUES (?, ?);", (score.name, score.highscore))
    cur.commit()
    cur.close()

app.mount('/', StaticFiles(directory=app_dir, html=True), name="static")
