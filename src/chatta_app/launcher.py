from pathlib import Path

from streamlit.web import cli


def main():
    exec_path = Path(__file__).parent / "app.py"
    print(f"\nExecute file: {exec_path}")
    cli.main_run([str(exec_path)])


if __name__ == "__main__":
    main()
