from itcsimlib.thermo import *
from itcsimlib.model_drakon import *

# Autogenerated with DRAKON Editor 1.29
class Model(DRAKONIsingModel):
    description = "This is an Ising-based model with energies defined by a DRAKON graphical flow diagram."

    def configuration(self, config):
        #item 154
        bound_top = 0
        bound_bot = 0
        #item 1520001
        site = 0
        while True:
            #item 1520002
            if site < 7:
                pass
            else:
                break
            #item 155
            if self.occupied(config, site):
                #item 158
                bound_top += 1
                
                self.add_dG(config, 'dG_bind')
                self.add_dH(config, 'dH_bind')
            else:
                pass
            #item 159
            if self.occupied(config, site + 7):
                #item 163
                bound_bot += 1
                
                self.add_dG(config, 'dG_bind')
                self.add_dH(config, 'dH_bind')
            else:
                pass
            #item 1520003
            site += 1
        #item 1650001
        site = 0
        while True:
            #item 1650002
            if site < 7:
                pass
            else:
                break
            #item 167
            if bound_top >= self.ring_sat:
                #item 170
                self.add_dG(config, 'dG_couple')
            else:
                pass
            #item 171
            if bound_bot >= self.ring_sat:
                #item 180
                self.add_dG(config, 'dG_couple')
            else:
                pass
            #item 1650003
            site += 1


    def setup(self):
        #item 136
        self.initialize(nsites=14, circular=False)
        #item 30
        self.add_parameter("dG_bind", type="dG")
        #item 145
        self.add_parameter("dG_couple", type="dG")
        #item 146
        self.add_parameter("ring_sat", type="n")
        #item 32
        self.add_parameter("dH_bind", type="dH")

