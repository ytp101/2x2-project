import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def factory_and_increase_value(factory):
    factory[-1] += 1
    for i in range(len(factory) - 1, -1, -1):
        if factory[i] > 4:
            factory[i] = 1
            if i > 0:
                factory[i - 1] += 1

def process_pattern(pattern):
    results = [0] * 4
    for value in pattern:
        results[0] ^= value in (1, 2, 3)
        results[1] ^= value in (1, 2, 4)
        results[2] ^= value in (1, 3, 4)
        results[3] ^= value in (2, 3, 4)
    return results

def generate_data():
    data = []
    pattern_factory = [1, 1, 1, 0]

    for _ in range(4 ** len(pattern_factory)):
        processed_pattern = process_pattern(pattern_factory)
        pattern_values = pattern_factory[:]
        data.append({
            'ID': len(data) + 1,
            'Result': processed_pattern,
            'Pattern': pattern_values,
            'R1': processed_pattern[0],
            'R2': processed_pattern[1],
            'R3': processed_pattern[2],
            'R4': processed_pattern[3],
            'P1': pattern_values[0],
            'P2': pattern_values[1],
            'P3': pattern_values[2],
            'P4': pattern_values[3]
        })
        factory_and_increase_value(pattern_factory)

    return data

def main():
    columns = ['ID', 'Result', 'R1', 'R2', 'R3', 'R4', 'Pattern', 'P1', 'P2', 'P3', 'P4']
    data = generate_data()
    df = pd.DataFrame(data, columns=columns)

    # Plot each pattern along with its corresponding result
    patterns = df['Pattern']
    results = df['Result']

    num_patterns = len(patterns)
    num_scaled_values = len(results.iloc[0])

    plt.figure(figsize=(10, 6))

    # X positions for each group of patterns
    pattern_positions = np.arange(num_patterns)

    # Width of each bar within a group
    bar_width = 0.2

    plt.xlabel('Pattern')
    plt.ylabel('Result')
    plt.title('Result for Each Pattern')
    # Plot each pattern's result as a grouped bar
    for i in range(num_scaled_values):
        x_positions = pattern_positions + i * bar_width
        plt.bar(x_positions, [result[i] for result in results], width=bar_width, label=f'R{i+1}')

    # Adjust x-axis ticks to center grouped bars
    plt.xticks(pattern_positions + bar_width * (num_scaled_values - 1) / 2, patterns, rotation=45)
    plt.legend()
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    main()