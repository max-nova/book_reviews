import argparse
import glob
import os


def merge(covers_dir, out_fn):
    """
    Useful for updating header image on blog and on cards
    """
    covers = glob.glob(os.path.join(covers_dir, '*'))
    html = """
<html>
<head>
    <style>
        .cover {
            height: 300px;
            width: 200px;
            display: inline-block;
            vertical-align:top;
            line-height: 0px;
            padding: 0px;
            margin: 0px;
        }
    </style>
</head>

<body>
"""
    for c in covers:
        html += '<img src="%s" class="cover">' % c

    html += """
</body>
</html>
"""
    with open(out_fn, 'w') as f:
        f.write(html)

    return out_fn


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create HTML with all titles')
    parser.add_argument('covers_dir', type=str)
    parser.add_argument('out_fn', default='/tmp/covers.html')
    args = parser.parse_args()
    print merge(args.covers_dir, args.out_fn)
