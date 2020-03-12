# David René
# d2rene@uwaterloo.ca

import pandas as pd
from numpy import *

# A Leader is a person that will participate in Orientation.
class Leader():

    def __init__(self, n, r, a, e, c, t, f):
        '''
        Creates a leader object.
        :param n: str, the full name of the leader.
        :param r: bool, True if the leader is a returning leader.
        :param a: bool, True if the leader is a returning ALR.
        :param e: str, the email adress of the leader
        :param c: bool, True if coordinator.
        :param t: bool, True if Team Captain.
        :param f: bool, True if FuPo.
        '''
        self.__setName(n)
        self.__setRet(r)
        self.__setALR(a)
        self.__setEmail(e)
        self.__setCoord(c)
        self.__setTC(t)
        self.__setFUPO(f)
        self.__setScore(self.__calcScore())

    def __calcScore(self):
        '''
        Calculates the score of a leader. A leader starts with a score of 3, then 3 is added if they are a returning leader
        and 3 is added if they are a returning ALR.
        :return: int, the score of the leader
        '''
        s = 3
        if self.getRet():
            s += 3
        if self.getALR():
            s += 3
        return s

    def __setScore(self, score):
        '''
        Sets the score of a leader to the score value sent.
        :param score: int, the score of the leader.
        '''
        self.__score = score

    def __setRet(self, bool):
        '''
        Sets if the leader is a returning leader or not.
        :param bool: bool, True if the leader is a returning leader.
        '''
        self.__returning = bool

    def __setALR(self, bool):
        '''
        Sets if the leader is a returning ALR or not.
        :param bool: bool, True if the leader is a returning leader.
        '''
        self.__alr = bool

    def __setCoord(self, bool):
        '''
        Sets if the leader is a coordinator or not.
        :param bool: bool, True if the leader is a coordinator.
        '''
        self.__coord = bool

    def __setTC(self, bool):
        '''
        Sets if the leader is a TC or not.
        :param bool: bool, True if the leader is a TC.
        '''
        self.__tc = bool

    def __setFUPO(self, bool):
        '''
        Setf is the leader is a FuPo or not.
        :param bool: bool, True if the leader is a FuPo.
        :return:
        '''
        self.__fp = bool

    def __setName(self, name):
        '''
        Sets the name of the leader.
        :param name: str, the name of the leader.
        '''
        self.__name = name

    def __setEmail(self, email):
        '''
        Sets the email of the leader.
        :param email: str, the email of the leader.
        :return:
        '''
        self.__email = email

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

    def getCoord(self):
        '''
        Returns if the leader is a coord or not.
        :return: bool, the state of this condition
        '''
        return self.__coord

    def getTC(self):
        '''
        Returns if the leader is a TC.
        :return: bool, the state of this condition.
        '''
        return self.__tc

    def getFUPO(self):
        '''
        Returns if the leader is a FuPo
        :return: bool, the state of this condition.
        '''
        return self.__fp

    def getEmail(self):
        '''
        Returns the email adress of the leader.
        :return: str, the email adress of the leader.
        '''
        return self.__email

    def __str__(self):
        '''
        When a leader object is converted to a string, it will show their name.
        :return: str, the name of the leader.
        '''
        return self.getName()

