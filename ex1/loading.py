import importlib
import sys

def check_dependencies() -> bool:
    """Check if all required modules are installed."""
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    
    dependencies = ["pandas", "numpy", "matplotlib"]
    all_ok = True
    
    for dep in dependencies:
        try:
            module = importlib.import_module(dep)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {dep} ({version})")
        except ImportError:
            all_ok = False
            print(f"[FAIL] {dep} is missing.")
            
    if not all_ok:
        print("\nDependencies are missing! You must load the programs.")
        print("To install with pip, run:")
        print("pip install -r requirements.txt")
        print("To install with Poetry, run:")
        print("poetry install")
        print("poetry run python loading.py")
        return False
        
    print("Data manipulation ready")
    print("Numerical computation ready")
    print("Visualization ready")
    return True

def analyze_matrix() -> None:
    """Generate simulated data, analyze it, and create a visualization."""

    import numpy
    import pandas
    import matplotlib.pyplot as plt
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    raw_signals = numpy.random.rand(1000)

    df = pandas.DataFrame(raw_signals, columns=["Signal_Strength"])

    print("Generating visualization...")
    plt.figure(figsize=(10, 5))
    plt.plot(df["Signal_Strength"], color="green", linewidth=0.8)
    plt.title("Matrix Signal Interception")
    plt.xlabel("Time (ms)")
    plt.ylabel("Signal Strength")    
    plt.savefig("matrix_analysis.png")    
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    """Main entry point for the loader."""
    if check_dependencies():
        analyze_matrix()
    else:
        exit(1)
    


if __name__ == "__main__":
    main()
