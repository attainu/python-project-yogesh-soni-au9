
import argparse 
import datetime 
class Maze:
    def __init__(self, maze):
        self.maze = maze

    def maze_runner_dfs(self, row, col):
        if self.maze[n-1][n-1] == 0:
            return False
        if (row == n-1) and (col == n-1):
            solution[row][col] = 1
            return True
        if (row >= 0 and col >= 0 and row < n and col < n and
                solution[row][col] == 0 and self.maze[row][col] == 1):
            solution[row][col] = 1  
            if(self.maze_runner_dfs(row+1, col) or
               self.maze_runner_dfs(row-1, col) or
               self.maze_runner_dfs(row, col+1) or 
               self.maze_runner_dfs(row, col-1)):
                return True
            else:

                solution[row][col] = 0  

            return False
        else:

            return False

    def print_path(self, sol):
        file2.write("***\n\n" + "the  path followed is " +
                    self.direction(sol) + "reach to the destination: \n\n")
        for i in sol:
            for j in i:
                file2.write(" " + str(j) + " ")
            file2.write('\n')
        time = datetime.datetime.now()
        file2.write("***\n" + "Time of execution at : " +
                    time.strftime("%d-%m-%Y * %H:%M:%S\n" + "***\n\n"))

    def direction(self, solvedMaze):  
        n = len(solvedMaze)   
        visited = [[False for _ in range(n)] for _ in range(n)]
        arr = ""
        i = j = 0
        while i != n-1 or j != n-1:
            if j == n-1:
                if solvedMaze[i+1][j] == 1 and visited[i+1][j] is False:
                    visited[i+1][j] = True
                    i = i+1
                    arr += "D=>"
                elif solvedMaze[i][j-1] == 1 and visited[i][j-1] is False:
                    visited[i][j-1] = True
                    j = j-1
                    arr += "L=>"
            elif i == n-1:
                if solvedMaze[i][j+1] == 1 and visited[i][j+1] is False:
                    visited[i][j+1] = True
                    j = j+1
                    arr += "R=>"
                elif solvedMaze[i-1][j] == 1 and visited[i-1][j] is False:
                    visited[i-1][j] = True
                    i = i-1
                    arr += "U=>"
            else:
                if solvedMaze[i+1][j] == 1 and visited[i+1][j] is False:
                    visited[i+1][j] = True
                    i = i+1
                    arr += "D=>"
                elif solvedMaze[i][j+1] == 1 and visited[i][j+1] is False:
                    visited[i][j+1] = True
                    j = j+1
                    arr += "R=>"
                elif solvedMaze[i-1][j] == 1 and visited[i-1][j] is False:
                    visited[i-1][j] = True
                    i = i-1
                    arr += "U=>"
                elif solvedMaze[i][j-1] == 1 and visited[i][j-1] is False:
                    visited[i][j-1] = True
                    j = j-1
                    arr += "L=>"
        return arr


#******Driver Function******   


if __name__ == "__main__":
    maze = []  
    maze1 = Maze(maze)    
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Input File")
    parser.add_argument("-o", help="Output File")
    args = parser.parse_args()
    file1 = open(args.i, 'r')  
    file2 = open(args.o, 'a')  

    for data in file1:
        [test.strip('\n\r') for test in data]
        maze.append([int(x) for x in data.split()])
    n = len(maze)
    solution = [[0]*n for _ in range(n)]

    if(maze1.maze_runner_dfs(0, 0)): 
        maze1.print_path(solution)
    else:
        file2.write("***\n-1\n")
        file2.write(
            " sorry there is no any path available to reach destination.")
        now = datetime.datetime.now()
        file2.write("\nTime of execution at : " +
                    now.strftime("%d-%m-%Y * %H:%M:%S") + "\n***\n\n\n")