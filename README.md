# JSONPlaceholder 接口自动化测试

针对公开测试接口 jsonplaceholder.typicode.com 的接口自动化测试项目。

## 技术栈
Python / requests / pytest / pytest-html / pytest-rerunfailures

## 用例覆盖
- GET 查询：正常流 + 参数化异常流（0、负数、非数字、超大 id）
- POST 创建：正常创建 + 空对象行为基线（接口不为缺失字段补默认值）
- DELETE + 生命周期：参数关联、fixture 自动清理（失败也 teardown）

## 运行方式
pip install -r requirements.txt
pytest

## 测试报告
运行后自动生成 report.html，浏览器打开查看。