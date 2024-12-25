from pprint import pprint
import argparse
from . import IBDFileParser


def main():
    parser = argparse.ArgumentParser(description='InnoDB IBD file parser')
    parser.add_argument('-f', '--file', required=True, help='Path to .ibd file')

    subparsers = parser.add_subparsers(dest='command', required=True, help='Sub-command to run')

    # Sub-command: header
    header_parser = subparsers.add_parser('page-dump', help='Show page header')
    header_parser.add_argument('--page', type=int, required=True, help='Page number to analyze')


    args = parser.parse_args()

    ibd_parser = IBDFileParser(args.file)

    if args.command == 'page-dump':
        result = ibd_parser.page_dump(args.page)
        print("file header:")
        print(result['header'].format())
        print("\nfile trailer:")
        print(result['trailer'].format())
        if 'page_header' in result:
            print("\npage header:")
            print(result['page_header'].format_as_string())
        if 'page_directory' in result:
            print("\npage directory:")
            pprint(result['page_directory'])

if __name__ == '__main__':
    main()
