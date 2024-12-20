import numpy as np  # For grid handling
from queue import Queue  # For BFS pathfinding

# 1. Environment Setup: Create a 5x5 grid with obstacles (1) and target (2)
GRID_SIZE = 5  # Grid dimensions (5x5)
grid = np.array([
    [0, 1, 0, 0, 0],  # 1 = Obstacle, 0 = Open space
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 2]   # 2 = Target position at (4,4)
])

start_position = (0, 0)  # Start position of the agent

# 2. Helper Function: Check if a position is within grid and not blocked
def is_valid_move(position):
    x, y = position
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and grid[x][y] != 1

# 3. Agent Class: Handles agent actions and movement
class Agent:
    def __init__(self, start):
        self.position = start  # Initialize agent at the starting position

    def sense_environment(self):
        """Sense adjacent cells: up, down, left, right."""
        x, y = self.position
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return [n for n in neighbors if is_valid_move(n)]

    def move(self, new_position):
        """Move the agent to a new position."""
        self.position = new_position

# 4. Pathfinding using BFS (Breadth-First Search)
def bfs(start, target):
    visited = set()  # Track visited positions
    queue = Queue()  # Queue for BFS
    queue.put((start, [start]))  # Store position and path

    while not queue.empty():
        current, path = queue.get()  # Get current position and path
        if current == target:
            return path  # Return the path if target is found

        for neighbor in Agent(current).sense_environment():
            if neighbor not in visited:
                visited.add(neighbor)  # Mark neighbor as visited
                queue.put((neighbor, path + [neighbor]))  # Add to queue

    return None  # No path found

# 5. Main Simulation Logic
def run_simulation():
    agent = Agent(start_position)
    target_position = (4, 4)  # Define the target position

    path = bfs(agent.position, target_position)  # Find path using BFS

    if path:
        print("Path found:", path)
        for step in path:
            agent.move(step)
            print(f"Agent moved to {agent.position}")
    else:
        print("No path found to the target.")

# 6. Entry Point: Run the simulation when the script is executed
if __name__ == "__main__":
    run_simulation()
