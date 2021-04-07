import logging
import argparse
import os
from validations import validate
from groupExport import group_export_import
from exceptions import IsNotDirectoryError
from config import get_config
from cleanup import clean_files
from projectsExport import migrate_projects


def parse_args():
    parser = argparse.ArgumentParser(
        description="""Create and configure repositories in gitlab"""
    )
    parser.add_argument(
        "-l",
        "--level",
        choices=["INFO", "WARNING", "ERROR", "CRITICAL", "DEBUG"],
        required=False,
        dest="debug",
        default="ERROR",
        help="""level of logging""",
        type=str,
    )
    parser.add_argument(
        "-p",
        "--local-path",
        required=True,
        dest="path_dir",
        help="""Path necessary for save gitlab export files""",
        type=str,
    )

    return parser.parse_args()

def main():
    args = parse_args()
    
    logging.basicConfig(
        format="%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s",
        level  = args.debug,
    )
    
    if not os.path.isdir(args.path_dir):
        raise IsNotDirectoryError(args.path_dir)
    
    validate(args.path_dir)

    # Export group structure
    group_export_import(get_config()["OLD_GROUP_ID"],args.path_dir)
    
    logging.info("Exporting projects")
    migrate_projects(args.path_dir)
    
    # Clean  
    clean_files(args.path_dir)
    

if __name__ == "__main__":
    main()