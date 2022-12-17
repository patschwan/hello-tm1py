"""
Read rules from all cubes and sort cubes by some metrics (Number rows, Number feeders,... )
"""

import configparser
from TM1py.Services import TM1Service

# storing the credentials in a file is not recommended for purposes other than testing.
# it's better to setup CAM with SSO or use keyring to store credentials in the windows credential manager. Sample:
# Samples/credentials_best_practice.py
config = configparser.ConfigParser()
config.read(r'../.config/config.ini')

RESULT_FILE = r'/home/psw/code/hello-tm1py/output/cube_rule_stats.txt'
log_lines = []

with TM1Service(**config['24retail']) as tm1:
    cubes = tm1.cubes.get_all()
    # print(len(cubes))
    # cubes with SKIPCHECK
    cubes_with_skipcheck = [cube.name for cube in cubes if cube.skipcheck]
    # print(len(cubes_with_skipcheck))
    # log_lines.append("Cubes with SKIPCHECK:")
    # log_lines.append(cubes_with_skipcheck)
    # print(log_lines)

    # cubes with UNDEFVALS
    cubes_with_undefvals = [cube.name for cube in cubes if cube.undefvals]
    # log_lines.append("Cubes with UNDEFVALS:")
    # log_lines.append(cubes_with_undefvals)

    # cubes ordered by the number of rule statements
    cubes.sort(key=lambda cube: len(cube.rules.rule_statements) if cube.has_rules else 0, reverse=True)
    log_lines.append("Cubes sorted by number of Rule Statements:")
    log_lines.append([cube.name for cube in cubes])

    # cubes ordered by the number of feeder statements
    cubes.sort(key=lambda cube: len(cube.rules.feeder_statements) if cube.has_rules else 0, reverse=True)
    log_lines.append("Cubes sorted by number of Feeder Statements:")
    log_lines.append([cube.name for cube in cubes])

with open(RESULT_FILE, 'w', encoding='utf-8') as file:
    log_lines.append("Cubes with SKIPCHECK:")
    for cube in cubes_with_skipcheck:
        log_lines.append(cube)

    log_lines.append("Cubes with UNDEFVALS:")
    for cube in cubes_with_undefvals:
        log_lines.append(cube)

    
    # print(log_lines)
    file.write("\n".join(str(line) for line in log_lines))
    file.close()