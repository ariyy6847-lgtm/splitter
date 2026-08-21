"""Minimal example for Splitter."""

from splitter import splitter


def main():
 runner = splitter({"name": "Splitter", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()