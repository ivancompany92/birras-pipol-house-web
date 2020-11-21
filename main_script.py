import argparse
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr


def argument_parser():
    choices_list = ['Y', 'N']
    parser = argparse.ArgumentParser(description='Set conditions to the program')
    parser.add_argument("-s", "--scraping", type=str, choices=choices_list, dest='scrape',
                        default='N', help="Scrape and update the beer database")

    args = parser.parse_args()
    return args


def main(scrape):
    print('Starting Pipeline...')
    mac.acquire(scrape)
    mwr.wrangle(scrape)
    print('Finished Pipeline')


if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments.scrape)
