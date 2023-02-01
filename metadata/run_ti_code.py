"""
Run TI/TM1 Code 
"""
from TM1py.Services import TM1Service

with TM1Service(address='172.24.16.1', port=52670, user='admin', password='apple', ssl=False) as tm1:
    ti_statements = [
        "SaveDataAll;",
        "DeleteAllPersistentFeeders;",
        "SecurityRefresh;",
        "CubeProcessFeeders('Plan_BudgetPlan');" # Wirft Fehler aus HTTPResponse und TM1ErrorLog, weil Cube nicht vorhanden = sehr gut!
    ]
    tm1.processes.execute_ti_code(lines_prolog=ti_statements, lines_epilog=[])