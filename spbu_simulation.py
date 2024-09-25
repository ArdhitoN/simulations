import numpy as np
import matplotlib.pyplot as plt

# Parameters
D_0 = 10000     # Base demand ketika harganya sama (L/hari)
b = 50      # Koefisien sensitivitas market terhadap harga (L/unit rupiah)
C = 10000       # Harga per liter 
P_A = 18000     # Harga bensin di stasiun A

# Dengan cara analitik untuk menentukan optimal price Stasiun B
P_B_optimal = (D_0 / (2 * b)) + (P_A / 2) + (C / 2)

print(f"[Analytical Approach] Harga Optimal Stasiun B: {P_B_optimal:.4f} rupiah/L")

# Range of prices for Station B to simulate
Max_Difference_PA_PB = 10000 
P_B_values = np.linspace(C, P_A + Max_Difference_PA_PB, 500)  

# Menghitung demand dan profit untuk setiap harga
D_B_values = D_0 - b * (P_B_values - P_A)
pi_B_values = (P_B_values - C) * D_B_values

# Mencari profit maksimum 
max_profit_index = np.argmax(pi_B_values)
P_B_max_profit = P_B_values[max_profit_index]
max_profit = pi_B_values[max_profit_index]

print(f"[Simulation] Harga Optimal Stasiun B: {P_B_max_profit:.4f} rupiah/L")
print(f"[Simulation] Maximum Profit Stasiun B: {max_profit:.2f} rupiah/hari")

# Visualisasi Dampak Harga Per Liter Terhadap Profit Per Hari
plt.figure(figsize=(10, 6))
plt.plot(P_B_values, pi_B_values, label='Profit Function')
plt.axvline(x=P_B_optimal, color='r', linestyle='--', label=f'Analytical Optimal Price = {P_B_optimal:.4f}')
plt.axvline(x=P_B_max_profit, color='g', linestyle='--', label=f'Simulated Optimal Price = {P_B_max_profit:.4f}')
plt.title('Profit vs. Price per Litre (Stasiun B)')
plt.xlabel('Harga Per Liter (Rupiah)')
plt.ylabel('Profit (per hari)')
plt.legend()
plt.grid(True)
plt.show()
