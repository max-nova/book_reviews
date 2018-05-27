import argparse
import pandas as pd


def parse(fn, out_fn):
    df = pd.read_csv(fn, header=7)  # starts on line 7
    with open(out_fn, 'w') as f:
        for note in df['Annotation']:
            f.write(note + '\n\n')

    return out_fn


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract Kindle highlights')
    parser.add_argument('kindle_highlights', type=str)
    parser.add_argument('out_fn', default='/tmp/highlights.txt')
    args = parser.parse_args()
    print parse(args.kindle_highlights, args.out_fn)
