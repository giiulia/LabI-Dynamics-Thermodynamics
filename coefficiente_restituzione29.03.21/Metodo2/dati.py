import numpy as np
from strumenti_utili_v4 import *
#------------------------PALLINA1(pin pong)------------------------
#8cm
pallina1_intervalli_h1 = np.array([
    [0.254729167, 0.252895833, 0.251125000, 0.250166667, 0.248854167],
    [0.241770833, 0.239270833, 0.238187500, 0.237125000, 0.235729167],
    [0.226125000, 0.233375000, 0.226083333, 0.224625000, 0.223062500],
    [0.217145833, 0.213083333, 0.213395833, 0.214479167, 0.211895833],
    [0.206625000, 0.202291667, 0.203125000, 0.203375000, 0.201395833],
    [0.195604167, 0.191437500, 0.192708333, 0.192604167, 0.191541667],
    [0.182979167, 0.182083333, 0.182520833, 0.182687500, 0.182437500],
    [0.173812500, 0.173041667, 0.175000000, 0.173770833, 0.173541667]
])

#10cm
pallina1_intervalli_h2 = np.array([
    [0.276895833, 0.273416667, 0.274708333, 0.276708333, 0.274083333], #n=1
    [0.262125000, 0.258375000, 0.263312500, 0.258729167, 0.260979167], #n=2
    [0.247479167, 0.244520833, 0.245125000, 0.246770833, 0.244020833], #n=3
    [0.234750000, 0.234770833, 0.230937500, 0.234083333, 0.231041667], #n=4
    [0.223041667, 0.223375000, 0.218270833, 0.222145833, 0.218770833], #n=5
    [0.205229167, 0.211062500, 0.204791667, 0.210750000, 0.207312500], #n=6
    [0.200687500, 0.200333333, 0.194395833, 0.200187500, 0.197041667], #n=7
    [0.189687500, 0.190187500, 0.185166667, 0.190041667, 0.187187500] #n=8
])

#15cm
pallina1_intervalli_h3 = np.array([
    [0.338916667, 0.340562500, 0.339125000, 0.339604167, 0.336812500],
    [0.318250000, 0.319041667, 0.318979167, 0.319000000, 0.317458333],
    [0.298437500, 0.298604167, 0.299354167, 0.298854167, 0.2969166670],
    [0.280500000, 0.281791667, 0.282458333, 0.281500000, 0.280041667],
    [0.264833333, 0.266270833, 0.266458333, 0.265750000, 0.268187500],
    [0.250333333, 0.252541667, 0.250854167, 0.250770833, 0.251041667],
    [0.232729167, 0.237229167, 0.235958333, 0.236458333, 0.236791667],
    [0.218833333, 0.225354167, 0.224062500, 0.224416667, 0.224479167]
    
])

#18cm
pallina1_intervalli_h4 = np.array([
    [0.362791667, 0.367750000, 0.367083333, 0.367958333, 0.362187500],
    [0.339041667, 0.342229167, 0.341270833, 0.344020833, 0.338229167],
    [0.318062500, 0.319916667, 0.320395833, 0.323229167, 0.317812500],
    [0.298395833, 0.301125000, 0.300104167, 0.302416667, 0.297729167],
    [0.282041667, 0.283500000, 0.282500000, 0.285104167, 0.281208333],
    [0.261270833, 0.265250000, 0.268583333, 0.269125000, 0.264333333],
    [0.246916667, 0.251125000, 0.251041667, 0.254687500, 0.251208333],
    [0.233312500, 0.237083333, 0.232479167, 0.237958333, 0.237895833]
])

