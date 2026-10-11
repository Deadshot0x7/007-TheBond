from pathlib import Path
import subprocess
import sys
import argparse

# glob
red = "\033[31m"
yellow = "\033[33m"
reset_c = "\033[0m"


class AutoInstaller:
    def __init__(self):
        self.py_exec , self.pip_exec = None, None

    def get_modules(
        self, file: str | None = None, delim: str | None = None
    ) -> list[str]:
        """
        parse modules from a requirements.txt or a given file
        """
        file = file if file else "requirements.txt"
        delim = delim if delim else "#"
        modules: list[str] = []

        if not Path(file).exists():
            return modules

        with open(file, mode="r", encoding="utf-8") as fp:
            for line in fp:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                module = line.split(delim)[0].strip()
                if module:
                    modules.append(module)

        return modules

    def create_and_setup_venv(self, v_path:str) -> None:
        """
        creates and sets up a virtual env for python
        """
        v_path = v_path
        venv_path = Path(v_path)
        
        if sys.platform == "win32":
            self.py_exec = venv_path / "Scripts" / "python.exe"
            self.pip_exec = venv_path / "Scripts" / "pip.exe"
        else:
            self.py_exec = venv_path / "bin" / "python"
            self.pip_exec = venv_path / "bin" / "pip"

        # creating the venv
        if not venv_path.exists():
            print(f"+ creating virtual environment at {v_path}")
            result = subprocess.run(
                [sys.executable, "-m", "venv", str(venv_path)],
                capture_output=True,
                text=True,
                check=False,
            )
            if result.returncode != 0:
                print(f"+ error: {red}{result.stderr.strip()}{reset_c}")
                return
        else:
            print("+ a virtual environment already exists.")

        # upgrading pip
        print("+ upgrading pip")
        upgrade_pip = subprocess.run(
            [str(self.py_exec), "-m", "pip", "install", "--upgrade", "pip"],
            capture_output=True,
            text=True,
            check=False,
        )

        if upgrade_pip.returncode != 0:
            print(f"+ warn: {yellow}unable to upgrade pip.{reset_c}")
            print(f"> details: {upgrade_pip.stderr.strip()}")

        # installing packages using self.get_modules()
        modules = self.get_modules()
        if not modules:
            print("+ no modules found to install.")
            return

        print(f"+ installing packages: {modules}")
        install_result = subprocess.run(
            [str(self.pip_exec), "install"] + modules,
            capture_output=True,
            text=True,
            check=False,
        )

        if install_result.returncode != 0:
            print(f"+ error: {red}unable to install modules{reset_c}")
            print(f"> details: {install_result.stderr.strip()}")
        else:
            print("+ all packages installed successfully!")

    def run_thebond(self):
        path = Path("scripts/007-TheBond.py")
        if not path.exists():
            print(f"+ unable to find {str(path)}")
            return

        result = subprocess.run([str(self.py_exec), str(path)])
        if result.returncode != 0:
            print(f"+ error: {red}unable to run{reset_c} {str(path)}")
            print(f"> details: {result.stderr.strip()}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="auto-installer args Menu")

    parser.add_argument("-vp", "--venv-path", required=False, type=str, default=".venv", help="specify where to create venv")

    return parser.parse_args()

def main():
    args = parse_args()
    min_required_ver = (3, 10)
    installer = AutoInstaller()

    if sys.version_info < min_required_ver:
        print(
            f"python 3.10+ is required. found python {sys.version_info[0]}.{sys.version_info[1]}"
        )
        return

    installer.create_and_setup_venv(args.venv_path)
    installer.run_thebond()


if __name__ == "__main__":
    main()
