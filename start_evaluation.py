from optparse import OptionParser
from apievaluation import apievaluation
import json
import sys
import settings


def main(argv):


    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-n", "--noimages", dest="no_images",
                      help="number images to parse", metavar="integer")

    (options, args) = parser.parse_args()

    if (options.no_images is None) or (len(options.no_images) == 0):
        parser.error("Missing argument -n")
    elif int(options.no_images) > 0:
        result = apievaluation.initiate_test(int(options.no_images))
        file = open(settings.ROOT_DIR+'/res/result.json', 'w+')
        file.write(json.dumps(result, sort_keys=True, indent=4, separators=(',', ': ')))
        print 'Wrote result to "%s"' % settings.ROOT_DIR+'/res/result.json'
    else:
        parser.error("Argument -n should be more than %d" % int(options.no_images))







if __name__ == "__main__":
    main(sys.argv)