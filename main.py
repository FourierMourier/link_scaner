import os
from pathlib import Path
import re
import argparse
import csv
import logging


def main(args: argparse.Namespace) -> int:
    """
    Scans files in the provided directory for URLs and logs results in a CSV file.

    :param args: argparse.Namespace object containing CLI arguments
    :return: 1 if successful, 0 otherwise
    """
    _file_mode: str = 'r'

    source_dir = args.dirpath
    extensions = args.extensions.split(',')
    output_path = args.output
    pattern = re.compile(args.regex)

    ends_with_extensions = tuple(extensions)

    strange_files = []
    output = []

    output_path = Path(output_path)
    output_path.absolute().parents[0].mkdir(exist_ok=True)

    logging.basicConfig(filename='scan_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    for root, _, files in os.walk(source_dir):
        for file in files:
            if not file.endswith(ends_with_extensions):
                continue

            abs_path = os.path.join(root, file)

            with open(abs_path, _file_mode, encoding=args.encoding) as f:
                body = f.read()

            matches = pattern.findall(body)
            if matches:
                for m in matches:
                    output.append((m, abs_path))
                strange_files.append(abs_path)

    if strange_files:
        logging.info(f"Strange files: {strange_files}")
        print(f"Strange files: {strange_files}")
    else:
        logging.info("No strange files found.")
        print("No strange files found.")

    if output:
        header = ['URL', 'File']
        output.insert(0, header)
        with open(str(output_path), 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(output)
            logging.info(f"Output saved to {output_path}")
    else:
        logging.info("No URLs found in the specified directory.")

    return 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Find URLs in source files')
    parser.add_argument('--dirpath', help='Source directory to search for files')
    parser.add_argument('--output', default='strange_files.csv',
                        help='Output CSV file path (can be relative)')
    parser.add_argument('--extensions', default='.py,.yml,.yaml,.txt,.cfg,.ini',
                        help='Comma-separated list of file extensions to scan')
    parser.add_argument('--regex', default=r'https?://\S+',
                        help='Regular expression that will be used to find hidden links in the files')
    parser.add_argument('--encoding', default='utf-8', help='Encoding to open text files')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    main(args)
