import numpy as np

# parameters
a_hit = 0.8
a_short = 0.1 
a_max = 0.05
a_rand = 0.05
lambda_short = 0.1
sigma_hit = 0.2
z_max = 7.0
eps = 1e-6

def p_hit(actual, predicted):
    if 0 <= actual <= z_max:
        a = 1.0 / (np.sqrt(2 * np.pi) * sigma_hit)
        b = np.exp(-0.5 * ((actual - predicted) / sigma_hit) ** 2)
        return a * b
    return 0.0

def p_short(actual, predicted):
    if 0 <= actual <= predicted:
        den = 1.0 - np.exp(-lambda_short * predicted)
        num = lambda_short * np.exp(-lambda_short * actual)
        return num / den
    return 0.0

def p_rand(actual, predicted):
    if 0 <= actual <= z_max:
        return 1.0 / z_max
    return 0.0

def p_max(actual, predicted):
    return 1.0 if abs(actual - z_max) < eps else 0.0

def beam_model(z, z_star):
    return (a_hit * p_hit(z, z_star)) + (a_short * p_short(z, z_star)) + (a_max * p_max(z, z_star)) + (a_rand * p_rand(z, z_star))
        
def main():
    real_readings = [2.2, 4.67, 6.1, 7.0]

    particles = [
        [4*np.sqrt(2), 4*np.sqrt(2), np.sqrt(2), np.sqrt(2)],   # p1
        [np.sqrt(2), 2*np.sqrt(2), 2*np.sqrt(2), np.sqrt(2)],   # p2
        [2.0, 1.0, 10.0, 4.0],                                  # p3
        [5.0, 2.0, 3.0, 10.0]                                   # p4
    ]

    print("P\t" + "\t".join([f"z={z:.2f}   " for z in real_readings]))
    for i in range(len(real_readings)):
        print(f"{i+1}", end="")
        for j in range(len(real_readings)):
            prob = beam_model(real_readings[j], particles[i][j])
            print(f"\t{prob:.6f}", end="")
        print()


if __name__ == "__main__":
    main()