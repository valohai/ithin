import click
import pickle
import os

from ithin.summarizer import make_summary_html
from ithin.processor import get_images, IthinProcessor


@click.command()
@click.option('-d', '--directory', required=True)
@click.option('-o', '--output', required=True, type=click.Path(dir_okay=False))
@click.option('-t', '--threshold', type=float, default=0.03, help='difference threshold', show_default=True)
@click.option('-s', '--size', type=int, default=64, help='resize images to a square of this size', show_default=True)
def process(directory, threshold, output, size):
    """
    Process a directoryful of images into a pickle file of groups
    """
    images = get_images(directory)
    print('%d JPEGs found.' % len(images))
    proc = IthinProcessor(threshold=threshold, size=size)
    with click.progressbar(images, width=50) as images:
        for filename in images:
            try:
                proc.process_file(name=filename, filename=os.path.join(directory, filename))
            except (OSError, IOError) as e:
                print('!', filename, e)

    with open(output, 'wb') as outf:
        pickle.dump(proc.groups, outf)


@click.command()
@click.option('-i', '--input', type=click.Path(file_okay=True, exists=True, dir_okay=False))
@click.option('-o', '--output', default='summary.html')
def summarize(input, output):
    """
    Summarize the contents of a pickle file into HTML
    """
    with open(input, 'rb') as infp:
        groups = pickle.load(infp)
    html = make_summary_html(groups)
    with open(output, 'w') as outfp:
        outfp.write(html)


@click.group()
def cli():
    pass

cli.add_command(process)
cli.add_command(summarize)
