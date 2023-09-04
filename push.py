from __future__ import annotations
import subprocess
import os


MAX_BLOCK_SIZE = 100_000_000


def unadded_files() -> list[str]:
    return (
        subprocess.check_output(["git", "ls-files", "--others", "--exclude-standard"]).decode().split("\n")[:-1]
    )


def unadded_files_with_size(list_of_files: list[str]) -> list[tuple[str, int]]:
    return [(file, os.path.getsize(file)) for file in list_of_files]


def group_files(list_of_files: list[tuple[str, int]]) -> list[list[tuple[str, int]]]:
    groups = []
    current_group = []
    current_size = 0
    for file, size in list_of_files:
        if current_size + size > MAX_BLOCK_SIZE:
            groups.append(current_group)
            current_group = []
            current_size = 0
        current_group.append((file, size))
        current_size += size
    groups.append(current_group)
    return groups


def main():
    for unadded_file in unadded_files():
        subprocess.run(["git", "add", unadded_file])
        subprocess.run(["git", "commit", "-m", f"Add {unadded_file}"])
        subprocess.run(["git", "push"])


if __name__ == "__main__":
    main()