#30cm
pallina1_intervalli_h5 = np.array([
    [0.462354167, 0.459291667, 0.460208333, 0.462666667, 0.459604167],
    [0.424520833, 0.423958333, 0.425333333, 0.422083333, 0.423958333],
    [0.393895833, 0.390479167, 0.394979167, 0.391354167, 0.392395833],
    [0.364625000, 0.364062500, 0.368187500, 0.364333333, 0.364895833],
    [0.343645833, 0.340125000, 0.339083333, 0.340104167, 0.340479167],
    [0.322541667, 0.319854167, 0.322708333, 0.318041667, 0.319666667],
    [0.298937500, 0.298979167, 0.303708333, 0.298395833, 0.298458333],
    [0.285729167, 0.282229167, 0.281500000, 0.280437500, 0.281104167]
])

pallina1_intervalli = np.array([
    pallina1_intervalli_h1,
    pallina1_intervalli_h2,
    pallina1_intervalli_h3,
    pallina1_intervalli_h4,
    pallina1_intervalli_h5
])
print("------------pallina1------------\n{}".format(pallina1_intervalli))

#------------------------PALLINA2(blu)------------------------
#65cm
pallina2_intervalli_h1 = np.array([
    [0.642666667, 0.651791667, 0.639770833, 0.641437500, 0.632562500], #n=1
    [0.569437500, 0.568062500, 0.556270833, 0.565395833, 0.560333333], #n=2
    [0.504333333, 0.498145833, 0.492666667, 0.489708333, 0.496916667], #n=3
    [0.453020833, 0.437041667, 0.426479167, 0.438520833, 0.352166667], #n=4
    [0.386166667, 0.377312500, 0.388083333, 0.379187500, 0.380729167], #n=5
    [0.334875000, 0.342645833, 0.325937500, 0.338229167, 0.240875000], #n=6
    [0.297062500, 0.300937500, 0.292000000, 0.299062500, 0.211500000], #n=7
    [0.264458333, 0.247645833, 0.261833333, 0.253145833, 0.185083333] #n=8
])

#55cm
pallina2_intervalli_h2 = np.array([
    [0.598083333, 0.588041667, 0.609125000, 0.586687500, 0.591562500],
    [0.522333333, 0.517729167, 0.510250000, 0.507895833, 0.518729167],
    [0.456333333, 0.453312500, 0.446541667, 0.450812500, 0.459083333],
    [0.406645833, 0.399854167, 0.399729167, 0.401000000, 0.403666667],
    [0.366604167, 0.351479167, 0.352541667, 0.350041667, 0.349416667],
    [0.326125000, 0.311250000, 0.307229167, 0.314479167, 0.312062500],
    [0.294208333, 0.271770833, 0.267479167, 0.279416667, 0.285187500],
    [0.260770833, 0.252500000, 0.246395833, 0.251250000, 0.251250000]
])

#45cm
pallina2_intervalli_h3 = np.array([
    [0.531729167, 0.530645833, 0.537166667, 0.537645833, 0.536250000],
    [0.465854167, 0.466104167, 0.467500000, 0.477437500, 0.479000000],
    [0.411562500, 0.407666667, 0.415479167, 0.420166667, 0.410854167],
    [0.364645833, 0.350520833, 0.373479167, 0.375041667, 0.383416667],
    [0.325479167, 0.316562500, 0.329125000, 0.326812500, 0.332875000],
    [0.291729167, 0.265770833, 0.291416667, 0.283875000, 0.287333333],
    [0.255645833, 0.241833333, 0.259458333, 0.245979167, 0.260479167],
    [0.222208333, 0.213791667, 0.221270833, 0.224395833, 0.232333333]
])

#35cm
pallina2_intervalli_h4 = np.array([
    [0.480645833, 0.480729167, 0.481541667, 0.487875000, 0.481291667],
    [0.428145833, 0.415979167, 0.408354167, 0.424562500, 0.419854167],
    [0.378583333, 0.357541667, 0.358291667, 0.375854167, 0.371312500],
    [0.336104167, 0.325770833, 0.319562500, 0.333937500, 0.321458333],
    [0.293854167, 0.288020833, 0.286270833, 0.293333333, 0.288270833],
    [0.252645833, 0.246583333, 0.246750000, 0.259645833, 0.249166667],
    [0.225895833, 0.220916667, 0.216020833, 0.227083333, 0.217750000],
    [0.203520833, 0.195395833, 0.187187500, 0.198687500, 0.207562500]
])

