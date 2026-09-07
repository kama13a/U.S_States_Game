# 🗺️ U.S. States Game

An interactive geography quiz game built with Python's Turtle module and Pandas. Test your knowledge of U.S. states by guessing their names and locations on the map!

---

## 🎯 Project Overview

The game displays a blank map of the United States. The player types state names, and each correct guess places the state name at its correct position on the map. The game tracks your progress and shows your final score.

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| **Interactive Map** | U.S. map with state boundaries |
| **Guess States** | Type any state name |
| **Correct Guess** | State name appears on the map |
| **Score Tracking** | Shows how many states you've guessed |
| **Progress Display** | Shows current score out of 50 |
| **Exit Option** | Type "exit" to end the game |
| **Missed States** | Shows list of states you missed |
| **Save Progress** | Missed states saved to `learn.csv` |

---

## 📁 Project Structure
ex02/
├── main.py # Game loop

├── 50_states.csv # State data (name, x, y coordinates)

├── blank_states_img.gif # U.S. map image

├── learn.csv # Missed states (generated)

└── README.md # Documentation


---

## 🛠️ Technologies Used

- **Python 3.x**
- **Turtle Graphics** – Map display and text placement
- **Pandas** – Data handling and CSV operations

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone git@github.com:kama13a/U.S_States_Game.git
cd ex02
python main.py