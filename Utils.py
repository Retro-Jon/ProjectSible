import json
# Load file
# Accepts a path
# Returns a dictionary
def load(path):
    f = open(path, "r")
    data = json.load(f)
    f.close()
    return json.loads(data)

# Save file
# Accepts a path and dictionary
def save(path, data):
    json_object = json.dumps(data, indent=4)
    f = open(path, "w")
    f.write(json_object)
    f.close()

# Is in row
# Accepts 2 dimensional array and row number
# Zero indexed
def in_row(grid, row, num):
    return num in grid[row]

# Is in column
# Accepts 2 dimensional array and column number
# Zero indexed
def in_column(grid, column, num):
    for row in grid:
        if num == row[column]:
            return True
    
    return False

