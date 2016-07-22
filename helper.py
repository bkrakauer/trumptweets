import numpy as np

def word_freqs(words):
    freqs = {}
    for tweet in words:
        for word in tweet:
            if word in freqs:
                freqs[word] += 1
            else:
                freqs[word] = 1
    return freqs

def get_state(loc):
    loc = str(loc).lower()
    state = np.nan
    
    if 'alabama' in loc or ', al' in loc:
        state = "AL"
    elif 'alaska' in loc or ', ak' in loc:
        state = "AK"
    elif 'arizona' in loc or ', az' in loc:
        state = "AZ"
    elif 'california' in loc or ', ca' in loc:
        state = "CA"
    elif 'colorado' in loc or ', co' in loc:
        state = "CO"
    elif 'connecticut' in loc or ', ct' in loc:
        state = "CT"
    elif 'delaware' in loc or ', de' in loc:
        state = "DE"
    elif 'florida' in loc or ', fl' in loc:
        state = "FL"
    elif 'georgia' in loc or ', ga' in loc:
        state = "GA"
    elif 'hawaii' in loc or ', hi' in loc:
        state = "HI"
    elif 'idaho' in loc or ', id' in loc:
        state = "ID"
    elif 'illinois' in loc or ', il' in loc:
        state = "IL"
    elif 'indiana' in loc or ', in' in loc:
        state = "IN"
    elif 'iowa' in loc or ', ia' in loc:
        state = "IA"
    elif 'kansas' in loc or ', ks' in loc:
        state = "KS"
    # We have to evaluate arkansas after kansas because the former is a substring of the later
    if 'arkansas' in loc or ', ar' in loc:
        state = "AR"
    elif 'kentucky' in loc or ', ky' in loc:
        state = "KY"
    elif 'louisana' in loc or ', la' in loc:
        state = "LA"
    elif 'maine' in loc or ', me' in loc:
        state = "ME"
    elif 'maryland' in loc or ', md' in loc:
        state = "MD"
    elif 'massachusetts' in loc or ', ma' in loc:
        state = "MA"
    elif 'michigan' in loc or ', mi' in loc:
        state = "MI"
    elif 'minnesota' in loc or ', mn' in loc:
        state = "MN"
    elif 'mississippi' in loc or ', mi' in loc:
        state = "MS"
    elif 'missouri' in loc or ', mo' in loc:
        state = "MO"
    elif 'montana' in loc or ', mt' in loc:
        state = "MT"
    elif 'nebraska' in loc or ', ne' in loc:
        state = "NE"
    elif 'nevada' in loc or ', nv' in loc:
        state = "NV"
    elif 'new hampshire' in loc or ', ak' in loc:
        state = "NH"
    elif 'new jersey' in loc or ', ak' in loc:
        state = "NJ"
    elif 'new mexico' in loc or ', nm' in loc:
        state = "NM"
    # We can handle 'nyc' as a special case because there may be enough of them to warrant it...
    elif 'new york' in loc or ', ny' in loc:
        state = "NY"
    elif 'north carolina' in loc or ', nc' in loc:
        state = "NC"
    elif 'north dakota' in loc or ', nd' in loc:
        state = "ND"
    elif 'ohio' in loc or ', oh' in loc:
        state = "OH"
    elif 'oklahoma' in loc or ', ok' in loc:
        state = "OK"
    elif 'oregon' in loc or ', or' in loc:
        state = "OR"
    elif 'pennsylvania' in loc or ', pa' in loc:
        state = "PA"
    elif 'rhode island' in loc or ', ri' in loc:
        state = "RI"
    elif 'south carolina' in loc or ', sc' in loc:
        state = "SC"
    elif 'south dakota' in loc or ', sd' in loc:
        state = "SD"
    elif 'tennessee' in loc or ', tn' in loc:
        state = "TN"
    elif 'texas' in loc or ', tx' in loc:
        state = "TX"
    elif 'utah' in loc or ', ut' in loc:
        state = "UT"
    elif 'vermont' in loc or ', vt' in loc:
        state = "VT"
    elif 'virginia' in loc or ', va' in loc:
        state = "VA"
    elif 'washington' in loc or ', wa' in loc:
        state = "WA"
    # This is an 'if' to catch virginia -> west virginia if necessary.
    if 'west virginia' in loc or ', wv' in loc:
        state = "WV"
    elif 'wisconsin' in loc or ', wi' in loc:
        state = "WI"
    elif 'wyoming' in loc or ', wy' in loc:
        state = "WY"
    elif 'district of columbia' in loc or ', dc' in loc:
        state = "DC"
    
    return state

# add population for each state (in millions)
pops = {
    "AL": 4.9,
    "AK": .7,
    "AZ": 6.8,
    "AR": 3,
    "CA": 39.1,
    "CO": 5.5,
    "CT": 3.6,
    "DE": .9,
    "FL": 20,
    "GA": 10.2,
    "HI": 1.4,
    "ID": 1.7,
    "IL": 12.9,
    "IN": 6.6,
    "IA": 3.1,
    "KS": 2.9,
    "KY": 4.4,
    "LA": 4.7,
    "ME": 1.3,
    "MD": 6,
    "MA": 6.8,
    "MI": 10,
    "MN": 5.5,
    "MS": 3,
    "MO": 6.1,
    "MT": 1,
    "NE": 1.9,
    "NV": 2.9,
    "NH": 1.3,
    "NJ": 9,
    "NM": 2.1,
    "NY": 20,
    "NC": 10,
    "ND": .8,
    "OH": 11.6,
    "OK": 3.9,
    "OR": 4,
    "PA": 12.8,
    "RI": 1,
    "SC": 4.9,
    "SD": .9,
    "TN": 6.6,
    "TX": 27.5,
    "UT": 3,
    "VT": .6,
    "VA": 8.4,
    "WA": 7.2,
    "WV": 1.8,
    "WI": 5.8,
    "WY": .6,
    "DC": .7
}