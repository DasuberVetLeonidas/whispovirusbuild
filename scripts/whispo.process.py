from __future__ import print_function
import os, sys
# we assume (and assert) that this script is running from the virus directory, i.e. inside H7N9 or zika
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
import base.process
from base.process import process


def collect_args():
    """Returns a Zika-specific argument parser.
    """
    parser = base.process.collect_args()
    parser.set_defaults(
        json="prepared/hendra.json"
    )
    return parser


config = {
    "dir": "hendra",
    "in": "prepared/hendra.json",
    "newick_tree_options": {"nthreads": 4},
    "clock_filter": {
        "n_iqd": 4,
    },
    "geo_inference": ['town'], # what traits to perform this on
    "geo_inference_options": {
        "root_state": {
            "town": "cliftonbeach",
            "host": "horse"
        },
    },
    "auspice": { ## settings for auspice JSON export
        "color_options": {
            # "authors": {"key":"authors", "legendTitle":"Authors", "menuItem":"authors", "type":"discrete"},
            "town": {"key": "town", "legendTitle": "Town", "menuItem": "town", "type": "discrete"},
            "host": {"key": "host", "legendTitle": "Host", "menuItem": "host", "type": "discrete"}
        },
        "controls": {'authors':['authors']},
        "defaults": {'mapTriplicate': True}
    },
    "timetree_options": {
        "Tc": 'opt',
        "confidence":True
    }
}

if __name__=="__main__":
    parser = collect_args()
    params = parser.parse_args()

    if params.clean:
        config["clean"] = True

    if params.json:
        config["in"] = params.json

    config["newick_tree_options"]["method"] = params.tree_method

    runner = process(config)
    runner.align(fill_gaps=True)
    print('runner.align finished')
    runner.build_tree()
    print('runner.build_tree finished')
    runner.timetree_setup_filter_run()
    print('runner.timetree_setup_filter_run finished')
    runner.run_geo_inference()
    print('runner.run_geo_inference() finished')
    runner.save_as_nexus()
    print('runner.save_as_nexus() finished')
    runner.auspice_export()
    print('runner.auspice_export finished')
