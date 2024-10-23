# MIDTERM - Samantha Townsend DATASCI 200 Introduction to Data Science Programming, UC Berkeley MIDS
# midterm.py

# Problem 1: Tweet Analysis (15 pts)
def count_retweets_by_username(tweet_list):
    """
    (list of tweets) -> dict of {username: int}
    Returns a dictionary in which each key is a username that was 
    retweeted in tweet_list and each value is the total number of times this 
    username was retweeted.
    """
    retweet_count = {}
    
    for tweet in tweet_list:
        # Find tweets that contain "RT @"
        if "RT @" in tweet:
            # Extract the username by finding the substring between "RT @" and ":"
            start_index = tweet.find("RT @") + 4  # 4 to move past "RT @"
            end_index = tweet.find(":", start_index)
            username = tweet[start_index:end_index]
            
            # Count occurrences of the retweeted username
            if username in retweet_count:
                retweet_count[username] += 1
            else:
                retweet_count[username] = 1
    
    return retweet_count


# Problem 2: Looking for Minerals (30 pts)
# 2a) Display sub-grid
def display(deposits, top, bottom, left, right):
    """
    Display a subgrid of the land, with rows starting at top and up to
    but not including bottom, and columns starting at left and up to but
    not including right. Grid squares without deposits are represented by "-"
    and squares with a deposit are represented by "X".
    """
    # Initialize the grid for the sub-region with "-"
    grid = [['-' for _ in range(left, right)] for _ in range(top, bottom)]

    # Place deposits ("X") in the appropriate grid locations
    for row, col, tons in deposits:
        if top <= row < bottom and left <= col < right:
            grid[row - top][col - left] = 'X'  # Adjust relative to the subgrid

    # Convert the 2D list into a multi-line string
    return '\n'.join(''.join(row) for row in grid)

# 2b) Calculate total tons inside the sub-grid
def tons_inside(deposits, top, bottom, left, right):
    """
    Returns the total number of tons of deposits for which the row is at least top,
    but strictly less than bottom, and the column is at least left, but strictly
    less than right.
    """
    total_tons = 0.0

    # Loop through deposits and sum the tons within the sub-region
    for row, col, tons in deposits:
        if top <= row < bottom and left <= col < right:
            total_tons += tons

    return total_tons

# Problem 3: Birthday planning (15 pts)
def birthday_count(dates_list):
    """
    Returns the total number of birthday pairs in the dates_list.
    """
    birthday_counts = {}
    count = 0
    
    # Count how many times each birthday occurs
    for birthday in dates_list:
        if birthday in birthday_counts:
            birthday_counts[birthday] += 1
        else:
            birthday_counts[birthday] = 1
    
    # For each birthday, calculate how many pairs can be formed
    for birthday, occurrences in birthday_counts.items():
        if occurrences > 1:
            count += (occurrences * (occurrences - 1)) // 2
    
    return count