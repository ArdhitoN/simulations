import random

def simulate_train_departure():
    departure_times = [13*60, 13*60+5, 13*60+10]  # Perhitungan jam dan menit keberangkatan kereta (relatif terhadap pukul 00.00)
    probabilities = [0.7, 0.2, 0.1]
    return random.choices(departure_times, probabilities)[0]

def simulate_travel_time():
    return random.randint(28, 32)  # Travel time di antara 28 hingga 32 menit

def simulate_passenger_arrival():
    arrival_times = [13*60+28, 13*60+30, 13*60+32, 13*60+34] # Perhitungan jam dan menit kedatangan pelanggan kereta (relatif terhadap pukul 00.00)
    probabilities = [0.3, 0.4, 0.2, 0.1]
    return random.choices(arrival_times, probabilities)[0]

def run_simulation(num_simulations):
    successes = 0

    for _ in range(num_simulations):
        train_departure = simulate_train_departure()
        travel_time = simulate_travel_time()
        train_arrival = train_departure + travel_time
        passenger_arrival = simulate_passenger_arrival()

        if passenger_arrival <= train_arrival:
            successes += 1

    probability = successes / num_simulations
    return probability

num_simulations = 100000
probability = run_simulation(num_simulations)

print(f"Probabilitas pelanggan kereta dapat menaiki kereta: {probability:.2%}")