#25cm
pallina2_intervalli_h5 = np.array([
    [0.4003333333, 0.4054583333, 0.4110833333, 0.4086458333, 0.4040000000],
    [0.3594791667, 0.3529583333, 0.3633125000, 0.3566666667, 0.3592708333],
    [0.3160416667, 0.3164166667, 0.3265625000, 0.3231250000, 0.3178750000],
    [0.2785208333, 0.2825833333, 0.2893333333, 0.2690625000, 0.2804583333],
    [0.2536041667, 0.2465833333, 0.2507916667, 0.2566666667, 0.2460416667],
    [0.2260416667, 0.2217708333, 0.2074791667, 0.2182708333, 0.2239791667],
    [0.2045625000, 0.1974375000, 0.1781250000, 0.1947291667, 0.2006666667],
    [0.1811666667, 0.1835625000, 0.1614375000, 0.1681875000, 0.1813541667]
])

pallina2_intervalli = np.array([
    pallina2_intervalli_h1,
    pallina2_intervalli_h2,
    pallina2_intervalli_h3,
    pallina2_intervalli_h4,
    pallina2_intervalli_h5
], dtype=object)
print("------------pallina2------------\n{}".format(pallina2_intervalli))

#------------------------PALLINA3(tennis)------------------------
#65cm
pallina3_intervalli_h1 = np.array([
    [0.5468333333, 0.5103125000, 0.5349166667, 0.5349583333, 0.5325416667], #n=1
    [0.4118125000, 0.3829583333, 0.4022500000, 0.3975833333, 0.4035208333],#n=2
    [0.3135416667, 0.3057708333, 0.3153750000, 0.3031875000, 0.3058958333],#n=3
    [0.2446458333, 0.2249375000, 0.2307291667, 0.2418125000, 0.2339583333] #n=4
])

#55cm
pallina3_intervalli_h2 = np.array([
    [0.4963125000, 0.5049166667, 0.5036875000, 0.4997500000, 0.4988750000],
    [0.3843541667, 0.3858958333, 0.3751250000, 0.3751666667, 0.3821666667],
    [0.2903958333, 0.2931666667, 0.2845000000, 0.2932916667, 0.2859375000],
    [0.2301666667, 0.2330625000, 0.2255833333, 0.2350625000, 0.2276666667]
])


#45cm
pallina3_intervalli_h3 = np.array([
    [0.4531458333, 0.4587708333, 0.4563333333, 0.4579583333, 0.4575000000],
    [0.3544375000, 0.3429583333, 0.3511666667, 0.3449166667, 0.3479791667],
    [0.2625208333, 0.2556875000, 0.2642083333, 0.2757291667, 0.2700208333],
    [0.1993750000, 0.2065000000, 0.2117916667, 0.1896458333, 0.2099375000]
])

#35cm
pallina3_intervalli_h4 = np.array([
    [0.4111458333, 0.4067708333, 0.4083333333, 0.4102916667, 0.4071875000],
    [0.3054166667, 0.3086666667, 0.3085000000, 0.3113541667, 0.3111875000],
    [0.2417708333, 0.2395208333, 0.2351041667, 0.2365000000, 0.2398958333],
    [0.1780625000, 0.1829375000, 0.1773541667, 0.1771250000, 0.1855208333]
])


#25cm
pallina3_intervalli_h5 = np.array([
    [0.3495833333, 0.3491666667, 0.3519583333, 0.3470833333, 0.3548125000],
    [0.2667083333, 0.2679166667, 0.2713958333, 0.2680000000, 0.2719791667],
    [0.2026250000, 0.2153750000, 0.2091666667, 0.2035000000, 0.2060625000],
    [0.1527708333, 0.1444375000, 0.1464583333, 0.1504583333, 0.1600833333]
])

