#!/usr/bin/env python3

from github_utils import gh_fetch_url_and_headers
def main():
    import os
    print([x for x in os.environ['SECRET']])


if __name__ == "__main__":
    main()
