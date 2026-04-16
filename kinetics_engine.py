import numpy as np

def predict_parenteral_stability(pH,temp,oxygen):

    H = 10**(-pH)
    OH = 10**(-(14-pH))

    kH = 0.02
    kOH = 0.01
    kw = 0.001

    ox_factor = {
        "Low":0.001,
        "Medium":0.005,
        "High":0.01
    }

    kobs = kH*H + kOH*OH + kw + ox_factor[oxygen]

    Ea = 50000
    R = 8.314
    T = temp + 273

    kT = kobs*np.exp((-Ea/R)*(1/T - 1/298))

    t90 = 0.105/kT

    return kT,t90