pallina3_intervalli = np.array([
    pallina3_intervalli_h1,
    pallina3_intervalli_h2,
    pallina3_intervalli_h3,
    pallina3_intervalli_h4,
    pallina3_intervalli_h5
])
print("------------pallina3------------\n{}".format(pallina3_intervalli))

#------------------------PALLINA4(golf)------------------------
#80cm
pallina4_intervalli_h1 = np.array([
    [0.649500000, 0.722562500, 0.723854167, 0.722104167, 0.723125000],
    [0.583729167, 0.642395833, 0.648666667, 0.646604167, 0.648875000],
    [0.523479167, 0.576687500, 0.587666667, 0.583750000, 0.576375000],
    [0.523479167, 0.517583333, 0.531875000, 0.525291667, 0.512875000],
    [0.463500000, 0.468562500, 0.479250000, 0.470791667, 0.459416667],
    [0.407291667, 0.422041667, 0.436229167, 0.421458333, 0.410541667],
    [0.364500000, 0.384208333, 0.391250000, 0.376354167, 0.365770833],
    [0.327770833, 0.348687500, 0.350125000, 0.337041667, 0.326104167]
])

#90cm
pallina4_intervalli_h2 = np.array([
    [0.675083333, 0.762458333, 0.759145833, 0.764041667, 0.763395833],
    [0.603562500, 0.682187500, 0.680041667, 0.682791667, 0.683354167],
    [0.533166667, 0.611833333, 0.606312500, 0.609437500, 0.614333333],
    [0.478479167, 0.551312500, 0.544041667, 0.545333333, 0.557520833],
    [0.432312500, 0.493812500, 0.488541667, 0.479354167, 0.504916667],
    [0.386291667, 0.439229167, 0.437062500, 0.425687500, 0.457833333],
    [0.349437500, 0.391437500, 0.387687500, 0.378437500, 0.416270833],
    [0.315729167, 0.344687500, 0.348875000, 0.338166667, 0.377729167]
    
])

#100cm
pallina4_intervalli_h3 = np.array([
    [0.793875000, 0.811083333, 0.804041667, 0.790958333, 0.803541667],
    [0.716062500, 0.725229167, 0.718270833, 0.709979167, 0.716270833],
    [0.636604167, 0.643500000, 0.644083333, 0.638375000, 0.644854167],
    [0.561562500, 0.580312500, 0.579645833, 0.574166667, 0.581125000],
    [0.503520833, 0.517604167, 0.500854167, 0.518145833, 0.524770833],
    [0.451520833, 0.460187500, 0.449791667, 0.468375000, 0.473125000],
    [0.403187500, 0.420666667, 0.400791667, 0.425020833, 0.429354167],
    [0.366895833, 0.359500000, 0.355875000, 0.385958333, 0.390625000]

])

#110cm
pallina4_intervalli_h4 = np.array([
    [0.845250000, 0.838125000, 0.837541667, 0.831916667, 0.845187500],
    [0.759895833, 0.750916667, 0.745604167, 0.742312500, 0.752770833],
    [0.681854167, 0.672937500, 0.666208333, 0.664833333, 0.675458333],
    [0.608395833, 0.606708333, 0.593541667, 0.591083333, 0.609083333],
    [0.543312500, 0.546562500, 0.527541667, 0.527125000, 0.549145833],
    [0.487625000, 0.492375000, 0.464895833, 0.472416667, 0.492645833],
    [0.420604167, 0.438041667, 0.416833333, 0.423125000, 0.441208333],
    [0.376979167, 0.388479167, 0.372500000, 0.364791667, 0.395562500]
])
cont = 1
for i in pallina4_intervalli_h4:
    crea_tabella(i, cont, 7, "computed_data/pallina4_intervalli_h4_n{}.tex".format(cont), "centrata")
    cont = cont+1


pallina4_intervalli = np.array([
    pallina4_intervalli_h1,
    pallina4_intervalli_h2,
    pallina4_intervalli_h3,
    pallina4_intervalli_h4
])
print("------------pallina4------------\n{}".format(pallina4_intervalli))
































