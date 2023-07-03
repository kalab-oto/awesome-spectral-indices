from enum import Enum, unique


@unique
class Bands(Enum):
    """
    Bands supported by SpectralIndex DataClass
    """

    AEROSOL = "A"
    BLUE = "B"
    GREEN1 = "G1"
    GREEN = "G"
    YELLOW = "Y"
    RED = "R"
    NIR = "N"
    NIR2 = "N2"
    WATERVAPOUR = "WV"
    RED1 = "RE1"
    RED2 = "RE2"
    RED3 = "RE3"
    SWIR1 = "S1"
    SWIR2 = "S2"
    TIR = "T"
    TIR1 = "T1"
    TIR2 = "T2"
    GAIN_FACTOR = "g"
    CANOPY_BACKGROUND_ADJUSTMENT = "L"
    AEROSOL_COEFFICIENT1 = "C1"
    AEROSOL_COEFFICIENT2 = "C2"
    C_EXPONENT = "cexp"
    N_EXPONENT = "nexp"
    GAMMA = "gamma"
    ALPHA = "alpha"
    BETA = "beta"
    SOIL_LINE_SLOPE = "sla"
    SOIL_LINE_INTERCEPT = "slb"
    PAR = "PAR"
    OMEGA = "omega"
    F_DELTA = "fdelta"
    EPSILON = "epsilon"
    SLOPE_PARAMETER_SOIL = "k"
    WAVELENGTH_NIR = "lambdaN"
    WAVELENGTH_RED = "lambdaR"
    WAVELENGTH_GREEN = "lambdaG"
    HV = "HV"
    HH = "HH"
    VV = "VV"
    VH = "VH"
    KNN = "kNN"
    KNR = "kNR"
    KNB = "kNB"
    KNL = "kNL"
    KGG = "kGG"
    KGR = "kGR"
    KGB = "kGB"
    KBB = "kBB"
    KBR = "kBR"
    KBL = "kBL"
    KRR = "kRR"
    KRB = "kRB"
    KRL = "kRL"
    KLL = "kLL"


class IndexType(Enum):
    """
    IndexType supported by SpectralIndex DataClass
    """

    VEGETATION = "vegetation"
    WATER = "water"
    BURN = "burn"
    SNOW = "snow"
    SOIL = "soil"
    URBAN = "urban"
    KERNEL = "kernel"
    RADAR = "radar"
