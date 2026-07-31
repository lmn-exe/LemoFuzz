import argparse
import options


class Cli:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def build_parser(self):
        self.parser.add_argument("-u", "--url", type=str, required=True, help="The URL to fuzz")
        self.parser.add_argument("-w", "--wordlist", type=str, required=True, help="Path to the wordlist file")
        self.parser.add_argument("-e", "--extension", type=str, help="Extension information")
        self.parser.add_argument("-s", "--status", type=str, help="Status information")
        self.parser.add_argument("-t", "--threads", type=int, help="Number of threads to use for scanning")

    def parse_args(self):
        args = self.parser.parse_args()
        
        opt = options.Options(
            url=args.url,
            wordlist_path=args.wordlist,
            extension=args.extension,
            status=args.status,
            num_threads=args.threads
        )
        return opt


# parser = argparse.ArgumentParser()

# def build_parser():
#     parser.add_argument("-u","--url", type=str, required=True, help="The URL to fuzz")
#     parser.add_argument("-w","--wordlist", type=str, required=True, help="Path to the wordlist file")
#     parser.add_argument("-e","--extension", type=str, help="Extension information")
#     parser.add_argument("-s","--status", type=str, help="Status information")


# def parse_args():
#     args = parser.parse_args()

#     opt = options.Options(
#         url=args.url,
#         wordlist_path=args.wordlist,
#         extension=args.extension,
#         status=args.status
#     )
#     return opt