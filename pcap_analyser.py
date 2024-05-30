# suppress PEP8 import errors due to PATH settings
# pylint: disable=E0401
"""Master script to run the packet capture analysis program."""

import argparse

from pcapanalyser.captureanalyser import CaptureAnalyser, FUNCTION_MAP
from pcapanalyser.utils import is_valid_pcap_file, create_logger


def parse_args() -> argparse.Namespace:
    """Set up argument parsing."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file",
        help="The PCAP file to analyse",
        type=lambda y: is_valid_pcap_file(y, parser),
    )
    parser.add_argument("command", default="all", choices=FUNCTION_MAP.keys())
    parser.add_argument(
        "--out",
        default="pcapanalyser/outputs/results.txt",
        help="File path to write the results of the analysis",
    )
    args = parser.parse_args()
    return args


def main(args: argparse.Namespace) -> None:
    """Create a CaptureAnalyser object and handle argument presences."""
    logger = create_logger()
    logger.info("Program Started")
    capture_analyser = CaptureAnalyser(args.file)
    # Use command from CLI input, map it to a python function and execute.
    # CaptureAnalyser.<input_command>()
    print(getattr(capture_analyser, FUNCTION_MAP[args.command])(writefile=args.out))


if __name__ == "__main__":
    arguments = parse_args()
    main(arguments)
