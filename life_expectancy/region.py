"""Check that only pass valid regions
"""
from enum import Enum
import pandas as pd

class Region(Enum):
    """List of valid regions
    """
    AT = 'AT'
    BE = 'BE'
    BG = 'BG'
    CH = 'CH'
    CY = 'CY'
    CZ = 'CZ'
    DK = 'DK'
    EE = 'EE'
    EL = 'EL'
    ES = 'ES'
    EU = 'EU'
    FI = 'FI'
    FR = 'FR'
    HR = 'HR'
    HU = 'HU'
    IS = 'IS'
    IT = 'IT'
    LI = 'LI'
    LT = 'LT'
    LU = 'LU'
    LV = 'LV'
    MT = 'MT'
    NL = 'NL'
    NO = 'NO'
    PL = 'PL'
    PT = "PT"
    RO = 'RO'
    SE = 'SE'
    SI = 'SI'
    SK = 'SK'
    DE = 'DE'
    AL = 'AL'
    EA = 'EA'
    EF = 'EF'
    IE = 'IE'
    ME = 'ME'
    MK = 'MK'
    RS = 'RS'
    AM = 'AM'
    AZ = 'AZ'
    GE = 'GE'
    TR = 'TR'
    UA = 'UA'
    BY = 'BY'
    UK = 'UK'
    XK = 'XK'
    FX = 'FX'
    MD = 'MD'
    SM = 'SM'
    RU = 'RU'

    @classmethod
    def list_valid_region(cls, df_with_region:pd.DataFrame, col_name: str ) -> list:
        """Remove inappropriate region values"""
        valid_region=[]
        for reg in df_with_region[col_name]:
            if len(reg) == 2:
                valid_region.append(reg)
        return valid_region
