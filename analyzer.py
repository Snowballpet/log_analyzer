from collections import Counter

def analyze_logs(file_path):
    with open(file_path, "r") as file:
        logs = file.readlines()

    errors = [line for line in logs if "ERROR" in line]
    warnings = [line for line in logs if "WARNING" in line]

    print("Total logs:", len(logs))
    print("Errors:", len(errors))
    print("Warnings:", len(warnings))

    error_types = Counter(errors)
    print("\nTop Errors:")
    for k, v in error_types.most_common(5):
        print(k.strip(), ":", v)

if __name__ == "__main__":
    analyze_logs("sample.log")