# A team is an Orientation Team that consists of many Orientation Leaders
class Team():

    def __init__(self, tName, tColor):
        '''
        Creates a Team Object. By default, the team is empty.
        :param tName: str, the name of the team.
        :param tColor: str, the color of the team.
        '''
        self.__setTeamName(tName)
        self.__setMembers([])
        self.__setNumber(0)
        self.__setTotalScore(0)
        self.__setTeamColor(tColor)

    def addMember(self, Leader):
        '''
        Adds a leader to the team. This function also updates the total score of the team, updates the amount of members
        in the team.
        :param Leader: Leader Object, the leader to add to the team.
        '''
        lst = self.getMembers()
        sc = self.getTotalScore()
        nbr = self.getNumber()
        lst.append(Leader)
        self.__setMembers(lst)
        self.__setTotalScore(sc+Leader.getScore())
        self.__setNumber(nbr+1)

    def rvMember(self, Leader):
        '''
        Removes a leader from the team. This function also updates the total score of the team, updates the amount of members
        in the team.
        :param Leader: Leader Object, the leader to remove from the team.
        '''
        lst = self.getMembers()
        sc = self.getTotalScore()
        nbr = self.getNumber()
        lst.remove(Leader)
        self.__setMembers(lst)
        self.__setTeamColor(sc - Leader.getScore())
        self.__setNumber(nbr - 1)

    def clearTeam(self):
        '''
        Clears the team.
        '''
        self.__setMembers([])
        self.__setNumber(0)
        self.__setTotalScore(0)

    def __setTeamName(self, tName):
        '''
        Sets the name of the team.
        :param tName: str, the name of the team.
        '''
        self.__teamName = tName

    def __setTeamColor(self, tColor):
        '''
        Sets the color of the team.
        :param tColor: str, the color of the team.
        '''
        self.__teamColor = tColor

    def __setMembers(self, lst):
        '''
        Sets the members of the team to the provided list.
        :param lst: List, list of Leader objects that are members of this team.
        '''
        self.__members = lst

    def __setNumber(self, nbr):
        '''
        Sets the number of members in the team to the provided nbr.
        :param nbr: int, the number of members in the team.
        '''
        self.__number = nbr

    def __setTotalScore(self, s):
        '''
        Sets the total score of the team to the provided number
        :param s: int, the total score of the team.
        '''
        self.__totScore = s

    def getEmailList(self):
        '''
        Returns the list of emails of all members of that team in the format email1; email2; email3; ...
        :return: str, the list of emails.
        '''
        s = ''
        i = 0
        for l in self.getMembers():
            if i==0:
                s = l.getEmail()
                i += 1
            else:
                s = s + '; ' +l.getEmail()
        return s

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

    def getTeamColor(self):
        '''
        Returns the color of the team.
        :return: str, the color of the team.
        '''
        return self.__teamColor

    def getTotalScore(self):
        '''
        Returns the total score of a team. The total score of a team is the sum of the score of all the
        members in the team.
        :return: int, the total score of the team.
        '''
        s = 0
        for m in self.getMembers():
            s += m.getScore()
        self.__setTotalScore(s)
        return self.__totScore

    def getFUPOS(self):
        '''
        Returns who are the FuPos in a team.
        :return: List, the list of FuPos in a team.
        '''
        lst = []
        for m in self.getMembers():
            if m.getFUPO():
                lst.append(m)
        return lst

    def getTCS(self):
        '''
        Returns who is/are the TC in a team.
        :return: List, the list of TC in a team.
        '''
        lst = []
        for m in self.getMembers():
            if m.getTC():
                lst.append(m)
        return lst

    def __str__(self):
        '''
        When a Team Object is converted to a string, it will automatically return:
        teamname (color): members
        TC: member
        FuPos: member, member
        Email list: email1; email2; ..

        :return: str, the string representation of a team.
        '''
        s = self.getTeamName() + ' (' + self.getTeamColor() + '): '
        i = 0
        for m in self.getMembers():
            if i == 0:
                s = s + m.getName()
                i += 1
            else:
                s = s + ', ' + m.getName()

        s = s + '\n' + 'TC: '
        i = 0
        for m in self.getTCS():
            if i == 0:
                s = s + m.getName()
                i += 1
            else:
                s = s + ', ' + m.getName()

        s = s + '\n' + 'FuPos: '
        i = 0
        for m in self.getFUPOS():
            if i == 0:
                s = s + m.getName()
                i += 1
            else:
                s = s + ', ' + m.getName()

        s = s + '\n' + 'Email list: ' + self.getEmailList() + '\n'
        return s

