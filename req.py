import pkg_resources
OUTPUT_FILE = 'requirements.txt'

with open(OUTPUT_FILE, mode='w') as f:
    for dist in pkg_resources.working_set:
        requirement = dist.project_name + '==' + dist.version
        f.write(requirement + '\n')
