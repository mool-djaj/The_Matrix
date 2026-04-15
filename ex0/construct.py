import sys
import os
import site


def is_in_venv() -> bool:
    """Check if the script is running inside a virtual environment."""
    return sys.prefix != sys.base_prefix


def print_outside_matrix() -> None:
    """Print the required output when not in a virtual environment."""
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate")
    print("Then run this program again.")


def print_inside_matrix() -> None:
    """Print the required output when running inside a virtual environment."""
    env_path: str = sys.prefix
    env_name: str = os.path.basename(env_path)
    site_packages: list[str] = site.getsitepackages()
    pkg_path: str = site_packages[0] if site_packages else "Unknown"

    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {env_path}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("Package installation path:")
    print(pkg_path)


def main() -> None:
    """Main execution function."""
    if is_in_venv():
        print_inside_matrix()
    else:
        print_outside_matrix()


if __name__ == "__main__":
    main()
