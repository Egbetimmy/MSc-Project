def eaton_method(Vp, Vs, phi):

    # Define constants
    rho_w = 1000  # density of water, kg/m^3

    # Calculate velocity ratio (Vs/Vp)
    vs_vp = Vs / Vp

    # Calculate pore pressure using Eaton's method
    pp = (rho_w * Vp * (vs_vp * 2) * (1 - phi)) / (1 - phi + (vs_vp * 2))
    return pp


def Bowers_method(Vp, Vs, phi):

    # Define constants
    rho_b = 2.65  # bulk density of the formation, g/cm^3
    Z = 0.95  # shale compaction factor

    # Convert bulk density from g/cm^3 to kg/m^3
    rho_b = rho_b * 1000

    # Calculate pore pressure using Bowers' method
    pp = 0.0087 * rho_b * (Vp / Vs) * (Z / (1 - Z)) * (1 / (phi ** 2))

    return pp


def Matthews_Kelly_method(depth, rho):
    """
    Function: Matthews_Kelly_method

    Description: Calculates pore pressure using the Matthews-Kelly method.

    Inputs:
    - depth: depth of the formation, in meters
    - rho: bulk density of the formation, in kg/m^3

    Outputs:
    - pp: pore pressure, in Pascals

    """

    # Define constants
    rho_w = 1000  # density of water, kg/m^3
    g = 9.81  # acceleration due to gravity, m/s^2

    # Calculate formation density
    rho_f = rho - rho_w

    # Calculate pore pressure using Matthews-Kelly method
    pp = rho_f * g * depth

    return pp
