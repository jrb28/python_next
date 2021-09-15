def bmi_loop(hts, wts):
    assert len(hts) == len(wts)
    
    ''' Convert English (in, lbs) to metric (cm, kg) '''
    hts_m = []
    wts_m = []
    for i in range(len(hts)):
        hts_m.append(hts[i] * 2.54)
        wts_m.append(wts[i] / 2.20464)
        
    bmi = []
    for i in range(len(hts_m)):
        bmi.append(wts_m[i]/hts_m[i]**2)
        
    return bmi