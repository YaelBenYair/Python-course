import argparse
from db_from_python import is_in_top_250, rating_more_then, func

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
            prog='movie searcher',
            description='The program return if the name of the movie exist',
            epilog='Text at the bottom of help')

    parser.add_argument('-m', '--moviename', type=str, help="name of movie")
    parser.add_argument('-n', '--num', help="num rating")

    args = parser.parse_args()
    if args.moviename is not None:
        print(is_in_top_250(args.moviename.split(",")))
        # print(func(args.moviename))
    if args.num is not None:
        print(rating_more_then(args.num))
