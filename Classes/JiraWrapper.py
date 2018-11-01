#!/usr/bin/env python
# -*- coding: utf-8 -*-
# current_day = datetime.datetime.now().day
# current_month = datetime.datetime.now().month
# current_year = datetime.datetime.now().year


import datetime
from datetime import timedelta
from LogFile import logger
from jira.client import JIRA
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class JiraException(Exception):
    pass


class Jira(object):

    def __init__(self, **kwargs):

        self.description = None
        self.issue_aus = None
        self.issue_us = None
        self.issue_uk = None
        self.issue_es = None
        self.issue_de = None
        self.issue_fr = None
        self.issue_apac = None
        self.issue_mea = None

        self.create_aus = None
        self.create_us = None
        self.create_apac = None
        self.create_de = None
        self.create_mea = None
        self.create_fr = None
        self.create_es = None
        self.create_uk = None

        self.options = {
            'server': 'https://neomediaworld.atlassian.net',
            'verify': False
        }

        self.client = None

        if len(kwargs) != 2:
            raise JiraException(
                'In order to use this class you need to specify a user and a password as keyword arguments!')
        else:
            if 'username' in kwargs.keys():
                self.username = kwargs['username']
            else:
                raise JiraException('You need to specify a username as keyword argument!')
            if 'password' in kwargs.keys():
                self.password = kwargs['password']
            else:
                raise JiraException('You need to specify a password as keyword argument!')

            try:
                self.client = JIRA(self.options, basic_auth=(self.username, self.password))
            except Exception:
                raise JiraException('Could not connect to the API, invalid username or password!')

    def get_projects(self, raw=False):

        projects = []
        for project in self.client.projects():
            if raw:
                projects.append(project)
            else:
                projects.append({'Name': str(project.key), 'Description': str(project.name)})
        return projects

    @staticmethod
    def date_create():
        my_date = datetime.datetime.now().date()
        return my_date

    @staticmethod
    def sixth_day():
        now = datetime.datetime.now().date()
        start_month = datetime.datetime(now.year, now.month, 1)
        date_on_next_month = start_month + datetime.timedelta(35)
        start_next_month = datetime.datetime(date_on_next_month.year, date_on_next_month.month, 1)
        last_day_month = start_next_month - datetime.timedelta(1)
        sixth_day_month = last_day_month.date() + timedelta(6)
        return sixth_day_month

    def issue_description(self):

        description = "Hi Team" + "\n" + "Hope you are doing well" + "\n" + \
                      "Kindly confirm the current advertisers and accounts from the PDF attached." + "\n" + \
                      "Making sure that for each platform the correct account id, advertiser or account name get" + \
                      "\n" + "included in the NDP data for ALL channels." + "\n" + \
                      "Note: Do let us know if there is any account that needs to be removed." + "\n" + \
                      "Please make sure that the media plan is uploaded on the NeoSageCentral SharePoint Folder." \
                      + "\n" \
                      + "https://insidemedia.sharepoint.com/sites/neosagecentral/Shared%20Documents/" \
                        "Forms/AllItems.aspx?id=%2Fsites%2Fneosagecentral%2FShared%20Documents%2FFY18%20Media%" \
                        "20Plans%2FQ4%20Media%20Plans" + "\n" + "Thanks," + "\n" + "Dharmendra"

        self.description = description

    def aus_issue(self):
        watch = ['corinne.hewlett', 'thuy.le', 'jon.windred']
        assignee = ['corinne.hewlett']
        attachment = ["C:/Adops-Git/Files/AUS.xlsx"]
        self.issue_aus = {
            'project': {'key': 'MOS'},
            'issuetype': {'name': 'Reporting'},
            'summary': 'Test NDP Data Audit {} AUS'.format(Jira.date_create().strftime('%B')),
            'description': self.description,
            'customfield_10038': {'value': 'AUS'},
            'customfield_10052': {'value': 'Ad hoc'},
            'customfield_10053': {'value': 'Monthly'},
            "assignee": {
                "name": assignee
            }, 'duedate': str(Jira.sixth_day())}

        self.create_aus = self.client.create_issue(fields=self.issue_aus, prefetch=True)
        for i in watch:
            self.client.add_watcher(self.create_aus.id, i)
        self.client.add_attachment(self.create_aus.id)

    def apac_issue(self):
        watch = []
        assignee = []
        attachment = ["C:/Adops-Git/Files/AUS.xlsx"]
        self.issue_aus = {
            'project': {'key': 'MOS'},
            'issuetype': {'name': 'Reporting'},
            'summary': 'Test NDP Data Audit {} APAC'.format(Jira.date_create().strftime('%B')),
            'description': self.description,
            'customfield_10038': {'value': 'APAC'},
            'customfield_10052': {'value': 'Ad hoc'},
            'customfield_10053': {'value': 'Monthly'},
            "assignee": {
                "name": assignee
            }, 'duedate': str(Jira.sixth_day())}

        self.create_aus = self.client.create_issue(fields=self.issue_aus, prefetch=True)
        for i in watch:
            self.client.add_watcher(self.create_aus.id, i)

        for m in attachment:
            self.client.add_attachment(self.create_aus.id, i)

    def main(self):
        self.get_projects()
        logger.info('reading issue Description' + " at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
        self.issue_description()
        logger.info('Done!reading issue Description' + " at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
        logger.info('Start!creating issue for AUS' + " at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
        self.aus_issue()
        logger.info('Done!creating issue for AUS' + " at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))


if __name__ == "__main__":
    MyJira = Jira(username='Dharmendra.mishra@neomediaworld.com', password='Password1')
    MyJira.main()