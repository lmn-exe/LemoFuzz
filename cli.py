import argparse
import options


class Cli:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def build_parser(self):
        self.parser.add_argument("-u", "--url", type=str, required=True, help="The URL to fuzz")
        self.parser.add_argument("-w", "--wordlist", type=str, required=True, help="Path to the wordlist file")
        self.parser.add_argument("-e", "--extension", type=str, help="Extension information")
        self.parser.add_argument("-s", "--status", type=int, default=0, help="Status information")
        self.parser.add_argument("-t", "--threads", type=int, default=4, help="Number of threads to use for scanning")
        self.parser.add_argument("-a", "--user-agent", type=str, default="LemoFuzz/1.0", help="User-Agent header to use for requests")

        self.parser.add_argument("-b", "--response-size", type=int, default=0, help="Response size to match")
        self.parser.add_argument("-c", "--content-type", type=str, default="", help="Content-Type to match")
        self.parser.add_argument("-m", "--text", type=str, default="", help="Text to search for in responses")
        self.parser.add_argument("-o", "--timeout", type=int, default=0, help="Timeout for requests in milliseconds")

    def parse_args(self):
        args = self.parser.parse_args()
        
        opt = options.Options(
            url=args.url,
            wordlist_path=args.wordlist,
            extension=args.extension,
            status=args.status,
            num_threads=args.threads,
            user_agent=args.user_agent
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