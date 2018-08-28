#! /usr/bin/env python
# -*- coding:utf-8 -*-

import jenkins

server = jenkins.Jenkins("http://10.235.214.142:8080",username="test123",password="8742e8330b27226b1c8da9c434f1fd2b")
user = server.get_whoami()

#for item in user.items():
#    print (item)

version = server.get_version()
jobs_count_now = server.jobs_count()
#print("*"*50+"\n\n")


"""
Example 3: Working with Jenkins Jobs
This is an example showing how to create, configure and delete Jenkins jobs.
"""

server.create_job("empty",jenkins.EMPTY_CONFIG_XML)
'''
jobs = server.get_jobs()
print("jobs:",jobs)
my_job = server.get_job_config("cool_job")
print ("my_job:",my_job)
server.build_job("empty")
server.disable_job("empty")
server.copy_job('empty', 'empty_copy')
server.enable_job("empty_copy")
server.reconfig_job("empty_copy",jenkins.RECONFIG_XML)

server.delete_job("empty")
server.delete_job("empty_copy")

# build a parameterized job
# requires creating and configuring the api-test job to accept 'param1' & 'param2'

server.build_job("api-test",{"param1":"test value 1","param2":"test value 2"})
last_build_number = server.get_job_info('api-test')['lastCompletedBuild']['number']
build_info = server.get_build_info('api-test', last_build_number)
print (build_info)

# get all jobs from the specific view
jobs = server.get_jobs(view_name='View Name')
print (jobs)
'''
