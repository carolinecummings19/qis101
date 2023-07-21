#!/usr/bin/env python3
"""hydrogen_spectrum.py"""

# Caroline Cummings - Task 08-01
# Calculates and displays wavelength (nm) for Pfund and Humphrey high energy
# spectral series of hydrogen

# From spectrum_bohr.py
def spectrum_bohr (n1: int, n2: int) -> float:
    """Calculates wavelength using Bohr's formula"""
    e_charge: float = 1.602e-19
    e_mass: float = 9.109e-31
    permittivity: float = 8.854e-12
    h_plank: float = 6.626e-34
    speed_light: float = 2.998e8

    # Bohr's formula for ground state energy
    e_0: float = (pow(e_charge, 4) * e_mass) / (
        8 * pow(permittivity, 2) * pow(h_plank, 2)
    )

    # Initial energy level
    e_i: float = -e_0 / pow(n2, 2)
    # Final energy level
    e_f: float = -e_0 / pow(n1, 2)
    # Formula for waveLength in nanometers
    wave_length: float = h_plank * speed_light / (e_i - e_f) * 1e9

    return wave_length

# From spectrum_rydberg.py
def spectrum_rydberg (n1: int, n2: int) -> float:
    """Calculates wavelength using Rydberg's formula"""
    rydberg_constant: float = 1.0967757e7
    # Formula for waveLength in nanometers
    wave_length: float = (
        1 / (rydberg_constant * (1 / pow(n1, 2) - 1 / pow(n2, 2))) * 1e9
    )
    return wave_length

def main() -> None:
    series: list[str] = ["Lyman", "Balmer", "Paschen", "Brackett", "Pfund", "Humphrey"]

    print("\tBohr Model for \t\t\tRydberg Formula for")
    print("\tHydrogen Spectral Lines \tHydrogen Spectral Lines")

    for k in range(1, 7):
        print(series[k - 1])
        for j in range(k + 1, k + 6):
            # Calculate Bohr
            wave_len1: float = spectrum_bohr(k, j)

            #Calculate Rydberg
            wave_len2: float = spectrum_rydberg(k, j)

            # Print output
            print(f"\t{j:>2} -> {k:>2}{wave_len1:8.0f} nm", 
                  f"\t\t{j:>2} -> {k:>2}{wave_len2:8.0f} nm") 
            
        print()

if __name__ == "__main__":
    main()


#Additionl comments

'''looks good only thing I would mention is that your output includes extra information that's not necessary.'''
'''Score 4'''