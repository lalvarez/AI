
'''
    Class gameProblem, implements simpleai.search.SearchProblem
'''


from simpleai.search import SearchProblem
import simpleai.search
import time

class GameProblem(SearchProblem):

    # Object attributes, can be accessed in the methods below

    MAP=None
    POSITIONS=None
    INITIAL_STATE=None
    GOAL=None
    CONFIG=None
    AGENT_START=None


    # --------------- Common functions to a SearchProblem -----------------


    def actions(self, state):

		'''Returns a LIST of the actions that may be executed in this state
		'''

		actions = ['North','South','West','East']


		#Case 1: North
		#Make sure you can get this state or is a wall
		if state[0][1] == 0:
			actions.remove('North')
		#If it is not a wall
		else:
			#Recorrer si X = "casilla arriba" y tipo = 'sea' no cambia el estado
				if(state[0][0],state[0][1]-1)in(self.POSITIONS['sea']):
						actions.remove('North')



		#Case 2: South
		#Make sure you can get this state or is a wall
		if state[0][1] + 1 == self.CONFIG['map_size'][1]:
			actions.remove('South')
		#If it is not a wall
		else:
			#Recorrer el diccionario y si X = "casilla arriba" y tipo = 'sea' no cambia el estado
			if(state[0][0],state[0][1]+1)in(self.POSITIONS['sea']):
						actions.remove('South')


		#Case 3: East
		#Make sure you can get this state or is a wall
		if state[0][0] + 1 == self.CONFIG['map_size'][0]:
			actions.remove('East')
		#If it is not a wall
		else:
			#Recorrer el diccionario y si X = "casilla arriba" y tipo = 'sea' no cambia el estado
			if(state[0][0]+1,state[0][1])in(self.POSITIONS['sea']):
						actions.remove('East')




		#Case 4: West
		#Make sure you can get this state or is a wall
		if state[0][0] == 0:
			actions.remove('West')
		#If it is not a wall
		else:
			#Recorrer el diccionario y si X = "casilla arriba" y tipo = 'sea' no cambia el estado
			if(state[0][0]-1,state[0][1])in(self.POSITIONS['sea']):
						actions.remove('West')

		#If battery is equal to 0, Dron can not move
		if state[2][0] == 0:
			actions[:]=[]

		return actions


    def result(self, state, action):
		'''Returns the state reached from this state when the given action is executed
		'''

		#We move the agent
		lista_aux = []
		auxPhotosPos = state[1]

		#Case North
		if action == 'North':
			#Mover agente
			auxPosAg = (state[0][0],state[0][1]-1)

			#Crear una lista con las nuevas posiciones de fotos
			i = 0
			for aux in auxPhotosPos:
				if aux == auxPosAg:
					lista_aux.insert(i,(-1,-1))
				else:
					lista_aux.insert(i,aux)
				i = i +1
			tuple_aux = tuple(lista_aux)

			battery = (state[2][0]-1,state[2][1])

			if auxPosAg == self.AGENT_START:
				battery = (-1, state[2][1])
			if self.MAP[auxPosAg[0]][auxPosAg[1]][0] == 'drone-fuel':
				battery = (state[2][1], state[2][1])

			final_state = (auxPosAg,tuple_aux,battery);


		#Case South
		if action == 'South':
			#Mover agente
			auxPosAg = (state[0][0],state[0][1]+1)
			#Crear una lista con las nuevas posiciones de fotos
			i = 0
			for aux in auxPhotosPos:
				if aux == auxPosAg:
					lista_aux.insert(i,(-1,-1))
				else:
					lista_aux.insert(i,aux)
				i = i +1
			tuple_aux = tuple(lista_aux)

			battery = (state[2][0]-1,state[2][1])

			if auxPosAg == self.AGENT_START:
				battery = (-1, state[2][1])
			if self.MAP[auxPosAg[0]][auxPosAg[1]][0] == 'drone-fuel':
				battery = (state[2][1], state[2][1])

			final_state = (auxPosAg,tuple_aux,battery);

		#Case East
		if action == 'East':
			#Mover agente
			auxPosAg = (state[0][0]+1,state[0][1])
			#Crear una lista con las nuevas posiciones de fotos
			i = 0
			for aux in auxPhotosPos:
				if aux == auxPosAg:
					lista_aux.insert(i,(-1,-1))
				else:
					lista_aux.insert(i,aux)
				i = i +1
			tuple_aux = tuple(lista_aux)
			battery = (state[2][0]-1,state[2][1])
			if auxPosAg == self.AGENT_START:
				battery = (-1, state[2][1])
			if self.MAP[auxPosAg[0]][auxPosAg[1]][0] == 'drone-fuel':
				battery = (state[2][1], state[2][1])
			final_state = (auxPosAg,tuple_aux,battery);


		#Case West
		if action == 'West':
			#Mover agente
			auxPosAg = (state[0][0]-1,state[0][1])
			#Crear una lista con las nuevas posiciones de fotos
			i = 0
			for aux in auxPhotosPos:
				if aux == auxPosAg:
					lista_aux.insert(i,(-1,-1))
				else:
					lista_aux.insert(i,aux)
				i = i +1
			tuple_aux = tuple(lista_aux)
			battery = (state[2][0]-1,state[2][1])
			if auxPosAg == self.AGENT_START:
				battery = (-1, state[2][1])
			if self.MAP[auxPosAg[0]][auxPosAg[1]][0] == 'drone-fuel':
				battery = (state[2][1], state[2][1])
			final_state = (auxPosAg,tuple_aux,battery);

		return final_state

    def is_goal(self, state):
        '''Returns true if state is the final state
        '''
        test = False #Put a FALSE when other methods are implemented
        if state == self.GOAL:
			test = True

        return test

    def cost(self, state, action, state2):
        '''Returns the cost of applying `action` from `state` to `state2`.
           The returned value is a number (integer or floating point).
           By default this function returns `1`.
        '''
        posAgF= state2[0]
        coste = self.MAP[posAgF[0]][posAgF[1]][2]['cost']

        return coste

    def heuristic(self, state):
		'''Returns the heuristic for `state`
		'''
		res = 0

		#HEURISTICA 1 MANHATTAN
		''''h =[]
		for aux in state[1]:
			h.append(abs(state[0][0]-aux[0]) + abs(state[0][1]-aux[1]))

		res = min(h)'''


		#HEURISTICA 2: FOTOS LEFT
		#res = len(state[1])

		#HEURISTICA 3 MANHATTAN MEJORADA
		h =[]
		for aux in state[1]:
			h.append(abs(state[0][0]-aux[0]) + abs(state[0][1]-aux[1]))

		res = min(h)

		i = list(state[1])

		for aux in state[1]:
			if (aux==(-1,-1)):
				i.pop()

		if len(i)==0:
				res = abs(state[0][0]-self.AGENT_START[0]) + abs(state[0][1]-self.AGENT_START[1])

		#HECURISTICA 4: FOTOS Y A CASA
		#res = len(state[1])+1


		return res


    def setup (self):
		print self.CONFIG['map_size'][0]
		print '\nMAP: ', self.MAP, '\n'
		print 'POSITIONS: ', self.POSITIONS, '\n'
		print 'CONFIG: ', self.CONFIG, '\n'


		#We are going to save the info of the game

		print 'START: ', self.AGENT_START
		print 'FUEEL: ', self.MAP[2][0][0]
		x = len(self.MAP[0])
		print 'x=',x

		y = len(self.MAP)
		print 'y=',y

		print 'LONGITUD'
		NgoalsLeft = len(self.POSITIONS['goal'])
		print 'Numero de fotos:', NgoalsLeft, '\n'
		GoalsLeftPos = self.POSITIONS['goal']
		print 'Fotos position:', GoalsLeftPos
		AgentPos = self.AGENT_START
		print 'Agent position:',AgentPos[0:2]

		tuplaGoals=tuple(GoalsLeftPos)

		batteryI= (self.CONFIG['battery'],self.CONFIG['battery'])

		initial_state = (AgentPos, tuplaGoals, batteryI)
		print initial_state[0][0]



		GoalsFinalState = []
		i=0

		while i< NgoalsLeft:
			GoalsFinalState.insert(i,(-1, -1))
			i = i+1

		final_tuple = tuple(GoalsFinalState)

		batteryF= (-1,self.CONFIG['battery'])

		final_state= (AgentPos, final_tuple, batteryF);


		algorithm = simpleai.search.astar



		return initial_state,final_state,algorithm



    # -------------------------------------------------------------- #
    # --------------- DO NOT EDIT BELOW THIS LINE  ----------------- #
    # -------------------------------------------------------------- #

    def getAttribute (self, position, attributeName):
        '''Returns an attribute value for a given position of the map
           position is a tuple (x,y)
           attributeName is a string

           Returns:
               None if the attribute does not exist
               Value of the attribute otherwise
        '''
        tileAttributes=self.MAP[position[0]][position[1]][2]
        if attributeName in tileAttributes.keys():
            return tileAttributes[attributeName]
        else:
            return None

    # THIS INITIALIZATION FUNCTION HAS TO BE CALLED BEFORE THE SEARCH
    def initializeProblem(self,map,positions,conf,aiBaseName):

        # Loads the problem attributes: self.AGENT_START, self.POSITIONS,etc.
        if self.mapInitialization(map,positions,conf,aiBaseName):

            initial_state,final_state,algorithm = self.setup()

            self.INITIAL_STATE=initial_state
            self.GOAL=final_state
            self.ALGORITHM=algorithm
            super(GameProblem,self).__init__(self.INITIAL_STATE)

            return True
        else:
            return False

    # END initializeProblem


    def mapInitialization(self,map,positions,conf,aiBaseName):
        # Creates lists of positions from the configured map
        # The initial position for the agent is obtained from the first and only aiBaseName tile
        self.MAP=map
        self.POSITIONS=positions
        self.CONFIG=conf

        if 'agentInit' in conf.keys():
            self.AGENT_START = tuple(conf['agentInit'])
        else:
            if aiBaseName in self.POSITIONS.keys():
                if len(self.POSITIONS[aiBaseName]) == 1:
                    self.AGENT_START = self.POSITIONS[aiBaseName][0]
                else:
                    print ('-- INITIALIZATION ERROR: There must be exactly one agent location with the label "{0}", found several at {1}'.format(aiAgentName,mapaPosiciones[aiAgentName]))
                    return False
            else:
                print ('-- INITIALIZATION ERROR: There must be exactly one agent location with the label "{0}"'.format(aiBaseName))
                return False

        return True


