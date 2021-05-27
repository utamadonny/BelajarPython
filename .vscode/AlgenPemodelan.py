'''
Find the global maximum for function: 10.4 + x * math.sin(3*np.pi*x) + y * math.sin(13*np.pi*y)
'''

import math
import numpy as np
from gaft import GAEngine
from gaft.components import BinaryIndividual
from gaft.components import Population
from gaft.operators import TournamentSelection
from gaft.operators import UniformCrossover
from gaft.operators import FlipBitMutation

# Analysis plugin base class.
from gaft.plugin_interfaces.analysis import OnTheFlyAnalysis
from gaft.operators.selection.roulette_wheel_selection import RouletteWheelSelection
from gaft.operators.mutation.flip_bit_mutation import FlipBitBigMutation
# Built-in best fitness analysis.
from gaft.analysis.fitness_store import FitnessStore

indv_template = BinaryIndividual(ranges=[(-2, 15.5), (3.27, 8.75)], eps=0.0001)
selection = RouletteWheelSelection()
crossover = UniformCrossover(pc=0.8, pe=0.5)
mutation = FlipBitBigMutation(pm=0.1, pbm=0.55, alpha=0.6)
population = Population(indv_template=indv_template,size=16).init()

engine = GAEngine(population=population, selection=selection,
                    crossover=crossover, mutation=mutation,
                    analysis=[FitnessStore])

@engine.fitness_register
def fitness(indv):
    x,y = indv.solution
    #return 10.4 + x * math.sin(3*np.pi*x) + y * math.sin(13*np.pi*y)
    #return 3.2+x**3*math.sin(3*np.pi*x)+2*x*math.sin(13*np.pi*y)
    return x**3+2*x+3

@engine.analysis_register
class ConsoleOutputAnalysis(OnTheFlyAnalysis):
    interval = 1
    master_only = True
    def register_step(self, g, population, engine):
        best_indv = engine.ori_fmax
        mean_indv = population.mean(engine.fitness)
        min_indv = population.min(engine.fitness)
        msg = 'Generation: {}, mean fitness: {:.3f}, best fitness: {:.3f}'.format(g, mean_indv, engine.ori_fmax)
        self.logger.info(msg)
    def finalize(self, population, engine):
        best_indv = population.best_indv(engine.fitness)
        x = best_indv.solution
        y = engine.ori_fmax
        msg = 'Optimal solution: ({}, {})'.format(x, y)
        self.logger.info(msg)

if '__main__' == __name__:
    # Run the GA engine.
    engine.run(ng=100)