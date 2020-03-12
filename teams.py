import pandas as pd
from numpy import *

class Leader():

    def __init__(self, n, r, a):
        self.__name = n
        self.__returning = r
        self.__alr = a
        self.__score = self.calcScore()
        self.__team = ''

    def calcScore(self):
        s = 3
        if self.__returning:
            s += 3
        if self.__alr:
            s += 3
        return s

    def setTeam(self, teamName):
        self.__team = teamName

    def getScore(self):
        return self.__score

    def getName(self):
        return self.__name

    def getRet(self):
        return self.__returning

    def getALR(self):
        return self.__alr

    def __str__(self):
        return self.__name

class Team():

    def __init__(self, tName):
        self.__teamName = tName
        self.__members = []
        self.__number = 0
        self.__totScore = 0

    def addMember(self, Leader):
        self.__members.append(Leader)
        self.__totScore += Leader.getScore()
        self.__number += 1
        Leader.setTeam(self.getTeamName())

    def rvMember(self, Leader):
        self.__members.remove(Leader)
        self.__number -= 1

    def clearTeam(self):
        self.__members.clear()
        self.__totScore = 0
        self.__number = 0

    def getTeamName(self):
        return self.__teamName

    def getMembers(self):
        return self.__members

    def getNumber(self):
        return self.__number

    def getTotalScore(self):
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

class TeamController():

    def __init__(self, s, n):
        self.__allTeams = []
        self.__allLeaders = []
        self.__fair = False
        self.__sList = []
        self.__nList = []
        self.__sCoeff = s
        self.__nCoeff = n
        self.load()
        self.makeFair()

    def load(self):
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
        while not self.__fair:
            self.Randomize()

            sDiff = max(self.__sList) - min(self.__sList)
            nDiff = max(self.__nList) - min(self.__nList)

            if sDiff<=self.__sCoeff and nDiff<=self.__nCoeff:
                self.__fair = True

    def getAllTeams(self):
        return self.__allTeams

    def __str__(self):
        s = ''
        for t in self.__allTeams:
            s = s + str(t) + '\n'
        return s





c = TeamController(4,1)

print(c)

