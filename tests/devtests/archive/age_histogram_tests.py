'''
Test the age-histogram analyzer.
'''

import covasim as cv

intervs = [cv.change_beta(days=40, changes=0.5), cv.test_prob(start_day=20, symp_prob=0.1, asymp_prob=0.01)] # Common interventions
pars = dict(
    pop_size      = 20000,    # Population size
    pop_infected  = 100,      # Number of initial infections -- use more for increased robustness
    pop_type      = 'hybrid', # Population to use -- "hybrid" is random with household, school,and work structure
    verbose       = 0,        # Don't print details of the run
    interventions = intervs   # Include the most common interventions
)

sim = cv.Sim(pars, analyzers=cv.age_histogram(datafile='example_age_data.csv'))
sim.run()
agehist = sim['analyzers'][0]
hists = agehist.get()
agehist.plot()

sim = cv.Sim(pars, analyzers=cv.age_histogram(days=['2020-04-01', 'end']))
sim.run()
agehist = sim['analyzers'][0]
agehist.plot(windows=True)