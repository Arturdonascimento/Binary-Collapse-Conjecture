# DeltaProcess.py
# Script to simulate the Binary Collapse (Delta) process

def rev_k(n):
    bin_n = bin(n)[2:]
    return int(bin_n[::-1], 2)

def delta_process(n):
    seen = set()
    steps = 0
    history = []
    while n != 0 and n not in seen:
        seen.add(n)
        history.append(n)
        k = n.bit_length()
        n = abs(n - rev_k(n))
        steps += 1
    return {
        "steps_to_collapse": steps,
        "final_value": n,
        "cycle": history[-2:] if n in seen else []
    }

# Example usage
if __name__ == "__main__":
    for i in range(1, 21):
        result = delta_process(i)
        print(f"n = {i}, steps = {result['steps_to_collapse']}, final = {result['final_value']}, cycle = {result['cycle']}")
