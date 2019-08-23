from howdoi import howdoi

def get_output(query):
    parser = howdoi.get_parser()
    args = vars(parser.parse_args(query.split(' ')))
    output = howdoi.howdoi(args)
    return output