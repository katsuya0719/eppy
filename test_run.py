# running from the ./docs folder
import sys
pathnameto_eppy = 'c:/santosh/eppy'
# pathnameto_eppy = '../'
sys.path.append(pathnameto_eppy)
import eppy.runner.runner


iddfile = "C:/EnergyPlusV8-3-0/Energy+.idd"
fname1 = "C:/EnergyPlusV8-3-0/ExampleFiles/1ZoneEvapCooler.idf"
epw = 'C:/EnergyPlusV8-3-0/WeatherData/USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw'
IDF5 = eppy.runner.runner.IDF5
IDF5.setiddname(iddfile)
idf = IDF5(open(fname1, 'r'), epw)

idf.run()