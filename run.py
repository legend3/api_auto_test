import pytest
import allure
from common import Shell
from common import Log
"""
1.
文件名必为'run

2.
pytest学习时，很多时候都是从在cmd中运行开始，实际工作中正常都是用IDE编写代码，为了方便，pytest提供了main函数调用pytest用例

3.
这是发生的事情：python执行test_script.py并因此执行pytest.main("– s"),它返回到文件系统并收集test_script.py作为测试模块.
当pytest导入test_script时,在收集期间再次调用pytest.main(…).第二次调用不会再次导入test_script,因为它现在在sys.modules中,但它执行测试功能.
当集合完成(并且内部pytest.main()运行已执行测试一次)时,测试函数也由外部pytest.main()调用执行.一切都清楚了吗？ 🙂

如果你想避免这种情况,你需要像这样包装pytest.main()调用：

if __name__ == "__main__":
    pytest.main("-s")

此调用不会在正常导入时执行,但会在发出python test_script.py时执行,因为python通过将__name__设置为__main__而执行命令行指定的脚本,
但在正常导入test_script导入时则执行test_script.
'"""
if __name__ == '__main__':
    result_report_path = '../../.././Report/html/allure-results'
    report_path = '../../../Report/html/allure-report'

    shell = Shell.Shell()
    log = Log.MyLog()
    args = ['-s', '-v', './test_case/test_FullText/test_Full_Text_Search.py']  # '--alluredir', './Report/html/allure-result'

    pytest.main(args)

    cmd = 'allure generate %s -o %s' % (result_report_path, report_path)

    try:
        shell.invoke(cmd)  # 执行cmd/shell命令
        log.info('报告生成！')
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise
