import pandas as pd
import numpy as np
import os

def generate_simulated_data(n=500):
    np.random.seed(42)

    # Create a folder if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Simulate the data
    data = pd.DataFrame({
        'age': np.random.randint(25, 50, size=n),
        'bmi': np.random.normal(24, 3, size=n),
        'hours_in_heat': np.random.randint(4, 10, size=n),
        'temp': np.random.normal(44, 2, size=n),
        'humidity': np.random.randint(10, 50, size=n),
        'bp_sys': np.random.normal(120, 10, size=n),
        'bp_dia': np.random.normal(80, 5, size=n),
        'heart_rate': np.random.normal(90, 15, size=n),
        'urine_color': np.random.randint(1, 5, size=n),
        'water_intake_liters': np.round(np.random.normal(2.5, 0.7, size=n), 2),
        'diabetes': np.random.choice([0, 1], size=n, p=[0.85, 0.15]),
        'prior_dehydration': np.random.choice([0, 1], size=n, p=[0.7, 0.3]),
    })

    # Define the risk column
    data['kidney_stress_risk'] = (
        (data['hours_in_heat'] > 6) & 
        (data['temp'] > 45) & 
        (data['water_intake_liters'] < 2.0) | 
        (data['urine_color'] >= 3) | 
        (data['prior_dehydration'] == 1)
    ).astype(int)

    # Save the CSV
    data.to_csv("data/simulated_health_data.csv", index=False)
    print("Simulated dataset saved to data/simulated_health_data.csv")

# Run the function
if __name__ == "__main__":
    generate_simulated_data()
