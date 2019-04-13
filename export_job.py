#!/bin/bash -xe
# -*- coding: utf-8 -*-

__version__ = '1.0.0'

import os
import argparse
import logs
import sys
import requests
from utils import Utils

logger = logs.logger

parser = argparse.ArgumentParser(prog='main',
                                 formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=100,
                                                                                     width=200))
parser.add_argument('-r', '--REPO_NAME', help='Repository identifier')
parser.add_argument('-s', '--SERVICE_NAME', help='Service Name identifier')

args = parser.parse_args()
repo_name = args.REPO_NAME
service_name = args.SERVICE_NAME

utils = Utils()
jenkins_url = "https://jenkins-<HOST>.com"
jenkins_user = 'admin'
jenkins_pass = os.environ["JENKINS_ADMIN_PASS"]

repo_suffix = 'repo' if repo_name == 'my_repo' else 'my_repo_next'


def parse_template():
    """
    :return:
    """
    context = {
        'service_name': service_name,
        'repo_suffix': repo_suffix
    }
    jenkins_job = utils.render('job_template.xml', context)
    return jenkins_job


def export_job(jenkins_job):
    """
    :param jenkins_job:
    :return:
    """
    logger.info("Creating new Jenkins job..")
    url = jenkins_url + '/createItem?name=docker-' + repo_name + "-" + service_name.replace("_", "-")
    auth = (jenkins_user, jenkins_pass)
    payload = jenkins_job
    headers = {"Content-Type": "application/xml"}
    response = requests.post(url, data=payload, auth=auth, headers=headers)

    # check response status
    if response.status_code == 400:
        logger.info('Jenkins Job Creation: %s Jenkins Job Already Exists <Response: [%d]> ' % (
            service_name, response.status_code))
    elif response.status_code != 200:
        rj = utils.return_json(response)
        logger.info('Jenkins  Job Import:  ', rj)
        if "Error" in rj:
            sys.exit(1)
    else:
        logger.info('=> Jenkins Job Creations: %s successfully created' % service_name)


def main():
    try:
        logger.info("*** Repo name is: " + repo_suffix + " ***")
        logger.info("*** Service name is: " + service_name + " ***")
        jenkins_job = parse_template()
        export_job(jenkins_job)

    except Exception as ex:
        logger.info("### Creation new Jenkins job was failed.." + str(ex) + " ###")
        sys.exit(os.EX_OSERR)


if __name__ == "__main__":
    main()
