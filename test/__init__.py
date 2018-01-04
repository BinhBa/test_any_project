from unittest2 import TestLoader, TestSuite
from HTMLTestRunner import HTMLTestRunner
import os
import importlib
import ast

if __name__ == '__main__':

    for root, dirs, file_names in os.walk('./test/'):
        for file_name in file_names:

            if 'test_' in file_name and len(root.split('/')) < 4:
                print(file_name)
                module_name = file_name.split('.')[0]

                file_path = os.path.join(root, file_name)
                file = open(file_path, 'r')

                file_content = file.read()
                p = ast.parse(file_content)
                classes = [node.name for node in ast.walk(p) if isinstance(node, ast.ClassDef)]
                for cls in classes:
                    # class_to_test = module_name + '.' + cls

                    file_report_name = module_name + '_' + cls
                    print(file_report_name)
                    report_path = 'test/report/Report_' + file_report_name + '.html'
                    f_load = open(report_path, 'w')
                    f_load.close()

                    runner = HTMLTestRunner(
                        stream=open(report_path, "wb"),
                        title="Unit Test Reports",
                        description='This is Unit test report of system.'
                    )

                    loader = TestLoader()

                    m = importlib.import_module(module_name)

                    # class_to_test = 'm.' + cls

                    suite = TestSuite((
                        loader.loadTestsFromTestCase(getattr(m, cls)),
                    ))
                    # run the test
                    runner.run(suite)