# The team controller manages all teams and all leaders and creates teams that are fair.
class TeamController():

    def __init__(self, s):
        '''
        Creates a TeamController object. Automatically imports leaders from an excel file named 'leaders.xlsx'.
        Will import leaders on the 'Leaders' sheet and team names from the 'Teams' sheet.
        :param s: int, the maximum score difference allowed between any team.
        '''
        self.__setAllTeams([])
        self.__setAllLeaders([])
        self.__setFair(False)
        self.__setScoreList([])
        self.__setNumberList([])
        self.__setScoreCoeff(s)
        self.__setNumberCoeff(1)
        self.__load()
        self.__makeFair()
        self.__export()

    def __load(self):
        '''
        Loads the leaders and the team names from the sheets 'Leaders' and 'Teams' from the excel file 'leaders.xlsx'.
        Also create the appropriate Team objects and Leader Objects and fills the list of teams and leaders.
        '''
        tempL = []
        tempT = []

        ldrs = pd.read_excel(r'leaders.xlsx', sheet_name='Leaders')
        tms = pd.read_excel(r'leaders.xlsx', sheet_name='Teams')

        leaders = ldrs.values
        teams = tms.values

        for l in leaders:
            tempL.append(Leader(l[0], l[1] == 'y', l[2] == 'y', l[3], l[4]=='Coordinator', l[4]=='TC', l[4]=='FuPo'))

        for t in teams:
            tempT.append(Team(t[0], t[1]))

        self.__setAllTeams(tempT)
        self.__setAllLeaders(tempL)

    def __Randomize(self):
        '''
        Creates teams at random. It first evenly and randomly distribute coordinators, it then evenly and randomly distributes TCs, then evenly and randomly
        distributes FUPOs, then it evenly and randomly distributes
        returning ALRs, then evenly and randomly distributes returning leaders and then evenly and randomly distributes new leaders.
        '''
        self.__setNumberList([])
        self.__setScoreList([])

        nList = []
        rList = []
        aList = []
        cList = []
        tList = []
        fList = []

        for t in self.__allTeams:
            t.clearTeam()
        temp = self.__allLeaders.copy()

        #Here we filter all leaders in order to put them in their appropriate bins.
        while len(temp)!=0:
            l=random.choice(temp)
            temp.remove(l)

            if l.getCoord():
                cList.append(l)
            elif l.getTC():
                tList.append(l)
            elif l.getFUPO():
                fList.append(l)
            elif l.getALR() and not l.getTC() and not l.getFUPO:
                aList.append(l)
            elif l.getRet() and not l.getALR() and not l.getTC() and not l.getFUPO:
                rList.append(l)
            else:
                nList.append(l)

        #First we then evenly distribute Coordinators.
        while len(cList)>=len(self.__allTeams):
            tlst = random.choice(self.__allTeams,len(self.__allTeams), replace = False)
            for t in tlst:
                l = cList[-1]
                cList.remove(l)
                t.addMember(l)
        if len(cList)!=0:
            tlst = random.choice(self.__allTeams,len(cList), replace = False)
            for t in tlst:
                l = cList[-1]
                cList.remove(l)
                t.addMember(l)

        #Second we then evenly distribute TCs.
        while len(tList)>=len(self.__allTeams):
            tlst = random.choice(self.__allTeams,len(self.__allTeams), replace = False)
            for t in tlst:
                l = tList[-1]
                tList.remove(l)
                t.addMember(l)
        if len(tList)!=0:
            tlst = random.choice(self.__allTeams,len(tList), replace = False)
            for t in tlst:
                l = tList[-1]
                tList.remove(l)
                t.addMember(l)

        #Third we then evenly distribute FuPos.
        while len(fList)>=len(self.__allTeams):
            tlst = random.choice(self.__allTeams,len(self.__allTeams), replace = False)
            for t in tlst:
                l = fList[-1]
                fList.remove(l)
                t.addMember(l)
        if len(fList)!=0:
            tlst = random.choice(self.__allTeams,len(fList), replace = False)
            for t in tlst:
                l = fList[-1]
                fList.remove(l)
                t.addMember(l)

        #Fourth we then evenly distribute returning ALRs that are only Leaders.
        while len(aList)>=len(self.__allTeams):
            tlst = random.choice(self.__allTeams,len(self.__allTeams), replace = False)
            for t in tlst:
                l = aList[-1]
                aList.remove(l)
                t.addMember(l)
        if len(aList)!=0:
            tlst = random.choice(self.__allTeams,len(aList), replace = False)
            for t in tlst:
                l = aList[-1]
                aList.remove(l)
                t.addMember(l)

        #Fifth we then evenly distribute returning Leaders.
        while len(rList) >= len(self.__allTeams):
            tlst = random.choice(self.__allTeams, len(self.__allTeams), replace=False)
            for t in tlst:
                l = rList[-1]
                rList.remove(l)
                t.addMember(l)
        if len(rList) != 0:
            tlst = random.choice(self.__allTeams, len(rList), replace=False)
            for t in tlst:
                l = rList[-1]
                rList.remove(l)
                t.addMember(l)

        #Sixth we then evenly distribute new Leaders.
        while len(nList) >= len(self.__allTeams):
            tlst = random.choice(self.__allTeams, len(self.__allTeams), replace=False)
            for t in tlst:
                l = nList[-1]
                nList.remove(l)
                t.addMember(l)
        if len(nList) != 0:
            tlst = random.choice(self.__allTeams, len(nList), replace=False)
            for t in tlst:
                l = nList[-1]
                nList.remove(l)
                t.addMember(l)

        #Finally we update all the team scores and all the team numbers.
        for t in self.__allTeams:
            self.__sList.append(t.getTotalScore())
            self.__nList.append(t.getNumber())

    def __makeFair(self):
        '''
        Creates randomized teams until the score difference and number of members difference is smaller than the one required.
        '''
        t = 1
        while not self.__fair:
            print('Try number ' + str(t))
            self.__Randomize()

            sDiff = max(self.__sList) - min(self.__sList)
            nDiff = max(self.__nList) - min(self.__nList)
            print(self.__sList)
            print(self.__nList)
            t +=1
            if sDiff<=self.__sCoeff and nDiff<=self.__nCoeff:
                self.__fair = True

    def __export(self):
        '''
        Creates a text file with all team names, members and email lists.
        '''
        f = open('teams.txt','w+')
        f.write(str(self))
        f.close()

    def __setAllTeams(self, lst):
        '''
        Sets the list of all the teams.
        :param lst: List, list of all Team Objects.
        '''
        self.__allTeams = lst

    def __setAllLeaders(self, lst):
        '''
        Sets the list of all leaders.
        :param lst: List, list of all Leader Objects.
        :return:
        '''
        self.__allLeaders = lst

    def __setFair(self, bool):
        '''
        Sets if the teams are fair.
        :param bool: bool, True if the teams are fair.
        '''
        self.__fair = bool

    def __setScoreList(self, lst):
        '''
        Sets the list of all team scores to the provided list.
        :param lst: List, list of ints (team scores).
        '''
        self.__sList = lst

    def __setNumberList(self, lst):
        '''
        Sets the list of all team member numbers to the provided list.
        :param lst: List, list of ints (team members)
        '''
        self.__nList = lst

    def __setScoreCoeff(self, s):
        '''
        Sets the score coefficient to the provided score coefficient. When creating teams, the algorithm
        will keep going until all teams are within this coefficient of difference.
        :param s: int, the score coefficient.
        '''
        self.__sCoeff = s

    def __setNumberCoeff(self, n):
        '''
        Sets the number coefficient to the provided number coefficient. When creating teams, the algorithm will keep going
        until all teams are within this coefficient of difference in terms of numbers.
        :param n: int, the number coefficient.
        '''
        self.__nCoeff = n

    def getAllTeams(self):
        '''
        Returns the list of all the teams.
        :return: List, the list of all the teams.
        '''
        return self.__allTeams

    def getAllLeaders(self):
        '''
        Returns the list of all leaders.
        :return: List, the list of all leaders.
        '''
        return self.__allLeaders

    def __str__(self):
        '''
        Returns a string representation of the controller in this format:

        Teamname1 (color): members
        TC: members
        FuPos: members
        Email List: email1; email2;...

        .
        .
        .

        TCs:
        Email List:

        FuPos:
        Email List:

        :return: str, the string representation of the controller.
        '''
        s = ''
        for t in self.__allTeams:
            s = s + str(t) + '\n'
        s = s + '\n' + 'TCs: '
        i = 0
        for m in self.getAllLeaders():
            if m.getTC():
                if i == 0:
                    s = s + m.getName()
                    i += 1
                else:
                    s = s + ', ' + m.getName()

        s = s + '\n' + 'Email List: '
        i = 0
        for m in self.getAllLeaders():
            if m.getTC():
                if i == 0:
                    s = s +  m.getEmail()
                    i += 1
                else:
                    s = s + '; ' + m.getEmail()

        s = s + '\n\n' + 'FuPos: '
        i = 0
        for m in self.getAllLeaders():
            if m.getFUPO():
                if i == 0:
                    s = s + m.getName()
                    i += 1
                else:
                    s = s + ', ' + m.getName()

        s = s + '\n' + 'Email List: '
        i = 0
        for m in self.getAllLeaders():
            if m.getFUPO():
                if i == 0:
                    s = s + m.getEmail()
                    i += 1
                else:
                    s = s + '; ' + m.getEmail()

        return s

###############################################################################################
# Main

TeamController(15)



