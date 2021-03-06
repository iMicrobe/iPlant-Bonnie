#!/usr/bin/env python
import csv

from optparse import OptionParser
import FeatureApi

def main():

	parser = OptionParser()
	parser.add_option("-f", "--file", dest="ifile",
                  help="file to be imported", type="string")

	(options, args) = parser.parse_args()

	if options.ifile == None :
                raise TypeError('filename missing from command-line.')

	api = FeatureApi.FeatureApi()
	api.feature_annotate(options.ifile)

if __name__ == "__main__":
    main()

