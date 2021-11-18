from enum import Enum, unique

@unique
class Bands(Enum):
    """
    Bands supported by SpectralIndex DataClass
    """
    AEROSOL = "A"
    BLUE = "B"
    GREEN = "G"
    RED = "R"
    NIR = "N"
    RED1 = "RE1"
    RED2 = "RE2"
    RED3 = "RE3"
    RED4 = "RE4"
    SWIR1 = "S1"
    SWIR2 = "S2"
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
    SOIL_LINE_SLOPE = "sla"
    SOIL_LINE_INTERCEPT = "slb"
    PAR = "PAR"
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
    DROUGHT = "drought"
    URBAN = "urban"
    KERNEL = "kernel"