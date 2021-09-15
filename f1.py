def bmi_list_comp(hts, wts):
    assert len(hts) == len(wts)
    return [wts[i]*2.20464/(hts[i]*2.54)**2 for i in range(len(hts))]