# David René
# d2rene@uwaterloo.ca

import pandas as pd
from numpy import *

# A Leader is a person that will participate in Orientation.
class Leader():

    def __init__(self, n, r, a):
        '''
        Creates a leader object.
        :param n: str, the full name of the leader.
        :param r: bool, True if the leader is a returning leader.
        :param a: bool, True if the leader is a returning ALR.
        '''
        self.__name = n
        self.__returning = r
        self.__alr = a
        self.__score = self.calcScore()
        self.__team = ''

    def calcScore(self):
        '''
        Calculates the score of a leader. A leader starts with a score of 3, then 3 is added if they are a returning leader and 3 is added if they are a returning ALR.
        :return: int, the score of the leader
        '''
        s = 3
        if self.__returning:
            s += 3
        if self.__alr:
            s += 3
        return s

    def setTeam(self, teamName):
        '''
        Sets the team name of a leader.
        :param teamName: str, the name of the team.
        '''
        self.__team = teamName

    def getScore(self):
        '''
        Returns the score of a leader.
        :return: int, score of a leader.
        '''
        return self.__score

    def getName(self):
        '''
        Returns the name of a leader.
        :return: str, the name of a leader.
        '''
        return self.__name

    def getRet(self):
        '''
        Returns if the leader is a returning leader or not.
        :return: bool, the state of this condition.
        '''
        return self.__returning

    def getALR(self):
        '''
        Returns if the leader is a returning ALR or not.
        :return: bool, the state of this condiditon.
        '''
        return self.__alr

    def __str__(self):
        return self.__name

# A team is an Orientation Team that consists of many Orientation Leaders
class Team():

    def __init__(self, tName):
        '''
        Creates a Team Object. By default, the team is empty.
        :param tName: str, the name of the team.
        '''
        self.__teamName = tName
        self.__members = []
        self.__number = 0
        self.__totScore = 0

    def addMember(self, Leader):
        '''
        Adds a leader to the team. This function also updates the total score of the team, updates the amount of members
        in the team and sets the name of the leaders team to the appropriate name.
        :param Leader: Leader Object, the leader to add to the team.
        '''
        self.__members.append(Leader)
        self.__totScore += Leader.getScore()
        self.__number += 1
        Leader.setTeam(self.getTeamName())

    def rvMember(self, Leader):
        '''
        Removes a leader from the team. This function also updates the total score of the team, updates the amount of members
        in the team and sets the name of the leaders team to the appropriate name.
        :param Leader: Leader Object, the leader to remove from the team.
        '''
        self.__members.remove(Leader)
        self.__totScore -= Leader.getScore()
        self.__number -= 1
        Leader.setTeam('')

    def clearTeam(self):
        '''
        Clears the team.
        '''
        self.__members = []
        self.__totScore = 0
        self.__number = 0

    def getTeamName(self):
        '''
        Returns the name of the team.
        :return: str, the team name.
        '''
        return self.__teamName

    def getMembers(self):
        '''
        Returns the list of the members of this team.
        :return: List, the members of the team.
        '''
        return self.__members

    def getNumber(self):
        '''
        Returns the number of members in the team.
        :return: int, the number of members in the team.
        '''
        return self.__number

    def getTotalScore(self):
        '''
        Returns the total score of a team. The total score of a team is the sum of the score of all the
        members in the team.
        :return: int, the total score of the team.
        '''
        s = 0
        for m in self.__members:
            s += m.getScore()
        self.__totScore = s
        return self.__totScore

    def __str__(self):
        s = self.__teamName + ': '
        for m in self.__members:
            s = s + m.getName() + ' '
        return s

# The team controller manages all teams and all leaders and creates teams that are fair.
class TeamController():

    def __init__(self, s, n):
        '''
        Creates a TeamController object. Automatically imports leaders from an excel file named 'leaders.xlsx'.
        Will import leaders on the 'Leaders' sheet and team names from the 'Teams' sheet.
        :param s: int, the maximum score difference allowed between any team.
        :param n: int, the maximum number of members difference allowed between any team.
        '''
        self.__allTeams = []
        self.__allLeaders = []
        self.__fair = False
        self.__sList = []
        self.__nList = []
        self.__sCoeff = s
        self.__nCoeff = n
        self.load()
        self.makeFair()
        print(self)

    def load(self):
        '''
        Loads the leaders and the team names from the sheets 'Leaders' and 'Teams' from the excel file 'leaders.xlsx'.
        Also create the appropriate Team objects and Leader Objects and fills the list of teams and leaders.
        '''
        self.__allTeams = []
        self.__allTeams = []

        ldrs = pd.read_excel(r'leaders.xlsx', sheet_name='Leaders')
        tms = pd.read_excel(r'leaders.xlsx', sheet_name='Teams')

        leaders = ldrs.values
        teams = tms.values

        for l in leaders:
            self.__allLeaders.append(Leader(l[0], l[1] == 'y', l[2] == 'y'))

        for t in teams:
            self.__allTeams.append(Team(t[0]))

    def Randomize(self):
        '''
        Creates teams at random. Selects a random leader from the list and puts them randomly in one of the teams from the list.
        This process is repeated until all leaders are placed.
        '''
        self.__nList = []
        self.__sList = []

        for t in self.__allTeams:
            t.clearTeam()
        temp = self.__allLeaders.copy()

        while len(temp)!=0:
            t=random.choice(self.__allTeams)
            l=random.choice(temp)

            temp.remove(l)
            t.addMember(l)

        for t in self.__allTeams:
            self.__sList.append(t.getTotalScore())
            self.__nList.append(t.getNumber())

    def makeFair(self):
        '''
        Creates randomized teams until the score difference and number of members difference is smaller than the one required.
        '''
        while not self.__fair:
            self.Randomize()

            sDiff = max(self.__sList) - min(self.__sList)
            nDiff = max(self.__nList) - min(self.__nList)

            if sDiff<=self.__sCoeff and nDiff<=self.__nCoeff:
                self.__fair = True

    def getAllTeams(self):
        '''
        Returns the list of all the teams.
        :return: List, the list of all the teams.
        '''
        return self.__allTeams

    def __str__(self):
        s = ''
        for t in self.__allTeams:
            s = s + str(t) + '\n'
        return s

###############################################################################################
# Main

TeamController(4,1)



