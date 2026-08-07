## we call def cli to get options cli
## call scanner with options

# import cli
# import http_engine

# def main():
#     cli_instance = cli.Cli()
#     cli_instance.build_parser()
#     options = cli_instance.parse_args()

#     print(options.url)
    
# main()
import cli
import http_engine
import scanner

def main():
    cli_instance = cli.Cli()
    cli_instance.build_parser()
    options = cli_instance.parse_args()

    engine = http_engine.HttpEngine(options)

    response = engine.send(options.url)

    if response is None:
        print("Request failed.")
    else:
        print(f"Status Code: {response.status_code}")
        print(f"URL: {response.url}")
        print(response.text[:200])  # Print first 200 characters
        scanner_instance = scanner.Scanner(options)
        scanner_instance.run()
    


if __name__ == "__main__":
    main()