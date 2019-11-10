import random

from util import Queue


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # !!!! IMPLEMENT ME
        # Add users
        # call addUser() until our number of users is numUsers
        for i in range(numUsers):
            self.addUser(f"User {i+1}")

        # Create random friendships
        # totalFriendships = avgFriendships * numUsers
        # Generate a list of all possible friendships

        possibleFriendships = []
        # Avoid dups by ensuring the first ID is smaller than the second
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))

        # Shuffle the list
        random.shuffle(possibleFriendships)
        print("random friendships:")
        print(possibleFriendships)

        # Slice off totalFriendships from the front, create friendships
        totalFriendships = avgFriendships * numUsers // 2
        print(f"Friendships to create: {totalFriendships}\n")
        for i in range(totalFriendships):
            friendship = possibleFriendships[i]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        # Take this:
        # userID = argument

        # Return dictionary with:
        # friendID = key
        # path = value
        # example:
        # {friendID: [shortest path to friendID], friendID: [path], etc.}

        # vert is userID
        # edges are friendID

        # using id's from all generated friends
        # use BFS to get path from current id of friend
        # add path from current id to userIDarg as value to that userID
        # set value equal to id key

        visited = {}  # Note that this is a dictionary, not a set

        # for every person in friendships...
        for id in self.friendships:
            # set value equal to path generated from BFS
            visited[id] = self.bfs_social(userID, id)

        print(f"visisted allSocialPaths: {visited}")
        return visited

    def bfs_social(self, starting_id, ending_id):

        # Create an empty queue
        q = Queue()
        # add starting id to queue
        q.enqueue([starting_id])

        # create an empty set for visited verts
        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            if v not in visited:
                # check if v is target
                if v == ending_id:
                    # return entire path
                    return path
                # Mark it as visited..
                visited.add(v)
                # Then add a path to it's neighbors to the back of the que
                for neighbor in self.friendships[v]:
                    copy = list(path)
                # append neighbor to the back
                    copy.append(neighbor)
                    q.enqueue(copy)


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

# Example:
    # sg = SocialGraph()
    # sg.populateGraph(10, 2)
    # print(sg.friendships)
    # {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2},
    #  6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
    # connections = sg.getAllSocialPaths(1)
    # print(connections)
    # {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2],
    #  6: [1, 10, 6], 7: [1, 10, 2, 7]}
